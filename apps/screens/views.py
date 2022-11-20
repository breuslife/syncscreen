from django.shortcuts import render, redirect

from screens.models import Screen


def screen_page(request, *args, **kwargs):
    screen, _ = Screen.objects.get_or_create(id=1)
    context = {
        'screen': screen,
    }
    return render(request, "screens/screen_page.html", context)
