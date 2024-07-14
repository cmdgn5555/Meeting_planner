from django.urls import path
from rooms.views import room_list, room_detail, create_room, update_room, delete_room

urlpatterns = [
    path("rooms", room_list, name="rooms"),

    path("detail/<int:id>", room_detail, name='room_detail'),

    path('create', create_room, name='create_room'),

    path("update/<int:id>", update_room, name='update_room'),

    path("delete/<int:id>", delete_room, name='delete_room'),

]

