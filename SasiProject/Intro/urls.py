from django.urls import path

from . import views

urlpatterns = [
    path('', views.greet,name='demo-page'),
    path('hai', views.hello, name='DTL-page'),
]
