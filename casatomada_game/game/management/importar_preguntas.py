from django.core.management.base import BaseCommand
from game.models import Pregunta, Respuesta

class Commandimport(BaseCommand):
    help = 'Importa preguntas desde diccionarios y carga en la base de datos'

    def handle(self, *args, **kwargs):
        # Define tus diccionarios de preguntas y respuestas aquí
        dicc_preguntas_respuestas = [
            {
                'p1': {
                    'pregunta': '¿La casa en la historia es un lugar de seguridad para los personajes al principio?',
                    'respuesta': True
                },
                'p2': {
                    'pregunta': '¿Los personajes principales sienten que la casa está siendo invadida?',
                    'respuesta': False
                },
                'p3': {
                    'pregunta': '¿La casa está situada en una ciudad grande?',
                    'respuesta': False
                },
                'p4': {
                    'pregunta': '¿La historia se desarrolla en una casa antigua?',
                    'respuesta': True
                },
                'p5': {
                    'pregunta': '¿Los personajes intentan luchar contra la invasión de la casa?',
                    'respuesta': False
                },
                'p6': {
                    'pregunta': '¿El cuento utiliza elementos sobrenaturales para crear su atmósfera?',
                    'respuesta': True
                },
                'p7': {
                    'pregunta': '¿La relación entre los personajes principales está clara en la narrativa?',
                    'respuesta': True
                },
                'p8': {
                    'pregunta': '¿El cuento se enfoca principalmente en el diálogo entre los personajes?',
                    'respuesta': False
                },
                'p9': {
                    'pregunta': '¿La historia tiene un final ambiguo?',
                    'respuesta': True
                },
                'p10': {
                    'pregunta': '¿El cuento "La Casa Tomada" fue escrito por Julio Cortázar?',
                    'respuesta': True
                },
                'p11': {
                    'pregunta': '¿El cuento "La Casa Tomada" de Julio Cortázar es conocido por su estilo de escritura evocador?',
                    'respuesta': True
                },
                'p12': {
                    'pregunta': '¿La historia explora temas de aislamiento y pérdida?',
                    'respuesta': True
                },
                'p13': {
                    'pregunta': '¿Los personajes principales son hermanos en el cuento?',
                    'respuesta': False
                },
                'p14': {
                    'pregunta': '¿La narración se vuelve cada vez más expansiva a medida que avanza la historia?',
                    'respuesta': False
                }
            }
        ]

        for pregunta in dicc_preguntas_respuestas:
            pregunta = Pregunta.objects.create(texto_pregunta=pregunta['pregunta'])
            Respuesta.objects.create(pregunta=pregunta, respuesta=pregunta['respuesta'])

        self.stdout.write(self.style.SUCCESS('Preguntas importadas exitosamente.'))

