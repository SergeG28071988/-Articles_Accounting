from django.db import models

# Create your models here.


class Person(models.Model):

    last_name = models.CharField(max_length=100, verbose_name="Фамилия автора")
    first_name = models.CharField(max_length=100, verbose_name="Имя автора")    
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=True, blank=True)   

    class Meta:
        abstract = True
 

    def __str__(self):
        return self.last_name      


class Author(Person):
    pass


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи")
    content = models.TextField(verbose_name="Содержание статьи")
    date_published = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)

    def __str__(self):
        return self.title