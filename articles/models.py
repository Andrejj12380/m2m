from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):
    title = models.CharField(max_length = 256, verbose_name = 'Название')
    text = models.TextField(verbose_name = 'Текст')
    published_at = models.DateTimeField(verbose_name = 'Дата публикации')
    image = models.ImageField(null = True, blank = True, verbose_name = 'Изображение', )
    tags = models.ManyToManyField(Tag, through = 'Scope')

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'scopes', verbose_name = 'СТАТЬЯ')
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, related_name = 'scopes', verbose_name = 'РАЗДЕЛ')
    is_main = models.BooleanField(default = False, verbose_name = 'ОСНОВНОЙ')

    class Meta:
        ordering = ['-is_main', 'tag']