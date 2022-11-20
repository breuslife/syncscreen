from django.db import models

from screens.mixins import AsyncMixin


class Screen(AsyncMixin):
	message = models.TextField()
