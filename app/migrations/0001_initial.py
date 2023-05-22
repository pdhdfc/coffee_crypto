# Generated by Django 4.2.1 on 2023-05-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PopularMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='image size 86 X 86', upload_to='image/menu/popular')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(help_text='end with .00', max_length=10)),
            ],
        ),
    ]
