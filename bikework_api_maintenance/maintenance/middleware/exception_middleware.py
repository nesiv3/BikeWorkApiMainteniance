import traceback
from django.http import JsonResponse

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=500)
