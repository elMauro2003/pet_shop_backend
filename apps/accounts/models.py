from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Usuario'),
        ('shelter', 'Refugio/Protectora'),
        ('admin', 'Administrador'),
        ('volunteer', 'Voluntario'),
    )
    
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('teléfono'), max_length=20, blank=True)
    role = models.CharField(_('rol'), max_length=20, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(_('biografía'), blank=True)
    location = models.CharField(_('ubicación'), max_length=255, blank=True)
    is_verified = models.BooleanField(_('verificado'), default=False)
    created_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    updated_at = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    
    # Campos específicos para refugios
    shelter_name = models.CharField(_('nombre del refugio'), max_length=255, blank=True)
    shelter_description = models.TextField(_('descripción del refugio'), blank=True)
    shelter_logo = models.ImageField(_('logo del refugio'), upload_to='shelter_logos/', blank=True, null=True)
    shelter_website = models.URLField(_('sitio web del refugio'), blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        ordering = ['-date_joined']
    
    def __str__(self):
        if self.role == 'shelter' and self.shelter_name:
            return f"{self.shelter_name} ({self.email})"
        return self.email
    
    @property
    def is_admin(self):
        return self.role == 'admin'
    
    @property
    def is_shelter(self):
        return self.role == 'shelter'
    
    @property
    def is_volunteer(self):
        return self.role == 'volunteer'