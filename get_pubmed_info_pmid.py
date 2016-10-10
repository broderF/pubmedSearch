import urllib2
import json
import time
from datetime import date

start_date =  date(1980, 1, 1)
end_date = date(2007,12,31)
keywords = "STAT3,ATG16L1,NOD2,IL23R,\"HLA\" OR \"MHC\",GWAS,autophagy"
line = start_date.isoformat()
for gene in keywords.split(","):
        disease = "\"Inflammatory Bowel Diseases\" OR \"Crohn\'s disease\" OR \"ulcerative colitis\""
        time = "\""+start_date.strftime("%Y/%m/%d")+"\"[Date - Publication] : \""+end_date.strftime("%Y/%m/%d")+"\"[Date - Publication]"

        basic = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
        database_search = 'db=pubmed'
        return_mode = 'retmode=json'
        ret_max = 'retmax=10000'
        search_terms = "term=(("+gene +") AND ("+disease +" ) AND("+time+"))"

        full_text = basic+'?'+database_search+'&'+return_mode+'&'+ret_max+'&'+search_terms
        full_text = full_text.replace(" ","+")
    # print full_text
        answer = urllib2.urlopen(full_text).read()
#        print answer
        data = json.loads(answer)
        pubids = data["esearchresult"]["idlist"]
        pub_file = open(gene+'publications_'+str(len(pubids))+'.txt','w')
        pub_file.write('date,edate\n')

        for pubid in pubids:
                request = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&rettype=abstract&id='+pubid
                answer = urllib2.urlopen(request).read()
                data = json.loads(answer)
                date = data["result"][pubid]['pubdate']
                edate = data["result"][pubid]['epubdate']
                pub_file.write(date+','+edate+'\n')
