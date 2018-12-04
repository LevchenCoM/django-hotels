"""bna_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from pages import views as pages_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', include('home.urls')),
    path('apartments/',include('apartments.urls')),
    path('reservations/',include('reservations.urls')),
    path('user/',include('user.urls')),
    path('contact/',include('contact.urls')),
    path('about-us/', pages_views.about_us),
    path('blog/', include('blog.urls')),
) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
