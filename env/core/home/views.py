from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    pple = [
        {'name':"Divyansh", "age":21},
        {'name':"Ansh", "age":23},
        {'name':"Divy", "age":14},
        {'name':"Anshika", "age":29},
        {'name':"Anshu", "age":11},
        ]
    veg = ['Pumpkin', 'Tomato', 'Potato']
    text = '''
            Cupa  it deserunt sunt esse occaecat excepteur. Anim ea incididunt non aliquip.

            Non et excepteur in veniam commodo in id. Deserunt ex dolore incididunt voluptate id irure. Ipsum cupidatat eu excepteur reprehenderit ipsum qui eu quis adipisicing elit dolore voluptate sit sit. Deserunt tempor in duis eu dolor nostrud ea est nostrud mollit ullamco. Ipsum et eiusmod et elit voluptate dolor ullamco mollit cillum dolore.

            Esse occaecat mollit labore aliquip do ullamco elit dolore dolor reprehenderit sit reprehenderit in laborum. Cillum non excepteur eu reprehenderit elit minim ut. Quis aliquip anim ullamco consectetur in est qui.
        '''

    return render(request, "home/index.html", context={"peoples" : pple, "text" : text})


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')