# Generated by Django 4.2.2 on 2023-07-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=55, unique=True),
        ),
    ]