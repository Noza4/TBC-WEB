# Generated by Django 5.0.4 on 2024-04-15 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='CoverType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Cover',
                'verbose_name_plural': 'Covers',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('page_count', models.IntegerField(verbose_name='Page Count')),
                ('category', models.CharField(max_length=200, null=True, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.author', verbose_name='Author')),
                ('cover', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.covertype', verbose_name='Cover')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
