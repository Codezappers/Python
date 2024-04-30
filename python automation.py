import requests
import schedule
import time

mobile_number = input('Enter the mobile number: ')

def send_sms(mobile_number):
    resp = requests.post('https://textbelt.com/text', { 'phone': mobile_number, 'message': 'Hello babe this message is from a python bot i made', 'key': 'textbelt' })

    print(resp.json())

schedule.every().day.at("06:00").do(send_sms, mobile_number)
#schedule.every(10).seconds.do(send_sms, mobile_number)

while True:
    schedule.run_pending()
    time.sleep(1)