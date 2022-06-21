from django.db import models

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    start_date = models.models.DateField("노출 시작 일자")
    end_date = models.models.DateField("노출 종료 일자")