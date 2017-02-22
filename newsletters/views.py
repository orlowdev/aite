from django.contrib import messages
from django.shortcuts import render, redirect


def subscription(request):
    messages.add_message(
        'success',
        'You successfully subscribed to AITE newsletter! Keep in touch!'
    )

    return redirect('index')
