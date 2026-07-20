from django.db import models

from apps.core import translations
from apps.users.models import User


class TimeStamp(models.Model):
    """
    An abstract base class model that provides self-updating
    `created_at` and `updated_at` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=translations.CREATED_AT)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=translations.UPDATED_AT)

    class Meta:
        abstract = True


class UserObject(models.Model):
    created_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="%(class)s_created_objects", verbose_name=translations.CREATED_BY)
    updated_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="%(class)s_updated_objects", verbose_name=translations.UPDATED_BY)

    class Meta:
        abstract = True
