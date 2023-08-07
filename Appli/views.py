from django.shortcuts import render
from . import models
import random

def word_generator_sheet1(request):
    generated_word = models.Sheet1.objects.all()
    return random.choice(generated_word)


def word_generator_sheet2(request):
    generated_word = models.Sheet2.objects.all()
    return random.choice(generated_word)


def word_generator_sheet3(request):
    generated_word = models.Sheet3.objects.all()
    return random.choice(generated_word)


def word_generator_sheet4(request):
    generated_word = models.Sheet4.objects.all()
    return random.choice(generated_word)


def word_generator_sheet5(request):
    generated_word = models.Sheet5.objects.all()
    return random.choice(generated_word)


def display(request):
    generated_word = None
    if request.method == "POST":
        sheet = request.POST.get("Sheet")
        if sheet == 'Sheet1':
            generated_word = word_generator_sheet1(request)
        elif sheet == 'Sheet2':
            generated_word = word_generator_sheet2(request)
        elif sheet == 'Sheet3':
            generated_word = word_generator_sheet3(request)
        elif sheet == 'Sheet4':
            generated_word = word_generator_sheet4(request)
        elif sheet == 'Sheet5':
            generated_word = word_generator_sheet5(request)
        else:
            return render(request, 'Appli/word_list.html', {'generated_word':None})
    
    return render(request, 'Appli/word_list.html', {'generated_word':generated_word})