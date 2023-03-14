from django.shortcuts import redirect, render
from item.models import Category, Item


def view_404(request, exception=None):
    return redirect('index')


def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})


def contact(request):
    return render(request, 'core/contact.html')
