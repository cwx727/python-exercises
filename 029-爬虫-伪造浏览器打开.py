
import urllib.request
#import urllib.parse 
url = "http://www.baidu.com"
send_headers = {
	'BAIDUID':'AAB7C508C26FD3C48439B7183E83E123:FG=1',
	'BD_CK_SAM':'1',
	'BD_HOME':'0',
	'BD_UPN':'133352',
	'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
	'BIDUPSID':'AAB7C508C26FD3C48439B7183E83E123',
	'delPer':'0',
	'H_PS_PSSID':'1459_21098_28205_28132_26350_28140_22157',
	'locale':'zh',
	'PSINO':'5',
	'PSTM':'1544754589',
	'ZD_ENTRY':'baidu'
	}

request = urllib.request.Request(url,headers=send_headers)

reponse = urllib.request.urlopen(request).read()


#print(reponse)
'''

import urllib.request 
import urllib.parse 
url = 'http://www.baidu.com' 
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36' } 
request = urllib.request.Request(url, headers=header) 
reponse = urllib.request.urlopen(request).read() 
fhandle = open("./baidu.html", "wb") 
fhandle.write(reponse) 
fhandle.close()
'''
