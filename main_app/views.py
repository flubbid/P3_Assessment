from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish
from django.shortcuts import render

# Create your views here.
def wish_index(request):
    wish = Wish.objects
    return render(request, 'index.html', {'wish':wish})

class WishCreate(CreateView):
    model = Wish
    fields = ['description']



