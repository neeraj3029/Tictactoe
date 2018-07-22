from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.core.validators import *
# Create your models here.

GAME_CHOICES = {
    ('F', 'First PLayer Move'),
    ('S', 'Second Player To Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw')

}

class GameQuerySet(models.QuerySet):
    def all_games_user(self,user):
        return self.filter(Q(second_player = user) | Q(first_player = user))
    def active(self):
        return self.filter(Q(status = 'F') | Q(status = 'S'))


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name = "game_first_player", on_delete = models.CASCADE)
    second_player = models.ForeignKey(User, related_name = "game_second_player", on_delete = models.CASCADE)
    #start_time = models.DateTimeField(auto_now = True)
    #end_time = models.DateTimeField(auto_add = True)
    objects = GameQuerySet.as_manager()
    status = models.CharField(max_length= 1, default = 'F', choices = GAME_CHOICES)

    def __str__(self):
        return "{0} {1} vs {2}".format(self.pk,self.first_player,self.second_player)
    def get_absolute_url(self):
        return reverse(('gameplay_detail'), args = [self.id])
    def is_users_move(self, user):
        return (user == self.second_player and self.status == 'S' or user == self.first_player and self.status == 'F')
    def board(self):
        board = [[None for x in range(0,3)] for y in range(0,3)]
        for move in self.move_set.all():
            board[move.y][move.x] = move
        return board
    def new_move(self):
        if self.status not in ['F','S']:
            raise ValueError('Game is already finished')
        return move(game = self, by_first_player = self.status == 'F')
    def update_game_status(self, move):
        self.status = self.get_game_status(move)
        self.save()

    def get_game_status(self, move):
        x,y = move.x , move.y
        b = self.board()
        if(b[y][0] == b[y][1] == b[y][2]) or \
           (b[0][x] == b[1][x] == b[2][x]) or \
            (b[0][0] == b[1][1]==b[2][2]) or \
                (b[0][2] == b[1][1] == b[2][0]):
                return 'W' if move.by_first_player else 'L'
        if self.move_set.count() == 9:
            return 'D'
        return 'S' if move.by_first_player else 'F'



class move(models.Model):
    x = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(2)])
    y = models.IntegerField(validators = [MaxValueValidator(2),MinValueValidator(0)])
    comment = models.CharField(max_length = 300, blank = True)
    by_first_player = models.BooleanField(editable = False, default = True)
    #er = models.CharField(max_length = 300, blank = True, default = 'sdf')
    game = models.ForeignKey(Game, on_delete = models.CASCADE)

    def __eq__(self, other):
        if other is None:
            return False
        return self.by_first_player == other.by_first_player
'''
    def save(self, *args, **kwargs):
        super(move, self).save(*args, **kwargs)
        self.game.update_game_status(self)
        self.game.save()
'''
