from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
from django.contrib.postgres.search import SearchVector

import csv
import pandas as pd
global resul

def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('About')
    return render(request, 'about.html')


def contact(request):
    print('Contact')
    return render(request, 'contact.html')

'''def data_analysis(request):
    print('Data analysis')
    if request.method == 'POST':
        form=TextForm(request.POST)
        if form.is_valid():
           
            fs = FileSystemStorage()
            filename = fs.path('\static\data\songs.csv')
            searched = form.cleaned_data['text']
            myfile = request.data['myfile']

            print('Lets find it:')
            with fs.open(filename, 'rt') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for (i, row) in enumerate(readCSV):
                    print(i)
                    if searched in row[1]:
                        found = row[0]
                        print('In song: %s' % found)
        
            print('Data analysis')
            return render(request, 'data_analysis.html',
                        {'result_present': True,
                        'found': found})

    return render(request, 'data_analysis.html')'''

def data_analysis(request): #kluczowa definicja
    print('Data analysis')
    if request.method == 'POST':
        searched = request.POST.get('searched', "")
        '''with open('text.txt','w') as test:
            test.write(searched)'''
        
        print (searched)
        with open(r'static\data\songs.csv','rt')as f:
            data = csv.reader(f)
            found=[]
            for (i, row) in enumerate(data):
                print(i)
                if searched.lower() in row[1].lower():
                    found.append(row[0])
                    print('In song: %s' % found)
                    with open('text.txt','a') as test:
                        test.write('\n!')
                else:
                    print('Not found' % found)
            print('Data analysis')
            result = " - ".join(found)
            return render(request, 'data_analysis.html',
                        {'searched': searched,
                        'result_present': True,
                        'found': result})
    return render(request, 'data_analysis.html')
