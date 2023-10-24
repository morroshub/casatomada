from django import forms

class RespuestaForm(forms.Form):
    respuesta = forms.BooleanField(required=True)