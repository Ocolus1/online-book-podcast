# Generated by Django 4.2.4 on 2023-08-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_bookchapter_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amazon_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
    ]
