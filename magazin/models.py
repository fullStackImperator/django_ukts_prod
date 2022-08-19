from django.db import models



# class Files(models.Model):
#     filename = models.CharField(max_length=100)
#     # owner = models.CharField(max_length=100)
#     pdf = models.FileField(upload_to='store/pdfs/')
#     cover = models.ImageField(upload_to='store/covers/', null=True, blank=True)

#     def __str__(self):
#         return self.filename

#     def delete(self, *args, **kwargs):
#         self.pdf.delete()
#         self.cover.delete()
#         super().delete(*args, **kwargs)



class Files(models.Model):
    class Meta:
        verbose_name = 'Magazin Izdanje'
        verbose_name_plural = 'Magazin Izdanja'

    name = models.CharField(max_length=100)
    broj = models.CharField(max_length=100)
    # owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='store/pdfs/')
    cover = models.ImageField(upload_to='store/covers/')
    # published to do


    def __str__(self):
        return self.name