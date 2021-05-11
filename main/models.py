from django.db import models

class Event(models.Model):
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    address = models.CharField('Адрес', max_length=100)
    text = models.TextField()
    admin_social_network = models.URLField()

class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name='Пост события', related_name='images', on_delete=models.RESTRICT)
    image = models.ImageField('Изображение', upload_to='images')
    description = models.CharField(verbose_name='Описание картинки', max_length=100)

class Profile(models.Model):
    social_network = models.URLField()
    events = models.ManyToManyRel(Event, to=Event)

class Music(models.Model):
    name = models.CharField('Название', max_length=40)
    author = models.CharField('Название', max_length=20)
    events = models.ManyToManyRel(Event, to=Event)

class Simbolic(models.Model):
    simbolic = models.CharField(max_length=20)