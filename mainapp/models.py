from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    imagen = models.ImageField(upload_to='avatares',null=True,blank= True)

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'

    def __str__(self):
        return f"{self.user} - {self.imagen}"
     