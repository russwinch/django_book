from datetime import date
from django.shortcuts import render, get_object_or_404

from . models import Page


def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    current_year = date.today().year
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'current_year': current_year,
        'pages_list': Page.objects.all()
    }
    # assert False
    return render(request, 'pages/page.html', context)
