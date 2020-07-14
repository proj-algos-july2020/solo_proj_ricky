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
    path('view_game/<int:id>', views.view_game),
    path('join_game/<int:id>', views.join_game),
    path('remove_my_game/<int:id>', views.remove_my_game),
    path('search', views.search),
]