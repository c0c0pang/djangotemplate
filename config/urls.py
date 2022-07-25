
import imp
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from board import views
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('home/', include('board.urls')),
    path('auth/', include('users.urls')),
]
