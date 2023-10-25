
# Pregunta: Representa una pregunta que se mostrará en el juego.
# PerfilUsuario: Extiende el modelo de usuario incorporado de Django para almacenar información adicional, como el puntaje del usuario en el juego.

from django.db import models
from django.contrib.auth.models import User



# class PerfilUsuario(models.Model):
# #     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
# #     puntaje = models.IntegerField(default=0)

# #     class Meta:
# #         app_label = 'game'  

# class Pregunta(models.Model):
#     texto_pregunta = models.CharField(max_length=255)
#     es_correcta = models.BooleanField(default=False)

# class Respuesta(models.Model):
#     pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
#     respuesta = models.BooleanField()  # True o False, según la respuesta del usuario

#     def __str__(self):
#         return f"Respuesta a la pregunta {self.pregunta.id}: {self.respuesta}"


