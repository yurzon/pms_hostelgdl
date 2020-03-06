from django.shortcuts import render

def beds_index(request):
    return render(request, 'beds_index.html')
