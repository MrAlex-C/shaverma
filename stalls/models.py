from django.db import models


class Stall(models.Model):

    name = models.CharField(max_length=40)
    main_picture = models.ImageField()
    description = models.CharField(max_length=400)
    reviews_counter = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    address = models.CharField(max_length=200)


class FoodList(models.Model):

    stall = models.ForeignKey(Stall)
    food_name = models.CharField(max_length=40)
    price = models.FloatField(default=0)


class StallPictures(models.Model):

    stall = models.ForeignKey(Stall)
    picture = models.ImageField()
