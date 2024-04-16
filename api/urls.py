from django.urls import path
from .views import CardApiView,OneCardApiView


urlpatterns = [
    path('cards/', CardApiView.as_view(), name='cards'),
    path('one-card/', OneCardApiView.as_view(), name='one_card'),

]