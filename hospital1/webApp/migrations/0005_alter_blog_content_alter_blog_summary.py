# Generated by Django 4.2.6 on 2023-12-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(),
        ),
    ]
