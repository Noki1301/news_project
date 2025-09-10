from django.urls import path, reverse_lazy
from .views import (
    HomePageView,
    ContactPageView,
    news_detail,
    news_list,
    LocalNewsView,
    XorijNewsView,
    SportNewsView,
    TechnologyNewsView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
)

app_name = "news"  # agar namespace ishlatsangiz

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("contact/", ContactPageView.as_view(), name="contact_page"),
    path("news/", news_list, name="all_news_list"),
    path("mahalliy/", LocalNewsView.as_view(), name="mahalliy_news_page"),
    path("xorij/", XorijNewsView.as_view(), name="xorij_news_page"),
    path("technologiya/", TechnologyNewsView.as_view(), name="technology_news_page"),
    path("sport/", SportNewsView.as_view(), name="sport_news_page"),
    path("create/", NewsCreateView.as_view(), name="news_create"),
    path("<slug:slug>/update/", NewsUpdateView.as_view(), name="news_update"),
    path("<slug:slug>/delete/", NewsDeleteView.as_view(), name="news_delete"),
    path("<slug:slug>/", news_detail, name="news_detail"),
]
