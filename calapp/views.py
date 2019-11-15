from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'base.html')
def calculate(request):
    try:
        a=request.GET['t1']
        x=int(a)
        b=request.GET['t2']
        y=int(b)
        op=request.GET["operation"]
    except(ValueError):
        return render(request, 'base.html')
    if op=="add":
        z=x+y
        return HttpResponse("""<html><body bgcolor=blue><h1>sum is:"""+str(z)+"""</h1></body></html>""")
    elif op=="sub":
        z=x-y
        return HttpResponse("""<html><body bgcolor=green><h1>substraction is:""" + str(z) + """</h1></body></html>""")
    elif op=="mul":
        z=x*y
        return HttpResponse("""<html><body bgcolor=yellow><h1>multiplication is:""" + str(z) + """</h1></body></html>""")
    elif op=="div":
        try:
            z=x/y
            return HttpResponse("""<html><body bgcolor=cyan><h1>division is:""" + str(z) + """</h1></body></html>""")
        except(ZeroDivisionError):
            return HttpResponse("can not divide no by zero")
