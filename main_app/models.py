from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

COLOR_SPACE = (
    ('sRGB','sRGB'), 
    ('Adobe RGB','Adobe RGB')
)
ISO = (
    ('Auto','Auto'), 
    ('200','200'), 
    ('400','400'), 
    ('800','800'), 
    ('1600','1600'), 
    ('3200','3200'), 
    ('6400','6400'),
    ('12800','12800')
)
COLOR_CHROME_EFFECT = (
    ('Off','Off'),
    ('Strong','Strong'),
    ('Weak','Weak')
)
GRAIN_EFFECT = (
    ('Off','Off'),
    ('Strong','Strong'),
    ('Weak','Weak')
)
GRAIN_SIZE = (
    ('Large','Large'),
    ('Small','Small')
)
FILM_SIMULATION = (
    ('Acros','Acros'),
    ('Acros + G','Acros + G'),
    ('Acros + R','Acros + R'),
    ('Acros + Ye','Acros + Ye'),
    ('Classic Neg.','Classic Neg.'),
    ('Eterna','Eterna'),
    ('Eterna Bleach Bypass','Eterna Bleach Bypass'),
    ('Provia/Standard','Provia/Standard'),
    ('Velvia/Vivid','Velvia/Vivid'),
    ('Astia/Soft','Astia/Soft'),
    ('Classic Chrome','Classic Chrome'),
    ('PRO Neg. Hi','PRO Neg. Hi'),
    ('PRO Neg. Std','PRO Neg. Std'),
    ('Monochrome','Monochrome'),
    ('Monochrome + G','Monochrome + G'),
    ('Monochrome + R','Monochrome + R'),
    ('Monochrome + Ye','Monochrome + Ye'),
    ('Sepia','Sepia')
)
DYNAMIC_RANGE = (
    ('DR100%','DR100%'),
    ('DR200%','DR200%'),
    ('DR400%','DR400%'),
    ('DR-Auto','DR-Auto')
)
SENSOR = (
    ('X-trans I','X-trans I'),
    ('X-trans II','X-trans II'),
    ('X-trans III','X-trans III'),
    ('X-trans IV','X-trans IV'),
    ('X-trans V','X-trans V'),
    ('X-trans V HS','X-trans V HS'),
    ('X-trans V HR','X-trans V HR')
)

# Create your models here.
class Recipe(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sensor = models.CharField(max_length=12, choices=SENSOR)
    dynamic_range = models.CharField(max_length=7, choices=DYNAMIC_RANGE)
    film_simulation = models.CharField(max_length=20, choices=FILM_SIMULATION)
    monochromatic_color_WC = models.IntegerField(default=0, validators=[MinValueValidator(-9), MaxValueValidator(9)])
    monochromatic_color_MG = models.IntegerField(default=0, validators=[MinValueValidator(-9), MaxValueValidator(9)])
    highlight_tone = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    shadow_tone = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    color = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    noise_reduction = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    clarity = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    grain_effect = models.CharField(max_length=6, choices=GRAIN_EFFECT)
    grain_size = models.CharField(max_length=5, choices=GRAIN_SIZE)
    color_chrome_effect = models.CharField(max_length=6, choices=COLOR_CHROME_EFFECT)
    white_balance = models.CharField(max_length=50)
    white_balance_shift_red = models.IntegerField(default=0, validators=[MinValueValidator(-9), MaxValueValidator(9)])
    white_balance_shift_blue = models.IntegerField(default=0, validators=[MinValueValidator(-9), MaxValueValidator(9)])
    sharpness = models.IntegerField(default=0, validators=[MinValueValidator(-4), MaxValueValidator(4)])
    long_exposure_nr = models.BooleanField()
    lens_modulation_optimizer = models.BooleanField()
    color_space = models.CharField(max_length=9, choices=COLOR_SPACE)
    iso = models.CharField(max_length=5, choices=ISO)
    exposure_compensation = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Post(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    recipe_id = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    camera_used = models.CharField(max_length=100)
    photo = models.FileField(upload_to='media/')
    msg_body = models.CharField(max_length=300)

    def __str__(self):
        return self.msg_body

class Comment(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post_id = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    msg_body = models.CharField(max_length=300)

    def __str__(self):
        return self.msg_body