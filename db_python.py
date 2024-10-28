# Rashid available shift time


select empid from emp_details where datetime.now()

emp_details_arr = ['empid']
static_shift_time = {'early_morning': [7, 00.30], 'morning' : [9, 17], 'afternoon': [14, 12.30]}

for shift_name, shift_time in static_shift_time: # [7, 00.30]
    for emp_id in emp_details_arr:
        available_time = datetime.now()
        if available_time in shift_time [0] and available_time in shift_time [1]  :
            print("Shift time of  the employee id {0} is {1} i.e {2}".format(emp_id, shift_name, (',', join(shift_time))))
