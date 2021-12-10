from django.shortcuts import render, get_object_or_404
from .models import Captures


def all_captures(request):
    """ A view to show all captures, including sorting and search queries """
    captures = Captures.objects.all()

    context = {
        'captures': captures,
    }

    return render(request, 'captures/captures.html', context)


def capture_detail(request, capture_id):
    """ A view to show product details """
    capture = get_object_or_404(Captures, pk=capture_id)

    context = {
        'capture': capture,
    }
    return render(request, 'captures/capture_detail.html', context)
