import urllib.parse
import urllib.request
import time

def postt(posturl, data):
    req = urllib.request.Request(posturl, data)
    return urllib.request.urlopen(req)

if __name__ == '__main__':
    posturl = 'http://47.92.48.100:9001/upload'
    dd =  urllib.parse.urlencode({
        'api_key': 'sdakasyri',
        'device_id': '1',
        'data': 'ON'}).encode('utf-8')
    while(True):
        postt(posturl, dd)
        time.sleep(2)

