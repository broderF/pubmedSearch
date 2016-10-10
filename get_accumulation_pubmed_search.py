import urllib2
import json
import time
from datetime import date
import argparse

print "here"
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='search input string')
args = parser.parse_args()
search_term=args.i
print search_term

start_date =  date(1995, 1, 1)
end_date = date(1995,12,31)
today = date.today()
while start_date < today:
    line = start_date.isoformat()
    time = "\""+start_date.strftime("%Y/%m/%d")+"\"[Date - Publication] : \""+end_date.strftime("%Y/%m/%d")+"\"[Date - Publication]"

    basic = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    database_search = 'db=pubmed'
    return_mode = 'retmode=json'
    ret_max = 'retmax=1000'
    search_term_yearly = "term=(("+search_term +" ) AND("+time+"))"

    full_text = basic+'?'+database_search+'&'+return_mode+'&'+ret_max+'&'+search_term_yearly
    full_text = full_text.replace(" ","+")
    # print full_text
    answer = urllib2.urlopen(full_text).read()
#        print answer
    data = json.loads(answer)
    count = data["esearchresult"]["count"]
    line= line + ";"+str(count)
    print line

    start_date = start_date.replace(year = start_date.year + 1)
    end_date = end_date.replace(year = end_date.year + 1) 
