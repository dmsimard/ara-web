from django.shortcuts import render


def handle_400(request):
    args = {
        'kind': 'HTTP 400: Bad Request'
    }
    return render(request, 'error.html', args, status=400)


def handle_403(request):
    args = {
        'kind': 'HTTP 403: Forbidden'
    }
    return render(request, 'error.html', args, status=403)


def handle_404(request):
    args = {
        'kind': 'HTTP 404: Not Found'
    }
    return render(request, 'error.html', args, status=404)


def handle_500(request):
    args = {
        'kind': 'HTTP 500: Internal Server Error'
    }
    return render(request, 'error.html', args, status=400)
