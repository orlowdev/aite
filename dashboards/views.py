from django.shortcuts import render


def dashboard_main(request):
    return render(request, 'calendar.html')
