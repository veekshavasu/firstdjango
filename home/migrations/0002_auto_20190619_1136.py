# Generated by Django 2.2.2 on 2019-06-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(help_text='Book author', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(help_text='Book Name', max_length=100, null=True),
        ),
    ]
