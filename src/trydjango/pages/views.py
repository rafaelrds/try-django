from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is a context text",
        "my_number": "123456",
        "my_list": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, "fibonacci"]
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
