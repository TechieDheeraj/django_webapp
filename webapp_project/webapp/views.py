from django.shortcuts import render

def test_app(request):
        return render(request, 'app.html', {})

# Create your views here.
