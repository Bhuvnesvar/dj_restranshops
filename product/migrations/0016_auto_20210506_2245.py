# Generated by Django 3.1.7 on 2021-05-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
