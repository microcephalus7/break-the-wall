from django.db import models
from django.contrib.postgres.fields import ArrayField


class Account(models.Model):
    emailId = models.EmailField(max_length=128)
    email = models.EmailField(max_length=128)
    kakaoId = models.TextField(max_length=100)
    appleId = models.TextField(max_length=100)
    googleId = models.TextField(max_length=100)
    password = models.EmailField(max_length=50)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.email) > 20:
            return self.email[0:20] + '...'
        return self.email


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now_add=True, null=True)
    updateDate = models.DateTimeField(auto_now=True)
    name = models.TextField(max_length=20, null=True)
    nickname = models.TextField(max_length=50, null=True)
    cellPhone = models.TextField(max_length=12, null=True)
    # 유저 상태
    status = ['active', 'inActive', "withdrawal"]
    gender = ['male', 'femail', 'unknown']
    birthday = models.DateField(null=True)
    # 위치 정보
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def checkProfile(self):
        if None in [self.account, self.phoneNumber, self.username, self.male, self.birthday]:
            return False
        else:
            return True

    def __str__(self) -> str:
        return self.username
