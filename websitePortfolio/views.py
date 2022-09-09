from django.shortcuts import render

def home(request):
    return render(request, 'home.html') # same way comparing with bottom 2 lines.
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render({},request)) 
def project(request):
     return render(request, 'project.html')

def contact(request):
     return render(request, 'contact.html')


def stock(request):
     return render(request, 'stock.html')

def indeed(request):
     return render(request, 'indeed.html')

def twitter(request):
     return render(request, 'twitter.html')

