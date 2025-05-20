from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import GraffitiForm
from .models import Graffiti


@login_required
def graffiti_create(request):
    if request.method == "POST":
        form = GraffitiForm(request.POST)
        if form.is_valid():
            graffiti = form.save(commit=False)
            graffiti.author = request.user
            graffiti.save()
            return redirect("/")
    else:
        form = GraffitiForm()
    return render(request, "graffiti/create.html", {"form": form})


@login_required
def graffiti_detail(request, pk):
    graffiti = get_object_or_404(Graffiti, pk=pk)
    return render(request, "graffiti/detail.html", {"graffiti": graffiti})


@login_required
def graffiti_delete(request, pk):
    graffiti = get_object_or_404(Graffiti, pk=pk)
    if graffiti.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this graffiti.")
    if request.method == "POST":
        graffiti.delete()
        return redirect("/")
    return render(request, "graffiti/delete.html", {"graffiti": graffiti})


def graffiti_list(request):
    graffitis = Graffiti.objects.all().order_by("-created_at")
    return render(request, "graffiti/list.html", {"graffitis": graffitis})


@login_required
def like_graffiti(request, pk):
    if request.method != "POST":
        return HttpResponseForbidden("Only POST requests are allowed.")
    graffiti = get_object_or_404(Graffiti, pk=pk)
    liked = False
    if graffiti.likes.filter(id=request.user.id).exists():
        graffiti.likes.remove(request.user)
    else:
        graffiti.likes.add(request.user)
        liked = True
    return JsonResponse({"likes_count": graffiti.likes.count(), "liked": liked})
