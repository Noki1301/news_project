from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.
class PublishedNewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.name == "Маҳаллий":
            return reverse("news:mahalliy_news_page")
        elif self.name == "Хориж":
            return reverse("news:xorij_news_page")
        elif self.name == "Технология":
            return reverse("news:technology_news_page")
        elif self.name == "Спорт":
            return reverse("news:sport_news_page")
        return "#"


class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news_images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )

    objects = models.Manager()  # The default manager.
    published = PublishedNewsManager()  # Our custom manager.

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:news_detail", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email
