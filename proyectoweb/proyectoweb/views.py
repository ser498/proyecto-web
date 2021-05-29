from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

def inicio(request):
    doc_externo = get_template ('inicio.html')
    documento=doc_externo.render()
    return HttpResponse(documento)