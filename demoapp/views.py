from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pathview(request, name, id):
    content = '''
    <html><h1> Example for returning the parameters to the user </h1>
    <p>Name: {}</p>
    <p>Id: {}</p>
    '''.format(name, id)
    return HttpResponse(content)

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("name: {}, id: {}".format(name, id))

def showform(request): 
    return render(request, "form.html") 

def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
        return HttpResponse("Name: {} & UserId: {}".format(name, id))


def dishesitem(request, dish):

    items = {
        'falfel' : 'Egyptian food made with fool',
        'pasta' : ' the most famous italian food',
        'rice' : 'the most popular food in the world',
    }

    description = items[dish]

    return HttpResponse(f"<h1>{dish}</h1><p>{dish} is a {description}</p>")

