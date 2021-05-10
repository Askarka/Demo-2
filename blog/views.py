from django.shortcuts import render


def flow(request):
    return render(request, 'blog/flow.html')
