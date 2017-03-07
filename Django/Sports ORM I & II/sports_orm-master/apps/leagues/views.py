from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
	# Sports ORM I
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
		# "players": Player.objects.filter(first_name='Alexander')|Player.objects.filter(first_name='Wyatt'),
	# Sports ORM II
		# 1
		# "teams": Team.objects.filter(league__name='Atlantic Soccer Conference'),
		# 2
		# "players": Player.objects.filter(curr_team__team_name='Penguins'),
		# 3
		# "players": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference'),
		# 4
		# "players": Player.objects.filter(curr_team__league__name='American Conference of Amateur Football', last_name='Lopez'),
		# 5
		# "players": Player.objects.filter(curr_team__league__sport__contains='football'),
		# 6
		# "teams": Team.objects.filter(curr_players__first_name='Sophia'),
		# 7
		# "leagues": League.objects.filter(teams__curr_players__first_name='Sophia'),
		# 8
		# "players": Player.objects.filter(last_name='Flores').exclude(curr_team__team_name='Roughriders'),
		# 9
		# "teams": Team.objects.filter(all_players__first_name='Samuel', all_players__last_name='Evans'),
		# 10
		# "players": Player.objects.filter(all_teams__team_name='Tiger-Cats'),
		# 11
		# "players": Player.objects.filter(all_teams__team_name='Vikings').exclude(curr_team__team_name='Vikings'),
		# 12
		# "teams": Team.objects.filter(all_players__first_name='Jacob', all_players__last_name='Gray').exclude(team_name='Oregon Cats'),
		# 13
		# "players": Player.objects.filter(first_name='Joshua', all_teams__league__name='Atlantic Federation of Amateur Baseball Players')
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_players(50)
	team_maker.gen_players(200)

	return redirect("index")
