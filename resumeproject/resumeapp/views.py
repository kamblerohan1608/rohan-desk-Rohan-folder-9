from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def education(request):

    edu={
        'one':{'sr.no':'1','study':'Ssc','passing_year':2013,'board':'Maharashtra board','Percentages':76.80},
        'two':{'sr.no':'2','study':'Hsc','passing_year':2015,'board':'Maharashtra board','Percentages':61.51},
        'three':{'sr.no':'3','study':'B.E','passing_year':2021,'board':'Mumbai University','Percentages':60.00},
    }

    data = {'education':edu}

    return render(request,'education.html',data)

def skills(request):

    s1 = {
        'PYTHON':60,
        'JAVASCRIPT':50,
        'HTML':50,
        'CSS':45,
        'BOOTSTRAP':45,
    }

    s2={'skills':s1}

    return render(request,'skills.html',s2)

def projects(request):
    return render(request,'projects.html')

def exp(request):
    return render(request,'exp.html')

def contact(request):
    return render(request,'contact.html')

def thanks(request):
    return render(request,'thanks.html')
