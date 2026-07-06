#import csv

#def insertData(data):
    #field=['Name', "Father's Name", "Gender", "DOB","Crimes"]
    #x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    #filen = "Criminal.csv"
    #with open(filen, 'a') as csvfile:
        #csvwriter = csv.writer(csvfile)
        #csvwriter.writerow(field)
        #csvwriter.writerow(x)

        #df.to_csv('existing.csv', mode='a', index=False, header=False)


# Import writer class from csv module
from csv import writer
  
def insertData(data):

    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
  
# Open our existing CSV file in append mode
# Create a file object for this file
    with open('Criminal.csv', 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(x)
    
        #Close the file object
        f_object.close()