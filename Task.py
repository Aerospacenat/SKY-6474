import requests
import re
ips_read = []
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
    
    match = re.findall(r"^[^{]*{([^}]*)}.*$", select.strip())
    ips = []
    try: 
       ips = re.findall(r'[^"]*"([^"]*)"', match[0])
    except IndexError as e:
       pass
    array = array+ips

with open('skyText.odt', 'r') as filehandle:
    ips_read = [current_place.rstrip() for current_place in filehandle.readlines()]

print(ips_read)

def Diff(ips_read, array): 
    return (list(set(ips_read) - set(array))) 

print("Difference of =")
diff_lists = Diff( ips_read, array)
print(diff_lists) 

if diff_lists == []:
    print("No difference, will now end" )
    exit()
else :
    print("Difference, writing to file")
    print("Red Alert")
    with open('skyText.odt', 'w') as filehandle:
        for ip in array:
            filehandle.write('%s\n' % ip)

#set(array).intersection(b)
        







