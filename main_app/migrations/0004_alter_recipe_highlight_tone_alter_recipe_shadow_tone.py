# Generated by Django 4.1.7 on 2023-03-27 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_white_balance_shift_recipe_white_balance_shift_blue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='highlight_tone',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='shadow_tone',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
