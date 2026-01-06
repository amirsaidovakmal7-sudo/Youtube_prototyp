from django.db import models
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Категория")
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.category_name


class Video(models.Model):
    news_video_name = models.CharField(max_length=150, verbose_name='Название видео')
    news_video_description = models.TextField(verbose_name="Описание")
    news_video = models.FileField(upload_to='media', verbose_name='Видео')
    video_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.news_video_name


class AddVideo(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Video, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Загрузка'
        verbose_name_plural = 'Загрузки'

    def __str__(self):
        return f'Форма добавления пользователя с ID {self.user_id}'
