from django import template

register = template.Library()

# Example
# @register.simple_tag
# def multiply(value, arg):
#     return value * arg


@register.simple_tag
def menu(user):
    from django.contrib.auth.models import User
    from base.models import Menu

    print(f"\n\n passei aqui USER: {user} \n\n")

    try:
        _user = User.objects.get(pk=user)

        if _user.is_active:
            print(f"\n\n passei aqui 2 USER: {_user.pk} \n\n")
            if _user.is_staff:
                return Menu.objects.filter(admin=False, support=True)
            elif _user.is_superuser:
                return Menu.objects.filter(admin=True, support=True)
            
            # return Menu.objects.filter(admin=False, support=False)
            return [dict(name="TESTE", icon="teste"),]
    except:
        return [dict(name="TESTE", icon="teste"),]
