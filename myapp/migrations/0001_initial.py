# Generated by Django 3.0.5 on 2020-08-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='myapp/images/')),
            ],
        ),
    ]
