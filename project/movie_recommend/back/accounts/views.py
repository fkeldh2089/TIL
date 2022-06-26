from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import UserNameSerializer

from collections import defaultdict


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')


@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    serializer = UserNameSerializer(person)
    tmp_data = serializer.data
    my_dict = serializer.data['reviewed_data']
    review_grade_sort = defaultdict(list)
    for p in tmp_data['moviereview_set']:
        review_grade_sort[p['grade']].append([p['movie']['id'], p['movie']['poster_path']])
    # print(review_grade_sort)
    sorted_dict1 = sorted(my_dict.items(), key= lambda x : x[1][1], reverse=True)
    sorted_dict2 = sorted(my_dict.items(), key= lambda x : x[1][1]/x[1][0] if(x[1][0]) else x[1][1], reverse=True)

    tmp_data.update({"user_many_genre":sorted_dict1[0:2], "user_vote_genre":sorted_dict2[0:2]})
    tmp_data.update(review_grade_sort)
    return Response(tmp_data)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            
            follow_status={
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
                'followings_count': person.followings.count(), 
            }
            return JsonResponse(follow_status)
    return redirect('accounts:profile', person.username)
