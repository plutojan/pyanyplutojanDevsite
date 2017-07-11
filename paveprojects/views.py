from django.shortcuts import render

def ProjectView(request):
    return render(request, "paveprojects.html", {})
