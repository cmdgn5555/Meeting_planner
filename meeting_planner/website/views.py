from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


# Create your views here.

def welcome(request):
    return render(request=request,
                  template_name="website/welcome.html",
                  context={
                      "message": "Welcome to the Meeting Planner App",
                      "num_meeting": Meeting.objects.count(),
                      "meetings": Meeting.objects.all()
                  })


def date(request):
    return HttpResponse(f"this page was served at{str(datetime.now())}")


def about(request):
    return HttpResponse("copyright Tyson solutions")
