import requests
import re
#regex = r"^[^{]*{([^}]*)}.*$"
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


#for ip in array:
    #write each line
 #   f = open("skyText.odt", "w")
  #  f.writelines(array)
   # f.close()

with open('skyText.odt', 'w') as filehandle:
    for ip in array:
        filehandle.write('%s\n' % ip)

        
# open file and read the content in a list
with open('skyText.odt', 'r') as filehandle:
    ips_read = [current_place.rstrip() for current_place in filehandle.readlines()]

print(ips_read)

#for ip in array:
    #write each line
 #   f = open("skyText.odt", "w")
  #  f.writelines(array)
   # f.close()
#f = open('skyText.odt', 'r')
#count = 0  
#while True:
    #count +=1
    #ips_read = f.readlines()

    #if not ips_read:
       # break
    #print(ips_read)
#f = open("taskfile.rtf","r+")
#f.truncate(0)
#f.close()

#print("----------")

#print(array)
#f = open("taskfile.rtf", "a")
#f.write(array)
#f.close()
#f = open('taskfile.rtf', 'r')
#lines = f.readlines()

#f.close()

#print (select)   

#matches = re.sub(regex, select, re.MULTILINE)
