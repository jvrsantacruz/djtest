# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from filetransfers.api import prepare_upload, serve_file

from djtest.models import PressNew
from djtest.forms import SendPressNewForm


def index(request):
    news = PressNew.objects.all()
    return render_to_response('djtest/news.html', {'news': news},
                             context_instance=RequestContext(request))


@login_required(login_url='/login')
def sendnews(request):
    "Uploads a new PressNew"
    form = SendPressNewForm()
    view_url = reverse('djtest.views.sendnews')

    # Receiving data
    if request.method == "POST":
        form = SendPressNewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('djtest/sent.html', {'new': form},
                                      context_instance=RequestContext(request))

    # Emtpy/Erroneus form
    upload_url, upload_data = prepare_upload(request, view_url)
    return render_to_response('djtest/sendnews.html/',
                              {'form': form, 'upload_url': upload_url,
                               'upload_data': upload_data},
                              context_instance=RequestContext(request))


def pressimg(request, pressnewid):
    "Fall-back to provide public urls to blobstore stored files"
    new = get_object_or_404(PressNew, pk=pressnewid)
    return serve_file(request, new.img)


def register(request):
    "Create a new press new sender account"

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(form.username, form.password1)
            return HttpResponseRedirect(reverse('djtest-main'))

    return render_to_response('registration/register.html', {'form': form},
                              context_instance=RequestContext(request))
