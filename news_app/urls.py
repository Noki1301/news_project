from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("news/", news_list, name="all_news_list"),
    path("all<int:id>/", news_detail, name="news_detail"),
    path("contact/", ContactPageView.as_view(), name="contact_page"),
]
