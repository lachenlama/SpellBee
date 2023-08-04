from django.shortcuts import render
from .models import Sheet1
from random import randrange

def word_list(request):
    words = Sheet1.objects.all()
    n = randrange(len(words))
    generated_word = words[n]
    return render(request, 'Appli/word_list.html', {'generated_word':generated_word})