from django.shortcuts import redirect, render


def view_404(request, exception=None):
    return redirect('index')


def index(request):
    return render(request, 'core/index.html')


def contact(request):
    return render(request, 'core/contact.html')
