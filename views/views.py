from django.shortcuts import render
from django.apps import apps
from django.contrib import admin


def dashboard(request):
    return render(request, 'dashboard.html', locals())


def changelist(request, app, model):
    model = apps.get_model(app, model)
    title = model._meta.verbose_name_plural

    model_admin = admin.site._registry.get(model)
    if model_admin:
        list_display = model_admin.list_display
    else:
        list_display = None

    values = model.objects.all()

    return render(request, 'base/changelist.html', locals())