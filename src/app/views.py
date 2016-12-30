from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from forms import *



def test(request):
    # db = request.db
    # db = django_couch.db()
    # data = request.db.view('newDesing/cars').rows
    #
    # datas = {
    #     "car": "Porshe",
    # }
    #
    # request.db.create(datas)
    #db.delete(db['bb173cf5649faf077b70c735ed00c960'])
    #db.update(db[])
    posts = request.db.view('blog/posts').rows
    form = postForm(request.POST or None)
    if request.POST:
        if form.is_valid():

            data = form.cleaned_data

            data.update({'type': 'title'})
            # data = {
            #     "author": request.POST.get('author'),
            #     "title": request.POST.get('title'),
            #     "text": request.POST.get('text'),
            #     "type": "title"
            # }
            request.db.create(data)

            return redirect('index')

    return render(request, 'index.html', {'form': form, 'posts': posts})


def remove_post(request, post_id):
    request.db.delete(request.db[post_id])
    return redirect('index')


def create_comment(request, post_id):
    form = commentForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        data.update({'post': str(post_id)})

        request.db.create(data)
        return render(request, 'comment.html', {'form2': form})

    return render(request, 'comment.html', {'form2': form})


def post_edit(request, post_id):

    post = request.db[post_id]
    form = postForm(post)
    if request.POST:



        if form.is_valid():
            data = form.cleaned_data
            data.update({'type': 'title',
                         'text': request.POST.get('text'),
                         'title': request.POST.get('title'),
                         'author': request.POST.get('author')})
            post.update(data)
            post.save()
            return redirect('index')
        else:
            if form.errors['title']:
                data = form.cleaned_data['text','author']
                data.update({'type': 'title',
                             'text': request.POST.get('text'),
                             'author': request.POST.get('author')})
                print 'validate'
    return render(request, 'edit.html', {'form': form})
