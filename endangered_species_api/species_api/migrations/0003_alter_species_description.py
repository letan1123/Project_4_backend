# Generated by Django 4.0.5 on 2022-06-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species_api', '0002_rename_suborder_species_genus_species_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]