from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html')


def reverse(requests):
    return render(requests, 'reverse.html')
