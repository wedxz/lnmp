#!/usr/bin/python
#coding:utf-8
try:
    import sys,urllib2,json
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % sys.argv[1] 
    content = urllib2.urlopen(apiurl).read()
    data = json.loads(content)['data']
    code = json.loads(content)['code']
    if code == 0:
        print data['country_id']
    else:
        print data
except:
    print "Usage:%s IP" % sys.argv[0]