# Generated by Django 4.1.7 on 2023-04-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_client_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=255, unique=True, verbose_name='Справочники')),
            ],
        ),
    ]
