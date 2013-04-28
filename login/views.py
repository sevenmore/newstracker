from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("../")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("../")
            else:
            # Return a 'disabled account' error message
                return HttpResponse("<ul><li><a href=\"/\">Index""</a>"
                                    "</li></ul>Disabled account")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<ul><li><a href=\"/\">Index</a>"
                                "</li></ul>Invalid login")
    else:
        return render(request, 'login/index.html')


def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    auth.logout(request)
    return HttpResponse("<ul><li><a href=\"/\">Index</a>"
                        "</li></ul>You've been logged out.")


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()
    return render_to_response("login/register.html", {'form': form, })
