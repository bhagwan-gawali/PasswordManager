# Generated by Django 4.0.6 on 2022-07-31 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_address_customuser_age_customuser_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='ssd', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pincode',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
