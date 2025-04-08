from django.utils.translation import activate  # Bu yerda activate funksiyasini import qilish kerak
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = [
            "title_ru",
            "title_uz",
            "title_en",
            'description_uz',
            'description_en',
            'description_ru',
        ]

    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if not instance.translate_fields:
    #         return representation
    #     for i in instance.translate_fields:
    #         language = self.context["request"].session["language"]
    #         representation[i] = getattr(instance, f"{i}_{language}")
    #     return representation