# Generated by Django 2.2 on 2019-05-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190428_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.CharField(default="", max_length=10000),
            preserve_default=False,
        ),
    ]
