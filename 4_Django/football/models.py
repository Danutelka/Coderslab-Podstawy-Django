from django.db import models

# Create your models here.
TEAMS = (
    (1, "Piast Piastów"),
    (2, "Perła Złotokłos"),
    (3, "LKS Chlebnia"),
    (4, "Naprzód Brwinów"),
    (5, "KS Teresin"),
    (6, "Józefovia Józefów"),
    (7, "Okręcie Warszawa"),
    (8, "Żyrardowianka Żyrardów"),
    (9, "Przyszłość Włochy"),
    (10, "Ryś Laski"),
    (11, "SEMP Ursynów"),
    (12, "Promyk Nowa Sucha"),
    (13, "Świt Warszawa"),
    (14, "FC Lesznowola"),
    (15, "Pogoń II Gdodzisk Mazowiecki"),
    (16, "Milan Milanówek"), 
)

class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
            return "{name}; {points}" .format(name=self.name, points=self.points)
    
    class Meta:
        managed = False
        db_table = 'teams'
      

class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home = models.ForeignKey('Teams', related_name='gospodarze', db_column='team_home', null=True, on_delete=models.CASCADE)
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away = models.ForeignKey('Teams', related_name='goscie', db_column='team_away', null=True, on_delete=models.CASCADE)
    team_away_goals = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'
    