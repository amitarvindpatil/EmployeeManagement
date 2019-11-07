from django.urls import path
from . import views
urlpatterns = [
    path('listings/', views.EmployeeFrontView.listings, name='listings'),
    path('employee_details/<id>/',
         views.EmployeeFrontView.employee_details, name='employee_details'),
    path('listingsjson/', views.EmployeeFrontView.listingsjson, name='listingsjson'),

    # search
    path('search', views.EmployeeFrontView.search, name='search'),
]
