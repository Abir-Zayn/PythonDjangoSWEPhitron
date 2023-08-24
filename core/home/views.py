from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples =[
        {'name' : 'Abir Zayn' , 'age':18},
        {'name':'Kazi R ', 'age':19},
        {'name': 'Sandeep', 'age':21},
        {'name': 'Nasir', 'age':24},
    ]
    
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    """
    
    vegatable=[
        'Pumpkin','Tomato','Potatoes'
    ]

# As we passing the data from backend therefore we will have pass it through the context. Important
# use the '1st name' in the template and '2nd name' is the data been setted in the view page.

    return render(request,"index.html",context={'people':peoples, 'text':text, 'veg':vegatable}  )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#As its not linking with any other template thus it will show just a block a of text. 
def success_page(request):
    return HttpResponse("<h1>This is a success reponse<h1>")