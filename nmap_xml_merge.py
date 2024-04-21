#!/usr/bin/env python3

import os
import re
import logging
import xml.etree.ElementTree as ET

def merge_nmap(xml_files, merge_file):
    HOSTS = 0
    with open(merge_file, mode='a', encoding='utf-8') as merge_file:
        for xml_file in xml_files:
            with open(xml_file) as f:
                nmap_xml = ET.parse(f)
                for host in nmap_xml.findall('host'):
                    HOSTS += 1
                    current_host = ET.tostring(host, encoding='unicode', method='xml') 
                    merge_file.write(current_host)
                    merge_file.flush()    
    return HOSTS

def add_header(merge_file):
    nmap_header  = '<?xml version="1.0" encoding="UTF-8"?>'
    nmap_header += '<!DOCTYPE nmaprun>'
    nmap_header += '<?xml-stylesheet href="file:///usr/share/nmap/nmap.xsl" type="text/xsl"?>'
    nmap_header += '<nmaprun scanner="nmap" args="nmap -iL hostList.txt" start="1" version="7.70" xmloutputversion="1.04">'
    nmap_header += '<scaninfo type="syn" protocol="tcp" numservices="1" services="1"/>'
    nmap_header += '<verbose level="0"/>'
    nmap_header += '<debugging level="0"/>'

    with open(merge_file, "w") as mFile:  
        mFile.write(nmap_header)

def add_footer(merge_file, hosts_count):
    nmap_footer  = f'<runstats><finished time="1" timestr="Wed Sep  0 00:00:00 0000" elapsed="0" summary="Nmap done at Wed Sep  0 00:00:00 0000; {hosts_count} IP address scanned in 0.0 seconds" exit="success"/>'
    nmap_footer += '</runstats>'
    nmap_footer += '</nmaprun>'

    with open(merge_file, "a") as mFile:  
        mFile.write(nmap_footer)

def htmlER(merge_file):
    import os
    cmd = '/usr/bin/xsltproc'
    if os.path.isfile(cmd):
        out = re.sub(r'.xml', '.html', merge_file)
        cmd = f"{cmd} -o {out} {merge_file}"
        os.system(cmd)
        print("Output HTML File:", os.path.abspath(out))
    else:
        print(f"{cmd} does not exist")

def main_nmapmerge():
    xml_files = [file for file in os.listdir() if file.endswith('.xml')]
    if not xml_files:
        print("No XML files found in the current directory. Exiting.")
        exit()

    HOSTS = 0

    # Create the Merged filename
    from datetime import datetime
    dtNow = datetime.now() 
    dt = re.sub(r"\s+", '-', str(dtNow))
    dt = re.sub(r":", '-', str(dt))
    merge_file = f"nmap_merged_{dt}.xml"

    # Add Header to mergefile
    add_header(merge_file)

    HOSTS = merge_nmap(xml_files, merge_file)

    # Add Footer to mergefile
    add_footer(merge_file, HOSTS)
    print('')
    print("Output XML File:", os.path.abspath(merge_file))

    # Convert merged XML to html
    htmlER(merge_file)

if __name__ == "__main__":
    main_nmapmerge()
