from django.shortcuts import render, redirect
from .models import Poll
from .form import PollForm
from django.http import HttpResponse



def index(request):
    polls = Poll.objects.all()

    context = {"polls": polls}
    return render(request, "poll/index.html", context)


def create(request):
    form = PollForm()
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("index")

    context = {"form": form}
    return render(request, "poll/create.html", context)


def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    if request.method == "POST":
        select_option = request.POST["poll"]
        if select_option == "option_one":
            poll.option_one_count += 1
        elif select_option == "option_two":
            poll.option_two_count += 1
        elif select_option == "option_three":
            poll.option_three_count += 1
        else:
            return HttpResponse(404, "Invalid Form")

        poll.save()

        return redirect("results", poll.id)

    context = {"poll": poll}
    return render(request, "poll/vote.html", context)


def results(request, poll_id):
    poll = Poll.objects.get(id=poll_id)

    context = {"poll": poll}
    return render(request, "poll/results.html", context)