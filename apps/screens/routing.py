from django.urls import path
from screens.consumers import ScreenConsumer

# Here, "" is routing to the URL ScreenConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path("", ScreenConsumer.as_asgi()),
]
