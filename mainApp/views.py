from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')
def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у Вас остались вопросы, то задайте их мне по телефону', '(099) 73 72 73 5']})
