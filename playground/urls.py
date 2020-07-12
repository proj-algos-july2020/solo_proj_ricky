from django.urls import path
from . import views
urlpatterns=[
    path('', views.index),
    path('create_new_game', views.create_new_game),
    path('game_form', views.game_form),
    path('<int:id>', views.success_page),
    path('confirm', views.confirm),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit_game),
    path('update_game/<int:id>', views.update_game),
]