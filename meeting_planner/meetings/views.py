from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
from .forms import MeetingForm


def detail(request, id):
    return render(
        request=request,
        template_name="meetings/detail.html",
        context={
            "meeting": get_object_or_404(Meeting, pk=id)
        }
    )

def create(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("welcome")

    else:
        form = MeetingForm()

    return render(
        request=request,
        template_name="meetings/create.html",
        context={
            "form": form
        }
    )

def update(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)

        if form.is_valid():
            form.save()
            return redirect("welcome")

    else:
        form = MeetingForm(instance=meeting)

    return render(
        request=request,
        template_name="meetings/update.html",
        context={
            "form": form
        }
    )

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")

    return render(
        request=request,
        template_name="meetings/delete.html",
        context={
            "form": meeting
        }
    )



