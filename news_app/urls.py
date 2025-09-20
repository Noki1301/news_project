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
    admin_page_view,
    SearchResultsList,
    toggle_status,
    create_user_view,
    delete_user_view,
    reset_password_view,    
)

app_name = "news"

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("contact/", ContactPageView.as_view(), name="contact_page"),
    path("news/", news_list, name="all_news_list"),
    path("mahalliy/", LocalNewsView.as_view(), name="mahalliy_news_page"),
    path("xorij/", XorijNewsView.as_view(), name="xorij_news_page"),
    path("technologiya/", TechnologyNewsView.as_view(), name="technology_news_page"),
    path("sport/", SportNewsView.as_view(), name="sport_news_page"),
    path("create/", NewsCreateView.as_view(), name="news_create"),
    path("admin_page/", admin_page_view, name="admin_page"),
    path("search/", SearchResultsList.as_view(), name="search"),
    path("users/create/", create_user_view, name="user_create"),
    path("users/<int:pk>/delete/", delete_user_view, name="user_delete"),
    path(
        "users/<int:pk>/reset-password/",
        reset_password_view,
        name="user_reset_password",
    ),
    path("<slug:slug>/update/", NewsUpdateView.as_view(), name="news_update"),
    path("<slug:slug>/delete/", NewsDeleteView.as_view(), name="news_delete"),
    path("<slug:slug>/toggle-status/", toggle_status, name="news_toggle_status"),
    path("<slug:slug>/", news_detail, name="news_detail"),
]
