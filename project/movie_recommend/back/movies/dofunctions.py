def CheckGenre(request, movies, genre, num):
    genre_checked = request.POST.get(genre)
    me = User.objects.get(pk=request.user.pk)
    if genre_checked == 'to-off':
        me.fitering_data[genre] = 'off'
    elif genre_checked == 'to-on':
        me.fitering_data[genre] = 'on'
    if me.fitering_data[genre] == 'off':
        movies = movies.filter(genres=num)
    me.save()
    return movies