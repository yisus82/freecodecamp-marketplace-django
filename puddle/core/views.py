from django.shortcuts import redirect, render
from item.models import Category, Item

from .forms import SignUpForm


def view_404(request, exception=None):
    return redirect('index')


def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
