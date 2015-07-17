from django.shortcuts import render
import csv
import codecs
import os
from core import Analyser,FileDataSource
import csv
def index(request):
 folder='upload/output_file.csv'
 folder1='upload/output_analysed.csv'
 if request.POST :
     if 'Great' in request.POST and request.FILES :
         csvfile = request.FILES['csv_file']
         k=csvfile
         csvfile.open()
         uploaded_filename = request.FILES['csv_file'].name
         data = [row for row in csv.reader(csvfile.read().splitlines())]
         data1= [row for row in csv.reader(csvfile.read())]
         writer = csv.writer(open(folder, 'wb'))
         for row1 in data:

               writer.writerow(row1)
         return render(request, "myapp/index.html",{'data':data})
     elif 'your_name' in request.POST:

         dat=request.POST.get('your_name')
         if not dat=='' :
           k=FileDataSource.get_data(folder,dat)
           l=Analyser.Analyse(k)
           FileDataSource.save_data(l,folder1,folder,dat)

           print l
           data= [row for row in csv.reader(open(folder1,'rb'))]
           return render(request,"myapp/index.html",{'data':data})
         else:
             return render(request,"myapp/index.html")
     else:
         return render(request,"myapp/index.html")
 else:
     return render(request,"myapp/index.html")

