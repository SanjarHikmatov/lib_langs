from .models import Book
from modeltranslation.translator import translator, TranslationOptions

class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Book, BookTranslationOptions)
