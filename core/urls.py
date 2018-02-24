"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from Playbook import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'SME', views.SMEViewSet)
router.register(r'Team', views.TeamViewSet)
router.register(r'Calendar', views.CalendarViewSet)
router.register(r'Schedule', views.ScheduleViewSet)
router.register(r'ScheduleRotation', views.ScheduleRotationViewSet)
router.register(r'Actions', views.ActionsViewSet)
router.register(r'Play', views.PlayViewSet)
router.register(r'PlayBook', views.PlayBookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls), name='api'),
]
