# Generated by Django 4.1.3 on 2023-01-14 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_alter_newspage_cat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='new_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news_app.category'),
        ),
    ]
