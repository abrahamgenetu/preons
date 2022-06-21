import uuid

from django.db import models
from datetime import datetime

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    #category_image = models.ImageField(upload_to='categoryImage', blank=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

    def get_absolute_url(self):
        return redirect("main:homepage")

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category",
                                          on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    #series_image = models.ImageField(upload_to='seriesImage', blank=True)
    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

    def get_absolute_url(self):
        return redirect("main:homepage")

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content_first = models.TextField(default="This is the introduction content")
    content_second = models.TextField(default="This is the main lesson")
    content_third = models.TextField(default="This is the summary content with review questions")
    # tutorial_video = models.FileField(blank=True, null=True, verbose_name="Add video to tutorial")
    published = models.DateTimeField("date published", default=datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.SlugField(unique=True, default=uuid.uuid1)
    tutorial_image = models.FileField(blank=True, null=True, verbose_name="Add Photos to tutorial")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return redirect("main:homepage")

class News(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title