# Generated by Django 4.0.2 on 2022-03-10 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-dateCreation'], 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
