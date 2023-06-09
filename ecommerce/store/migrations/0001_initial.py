# Generated by Django 4.1.7 on 2023-03-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('brand', models.CharField(default='without brand', max_length=300)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
