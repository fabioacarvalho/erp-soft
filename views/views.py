from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html', locals())


def changelist(request, app, model):
    return render(request, 'base/changelist.html', locals())