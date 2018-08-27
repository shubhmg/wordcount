from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    mytext = request.GET['q']
    mytextlist = mytext.split()
    length = len(mytextlist)
    myworddict = {}
    for word in mytextlist:
        if word in myworddict:
            myworddict[word] += 1
        else:
            myworddict[word] = 1
    return render(request, 'count.html', {"worddict": myworddict.items(), "length": length})