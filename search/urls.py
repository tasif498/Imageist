from django.urls import path
from search import views

urlpatterns = [
    path('search/',views.search_api.as_view(),name='search'),
    # path('search/([0-9]+)$',views.search_api.as_view())
]
