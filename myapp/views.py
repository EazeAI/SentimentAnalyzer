from django.shortcuts import render
import csv
import codecs
import os
import yaml

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

def about(request):

    with open("dicts/positive.yml") as f:
     list_doc = yaml.safe_load(f)
     list_doc=str(list_doc)

     list_doc1 = list_doc.replace("positive", "");
     list_doc1 = list_doc1.replace("'", "");
     list_doc1 = list_doc1.replace(",", "");
     list_doc1 = list_doc1.replace("[]", "");

     list_doc1 = list_doc1.replace("{", "");
     list_doc1 = list_doc1.replace("}", "");
     list_doc1=list_doc1.split(':')
    data=list_doc1
    with open("dicts/negative.yml") as f1:
     list_doc2 = yaml.safe_load(f1)
     list_doc2=str(list_doc2)

     list_doc2 = list_doc2.replace("negative", "");
     list_doc2 = list_doc2.replace("'", "");
     list_doc2 = list_doc2.replace(",", "");
     list_doc2 = list_doc2.replace("[]", "");

     list_doc2 = list_doc2.replace("{", "");
     list_doc2 = list_doc2.replace("}", "");
     list_doc2=list_doc2.split(':')
    data1=list_doc2
    context_dict = {'boldmessage': "Warning:Do not Enter Booloean object like {no ,yes, true, false}",'data':list_doc1,'data1':list_doc2}
    print list_doc1[1]
    if request.POST:
       if 'Positive' in request.POST:
            dat=request.POST.get('your_name')
            print dat
            dat=str(dat)
            with open("dicts/positive.yml") as f:
               list_doc = yaml.load(f)

            #print list_doc
            if not dat=='' :
              list_doc[dat]=['positive']

              with open('dicts/positive.yml','w') as k:
                 yaml.dump(list_doc,k)
              with open("dicts/positive.yml") as f5:
                  list_doc = yaml.safe_load(f5)
                  list_doc=str(list_doc)
                  list_doc1 = list_doc.replace("positive", "");
                  list_doc1 = list_doc1.replace("'", "");
                  list_doc1 = list_doc1.replace(",", "");
                  list_doc1 = list_doc1.replace("[]", "");
                  list_doc1 = list_doc1.replace("{", "");
                  list_doc1 = list_doc1.replace("}", "");
                  list_doc1=list_doc1.split(':')
              context_dict = {'boldmessage': "Update:Entered Positive attribute",'data':list_doc1,'data1':list_doc2}
              render(request, 'myapp/about.html',context_dict)
            else:
              context_dict = {'boldmessage': "Error:Entered a Blank!!!!!!!!!!!!",'data':list_doc1,'data1':list_doc2}
              render(request, 'myapp/about.html',context_dict)
       elif 'Negative' in request.POST:
            dat=request.POST.get('your_name')
            print dat
            dat=str(dat)
            with open("dicts/negative.yml") as f:
               list_doc = yaml.load(f)

            if not dat=='' :
              list_doc[dat]=['negative']

              with open('dicts/negative.yml','w') as k:
                 yaml.dump(list_doc,k)
              with open("dicts/negative.yml") as f1:
                list_doc2 = yaml.safe_load(f1)
                list_doc2=str(list_doc2)

                list_doc2 = list_doc2.replace("negative", "");
                list_doc2 = list_doc2.replace("'", "");
                list_doc2 = list_doc2.replace(",", "");
                list_doc2 = list_doc2.replace("[]", "");

                list_doc2 = list_doc2.replace("{", "");
                list_doc2 = list_doc2.replace("}", "");
                list_doc2=list_doc2.split(':')
                data1=list_doc2
              context_dict = {'boldmessage': "Update:Entered Negative attribute",'data':list_doc1,'data1':list_doc2}
              render(request, 'myapp/about.html',context_dict)
            else:
              context_dict = {'boldmessage': "Error:Entered a Blank!!!!!!!!!!!!",'data':list_doc1,'data1':list_doc2}
              render(request, 'myapp/about.html',context_dict)


    return render(request, 'myapp/about.html',context_dict)