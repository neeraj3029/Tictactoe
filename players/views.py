from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import InvitationForm
from .models import Invitation
from gameplay2.models import Game
from django.views.generic import ListView
from django.views.generic import ListView


@login_required()
def home(request):
    my_games = Game.objects.all_games_user(request.user)
    active_games = my_games.active()
    finished_games = my_games.difference(active_games)
    invitations = request.user.invitations_received.all()
    return render(request, "players/home.html",
                  {'games': active_games, 'invitations': invitations, 'fin' : finished_games}
                  )


@login_required()
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request, "players/new_invitation_form.html", {'form': form})


@login_required()
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user,
            )
        invitation.delete()
        return redirect(game)
    else:
        return render(request,
                      "players/accept_invitation_form.html",
                      {'invitation': invitation}
                      )

class invi(ListView):
    model = Invitation


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'players/signup.html'
    success_url = reverse_lazy('player_home')
