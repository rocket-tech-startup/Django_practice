# Generated by Django 4.0.4 on 2022-04-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '패스트캠퍼스 게시글', 'verbose_name_plural': '패스트캠퍼스 게시글'},
        ),
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.tag', verbose_name='태그'),
        ),
    ]