from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import datetime
from pytz import timezone
from django.apps import apps
User = apps.get_model('login', 'User')

def index(request):
    user = User.objects.get(id=request.session['userid'])
    all_games=Game.objects.all().order_by("-created_at")
    outdated_game(all_games)

    context = {
        "user":user,
        "all_games":all_games,
    }
    return render(request, "sports/index.html",context)

def outdated_game(all_games):
    todays_date=datetime.datetime.now(timezone("US/Pacific")).strftime("%Y-%m-%d %H:%M:%S") #This line converts todays_date from a datetime to a string with the format Y-m-d H:M:S
    todays_date = datetime.datetime.strptime(todays_date,"%Y-%m-%d %H:%M:%S") #This line converts todays_date from a string back to a datetime, because we kept getting errors.... its stupid dont ask...

    for game in all_games:
        date=game.date
        time=game.time
        date=datetime.datetime(date.year, date.month, date.day, time.hour, time.minute)
        if date < todays_date:
            game.delete()

def create_new_game(request):
    user=User.objects.get(id=request.session['userid'])
    context={
        "user":user,
    }
    return render(request, "sports/game_form.html", context)

def game_form(request):
    
    errors=Game.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/sports/create_new_game')
    else:

        user=User.objects.get(id=request.session['userid'])

        game=Game.objects.create(location=request.POST['location'], state=request.POST['state'], city=request.POST['city'], zipcode=request.POST['zipcode'], sport=request.POST['sport'], comment=request.POST['comment'], time=request.POST['time'], date=request.POST['date'], captain=user)

        game.joiner.add(user)

        return redirect(f"/sports/{game.id}")

def success_page(request, id):
    game_id=Game.objects.get(id=id)
    user=User.objects.get(id=request.session['userid'])

    players=game_id.joiner.all()

    context={
        "game_id":game_id,
        "user": user,
        "players":players,
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
    errors=Game.objects.basic_validator(request.POST)

    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect(f'/sports/edit/{game_to_update.id}')
    else:
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

def view_game(request, id):
    game_id=Game.objects.get(id=id)
    user=User.objects.get(id=request.session['userid'])

    return redirect(f"/sports/{game_id.id}")

def join_game(request, id):
    user=User.objects.get(id=request.session['userid'])
    this_game=Game.objects.get(id=id)
    this_game.joiner.add(user)
    return redirect(f"/sports/{this_game.id}")

def remove_my_game(request, id):
    user=User.objects.get(id=request.session['userid'])
    this_game=Game.objects.get(id=id)
    this_game.joiner.remove(user)

    return redirect("/sports/")

def search(request):
    search = Game.objects.all().order_by("-created_at")
    if request.POST['sport'] != '':
        search=search.filter(sport__iexact=request.POST['sport'])
    if request.POST['location'] != '':
        search=search.filter(location__iexact=request.POST['location'])
    if request.POST['date'] != '':
        search=search.filter(date=request.POST['date'])
    if request.POST['time'] != '':
        search=search.filter(time=request.POST['time'])
    if request.POST['city'] != '':
        search=search.filter(city__iexact=request.POST['city'])
    if request.POST['zipcode'] != '':
        search=search.filter(zipcode=request.POST['zipcode'])
    if request.POST['state'] != '':
        search=search.filter(state__iexact=request.POST['state'])

    context={
        "all_games":search,
    }

    return render(request, "sports/search.html", context)

def reset(request):
    user = User.objects.get(id=request.session['userid'])
    all_games=Game.objects.all().order_by("-created_at")

    context = {
        "user":user,
        "all_games":all_games,
    }
    return render(request, "sports/reset.html",context)












