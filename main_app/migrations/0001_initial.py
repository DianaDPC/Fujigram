# Generated by Django 4.1.5 on 2023-03-28 18:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sensor', models.CharField(choices=[('X-trans I', 'X-trans I'), ('X-trans II', 'X-trans II'), ('X-trans III', 'X-trans III'), ('X-trans IV', 'X-trans IV'), ('X-trans V', 'X-trans V'), ('X-trans V HS', 'X-trans V HS'), ('X-trans V HR', 'X-trans V HR')], max_length=12)),
                ('dynamic_range', models.CharField(choices=[('DR100%', 'DR100%'), ('DR200%', 'DR200%'), ('DR400%', 'DR400%'), ('DR-Auto', 'DR-Auto')], max_length=7)),
                ('film_simulation', models.CharField(choices=[('Acros', 'Acros'), ('Acros + G', 'Acros + G'), ('Acros + R', 'Acros + R'), ('Acros + Ye', 'Acros + Ye'), ('Classic Neg.', 'Classic Neg.'), ('Eterna', 'Eterna'), ('Eterna Bleach Bypass', 'Eterna Bleach Bypass'), ('Provia/Standard', 'Provia/Standard'), ('Velvia/Vivid', 'Velvia/Vivid'), ('Astia/Soft', 'Astia/Soft'), ('Classic Chrome', 'Classic Chrome'), ('PRO Neg. Hi', 'PRO Neg. Hi'), ('PRO Neg. Std', 'PRO Neg. Std'), ('Monochrome', 'Monochrome'), ('Monochrome + G', 'Monochrome + G'), ('Monochrome + R', 'Monochrome + R'), ('Monochrome + Ye', 'Monochrome + Ye'), ('Sepia', 'Sepia')], max_length=20)),
                ('monochromatic_color_WC', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-9), django.core.validators.MaxValueValidator(9)])),
                ('monochromatic_color_MG', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-9), django.core.validators.MaxValueValidator(9)])),
                ('highlight_tone', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('shadow_tone', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('color', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('noise_reduction', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('clarity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('grain_effect', models.CharField(choices=[('Off', 'Off'), ('Strong', 'Strong'), ('Weak', 'Weak')], max_length=6)),
                ('grain_size', models.CharField(choices=[('Large', 'Large'), ('Small', 'Small')], max_length=5)),
                ('color_chrome_effect', models.CharField(choices=[('Off', 'Off'), ('Strong', 'Strong'), ('Weak', 'Weak')], max_length=6)),
                ('white_balance', models.CharField(max_length=50)),
                ('white_balance_shift_red', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-9), django.core.validators.MaxValueValidator(9)])),
                ('white_balance_shift_blue', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-9), django.core.validators.MaxValueValidator(9)])),
                ('sharpness', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-4), django.core.validators.MaxValueValidator(4)])),
                ('long_exposure_nr', models.BooleanField()),
                ('lens_modulation_optimizer', models.BooleanField()),
                ('color_space', models.CharField(choices=[('sRGB', 'sRGB'), ('Adobe RGB', 'Adobe RGB')], max_length=9)),
                ('iso', models.CharField(choices=[('Auto', 'Auto'), ('200', '200'), ('400', '400'), ('800', '800'), ('1600', '1600'), ('3200', '3200'), ('6400', '6400'), ('12800', '12800')], max_length=5)),
                ('exposure_compensation', models.CharField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('camera_used', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='media/')),
                ('msg_body', models.CharField(max_length=300)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.recipe')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('msg_body', models.CharField(max_length=300)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
