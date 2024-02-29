# Generated by Django 5.0.2 on 2024-02-28 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия автора')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('content', models.TextField(verbose_name='Содержание статьи')),
                ('date_published', models.DateField(verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author', verbose_name='Автор')),
            ],
        ),
    ]