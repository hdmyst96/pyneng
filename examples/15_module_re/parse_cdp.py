import re
from pprint import pprint


# first variant 
def parse_cdp_ver1(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            device_match = re.search(r'Device ID: (\S+)',line)
            platform = re.search('Platform: (\S+ \S+)', line)
            ios = re.search('Version (\S+)', line)
            if device_match:
                device = device_match.group(1)
                result[device]= {}
            elif platform:
                result[device]['Platform'] = platform.group(1)
            elif ios:
                result[device]['Ios'] = ios.group(1)
        return result
'''
if __name__ == "__main__":
    result = parse_cdp_ver1('sh_cdp_neighbors_sw1.txt')
    pprint(result)
'''

#second variant
def parse_cdp_ver2(filename):
    result = {}
    with open(filename) as f:
        for line in f: 
            if line.startswith('Device ID:'):
                device = re.search(r'Device ID: (\S+)', line).group(1)
                result[device] = {}
            elif line.startswith('Platform'):
                platform = re.search(r'Platform: (\S+ \S+)',line).group(1)
                result[device]['Platform'] = platform
            elif line.startswith('Cisco IOS Software'):
                ios = re.search(r'Version (\S+)', line).group(1)
                result[device]['IOS'] = ios
        return result

#third variant
def parse_cdp_ver3(filename):
    result = {}
    regex =(r'Device ID: (?P<device>\S+)|'
            r'Platform: (\?P<platform>S+ \S+)|'
            r'Version (?P<version>\S+)|'
            r'IP address:(?P<ip>\S+)')
    with open(filename) as f:
        for line in f:
           match = re.search(regex,line)
           if match:
               if match.lastgroup == 'device':
                   device = match.group('device')
                   result[device] = {}
               else:
                   group = match.lastgroup
                   result[device][group] = match.group(group)
        return result
'''
if __name__ == "__main__":
    result = parse_cdp_ver3('sh_cdp_neighbors_sw1.txt')
    pprint(result)
'''

#fourth variant
def parse_cdp_ver4_finditer(filename):
    data = {}
    regex =(r'Device ID: (?P<device>\S+).+?'
            r'IP address:(?P<ip>\S+).+?'
            r'Platform: (\?P<platform>S+ \S+).+?'
            r'Version (?P<ios>\S+)')
    with open(filename) as f:
           result = re.findinter(regex,f.read(),re.DOTALL)
           for match in result:
               device = match.group('device')
               groupdict = match.groupdict()
               del groupdict['device']
               data[device] = groupdict
           return data

if __name__ == "__main__":
    result = parse_cdp_ver3('sh_cdp_neighbors_sw1.txt')
    pprint(result)

