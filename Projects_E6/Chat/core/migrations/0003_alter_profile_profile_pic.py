# Generated by Django 4.1.1 on 2022-10-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
