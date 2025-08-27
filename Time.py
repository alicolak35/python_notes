from datetime import datetime
import time    



date = [2025, 8, 1, 8, 10,00]

def date_to_timestamp(start_date:list):
    dt = datetime(date[0], date[1], date[2], date[3], date[4], date[5])
    gmt_3 = 3*3600
    timestamp = int((dt.timestamp() + gmt_3)) * 1000 
    
    return timestamp

def timestap_check(last_ts):
    now = int(time.time() * 1000)
    
    diff = now - last_ts
    if diff > 900000:
        return 1
    else:
        return 0
    
if __name__ == '__main__':
    a = int(time.time()) * 1000
    b = 10
    
    
    