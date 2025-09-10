from django.urls import reverse
from .models import News


def latest_news(request):
    latest_news = News.published.all().order_by("-publish_time")[:5]
    return {"latest_news": latest_news}


def static_pages(request):
    return {
        "home_url": reverse("news:home_page"),
        "contact_url": reverse("news:contact_page"),
    }
