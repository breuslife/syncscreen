from django.urls import path
from screens import views as screens_views

urlpatterns = [
    path("", screens_views.screen_page, name="screen-page"),
]
