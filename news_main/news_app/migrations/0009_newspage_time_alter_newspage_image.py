# Generated by Django 4.1.5 on 2023-01-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0008_alter_category_options_alter_newspage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='image',
            field=models.ImageField(null=True, upload_to='my_image'),
        ),
    ]
