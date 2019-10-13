from django.shortcuts import render

# Create your views here.














def testpage(request):
    """Test page for production testing"""

    context={}

    return render(request, 'testpage.html', context=context )
