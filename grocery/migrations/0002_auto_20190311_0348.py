# Generated by Django 2.1.7 on 2019-03-11 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20190310_2322'),
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='recipes',
        ),
        migrations.AddField(
            model_name='grocerylist',
            name='recipes',
            field=models.ManyToManyField(to='recipe.Recipe'),
        ),
    ]
