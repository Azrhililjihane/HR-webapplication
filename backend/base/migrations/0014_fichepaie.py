# Generated by Django 4.0.4 on 2022-06-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichePaie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=200, null=True)),
                ('prenom', models.CharField(blank=True, max_length=200, null=True)),
                ('salaire', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
        ),
    ]
