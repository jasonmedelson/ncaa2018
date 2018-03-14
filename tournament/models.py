from django.db import models

# Create your models here.
# class TournamentTeamManager(models.manager):
#     def create_tournamentteam(self, teamName, teamRating):
#         tournamentteam = self.create(teamName = teamName, teamRating = teamRating)
#         return tournamentteam
class TournamentTeam(models.Model):
    teamName = models.CharField(max_length=30)
    teamRating = models.DecimalField(max_digits=3, decimal_places=1,default="")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.teamName
