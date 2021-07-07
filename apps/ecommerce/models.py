from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password):
        
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        usuario = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    
    def create_superuser(self, email, username, password):
        usuario = self.create_user(
            email,
            username = username,
            password = password,
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario
    
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length= 100)
    email = models.EmailField('Correo electronico', unique=True, max_length=254)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta: 
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
                
    def __str__(self):
        return f'{self.username}'
    
    def has_perm(self, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    
