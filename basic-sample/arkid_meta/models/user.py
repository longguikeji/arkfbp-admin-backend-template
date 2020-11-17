from arkid_meta.models.base import BaseModel
from django.db import models


class User(BaseModel):
    """
    ArkID User
    """

    class Meta:
        """
        set indexes
        """
        indexes = [models.Index(fields=['username'], name='username_index')]

    GENDER_CHOICES = (
        (0, '未知'),
        (1, '男'),
        (2, '女'),
    )
    # TODO 其他账号注册
    ORIGIN_CHOICES = (
        (0, '脚本添加'),
        (1, '管理员添加'),
        (2, '用户名+密码注册'),
        (3, '手机号注册'),
        (4, '电子邮箱注册'),
    )
    username = models.CharField(max_length=255, blank=False, verbose_name='用户名')
    password = models.CharField(max_length=1024, blank=False, verbose_name='账号密码')
    nickname = models.CharField(max_length=255, blank=True, default='', verbose_name='昵称')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    email = models.CharField(max_length=255, blank=True, default='', verbose_name='电子邮箱')
    # 支持 `18812341234`， `+86 18812341234` 两种格式
    mobile = models.CharField(max_length=64, blank=True, default='', verbose_name='手机号')
    origin = models.IntegerField(choices=ORIGIN_CHOICES, default=0, verbose_name='账号来源')
    remark = models.CharField(max_length=512, blank=True, default='', verbose_name='账号备注')
    last_active_time = models.DateTimeField(null=True, verbose_name='最近活跃时间')


class GitHubUser(BaseModel):
    """
    GitHub User
    """

    # class Meta:
    #     """
    #     set indexes
    #     """
    #     indexes = [models.Index(fields=['username'], name='username_index')]

    user = models.OneToOneField(User, verbose_name='用户', related_name='github_user', on_delete=models.PROTECT)
    github_user_id = models.CharField(max_length=255, blank=True, verbose_name='Github ID')


class WechatUser(BaseModel):
    """
    Wechat User
    """

    github_user = models.OneToOneField(GitHubUser, verbose_name='github用户', related_name='github_user', on_delete=models.PROTECT)
    wechat_user_id = models.CharField(max_length=255, blank=True, verbose_name='Github ID')
