from django.shortcuts import render


def search_views(request):
    return render(request, 'search.html')
