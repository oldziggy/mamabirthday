from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Wish

def index(request):
    wish_count = Wish.objects.count() #pyright: ignore
    context = {'wish_count': wish_count}
    return render(request, 'wishes/index.html', context)

def detail(request, wish_id = None):
    if wish_id == None:
        cur_wish = Wish.objects.last()                    # pyright: ignore
    else:
        cur_wish = get_object_or_404(Wish, id=wish_id)

    prev_wish = Wish.objects .filter(pub_date__lt=cur_wish.pub_date).order_by('pub_date').last()# pyright: ignore
    next_wish = Wish.objects.filter(pub_date__gt=cur_wish.pub_date).order_by('pub_date').first()# pyright: ignore

    prev_id = prev_wish.id if prev_wish else None
    next_id = next_wish.id if next_wish else None

    context = {'cur_wish_text': cur_wish.wish_text, 'prev_id': prev_id, 'next_id': next_id}
    return render(request, 'wishes/detail.html', context)



