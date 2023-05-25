# Generated by Django 4.0.4 on 2022-06-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_conge_nom_conge_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='adresse',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='CIN',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='CNSS',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]