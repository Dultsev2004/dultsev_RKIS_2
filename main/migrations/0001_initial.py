# Generated by Django 5.0 on 2023-12-17 14:24

import django.core.validators
import django.db.models.deletion
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, upload_to='cover/books/title', validators=[main.models.Cover.validate_image], verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('lastName', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('dateOfBirth', models.DateField(max_length=100, verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'unique_together': {('name', 'lastName', 'middle_name', 'dateOfBirth')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('yearOfRel', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)], verbose_name='Год выпуска')),
                ('genre', models.CharField(blank=True, max_length=100, verbose_name='Жанр')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='Категория')),
                ('publisher', models.CharField(blank=True, max_length=100, verbose_name='Издательство')),
                ('photoPreview', models.ImageField(null=True, upload_to='cover', validators=[main.models.Book.validate_image], verbose_name='Изображения')),
                ('bookFile', models.FileField(null=True, upload_to='books', verbose_name='Файл с книгой')),
                ('author', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='main.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'unique_together': {('title', 'author', 'yearOfRel', 'publisher')},
            },
        ),
    ]