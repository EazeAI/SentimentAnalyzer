import csv

def get_data(input_file,input_row):
    column = {}
    try:
        with open(input_file, 'r') as f:
            reader = csv.reader(f)
            headers = reader.next()

            for h in headers:
               column[h] = []
            #print column
            try:
               if input_row in column:
                   for row in reader:
                     for h, v in zip(headers, row):
                        column[h].append(v)

               else:
                   print "Wrong column Given"
                   print "The cloumns are:" + str(column)
                   exit(1)
            except(IOError):
                print "Try again"
    except ( IOError):
        print("Wrong file or file path or Row")

    return column[ input_row ]
def save_data(path,output_file,input_file,input_row):

    reader= csv.reader(open(input_file, 'rb'))
    row0=reader.next()

    j=0
    for i in range(len(row0)):
        if row0[i]==input_row:
            row0 = row0[0:i+1] +[('Analysis Report')] + row0[i+1:]
            break
        else:
            j=j+1
    #print j
    writer = csv.writer(open(output_file, 'wb'))
    writer.writerow(row0)
    i=0
    for row in reader:
        writer.writerow(row[0:j+1] + [path[i]] + row[j+1:])
        i=i+1