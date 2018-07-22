from django.shortcuts import render,redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game,move
from .forms import moveForm
@login_required()
def game_detail(request, id):
    game = get_object_or_404(Game, pk = id)
    form = moveForm()
    context = {'game': game}
    if game.is_users_move(request.user):
        context['form'] = form
    return render(request, 'gameplay2/game_detail.html',context)

@login_required()
def make_move_view(request, id):
    #return redirect('player_home')

    game = get_object_or_404(Game, pk = id)
    if not game.is_users_move(request.user):
        raise PermissionDenied
    ins = game.new_move()
    form = moveForm(instance = ins, data = request.POST)
    #form.clean()
    if form.is_valid():
        ins.save()
        game.update_game_status(ins)
        return redirect('gameplay_detail', id)
    else:
        return render(request, 'gameplay2/game_detail.html', {'game':game, 'form':form})

class AllGamesList(ListView):
    model = Game



