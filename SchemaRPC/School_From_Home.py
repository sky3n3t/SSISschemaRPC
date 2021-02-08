import urllib3
import json
def AtHome():
    http=urllib3.PoolManager()
    schema=f'https://api.ssis.nu/cal/?room=Hela%20skolan'
    filename=http.request('GET',schema)
    subjects=json.loads(filename.data)
    for i in subjects:
        if "fjärrundervisning" in i['subject'].lower():
            if 'a-k' in i['subject'].lower():
                return(True)
            else:
                return(False)
    return(False)