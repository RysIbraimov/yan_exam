from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token

from account.views import AuthorRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),

    path('api/register/author/', AuthorRegisterView.as_view()),
    path('api/token/',obtain_auth_token),

    path('api/',include('api.urls')),
]
