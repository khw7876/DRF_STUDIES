# Generated by Django 4.0.5 on 2022-06-21 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(max_length=255, verbose_name='내용')),
                ('start_date', models.DateField(verbose_name='노출 시작 일자')),
                ('end_date', models.DateField(verbose_name='노출 종료 일자')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='이름')),
                ('description', models.TextField(max_length=50, verbose_name='설명')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
