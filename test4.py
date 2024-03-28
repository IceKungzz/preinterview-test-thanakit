from datetime import datetime


date_x = datetime.strptime(input('กรอกวันที่ X รูปแบบ yyyymmdd: '),'%Y%m%d')
date_y = datetime.strptime(input('กรอกวันที่ Y รูปแบบ yyyymmdd: '),'%Y%m%d')
date_m = datetime.strptime(input('กรอกวันที่ M รูปแบบ yyyymmdd: '),'%Y%m%d')

if date_m >= date_x and date_m <= date_y:
    diff = (date_m-date_x).days
    print('true ห่างจากวันที่ x ',diff ,' วัน')
else:
    diff = (date_m-date_x).days
    print('false ห่างจากวันที่ x ',diff,' วัน')




