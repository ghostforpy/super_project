from django.contrib.auth import models
from django.db import models as md
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for super project."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    image = ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Image(md.Model):
    """Product images model."""
    image = md.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    position = md.IntegerField(default=1)

    class Meta:
        verbose_name = 'Изображения продуктов'
        verbose_name_plural = 'Изображения продуктов'
