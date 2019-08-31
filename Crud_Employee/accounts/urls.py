from django.urls import path
from . import views
urlpatterns = [

    # Login Authentication Urls
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    # data Retrivation URls
    path('dashboard', views.dashboard, name='dashboard'),

    # data creation URls
    path('add_record', views.add_record, name='add_record'),
    path('create_employee', views.create_employee, name='create_employee'),
    # data Modification URls
    path('edit_info/<id>/', views.edit_info, name='edit_info'),
    path('update_data/<id>', views.update_data, name='update_data'),
    path('update_file/<id>', views.update_file, name='update_file'),

    # data Deletion URls
    path('del_info/<id>/', views.del_info, name='del_info'),
    path('del_data/<id>', views.del_data, name='del_data'),


]
