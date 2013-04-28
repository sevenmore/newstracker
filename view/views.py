from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect


def index(request):
    return render_to_response("view/index.html",
                              context_instance=RequestContext(request))


def account(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if first_name:
            request.user.first_name = first_name
        if last_name:
            request.user.last_name = last_name
        if email:
            request.user.email = email
        if password:
            request.user.set_password(password)
        request.user.save()
        return render_to_response("view/account.html",
                                  context_instance=RequestContext(request))
    else:
        return render_to_response("view/account.html",
                                  context_instance=RequestContext(request))


def save(self, commit=True):
    self.user.set_password(self.cleaned_data['new_password1'])
    if commit:
        self.user.save()
    return self.user


def viz(request):
    return render(request, "view/viz.html")


def analysis(request):
    return render(request, "view/analysis.html")


def about(request):
    return render(request, "view/about.html")


def error_404(request):
    return render(request, "view/404.html")


def error_500(request):
    return render(request, "view/500.html")
