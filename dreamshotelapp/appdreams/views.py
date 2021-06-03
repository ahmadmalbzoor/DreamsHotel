from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def cards(request):
    return render(request,"checkout.html")

def voucher(request):
    return render(request,"voucher.html")