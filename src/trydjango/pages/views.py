from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Contact View</h1>")
