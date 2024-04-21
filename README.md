nmap_xml_merge
==========

Description
-----------

nmap_xml_merge is a Python script that allows you to merge multiple nmap XML output files into a single XML file. It simplifies the process of aggregating scan results from multiple Nmap scans into one consolidated file for easier analysis.

Features
--------

- Merge multiple Nmap XML output files into one XML file.
- Converts the merged XML file into an HTML file for easier viewing.
- Works with both Python 2.x and 3.x.

Installation
------------

To install nmap_xml_merge, simply clone the repository:

    git clone https://github.com/codesecure-org/nmap_xml_merge.git

Navigate to the cloned directory:

    cd nmap_xml_merge

And run the script:

    python nmap_xml_merge.py

Usage
-----

Simply run the nmap_xml_merge.py script in the directory containing your Nmap XML output files. The script will automatically merge all XML files in the directory and generate a single merged XML file and an HTML file for easy viewing.

    python nmap_xml_merge.py

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
