import csv
import datetime
from task_17_4 import convert_str_to_datetime
from task_17_4 import convert_datetime_to_str

result= []
unique_pairs = {}
with open('mail_log.csv') as src, open('result.csv', 'w') as dest:
    log  = csv.reader(src)
    header = next(src)
    header= header.strip().split(',')
    for element in log:
       name,email,date = element
       if email  in unique_pairs:
          if convert_str_to_datetime(date) > unique_pairs[email]:
              unique_pairs[email] = convert_str_to_datetime(date) 
       else:
           unique_pairs[email] =  convert_str_to_datetime(date)
           result.append([name,email,date])
    writer = csv.writer(dest)
    writer.writerow(header)
    for row in result:
        writer.writerow(row)

