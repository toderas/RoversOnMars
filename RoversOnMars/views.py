from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'welcome.html')


def sslcert(request):
    f = open('static/D4A8A9D509E77FB63021190BDE6DAD71.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
