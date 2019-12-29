from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from marriage.models import Guest
from django.http import Http404
from django.http import HttpResponseRedirect

# MAIN WEB PAGES

def index(request):
    return render(request, 'marriage/main-page/index.html')

# CLIENT WEB PAGES

def get_latest_messages():
    return Guest.objects.exclude(message='').exclude(message='-').order_by('pub_date')


def get_guest_name(param_id, param_guest_name):
    try:
        g = Guest.objects.get(id=param_id, guest_name=param_guest_name)
    except Guest.DoesNotExist:
        raise Http404("Guest with combination of id:%s and name:%s does not exist" % (str(param_id), str(param_guest_name)))
    return g.guest_name


def tania_dika_index(request):
    template = loader.get_template('marriage/tania-dika/index.html')
    context = {
        'latest_messages' : get_latest_messages(),
        'guest_name' : False
    }
    return HttpResponse(template.render(context, request))


def tania_dika_invitation(request, param_id, param_guest_name):
    template = loader.get_template('marriage/tania-dika/index.html')
    context = {
        'latest_messages' : get_latest_messages(),
        'guest_name' : get_guest_name(param_id, param_guest_name),
        'guest_id' : param_id,
    }
    return HttpResponse(template.render(context, request))


def tania_dika_submit_message(request, param_id, param_guest_name):
    if(request.method == 'POST'):
        try:
            g = Guest.objects.get(id=param_id, guest_name=param_guest_name)
            g.guest_role = request.POST['guest_role']
            g.message = request.POST['message']
            g.save()
        except Guest.DoesNotExist:
            raise Http404("Guest with combination of id:%s and name:%s does not exist" % (str(param_id), str(param_guest_name)))
        
    return HttpResponseRedirect('/tania-dika/%s/%s#notes_section' % (str(param_id), str(param_guest_name)))