from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

"""
You need to include viewset differently to a view - through a router
Router generates a list of URLs, which we then include in path with the include function
"""
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
