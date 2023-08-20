from django.shortcuts import render

# Create your views here.
# def contact(request):
#     return render(request, 'index.html',context={"name" : 'Sami', "aa":23})


# def newcontact(request):
#     return render(request, 'homes.html')

def contact(request):
    courses = [
        {
            'id': 1,
            'course': 'C',
            'teacher': 'Rahim'
        },
        {
            'id': 2,
            'course': 'C++',
            'teacher': 'Rahim'
        },
        {
            'id': 3,
            'course': 'Java',
            'teacher': 'Rahim'
        },
        {
            'id': 4,
            'course': 'Ruby',
            'teacher': 'Rahim'
        }
    ]
    return render(request, 'index.html', {'courses': courses})
