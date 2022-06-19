from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
    name = models.CharField('이름',max_length=120)
    description = models.TextField('설명',  max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    class Meta:
        db_table = "article"
    user = models.ForeignKey('user.User', verbose_name='작성자', on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=100)
    category = models.ManyToManyField(Category, verbose_name=("카테고리"))
    content = models.TextField("내용", max_length=255)

    def __str__(self):
        return self

class Comment(models.Model):
    class Meta:
        db_table = "comment"
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self