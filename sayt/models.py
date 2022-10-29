# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Ekologiya(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavxa')
    content = models.TextField(blank=True, verbose_name='Kontent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sana')
    updated_at = models.DateField(auto_now=True, verbose_name='Uzgartirilgan sana')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, verbose_name='Rasm')
    is_published = models.BooleanField(default=True, verbose_name='Qushilgan')
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ekologiya'
        verbose_name_plural = 'Ekologiyalar'
        ordering = ['-created_at', 'id']

class Menyu(models.Model):
    title=models.CharField(max_length=50, db_index=True, verbose_name='Asosiy menyu',)
    turi=models.CharField(max_length=2, verbose_name='Menyu turi',)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'
        ordering = ['title','turi']
class Katalog(models.Model):
    okpo=models.IntegerField(primary_key=True, verbose_name='okpo raqami',)
    soato=models.IntegerField(verbose_name='Hudud kodi',)
    name=models.CharField(max_length=50, verbose_name="Korxona nomi",)
    biznes=models.BooleanField(default=False, verbose_name="Kichik biznes",)

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavxa')
    content = models.TextField(blank=True, verbose_name='Matn')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sana')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan sana")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Rasm')
    is_published = models.BooleanField(default=True, verbose_name='Ruxsat berilgan')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1, verbose_name='Kategoriyasining nomi')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        ordering = ['-created_at', 'content']

class Category(models.Model):
    title =models.CharField(max_length=150, db_index=True, verbose_name='Kategotiya nomi')
    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})
    def __str__(self):
        return  self.title
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['title']
