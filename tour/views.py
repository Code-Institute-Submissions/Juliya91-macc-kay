from django.shortcuts import render

from .forms import TourForm


def tour(request):

    tour_form = TourForm()
    template = 'tour/tour.html'
    context = {
        'tour_form': tour_form,
    }

    return render(request, template, context)
