from django.shortcuts import render, redirect, get_object_or_404
from .models import Permissions
from django.contrib import messages, auth


class PermissionClass:

    def permission_list(request):
        permission_list = Permissions.objects.order_by('-id')

        permission_context = {
            'permission_list': permission_list
        }
        return permission_context
