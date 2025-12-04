from django.contrib import admin
from django.urls import path, include  # <-- 'include' is the key function here
from core import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('accounts/', include('allauth.urls')),
]
