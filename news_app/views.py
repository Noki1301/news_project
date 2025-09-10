from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView

# Create your views here.


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}
    return render(request, "news/news_list.html", context=context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)
    context = {"news": news}
    return render(request, "news/news_detail.html", context=context)


# def HomePageView(request):
#     news = News.published.all().order_by("-publish_time")[:3]
#     maxalliy_news = News.published.all().filter(category__name="Маҳаллий")[:3]
#     sport_news = News.published.all().filter(category__name="Спорт")[:3]
#     technology_news = News.published.all().filter(category__name="Технология")[:3]
#     external_news = News.published.all().filter(category__name="Хориж")[:3]
#     categories = Category.objects.all()
#     context = {
#         "news": news,
#         "categories": categories,
#         "maxalliy_news": maxalliy_news,
#         "sport_news": sport_news,
#         "technology_news": technology_news,
#         "external_news": external_news,
#     }
#     return render(request, "news/index.html", context=context)


class HomePageView(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["news"] = self.model.published.all().order_by("-publish_time")[:3]
        context["maxalliy_news"] = self.model.published.all().filter(
            category__name="Маҳаллий"
        )[:3]
        context["sport_news"] = self.model.published.all().filter(
            category__name="Спорт"
        )[:3]
        context["technology_news"] = self.model.published.all().filter(
            category__name="Технология"
        )[:3]
        context["external_news"] = self.model.published.all().filter(
            category__name="Хориж"
        )[:3]
        return context


def contactPageView(request):
    context = {}

    return render(request, "news/contact.html", context=context)


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         messages.success(request, "Biz bilan bog'langaningiz uchun rahmat!")
#         return redirect("home_page")
#     context = {"form": form}
#     return render(request, "news/contact.html", context=context)


class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form": form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Biz bilan bog'langaningiz uchun rahmat!")
            return redirect("home_page")
        context = {"form": form}
        return render(request, self.template_name, context=context)


def home_page(request):
    return render(request, "index.html")


def contact_page(request):
    return render(request, "contact.html")


class LocalNewsView(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = "mahalliy_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Маҳаллий")
        return news


class XorijNewsView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = "xorij_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Хориж")
        return news


class TechnologyNewsView(ListView):
    model = News
    template_name = "news/technologiya.html"
    context_object_name = "technologiya_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Технология")
        return news


class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_yangiliklar"

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Спорт")
        return news
