# Generated by Django 4.1.1 on 2022-11-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peda', '0004_followerscount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='def profile.jpg', upload_to='profile_images'),
        ),
    ]