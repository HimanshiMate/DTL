from django.shortcuts import render

# Create your views here.
def home(request):
    data={
       'name':'himanshi',
       'quali':'BTech',
       'city':'Bhopal'
    }
    return render(request,'home.html',data)


    # name='vedansh',
    # contact='45576890',
    # city='Indore',
    # return render(request,'home.html',{'key':"data"})  

    
     

