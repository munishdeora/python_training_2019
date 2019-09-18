"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json

with open("faculty.json",'r') as file:
    file_contents = file.read()
    
# Converts  JSON Data types to Python Data Types 
my_data = json.loads(file_contents)

##facuilty1 detail
fact_name=my_data['faculty'][0]['faculty1'][0]
print("facuilty1 detail : ")
print("first_name : ",fact_name['name'][0]['first_name'])
print("lastname : ",fact_name['name'][1]['lastname'])

fact_photo = my_data['faculty'][0]['faculty1'][4]['photo']
print("Photo : ",fact_photo)

depart= my_data['faculty'][0]['faculty1'][5]["department"]
print("Department : ",depart)

res_area=my_data['faculty'][0]['faculty1'][6]["research_area"]
print("Research Areas : ",res_area[0]," ",res_area[1])
#contact details of facuilty
cont_detail=my_data['faculty'][0]['faculty1']
first_id=cont_detail[3]['email_id'][0]['first_id']
second_id=cont_detail[3]['email_id'][1]['second_id']

first_no=cont_detail[2]['mobile_no'][0]['first_no']
second_no= cont_detail[2]['mobile_no'][1]['second_no']
print("mobile_no : {} , {} email_id : {} {}".format(first_no,second_no,first_id,second_id))



###facuilty2 detail
fact_name=my_data['faculty'][1]['faculty2'][0]
print("facuilty2 detail : ")
print("first_name : ",fact_name['name'][0]['first_name'])
print("lastname : ",fact_name['name'][1]['lastname'])

fact_photo = my_data['faculty'][1]['faculty2'][4]['photo']
print("Photo : ",fact_photo)

depart= my_data['faculty'][1]['faculty2'][5]["department"]
print("Department : ",depart)

res_area=my_data['faculty'][1]['faculty2'][6]["research_area"]
print("Research Areas : ",res_area[0]," ",res_area[1])
#contact details of facuilty
cont_detail=my_data['faculty'][1]['faculty2']
first_id=cont_detail[3]['email_id'][0]['first_id']
second_id=cont_detail[3]['email_id'][1]['second_id']

first_no=cont_detail[2]['mobile_no'][0]['first_no']
second_no= cont_detail[2]['mobile_no'][1]['second_no']
print("mobile_no : {} , {} email_id : {} {}".format(first_no,second_no,first_id,second_id))


