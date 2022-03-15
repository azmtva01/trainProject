from django.shortcuts import render


def post_list(request):
    return render(request, 'trainApp/post_list.html', {})
