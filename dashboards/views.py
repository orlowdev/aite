from django.shortcuts import render


def dashboard_main(request):
    return render(request, 'user_dashboard.html')
