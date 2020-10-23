from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def generate_secret():
    x = random.sample([1,2,3,4,5,6,7,8,9,0],4)
    return x

def count_bulls(answer,guess):
    i = 0
    bulls = 0
    while i < len(guess):
        if guess[i] == answer[i]:
            bulls += 1
        i += 1
    return bulls


def count_cows(answer,guess):
    i = 0
    cows = 0
    while i < len(guess):
        if guess[i] in answer:
            cows += 1
        i += 1
    return cows


def secret_code(request):
    answer = generate_secret()
    guess = [1,3,6,9]
    bulls = count_bulls(answer,guess)
    cows = count_cows(answer,guess)

    return render(request,template_name='api/home.html',context={'bulls':bulls,'cows':cows})



