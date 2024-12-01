from django.shortcuts import render, HttpResponse
from .utils import get_data
import datetime
import pytz
import re

def get_attendence(request):
    if request.method == 'POST':
        roll_num = ''.join(request.POST.getlist('roll')).upper()
        date_obj = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('Asia/Kolkata'))
        dta = get_data(rollno=roll_num, date_obj=date_obj)
        print(dta)
        if type(dta) != str:
            # Find the labs key (the one containing parentheses)
            labs_key = next((key for key in dta.keys() if '(' in str(key)), None)
            if labs_key:
                # Extract numbers from the labs string using regex
                labs_str = dta[labs_key]
                labs_numbers = re.findall(r'\d+', labs_str)
                dta['LABS'] = labs_numbers
                del dta[labs_key]  # Remove the old key

            # Convert all other values to proper format
            exclude_keys = {'roll_number', 'attendance_percentage', 'total_classes', 'LABS'}
            subject_data = {}
            for key, value in dta.items():
                if key not in exclude_keys:
                    subject_data[key] = value
            dta['subjects'] = subject_data

            return render(request, 'show_attendence.html', dta)
        else:
            return HttpResponse(dta)
    return render(request, 'get_attendence.html')
