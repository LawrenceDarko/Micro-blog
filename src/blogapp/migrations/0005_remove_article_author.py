# Generated by Django 3.0.1 on 2020-01-02 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]