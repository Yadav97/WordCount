
from django.http import HttpResponse
from django.shortcuts import render 
import operator


#def home(request):
 #   return HttpResponse("hello")

#  def home(request):
#      return render(request,'home.html',{"hello":"hello world it is django"})

def home(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET["fulltext"]
    print(fulltext)
    countedwords = fulltext.split()

    #now we use concept for what word most appeared in the input

    worddictionary = {}

    for word in countedwords:
        if word in worddictionary:
            #increase 
            worddictionary[word] = worddictionary[word] + 1
        else:
            #add to the dictinaory
            worddictionary[word] = 1


            sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse = True)





    return render(request,'count.html',{"full":fulltext,"countwords":len(countedwords),"worddict":sortedwords})
    # items() method is used to return the list with all dictionary keys with values.so we need loop for get the elements from the list so go in count.htl and use loop


def about(request):
    return render(request,'about.html')

