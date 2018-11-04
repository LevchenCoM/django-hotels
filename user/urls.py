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

from django.urls import path
from django.urls import reverse_lazy
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('sign-in/', auth_views.LoginView.as_view(template_name = 'user_auth/sign-in.html'), name='user-sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(next_page = reverse_lazy('home')), name='user-sign-out'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name = 'user_auth/change-password.html'), name="change_password"),
    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'user_auth/change-password-done.html'), name="password_change_done"),
    path('sign-up/', views.sign_up, name="user-sign-up"),
]
