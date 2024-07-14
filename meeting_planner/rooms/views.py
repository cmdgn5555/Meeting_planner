from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Room
from .forms import RoomForm


# Create your views here.

def room_list(requests):
    return render(
        request=requests,
        template_name="rooms/room_list.html",
        context={
            "rooms": Room.objects.all()
        }
    )


def room_detail(request, id):
    return render(
        request=request,
        template_name='rooms/detail.html',
        context={
            'room': get_object_or_404(Room, pk=id)
        }
    )


def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("rooms")

    else:
        form = RoomForm()

    return render(
        request=request,
        template_name="rooms/create.html",
        context={
            "form": form
        }
    )


def update_room(request, id):
    room = get_object_or_404(Room, pk=id)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect("rooms")

    else:
        form = RoomForm(instance=room)

    return render(
        request=request,
        template_name="rooms/update.html",
        context={
            "form": form
        }
    )

def delete_room(request, id):
    room = get_object_or_404(Room, pk=id)

    if request.method == "POST":
        room.delete()
        return redirect("rooms")

    return render(
        request=request,
        template_name="rooms/delete.html",
        context={
            "form": room
        }
    )
