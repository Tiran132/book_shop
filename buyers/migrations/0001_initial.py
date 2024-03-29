# Generated by Django 2.2 on 2019-05-12 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_auto_20190428_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BuyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.Book')),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='buyers.Buyer')),
            ],
        ),
    ]
