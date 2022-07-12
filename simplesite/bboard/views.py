from django.http import HttpResponse
from django.template import loader

from .models import Bb

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs':bbs}
    return HttpResponse(template.render(context, request))

def another(request):
    list_publish = 'List with publish \r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        list_publish += bb.title + '\r\n'+ bb.content + '\r\n\r\n'
    return HttpResponse(list_publish, content_type='text/plain; charset=utf-8')