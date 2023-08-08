from django.shortcuts import render, redirect
from .models import Sheet1, Sheet2, Sheet4, Sheet5
import random


def reset(request):
    if request.method == "POST":
        Sheet1.objects.update(used=False)
        Sheet2.objects.update(used=False)
        Sheet4.objects.update(used=False) 
        Sheet5.objects.update(used=False) 
        return redirect('display')
    return render(request, 'Appli/word_list.html', {'generated_word':None})


def word_generator_sheet1(request):
    generated_word = Sheet1.objects.filter(used=False)
    if generated_word.exists():
        generated_word = random.choice(generated_word)
        generated_word.used = True
        generated_word.save()
        return generated_word


def word_generator_sheet2(request):
    generated_word = Sheet2.objects.filter(used=False)
    if generated_word.exists():
        generated_word = random.choice(generated_word)
        generated_word.used = True
        generated_word.save()
        return generated_word


# def word_generator_sheet3(request):
#     generated_word = Sheet3.objects.all()
#     return random.choice(generated_word)


def word_generator_sheet4(request):
    generated_word = Sheet4.objects.filter(used=False)
    if generated_word.exists():
        generated_word = random.choice(generated_word)
        generated_word.used = True
        generated_word.save()
        return generated_word


def word_generator_sheet5(request):
    generated_word = Sheet5.objects.filter(used=False)
    if generated_word.exists():
        generated_word = random.choice(generated_word)
        generated_word.used = True
        generated_word.save()
        return generated_word


def display(request):
    generated_word = None
    if request.method == "POST":
        sheet = request.POST.get("Sheet")
        if sheet == 'Sheet1':
            generated_word = word_generator_sheet1(request)
        elif sheet == 'Sheet2':
            generated_word = word_generator_sheet2(request)
        # elif sheet == 'Sheet3':
        #     generated_word = word_generator_sheet3(request)
        elif sheet == 'Sheet4':
            generated_word = word_generator_sheet4(request)
        elif sheet == 'Sheet5':
            generated_word = word_generator_sheet5(request)
        else:
            return render(request, 'Appli/word_list.html', {'generated_word':None})
    
    return render(request, 'Appli/word_list.html', {'generated_word':generated_word})