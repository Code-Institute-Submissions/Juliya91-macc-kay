from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Captures


def all_captures(request):
    """ A view to show all captures, including sorting and search queries """
    captures = Captures.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('captures'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            captures = captures.filter(queries)

    context = {
        'captures': captures,
        'search_term': query,
    }

    return render(request, 'captures/captures.html', context)


def capture_detail(request, capture_id):
    """ A view to show product details """
    capture = get_object_or_404(Captures, pk=capture_id)

    context = {
        'capture': capture,
    }
    return render(request, 'captures/capture_detail.html', context)
