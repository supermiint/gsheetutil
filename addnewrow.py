from oauth2client.service_account import ServiceAccountCredentials
import gspread, datetime, random, time

# Gsheet initial parameter
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gsheetutil-acef7b498f91.json', scope)
client = gspread.authorize(creds)
sheet = client.open('test').worksheet('Sheet1')
start = datetime.datetime.now()
for i in range(1,200):
    try :
        sheet.update('B'+str(i), "let. "+ str(i))
    except gspread.exceptions.APIError:
        print('error')
        time.sleep(5)
        continue
stop = datetime.datetime.now()
dif = stop-start
print('proceed time ', dif.total_seconds()) 
