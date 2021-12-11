from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Captures, Artist


def all_captures(request):
    """ A view to show all captures, including sorting and search queries """
    captures = Captures.objects.all()
    query = None
    artists = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                captures = captures.annotate(lower_name=Lower('name'))
            if sortkey == 'artist':
                sortkey = 'artist__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            captures = captures.order_by(sortkey)

        if 'artist' in request.GET:
            artists = request.GET['artist'].split(',')
            captures = captures.filter(artist__name__in=artists)
            artists = Artist.objects.filter(name__in=artists)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('captures'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            captures = captures.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'captures': captures,
        'search_term': query,
        'current_artists': artists,
        'current_sorting': current_sorting,
    }

    return render(request, 'captures/captures.html', context)


def capture_detail(request, capture_id):
    """ A view to show product details """
    capture = get_object_or_404(Captures, pk=capture_id)

    context = {
        'capture': capture,
    }
    return render(request, 'captures/capture_detail.html', context)
