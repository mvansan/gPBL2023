# Generated by Django 4.2.1 on 2023-08-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('Fr', 'Frappuccino'), ('Ca', 'Cappuccino'), ('Cho', 'Chocolate'), ('La', 'Latte'), ('Am', 'Americano'), ('La', 'Latte'), ('Es', 'Espresso')], max_length=3)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
