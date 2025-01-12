# Generated by Django 5.1.4 on 2025-01-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('publication', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
