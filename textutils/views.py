# I have created this website - Girish
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello Harry Bhai</h1> <a href="https://www.youtube.com/watch?v=mZa-wKePntg&pbjreload=10">Django with Girish </a>''')
#
# def about(request):
#     return HttpResponse("About Harry Bhai")


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    if removepunc == "on":

    #analyzed = djtext

    #Analyze the text

        punctuations = ''' ?*&(%&%&*#&*&*#))@)!@}(()) '''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return  render(request, 'analyze.html', params)
    elif (spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext [index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charcount=="on"):
        analyzed = ""
        for char in djtext:
            if char in djtext:


                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")





    # return HttpResponse("Remove Punc <a href='/'> Back </a>")

# def capfirst(request):
#     return HttpResponse("capitalize first <a href='/'> Back </a>")
#
# def newlineremove(request):
#     return HttpResponse("New line remove <a href='/'> Back </a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'> Back </a>")
#
# def charcount(request):
#     return HttpResponse("Charecter count <a href='/'> Back </a>")
