from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.html import strip_tags
from rss.models import In, Tags, Feed, Subscription
from django.contrib.auth.models import User
from time import mktime
from datetime import date, datetime
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
    for i in entries:
        for j in Tags.objects.all():
            if(i['summary'].lower().find(j.tag_ltrack) > -1 or i['title'].lower().find(j.tag_ltrack) > -1):
                if(Feed.objects.filter(title=i['title']).count() == 0):
                    #f = Feed(title=i['title'], link=i['link'], summary=i['summary'], published=datetime.fromtimestamp(mktime(i['published_parsed'])), tag=j.tag_name)
                    f = Feed(title=i['title'], link=i['link'], summary=i['summary'],
                             published=i['published_parsed'])
                    f.tags = j.tag_ltrack
                    f.save()
                    f.tags_track.add(j)
                    f.save()
                else:
                    f = Feed.objects.filter(title=i['title'])
                    for fe in f:
                        if(j not in fe.tags_track.all()):
                            fe.tags_track.add(j)
                            fe.tags = fe.tags + "; " + j.tag_ltrack
                            fe.save()

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


def viz(request):
    today = date.today()
    u = []
    for i in range(1, 13):
        users = User.objects.filter(date_joined__year=today.year,
                                    date_joined__month=i).count()
        u.append(users)
    return render_to_response("view/viz.html", {'users': u},
                              context_instance=RequestContext(request))


def tracker(request):
    su = Subscription.objects.filter(user=request.user)[0]
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../")
    if request.method == 'POST':
        track = request.POST['track']
        t = None
        if Tags.objects.filter(tag_ltrack=track.lower()).count() == 0:
            t = Tags(tag_ltrack=track.lower(), tag_name=track)
            t.save()
        else:
            t = Tags.objects.filter(tag_ltrack=track.lower())[0]
        #if su.subs.filter(id_tag=[t.id_tag]).count() == 0:
        su.subs.add(t)
        su.save()
    return render_to_response("view/tracker.html", {'subs': su},
                              context_instance=RequestContext(request))

def trackertag(request, tag):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("../")
    t = Tags.objects.filter(tag_ltrack=tag.lower())[0]
    feeds = Feed.objects.filter(tags_track__in=[t.id_tag])
    return render_to_response("view/trackertag.html", {'feeds':feeds},
                              context_instance=RequestContext(request))


def tracked(request):
    return render(request, "view/tracked.html")


def about(request):
    return render(request, "view/about.html")


def error_404(request):
    return render(request, "view/404.html")


def error_500(request):
    return render(request, "view/500.html")
