from django.shortcuts import render

from blog.models import Post, PostImage


def flow(request):
    posts = Post.objects.all().prefetch_related('images')
    context = {'posts': posts}
    return render(request, 'blog/flow.html', context)

