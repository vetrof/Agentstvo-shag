from django.shortcuts import render

from homes.models import Home


def search_views(request):
    query = request.GET.get('q')
    max = request.GET.get('max')
    min = request.GET.get('min')

    if query:
        homes = Home.objects.filter(info__iregex=query)
    else:
        homes = Home.objects.all()

    if max:
        homes = homes.filter(cost__lte=max)

    if min:
        homes = homes.filter(cost__gte=min)

    return render(request, 'search.html', {'homes': homes})
