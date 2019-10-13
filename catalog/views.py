from django.shortcuts import render

# Create your views here.
def login(request):
    """REPLACE WITH REAL LOGIN"""

    context={}

    return render(request, 'login.html', context=context )












###DELETE WHEN IN PRODUCTION####
def testpage(request):
    """Test page for production testing"""

    context={}

    return render(request, 'testpage.html', context=context )
