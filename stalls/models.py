from django.db import models


class PreviewStall(models.Model):

    name = models.CharField(max_length=50)
    # remake it
    picture = models.AutoField()
    short_description = models.CharField(max_length=200)
    recalls_counter = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    address = models.CharField(max_length=200)


class FullStallDescription(models.Model):

    name = models.CharField(max_length=50)
    full_description = models.CharField(max_length=400)
    address = models.CharField(max_length=200)


class Recalls(models.Model):

    author = models.CharField(max_length=30)
    pub_date = models.DateTimeField('Date published')
    recall_text = models.CharField(max_length=400)
    rating_counter = models.IntegerField(default=0)


class Menu(models.Model):

    food_name = models.CharField(max_length=50)
    price = models.FloatField(default=0)


class StallPicture(models.Model):

    # remake it
    picture = models.AutoField()
