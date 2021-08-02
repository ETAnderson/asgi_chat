from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Room


class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    context_object_name = 'latest_room_list'

    def get_queryset(self):
        return Room.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')[:5]


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
