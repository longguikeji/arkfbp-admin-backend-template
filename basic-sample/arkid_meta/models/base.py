from django.db import models
import uuid


class ValidManager(models.Manager):
    """
    filter objects which are not deleted
    """
    def get_queryset(self):
        queryset = super(ValidManager, self).get_queryset().filter(is_del=False)
        return queryset


class ActiveManager(ValidManager):
    """
   filter objects which are active
    """
    def get_queryset(self):
        queryset = super(ActiveManager, self).get_queryset().filter(is_active=True)
        return queryset


class BaseModel(models.Model):
    """
    base model, it is abstract
    """
    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    is_del = models.BooleanField(default=False, verbose_name='是否删除')
    is_active = models.BooleanField(default=True, verbose_name='是否可用')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='更新时间')

    objects = models.Manager()
    valid_objects = ValidManager()
    active_objects = ActiveManager()
