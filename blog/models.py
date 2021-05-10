from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, verbose_name='Пост картинки', related_name='images', on_delete=models.RESTRICT)
    image = models.ImageField('Изображение', upload_to='images')
    description = models.CharField(verbose_name='Описание картинки', max_length=100)

    # Чтобы выбрать все товары вместе с их изображениями используйте prefetch_related:
    # qs = Product.objects.all().prefetch_related('images')
    # Тогда в цикле вы сможете перебрать товары следующим образом:
    # for product in qs:
    #     print(qs.name)
    #     for image in product.images.all():  # дополнительных запросов не будет
    #         print('->', image.url)
    def __str__(self):
        return self.description + 'для поста: ' + self.post.title

    # class Bb(models.Model):
    #     title = models.CharField(max_length=50, verbose_name='Товар')
    #     content = models.TextField(null=True, blank=True, verbose_name='Описание')
    #     price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    #     published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    #     rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    #
    #     class Meta:
    #         verbose_name_plural = 'Объявления'
    #         verbose_name = 'Объявление'
    #         ordering = ['-published']
    #
    # class Rubric(models.Model):
    #     name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    #
    #     def __str__(self):
    #         return self.name
