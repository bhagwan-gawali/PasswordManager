# Generated by Django 4.0.6 on 2022-08-01 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carddata',
            old_name='notes',
            new_name='cc_notes',
        ),
    ]
