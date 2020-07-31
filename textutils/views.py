# I have created this file - Parul Gupta
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')

def ex1(request):
    s='''<h2> Navigation Bar</h2><ul>
    <li><a href='https://www.codewithharry.com'>Django with Harry Bhai</a></li>
    <li><a href='https://www.amazon.com'>Amazon</a></li>
    <li><a href='https://www.flipkart.com'>Flipkart</a></li>
    <li><a href='https://www.google.com'>Google</a></li>
    </ul>'''
    return HttpResponse(s)
    
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc =="on":
        punctuations = '''!()-[]{};:"'\,<>./?@#%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analysed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analysed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analysed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(charcount=="on"):
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(removepunc !="on" and fullcaps!="on" and extraspaceremover != "on" and newlineremover!="on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)