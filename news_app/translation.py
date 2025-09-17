from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "body")  # tarjimani ishlatish uchun 1-usul bu


# translator.register(Category) bu 2-usul
register(Category)


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
