from bs4 import BeautifulSoup
import requests
import random
import string
from .models import Student
import os
from typing import Dict, Any

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


imp_info = {'token': ''}


def get_resp(date_obj, roll_no):
    try:
        student = Student.objects.get(roll_no=roll_no)
    except Student.DoesNotExist:
        return {
            'error': True,
            'message': f"Roll number {roll_no} not found. Please check and try again."
        }

    url = 'http://103.203.175.90:94/attendance/attendanceTillTodayReport.php'
    imp_info['indian_time'] = date_obj
    headers = {
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://103.203.175.90:94',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://103.203.175.90:94/attendance/attendanceTillADate.php',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'PHPSESSID={imp_info["token"]}',
        'Connection': 'close',
    }
    indian_time = imp_info['indian_time']
    data = {
        'acadYear': '2024-25',
        'yearSem': student.year,
        'branch': student.branch,
        'section': student.section.upper(),
        'dateOfAttendance': f'{indian_time.day if len(str(indian_time.day)) == 2 else "0" + str(indian_time.day)}-{indian_time.month if len(str(indian_time.month)) == 2 else "0" + str(indian_time.month)}-{indian_time.year}',
    }

    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    # print(imp_info['token'])
    return response


def get_data(rollno, date_obj):
    # try:
    resp_req = get_resp(date_obj, rollno)
    if isinstance(resp_req, dict) and resp_req.get('error'):
        return resp_req
    html = resp_req.text
    if "<tr><td>User Name</td><td>:</td><td><input type=textbox name='username' id='username'" in html:
        print(len(html))
        print('entered\n')
        rand_str: str = ''.join(random.choices(string.ascii_lowercase, k=3))
        sess_token: str = f"ggpmgfj8dssskkp2q2h6db{rand_str}0"
        url: str = "http://103.203.175.90:94/attendance/attendanceLogin.php"
        headers: Dict[str, str] = {
            "Cache-Control": "max-age=0",
            "Origin": "http://103.203.175.90:94",
            "Content-Type": "application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Sec-GPC": "1",
            "Accept-Language": "en-US,en",
            "Referer": "http://103.203.175.90:94/attendance/attendanceLogin.php",
            "Accept-Encoding": "gzip, deflate, br",
            "Cookie": f"PHPSESSID={sess_token}",
            "Connection": "keep-alive"
        }

        payload: str = f'username={USERNAME}&password={PASSWORD}&captcha='

        response: requests.Response = requests.post(url, headers=headers,
                                                    data=payload, allow_redirects=False)

        # print(response.text)
        imp_info['token'] = sess_token
        return get_data(rollno, date_obj)
    else:
        soup = BeautifulSoup(html, 'html.parser')
        tr_tag = soup.find('tr', {'id': f'{rollno}'})
        data = {}
        data['roll_number'] = tr_tag.find(
            'td', {'class': 'tdRollNo'}).text.strip().replace(' ', '')
        subject_data = {td['title']: td.text.strip()
                        for td in tr_tag.find_all('td') if 'title' in td.attrs}
        data.update(subject_data)
        td_percent_tag = tr_tag.find('td', {'class': 'tdPercent'})
        data['attendance_percentage'] = td_percent_tag.contents[0].strip()
        class_counts = td_percent_tag.find('font').text.strip()
        data['total_classes'] = class_counts
        return data
    # except:
    #     return "invalid roll number"
