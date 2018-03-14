from django.shortcuts import render
from django.http import HttpResponse
from tournament.models import TournamentTeam
import random

# Create your views here.

# def index(request):
#     return render(
#         request,
#         './index.html'
#     )
def index(request):
    all_team_Query = TournamentTeam.objects.all()
    team_name_list_top = []
    team_name_list_bottom = []
    round1_teams = []
    round2_teams = []
    round2_top = []
    round2_bottom=[]
    round3_teams = []
    round3_top = []
    round3_bottom = []
    round4_teams = []
    round4_top = []
    round4_bottom = []
    round5_teams = []
    round5_top = []
    round5_bottom = []
    round6_teams = []
    round6_top = []
    round6_bottom = []
    round7_teams = []
    for team in range(len(all_team_Query)):
        if team % 2 == 0:
            team_name_list_top.append(all_team_Query[team].teamName)
        else:
            team_name_list_bottom.append(all_team_Query[team].teamName)
        round1_teams.append([all_team_Query[team].teamName,all_team_Query[team].teamRating])
    #round 1 simulation
    for game in range(int(len(all_team_Query)/2)):
        team1_rating = round1_teams[game * 2][1]
        team2_rating = round1_teams[game * 2 + 1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464/400
        bottom_number = 1+10 ** exponent
        percent = 1/bottom_number*100
        randomnum = random.randint(1,100)
        if percent >= randomnum:
            round2_teams.append([round1_teams[game * 2][0],round1_teams[game * 2][1]])
        else:
            round2_teams.append([round1_teams[game * 2+1][0], round1_teams[game * 2+1][1]])
    for team in range(len(round2_teams)):
        if team % 2 == 0:
            round2_top.append(round2_teams[team][0])
        else:
            round2_bottom.append(round2_teams[team][0])
    #round 2 simulation
    for game in range(int(len(round2_teams) / 2)):
        team1_rating = round2_teams[game*2][1]
        team2_rating = round2_teams[game*2+1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464 / 400
        bottom_number = 1 + 10 ** exponent
        percent = 1 / bottom_number * 100
        randomnum = random.randint(1, 100)
        if percent >= randomnum:
            round3_teams.append([round2_teams[game * 2][0],round2_teams[game * 2][1]])
        else:
            round3_teams.append([round2_teams[game * 2+1][0], round2_teams[game * 2+1][1]])
    for team in range(len(round3_teams)):
        if team % 2 == 0:
            round3_top.append(round3_teams[team][0])
        else:
            round3_bottom.append(round3_teams[team][0])
    # round 3 simulation
    for game in range(int(len(round3_teams) / 2)):
        team1_rating = round3_teams[game * 2][1]
        team2_rating = round3_teams[game * 2 + 1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464 / 400
        bottom_number = 1 + 10 ** exponent
        percent = 1 / bottom_number * 100
        randomnum = random.randint(1, 100)
        if percent >= randomnum:
            round4_teams.append([round3_teams[game * 2][0], round3_teams[game * 2][1]])
        else:
            round4_teams.append([round3_teams[game * 2 + 1][0], round3_teams[game * 2 + 1][1]])
    for team in range(len(round4_teams)):
        if team % 2 == 0:
            round4_top.append(round4_teams[team][0])
        else:
            round4_bottom.append(round4_teams[team][0])

    # round 4 simulation
    for game in range(int(len(round4_teams) / 2)):
        team1_rating = round4_teams[game * 2][1]
        team2_rating = round4_teams[game * 2 + 1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464 / 400
        bottom_number = 1 + 10 ** exponent
        percent = 1 / bottom_number * 100
        randomnum = random.randint(1, 100)
        if percent >= randomnum:
            round5_teams.append([round4_teams[game * 2][0], round4_teams[game * 2][1]])
        else:
            round5_teams.append([round4_teams[game * 2 + 1][0], round4_teams[game * 2 + 1][1]])
    for team in range(len(round5_teams)):
        if team % 2 == 0:
            round5_top.append(round5_teams[team][0])
        else:
            round5_bottom.append(round5_teams[team][0])
    # round 5 simulation
    for game in range(int(len(round5_teams) / 2)):
        team1_rating = round5_teams[game * 2][1]
        team2_rating = round5_teams[game * 2 + 1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464 / 400
        bottom_number = 1 + 10 ** exponent
        percent = 1 / bottom_number * 100
        randomnum = random.randint(1, 100)
        if percent >= randomnum:
            round6_teams.append([round5_teams[game * 2][0], round5_teams[game * 2][1]])
        else:
            round6_teams.append([round5_teams[game * 2 + 1][0], round5_teams[game * 2 + 1][1]])
    for team in range(len(round6_teams)):
        if team % 2 == 0:
            round6_top.append(round6_teams[team][0])
        else:
            round6_bottom.append(round6_teams[team][0])

    # round 6 simulation
    for game in range(int(len(round6_teams) / 2)):
        team1_rating = round6_teams[game * 2][1]
        team2_rating = round6_teams[game * 2 + 1][1]
        rating_differential = team1_rating - team2_rating
        exponent = -1.0 * float(rating_differential) * 30.464 / 400
        bottom_number = 1 + 10 ** exponent
        percent = 1 / bottom_number * 100
        randomnum = random.randint(1, 100)
        if percent >= randomnum:
            round7_teams.append(round6_teams[game * 2][0])
        else:
            round7_teams.append(round6_teams[game * 2 + 1][0])

    zipped_teams1 = zip(team_name_list_top,team_name_list_bottom)
    zipped_teams2 = zip(round2_top, round2_bottom)
    zipped_teams3 = zip(round3_top, round3_bottom)
    zipped_teams4 = zip(round4_top, round4_bottom)
    zipped_teams5 = zip(round5_top, round5_bottom)
    zipped_teams6 = zip(round6_top, round6_bottom)
    return render(
        request,
        './test.html',
        context={"team_names1":zipped_teams1,"team_names2":zipped_teams2,"team_names3":zipped_teams3,"team_names4":zipped_teams4,
                 "team_names5":zipped_teams5,"team_names6":zipped_teams6, "team_names7":round7_teams, "spacer_1":range(16),"spacer_2":range(8),"spacer_3":range(4),
                 "spacer_4":range(2) },
    )