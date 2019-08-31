from django.urls import path
from . import views
urlpatterns = [
    path('listings/', views.listings, name='listings'),
    path('employee_details/<id>/', views.employee_details, name='employee_details'),
    path('listingsjson/', views.listingsjson, name='listingsjson'),

    # search
    path('search', views.search, name='search'),
]
