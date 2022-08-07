# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import (SearchQuery, SearchRank,
                                            SearchVector, TrigramSimilarity)
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from taggit.models import Tag

from .forms import CommentForm, EmailPostForm, SearchForm
from .models import Comment, Post


def post_search(request): 
    form = SearchForm() 
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET) 
        if form.is_valid():
            query = form.cleaned_data['query'] 

            search_vector = SearchVector('title', 'body')
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            search_rank = SearchRank(search_vector, search_query)
            # results = Post.published.annotate(search=search_vector, rank=search_rank).filter(rank__gte=0.1).order_by('-rank')
    
            results = Post.published.annotate(similarity=TrigramSimilarity('title', query), ).filter(similarity__gt=0.1).order_by('-similarity')

    context = {'form': form, 'query': query, 'results': results}

    return render(request,'blog/post/search.html', context)




class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


    
def post_list(request, tag_slug=None):
#    posts = Post.published.all()
    object_list = Post.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug) 
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5) # 3 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)


    # search
    query = request.GET.get("q")
    if query:
        posts=Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()


    # post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    # comments = post.comments.filter(active=True)

    context = {'page': page, 'posts': posts, 'tag': tag}

    return render(request, 'ukts/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    
    new_comment = None
    
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()


    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True) 
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    context = {'post': post, 'comments':comments, 
                'new_comment': new_comment, 'comment_form': comment_form, 'similar_posts': similar_posts}
                
    return render(request, 'detail.html', context)



# handling reply, reply view
def reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input
            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(post_url+'#'+str(reply.id))
    return redirect("/")



def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            #send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            send_mail(subject, message, 'stvel075@gmail.com', [cd['to']])

            sent = True
    else:
        form = EmailPostForm()
    
    return render(request, 'blog/post/share_form.html', {'post': post,'form': form, 'sent': sent})



def magazin_list(request):
    pass


def pdf(request):
    try:
        return FileResponse(open('<file name with path>', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404('not found')

def magazin_detail(request):
    return render(request,'template.html')
    

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Username or password is incorrect')
#             # return render(request, 'accounts/login.html', context)

#     context = {}
#     return render(request, 'login.html', context)


# def logoutUser(request):
#     logout(request)
#     return redirect('login')
