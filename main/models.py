from datetime import datetime

from django.db import models


class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.series


# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField("date published", default=datetime.now())
    series = models.ForeignKey(TutorialSeries, verbose_name="Series", on_delete=models.SET_DEFAULT, default=None,
                               blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
