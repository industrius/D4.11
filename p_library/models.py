from django.db import models

class Author(models.Model):
    full_name = models.TextField(verbose_name=("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=("Страна"))

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13,verbose_name=("Международный стандартный книжный номер"))
    title = models.TextField(verbose_name=("Название"))
    description = models.TextField(verbose_name=("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=("Цена"))
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE, verbose_name=("Автор"), related_name="book_author")
    publisher = models.ForeignKey("p_library.Publisher", on_delete=models.CASCADE, null="True", blank="True", verbose_name=("Издатель"), related_name="books")

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=250, verbose_name="Издательство")

    def __str__(self):
        return self.title