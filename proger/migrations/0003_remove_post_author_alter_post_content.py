# Generated by Django 4.1.4 on 2023-01-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proger', '0002_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]