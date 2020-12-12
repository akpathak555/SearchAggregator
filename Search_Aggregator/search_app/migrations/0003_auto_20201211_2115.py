# Generated by Django 3.1.4 on 2020-12-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0002_auto_20201211_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCluesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.CharField(blank=True, max_length=5000, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TataProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.CharField(blank=True, max_length=5000, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='PaytmProduct',
        ),
    ]
