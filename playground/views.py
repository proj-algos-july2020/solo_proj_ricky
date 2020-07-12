from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.apps import apps
User = apps.get_model('login', 'User')

def index(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        "user":user,
    }
    return render(request, "sports/index.html", context)

def create_new_game(request):
    user=User.objects.get(id=request.session['userid'])
    context={
        "user":user,
    }
    return render(request, "sports/game_form.html", context)

def game_form(request):
    user=User.objects.get(id=request.session['userid'])

    game=Game.objects.create(location=request.POST['location'], state=request.POST['state'], city=request.POST['city'], zipcode=request.POST['zipcode'], sport=request.POST['sport'], comment=request.POST['comment'], time=request.POST['time'], date=request.POST['date'], captain=user)

    return redirect(f"/sports/{game.id}")

def success_page(request, id):
    game_id=Game.objects.get(id=id)
    user=User.objects.get(id=request.session['userid'])

    context={
        "game_id":game_id,
        "user": user,
    }
    return render(request, "sports/success.html", context)

def confirm(request):
    return redirect("/sports/")

def delete(request, id):
    game_id=Game.objects.get(id=id)
    game_id.delete()
    return redirect("/sports/")

def edit_game(request, id):
    game_id=Game.objects.get(id=id)
    user=User.objects.get(id=request.session['userid'])
    game_id.date=str(game_id.date)
    game_id.time=str(game_id.time)

    context={
        "game_id":game_id,
        "user":user,
    }
    return render(request, "sports/edit_game.html", context)

def update_game(request, id):
    game_to_update=Game.objects.get(id=id)
    user=User.objects.get(id=request.session['userid'])

    game_to_update.state=request.POST['state']
    game_to_update.city=request.POST['city']
    game_to_update.zipcode=request.POST['zipcode']
    game_to_update.location=request.POST['location']
    game_to_update.sport=request.POST['sport']
    game_to_update.date=request.POST['date']
    game_to_update.time=request.POST['time']
    game_to_update.comment=request.POST['comment']
    game_to_update.save()

    return redirect("/sports/")









# Create your views here.
