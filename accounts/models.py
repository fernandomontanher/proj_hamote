from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name, password, is_staff, is_superuser, is_admin, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name = first_name,
            last_name = last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            is_admin=is_admin,
            date_joined=now(),
            last_login=now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, first_name , last_name, password=None):
        return self._create_user(
            email,
            first_name,
            last_name,
            password,
            False,
            False,
            False,
            **extra_fields
        )

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password,
            True,
            True,
            True,
            **extra_fields
        )
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    date_joined = models.DateTimeField(default=timezone.now())
    last_login = models.DateTimeField(default=timezone.now())
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )
    is_active = models.BooleanField(_('user status'), default=True,)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
    )

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

