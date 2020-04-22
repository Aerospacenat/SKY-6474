import requests
import re
#regex = r"^[^{]*{([^}]*)}.*$"

array = []
try:
    ret = requests.get('https://raw.githubusercontent.com/chromium/chromium/8574431a884cc99dfb7bdaaeb6cbf3b297fd9fba/net/dns/public/doh_provider_list.cc')
except e as Exception:
    print("getting source failed: %s" % str(e))
    os.exit(1)
if ret.status_code != 200:
    print("getting source failed, retrun code %d" % ret.status_code)
    os.exit(1)
source = ret.text
start = source.find('providers{{')
source = source[start+11:]
end = source.find('}};')
source = source[:end]

print (source)

for part in source.split('DohProviderEntry('):
    end1 = part.find('},')
    select = part[:end1+2]
    
    #matches = re.sub(regex, select, re.MULTILINE)
    match = re.findall(r"^[^{]*{([^}]*)}.*$", select.strip())
    ips = []
    try: 
       ips = re.findall(r'[^"]*"([^"]*)"', match[0])
    except IndexError as e:
       pass
    array = array+ips
   


print(array)
    


#print("----------")

#print(array)
f = open("taskfile.rtf", "a")
f.write(array)
f.close()
f = open('taskfile.rtf', 'r')
#lines = f.readlines()

#f.close()

#print (select)   

#f = open("taskfile.rtf","r+")
#f.truncate(0)
#f.close()   

