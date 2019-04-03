from django.db import models
#from accounts.models import User

class Dev(models.Model):
    #user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    github_link = models.CharField(
        verbose_name='GitHub', max_length=600, null=False, blank=False
    )
    contact_link = models.CharField(
        verbose_name='Contato', max_length=600, null=False, blank=False
    )
    profile_photo = models.ImageField(
        verbose_name='Foto de Perfil', blank=True
    )

    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"




