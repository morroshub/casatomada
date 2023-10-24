#Llamadas a modulos de django
from django.http import HttpResponse
from django.shortcuts import render, redirect



#Llamadas archivos dentro del projecto
from .models import Pregunta
from .models import Pregunta, Respuesta

from .forms import RespuestaForm
from .forms import RespuestaForm




def jugar_juego(request):
    pregunta = Pregunta.objects.order_by('?').first()  # Seleccionar una pregunta aleatoria
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['respuesta'] == pregunta.es_correcta:
                # La respuesta es correcta
                # Realiza la lógica para avanzar al siguiente nivel o tarea del juego
                return redirect('siguiente_nivel')
            else:
                # La respuesta es incorrecta, maneja la pérdida de vidas
                return redirect('perder_vida')
    else:
        form = RespuestaForm()

    return render(request, 'juego.html', {'pregunta': pregunta, 'form': form})


def mi_vista(request):
    # Lógica de la vista
    return render(request, 'templates/juego.html')



def juego(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = Respuesta(pregunta=pregunta, respuesta=form.cleaned_data['respuesta'])
            respuesta.save()
            return redirect('siguiente_pregunta')  # Redirige a la siguiente pregunta o acción

    else:
        form = RespuestaForm()

    return render(request, 'miapp/juego.html', {'pregunta': pregunta, 'form': form})
