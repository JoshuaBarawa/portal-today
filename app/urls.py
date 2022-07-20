
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('item/', ItemList.as_view()),
    path('item/<str:pk>/', ItemDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)