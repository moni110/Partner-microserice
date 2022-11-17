import csv
import json

def writeFunc():
    """ this will allow users to pull student data from your json file and then convert/write it to the
    csv file"""
    with open('your_student_json_file.json') as file:
        data = json.load(file)
    survey_data = data['survey_data']
    data_file = open('studentApp.csv', 'w')

    csv_writer = csv.writer(data_file)
    i = 0
    for students in survey_data:
        if i == 0:
            header = students.keys()  #placeing headers of CSV file
            csv_writer.writerow(header)
            i = i + 1
        csv_writer.writerow(students.values())
    data_file.close()

