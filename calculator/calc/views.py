from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculator(request):
    result = ''
    if request.method == 'POST':
        expression = request.POST.get('expression','')
        try:
            result = eval(expression)
        except Exception as e:
            result = "Error" 
    return render (request,'index.html',{'result':result})