# Generated by Django 4.1.7 on 2023-04-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
