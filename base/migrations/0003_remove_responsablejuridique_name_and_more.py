# Generated by Django 4.2.11 on 2024-04-12 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_responsablejuridique_responsablemaintenance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsablejuridique',
            name='name',
        ),
        migrations.RemoveField(
            model_name='responsablejuridique',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='responsablejuridique',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='responsablemaintenance',
            name='name',
        ),
        migrations.RemoveField(
            model_name='responsablemaintenance',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='responsablemaintenance',
            name='password2',
        ),
    ]
