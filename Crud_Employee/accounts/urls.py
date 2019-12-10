from django.urls import path

from . import views
urlpatterns = [

    # Login Authentication Urls
    path('registration', views.Authentication.registration, name='registration'),
    path('login', views.Authentication.login, name='login'),
    path('logout', views.Authentication.logout, name='logout'),
    #     path('edit_changepassword/<id>/',
    #          views.Authentication.edit_changepassword, name='edit_changepassword'),
    #     path('changepassword/<id>', views.Authentication.changepassword,
    #          name='changepassword'),


    # data Retrivation URls
    path('dashboard', views.Employees.dashboard, name='dashboard'),
    path('myprofile', views.Employees.myprofile, name='myprofile'),


    # Reports
    path('desginationwise_count', views.Reports.desginationwise_count,
         name='desginationwise_count'),

    # data creation URls
    path('add_record', views.Employees.add_record, name='add_record'),
    path('emp_search', views.Employees.emp_search, name='emp_search'),
    path('create_employee', views.Employees.create_employee, name='create_employee'),
    # data Modification URls
    path('edit_info/<id>/', views.Employees.edit_info, name='edit_info'),

    path('edit_empuser/<id>/', views.Employees.edit_empuser, name='edit_empuser'),
    path('update_data/<id>', views.Employees.update_data, name='update_data'),
    path('update_file/<id>', views.Employees.update_file, name='update_file'),

    # data Deletion URls
    path('del_info/<id>/', views.Employees.del_info, name='del_info'),
    path('del_data/<id>', views.Employees.del_data, name='del_data'),


    # -----------------------Department Urls---------------------
    path('add_dept', views.Departments.add_dept, name='add_dept'),
    path('department_list', views.Departments.department_list,
         name='department_list'),


    # --------------------Employee Authentications------------------

    path('auth_permission_dash', views.auth_permission_dash,
         name='auth_permission_dash'),



    # ----------------------Designations---------------------------


    path('add_designation', views.Designations.add_designation,
         name='add_designation'),
    path('designation_list',
         views.Designations.designation_list, name='designation_list'),
    path('edit_designation/<int:id>/',
         views.Designations.edit_designation, name='edit_designation'),

    path('update_designation/<int:id>',
         views.Designations.update_designation, name='update_designation'),

    path('del_designation/<int:id>/',
         views.Designations.del_designation, name='del_designation'),

    path('delete_designation/<int:id>',
         views.Designations.delete_designation, name='delete_designation'),

    # -----------------------Roles------------------------------------
    path('role_list',
         views.Roles.role_list, name='role_list'),

    path('role_permissions/<int:id>/',
         views.RolePermissions.role_permissions, name='role_permissions'),

    path('give_permissions/<int:id>',
         views.RolePermissions.give_permissions, name='give_permissions'),

    path('check_permissions',
         views.RolePermissions.check_permissions, name='check_permissions'),

    # -------------------Permissions---------------------------------
    path('permission_list',
         views.Permissions.permission_list, name='permission_list'),


]
