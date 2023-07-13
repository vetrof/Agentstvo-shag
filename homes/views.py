

from django.shortcuts import render

from homes.models import Home


def list_views(request):

    homes = Home.objects.all()

    return render(request, 'index.html', {'homes': homes})


