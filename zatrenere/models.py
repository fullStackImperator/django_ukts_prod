from django.db import models



class Planeri(models.Model):
    class Meta:
        verbose_name = 'Planer'
        verbose_name_plural = 'Planeri'

    ime = models.CharField(max_length=100)
    file = models.FileField(upload_to='planeri/pdfs/')
    cover = models.ImageField(upload_to='planeri/covers/')


    def __str__(self):
        return self.ime


class Lekarski(models.Model):
    class Meta:
        verbose_name = 'Lekarski'
        verbose_name_plural = 'Lekarski'

    FILE_CHOICES = (
        ('pdf', 'pdf'),
        ('word', 'word'),
        )

    ime = models.CharField(max_length=100)
    file = models.FileField(upload_to='lekarski/pdfs/')
    tip = models.CharField(max_length=5, choices=FILE_CHOICES, default='pdf')
    cover = models.ImageField(upload_to='lekarski/covers/')


    def __str__(self):
        return self.ime


class Uplatnice(models.Model):
    class Meta:
        verbose_name = 'Uplatnice'
        verbose_name_plural = 'Uplatnice'

    ime = models.CharField(max_length=100)
    file = models.FileField(upload_to='uplatnice/pdfs/')
    cover = models.ImageField(upload_to='uplatnice/covers/')


    def __str__(self):
        return self.ime


class Aplikacija(models.Model):
    class Meta:
        verbose_name = 'Uplatnice'
        verbose_name_plural = 'Uplatnice'

    ime = models.CharField(max_length=100)
    file = models.FileField(upload_to='uplatnice/pdfs/')
    cover = models.ImageField(upload_to='uplatnice/covers/')


    def __str__(self):
        return self.ime