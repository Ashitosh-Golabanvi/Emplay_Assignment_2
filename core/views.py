from django.http import JsonResponse

def status(request):
    return JsonResponse({'status': 'alive'}, status=200)
