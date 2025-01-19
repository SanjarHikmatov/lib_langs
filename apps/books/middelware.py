from django.utils import translation


class BooksLangMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        old_language = request.session.get('language')
        language = request.POST.get('language', old_language)
        if language not in ["uz", "en","ru"]:
            language = 'uz'
        language_code = {
            'uz': 'uz',
            'en': 'en',
            'ru': 'ru',
        }.get(language, 'uz')

        translation.activate(language_code)
        request.session['language'] = language

        response = self.get_response(request)

        return response
