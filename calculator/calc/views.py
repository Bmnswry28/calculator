from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def calculator(request):
    display = ''
    current_value = ''
    if request.method == 'POST':
        current_value = request.POST.get('display', '0')
        button = request.POST.get('button')
        
        if button == '=':
            try:
                current_value = current_value.replace('×', '*').replace('÷', '/').replace('−', '-')
                display = str(eval(current_value))
            except Exception as e:
                display = "Error"
        elif button == 'C':
            display = '0'
        elif button == 'CE':
            display = current_value[:-1] if current_value else '0'
        else:
            if current_value == '0' or current_value == 'Error':
                display = button
            else:
                display = current_value + button
    
    return render(request, 'index.html', {'display': display})
