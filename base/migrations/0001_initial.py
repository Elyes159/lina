# Generated by Django 4.2.11 on 2024-04-11 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonModele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ_texte', models.CharField(max_length=100)),
                ('champ_entier', models.IntegerField(default=0)),
            ],
        ),
    ]
