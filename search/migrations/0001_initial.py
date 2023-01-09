# Generated by Django 4.1.5 on 2023-01-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('colors', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=500)),
                ('images', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('product_link', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('sizes', models.CharField(max_length=500)),
                ('sku', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Imageist_DATA',
            },
        ),
    ]
