# usuarios/signals.py
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver

@receiver(pre_social_login)
def asignar_rol_por_correo(sender, request, sociallogin, **kwargs):
    if sociallogin.is_existing:
        # No hace nada, el rol ya está en la BD
        pass