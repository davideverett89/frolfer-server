"""frolfer_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
from frolferapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'courses', Courses, 'course')
router.register(r'holes', Holes, 'hole')
router.register(r'pins', Pins, 'pin')
router.register(r'players', Players, 'player')
router.register(r'rounds', Rounds, 'round')
router.register(r'round_holes', RoundHoles, 'round_hole')
router.register(r'score_cards', ScoreCards, 'score_card')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('logout', logout_user),
    # path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
