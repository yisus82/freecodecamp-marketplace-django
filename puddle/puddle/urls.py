from core.views import contact, index
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]

handler404 = 'core.views.view_404'
