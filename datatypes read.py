university_data = [
   {
      "name":"college1",
      "branch_details":{
         "CE":[
            "student_1",
            "student_2"
         ],
         "EC":[
            "student_3",
            "student_4"
         ]
      }
   },
   {
      "name":"college2",
      "branch_details":{
         "ME":[
            "student_5",
            "student_6"
         ],
         "EC":[
            "student_7",
            "student_8"
         ]
      }
   }
]

# Write a function which accepts 2 parameters student_roll and university_data. The function should print college name and branch name


def print_from_arr(student_roll, university_data):
    for records in university_data:
        try:
            
            for branch_names, stud_rolls in records['branch_details'].items():
                if student_roll in stud_rolls: 
                    return "The college name is '{0}' and branch name is '{1}'".format(records['name'], branch_names)
        except Exception as e:
            continue
    return "True"     
print(print_from_arr(str('student_5'), university_data))
print(print_from_arr(str('student_30'), university_data))