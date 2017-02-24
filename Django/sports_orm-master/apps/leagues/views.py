from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		# 1
		# "leagues": League.objects.filter(sport__contains='Baseball'),
		# 2
		# "leagues": League.objects.filter(name__contains='women'),
		# 3
		# "leagues": League.objects.filter(sport__contains='hockey'),
		# 4
		# "leagues": League.objects.exclude(sport__contains='football'),
		# 5
		# "leagues": League.objects.filter(name__contains='Conference'),
		# 6
		# "leagues": League.objects.filter(name__contains='Atlantic'),
		# 7
		# "teams": Team.objects.filter(location='Dallas'),
		# 8
		# "teams": Team.objects.filter(team_name='Raptors'),
		# 9
		# "teams": Team.objects.filter(location__contains='City'),
		# 10
		# "teams": Team.objects.filter(team_name__startswith='T'),
		# 11
		# "teams": Team.objects.order_by('team_name'),
		# 12
		# "teams": Team.objects.order_by('-team_name'),
		# 13
		# "players": Player.objects.filter(last_name='Cooper'),
		# 14
		# "players": Player.objects.filter(first_name='Joshua'),
		# 15
		# "players": Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua'),
		# 16
		"players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt'),
		}
		
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_players(50)
	team_maker.gen_players(200)

	return redirect("index")
