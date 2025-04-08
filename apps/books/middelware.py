from django.utils import translation
from django.conf import settings

class BooksLangMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_code = request.session.get('language')
        language = request.path.split('/')[1]
        if language not in ['uz', 'ru', 'en'] and language_code not in ['uz', 'ru', 'en']:
            language_code = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        elif language:
            request.session['language'] = language
            language_code = language
        translation.activate(language_code)

        response = self.get_response(request)
        return response
