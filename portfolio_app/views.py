from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def data_science(request):
    return render(request, 'data-science.html')

def full_stack(request):
    return render(request, 'full-stack.html')

def automation(request):
    return render(request, 'automation.html')    

def trading(request):
    return render(request, 'trading.html') 

def reading(request):
    return render(request, 'reading.html')            

def entrepreneurship(request):
    return render(request, 'entrepreneurship.html')  

def tutorials(request):
    return render(request, 'tutorials.html')  

def weightlifting(request):
    return render(request, 'weightlifting.html')   

def snowboarding(request):
    return render(request, 'snowboarding.html')   

def music(request):
    return render(request, 'music.html')  

def longboarding(request):
    return render(request, 'longboarding.html')                                    