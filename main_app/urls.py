from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wish_index, name="index"),
    path('create/', views.WishCreate.as_view(), name="create"),
    path('accounts/', include('django.contrib.auth.urls')),
]
