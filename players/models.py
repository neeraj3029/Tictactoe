from django.db import models

from django.contrib.auth.models import User

msg_choices = [
    ('f' , 'Hello, wanna play withme?' ),
    ( 's' , 'Lets play tictactoe')


]

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="invitations_received", on_delete=models.CASCADE)
    message = models.CharField(max_length=300, choices=msg_choices)
    image = models.CharField(max_length=500, default = '/Users/neeraj/Desktop/download.jpeg')
    #timestamp = models.DateTimeField(auto_now_add=True)
