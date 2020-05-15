#! /usr/bin/python
import requests
import re
import sys
import getopt
ips_read = []
array = []
URL = "https://raw.githubusercontent.com/chromium/chromium/8574431a884cc99dfb7bdaaeb6cbf3b297fd9fba/net/dns/public/doh_provider_list.cc"
FILE = "skyText.txt"
try:
    opts, args = getopt.getopt(sys.argv[1:], "hu:f:")
except getopt.GetoptError as err:
    print(err)  
    sys.exit(2)
for o, a in opts:
    if o == "-h":
        print("usage: %s -h -f file_with_ips -u source_code_url"  % sys.argv[0])
        sys.exit(0)
    elif o in ("-u"):
        URL = a 
        sys.exit()
    elif o in ("-f"):
        FILE = a
               
print("FILE: %s, URL: %s\n" % (FILE, URL))

try:
    ret = requests.get(URL)
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

try:
    with open(FILE, 'r') as filehandle:
        ips_read = [current_place.rstrip() for current_place in filehandle.readlines()]
except FileNotFoundError as e:
    print("Failed to open file")
    ips_read = []

def Diff(ips_read, array):
    return list((set(ips_read) - set(array)).union(set(array) - set(ips_read)))
diff_lists = Diff( ips_read, array)

if diff_lists != [] :
    print("Difference, writing to file")
    print("Red Alert")
    with open(FILE, 'w') as filehandle:
        for ip in array:
            filehandle.write('%s\n' % ip)
    sys.exit(1)
else:
    print("No difference, will now end" )
    sys.exit(0)
