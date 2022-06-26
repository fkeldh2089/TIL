1. 1:N True or False

- 1) T
- 2) T
- 3) T
- 4) F



2. ForeignKey column name

- Question_id, Question_Comment



3. 1:N model manager

- `question.comment_set.all()`



4. next parameter

- 1. 405, POST로 들어가지 않기 때문이다.

```python
@login_required
# @require_POST
def delete(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        if request.user.is_authenticated:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', pk)
```

