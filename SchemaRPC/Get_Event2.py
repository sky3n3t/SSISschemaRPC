import urllib3
from datetime import *
import dateutil
import json
def GetLesson(room):
    http=urllib3.PoolManager()
    schema=f'http://api.ssis.nu/cal/?room={room}'
    filename=http.request('GET',schema)
    lessons=json.loads(filename.data)
    for i in lessons:
        lesson=i
        starttime=lesson["start_time"].split(':')
        starttime = datetime(date.today().year,date.today().month,date.today().day,int(starttime[0]),int(starttime[1])).timestamp()
        endtime=lesson["end_time"].split(':')
        endtime = datetime(date.today().year,date.today().month,date.today().day,int(endtime[0]),int(endtime[1])).timestamp()
        if(starttime<datetime.now().timestamp()<endtime):
            #print(i['subject'])
            return(i['subject'],endtime)
    return('break','dont')
