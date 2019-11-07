from django.shortcuts import render, redirect, get_object_or_404
from .models import Role, Role_permissions
from django.contrib import messages, auth
from permission.models import Permissions


class RoleClass:

    def role_list(request):
        role_list = Role.objects.order_by('-id')

        role_context = {
            'role_list': role_list
        }
        return role_context


class RolePermissionsClass:

    def permisiondata():
        perdata = Permissions.objects.all()
        per_context = {
            'perdata': perdata
        }
        return per_context

    def role_permissions(request, id):
        role_perm = get_object_or_404(Role, pk=id)
        perm_context = RolePermissionsClass.permisiondata()

        role_context = {
            'role_perm': role_perm
        }

        def mergedata(role_context, perm_context):
            mgdata = {**role_context, **perm_context}
            return mgdata

        context = mergedata(role_context,
                            perm_context)

        return context

    def give_permissions(request, id):
        if request.method == "POST":

            roles = id
            print(roles)
            permissions = request.POST['permissions']
            print(permissions)
            if Role_permissions.objects.filter(roles_id=roles, permissions_id=permissions).exists():
                messages.error(request, 'Permission already provide')
                return redirect('role_list')
            else:

                roleermission_data = Role_permissions.objects.create(
                    roles_id=roles, permissions_id=permissions)
                rolepermission_data.save()
                messages.success(request, "Data Added successfully")

        return redirect('role_list')

    def check_permissions(request):
        check_per = Role_permissions.objects.all()
        check_context = {
            'check_per': check_per
        }
        return check_context
