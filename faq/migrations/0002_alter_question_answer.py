# Generated by Django 4.2.5 on 2023-09-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
