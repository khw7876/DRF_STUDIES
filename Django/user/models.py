from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username = username,
            password = password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField("이메일 주소", max_length=100)
    fullname = models.CharField("이름", max_length=20)
    join_data = models.DateField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' #로그인 할 때 무엇으로 로그인을 할 것인지!!
        
    REQUIRED_FIELDS = [] #로그인 할 때 무엇을 추가로 받을 것이냐.

    objects = UserManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Hobby(models.Model):
    name = models.CharField("취미 이름", max_length=20)

    def __str__(self):
        return self.name
        


class UserProfile(models.Model):
    # user = models.ForeignKey(User, verbose_name="유저", on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(to = User, verbose_name="유저", on_delete=models.CASCADE)
    introduction = models.TextField("자기소개", null=True, blank=True)
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")
    hobby = models.ManyToManyField(Hobby, verbose_name="취미")

    def __str__(self):
        return f"{self.user.username} 님의 프로필입니다."