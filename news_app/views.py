from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def news_list(request):
    news_list = News.published.all()
    context = {"news_list": news_list}
    return render(request, "news/news_list.html", context=context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {"news": news}
    return render(request, "news/news_detail.html", context=context)


def HomePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {"news": news, "categories": categories}
    return render(request, "news/index.html", context=context)


def contactPageView(request):
    context = {}

    return render(request, "news/contact.html", context=context)


def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Biz bilan bog'langaningiz uchun rahmat!")
        return redirect("home_page")
    context = {"form": form}
    return render(request, "news/contact.html", context=context)
