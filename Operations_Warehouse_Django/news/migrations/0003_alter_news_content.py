# Generated by Django 4.1.12 on 2024-05-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_associations_newsitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Content',
            field=models.CharField(max_length=50000),
        ),
    ]
