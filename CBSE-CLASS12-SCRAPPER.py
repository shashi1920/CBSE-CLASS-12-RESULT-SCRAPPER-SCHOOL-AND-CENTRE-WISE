
__author__ = 'Shashi'
"""CBSE 2017 Result scrapper school wise and centre wise"""
import requests

import codecs


def pdfdownloader(roll_no, cno,sch,url="http://cbseresults.nic.in/class12npy/class12th17.asp"):
    header = {"Origin":"http://cbseresults.nic.in",'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',"Referer":"http://cbseresults.nic.in/class12npy/class12th17.htm"}
    data={"B2":"Submit","cno":cno,"regno":roll_no,"sch":sch}
    response = requests.post(url,headers=header,data=data)
    print "Saving results for roll no:",roll_no
    file = codecs.open("results/" + roll_no + ".html","w","utf-8")
    file.write(response.text)
    file.close()

"""Everything here is just dummy data, use centre no and school no correctly"""
"""Results will be saved in 'result' folder of the same directory """
start_roll_no=5654000 #Enter start roll no here
end_roll_no=5654200 #Enter end roll no here
centre_no=5120 #This is centre no
school_no=51301 #This is school no
for i in range(start_roll_no,end_roll_no):
    pdfdownloader(str(i),str(centre_no),str(school_no))
