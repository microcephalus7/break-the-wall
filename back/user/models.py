from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django_mysql.models import ListTextField


class Account(User):
    emailId = models.EmailField(max_length=128, unique=True, blank=True)
    kakaoId = models.TextField(max_length=128, unique=True, blank=True)
    appleId = models.TextField(max_length=128, unique=True, blank=True)
    googleId = models.TextField(max_length=128, unique=True, blank=True)
    pubDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class UserStatus(models.TextChoices):
        ACTIVE = "active"
        INACTIVE = 'inActive'
        WITHDRAWAL = 'withdrawal'
    # 유저 상태
    status = models.CharField(
        max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE)
    # 유저 데이터
    # Token 발급 시 갱신
    lastAccessDate = models.DateTimeField(null=True)


class Profile(models.Model):
    # user 참조
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    # 생성일
    pubDate = models.DateTimeField(auto_now_add=True)
    # 수정일
    updateDate = models.DateTimeField(auto_now=True)
    # 유저 실명
    name = models.TextField(max_length=50, blank=True)
    # 전화번호
    phoneNumber = models.TextField(max_length=12, blank=True)
    # 성별
    gender = ['male', 'femail', 'unknown']
    # 생일
    birthday = models.DateField(blank=True)
    # 위치 정보
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    # 취향 정보
    tendencies = ListTextField(
        base_field=CharField(max_length=20),
        size=10,
        max_length=(20 * 11)
    )
