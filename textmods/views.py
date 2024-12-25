import re
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzer(request):
    #get the text
    djtext = request.POST.get('text','default')

    #check box value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    numberofchar = request.POST.get('numberofchar','off')
    #check which checkbox is on
    analyzed = ""
    punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~''' # type: ignore
    if removepunc =="on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations','analyzed_text':analyzed}
        djtext = analyzed
    
    if fullcaps == "on":
            analyzed = ""
            for char in djtext:
                analyzed  = analyzed + char.upper()
            params = {'purpose':'Changed to UPPER case','analyzed_text':analyzed}
            djtext = analyzed
    
    if newlineremover == "on":
            analyzed = ""
            for char in djtext:
                if char != "\n" and char !="\r":
                     analyzed =  analyzed + char
            params = {'purpose':'Remove the new lines','analyzed_text':analyzed}
            djtext = analyzed
            
    if extraspaceremover == "on":
            analyzed = ""
            for index,char in enumerate(djtext):
                if  djtext[index] == " " and djtext[index + 1] == " ":
                    pass
                else:
                    analyzed = analyzed + char
            params = {'purpose':'Remove extra space','analyzed_text':analyzed}
            djtext = analyzed

    if numberofchar == "on":
            analyzed = ""
            analyzed = len(djtext)
            params = {'purpose':'Number of Character','analyzed_text':analyzed}
    
    if removepunc !="on" and extraspaceremover !="on" and numberofchar != "on" and newlineremover !="on" and fullcaps != "on":     
        analyzed = djtext
        params = {'purpose':'Remove extra space','analyzed_text':analyzed}

    return render(request,'analyzer.html',params)  
