from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.html import strip_tags
from rss.models import In
from django.contrib.auth.models import User
from time import mktime
from datetime import datetime, date
import feedparser


def index(request):
    entries = []
    for r in In.objects.all():
        rss = r.url
        feed = feedparser.parse(rss)
        for i in feed['items']:
            i['summary'] = strip_tags(i['summary'])
            i['published_parsed'] = \
                datetime.fromtimestamp(mktime(i['published_parsed']))
        entries.extend(feed['items'])
        entries = sorted(entries, key=lambda entry: entry["published"])
        entries.reverse()
    return render_to_response("view/index.html", {'feed': entries},
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


def rss(request):
    rss = "http://www.24ur.com/rss/"
    feed = feedparser.parse(rss)
    for i in feed['items']:
        i['summary'] = strip_tags(i['summary'])
    return render_to_response("view/rss.html", {'feed': feed['items']})


def viz(request):
    today = date.today()
    u = []
    for i in range(1, 13):
        users = User.objects.filter(date_joined__year=today.year,
                                    date_joined__month=i).count()
        u.append(users)
    return render_to_response("view/viz.html", {'users': u})


def analysis(request):
    return render(request, "view/analysis.html")


def about(request):
    return render(request, "view/about.html")


def error_404(request):
    return render(request, "view/404.html")


def error_500(request):
    return render(request, "view/500.html")
