from django.shortcuts import render


def view_main(request):
    payload = render(request, "main/index.html")
    return payload
