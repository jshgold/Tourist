# Generated by Django 3.2.6 on 2021-08-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='UserID'),
        ),
    ]