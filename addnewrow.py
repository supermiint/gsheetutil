from oauth2client.service_account import ServiceAccountCredentials
import gspread, datetime, random, time

# Gsheet initial parameter
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('gsheetutil-acef7b498f91.json', scope)
client = gspread.authorize(creds)
sheet = client.open('account').worksheet('dec22')
start = datetime.datetime.now()

b = sheet.get_values('J2:K32')
tl = []
print(type(b))
print(b)
for i in b :
    for j in i:
        tl.append(int(j))
print(tl)
print(len(tl))

def updates(l,sheet):
    indexp = 1
    for i in l:
        while(True):
            try :
                sheet.update('E'+str(indexp+1), i)
                break
            except gspread.exceptions.APIError:
                print('error')
                time.sleep(5)
                continue
        indexp = indexp+1

def dendate(sheet):
    indexp = 2
    datei = 1
    while(True):
        if indexp%2 == 0 :
            if indexp > 19:
                while(True):
                    try :
                        sheet.update('B'+str(indexp), str(datei)+'/12/2022')
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
            else:             
                while(True):
                    try :
                        sheet.update('B'+str(indexp), '0'+str(datei)+'/12/2022')
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
        else :
            if indexp > 19:
                while(True):
                    try :
                        sheet.update('B'+str(indexp), str(datei)+'/12/2022')
                        datei=datei+1
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
            else:             
                while(True):
                    try :
                        sheet.update('B'+str(indexp), '0'+str(datei)+'/12/2022')
                        datei=datei+1
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
        if indexp == 63:
            break
        indexp = indexp+1

def densc(sheet):
    indexp = 2
    datei = 1
    while(True):
        if indexp%2 == 0 :
            if indexp > 19:
                while(True):
                    try :
                        sheet.update('D'+str(indexp), 'wash')
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
            else:             
                while(True):
                    try :
                        sheet.update('D'+str(indexp), 'wash')
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
        else :
            if indexp > 19:
                while(True):
                    try :
                        sheet.update('D'+str(indexp), 'dry')
                        datei=datei+1
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
            else:             
                while(True):
                    try :
                        sheet.update('D'+str(indexp), 'dry')
                        datei=datei+1
                        break
                    except gspread.exceptions.APIError:
                        print('error')
                        time.sleep(5)
                        continue
        if indexp == 63:
            break
        indexp = indexp+1

updates(tl,sheet)
dendate(sheet)
densc(sheet)
stop = datetime.datetime.now()
dif = stop-start
print('proceed time ', dif.total_seconds()) 
