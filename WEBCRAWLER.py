#citation : https://docs.python.org/2/library/htmlparser.html?highlight=htmlparser
#https://docs.python.org/2/howto/urllib2.html
#https://docs.python.org/2/library/unicodedata.html?highlight=unicodedata
#https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#The basic find method: findAll(name, attrs, recursive, text, limit, **kwargs)

import requests
import urllib2
from BeautifulSoup import BeautifulSoup 
import urllib
import unicodedata
from HTMLParser import HTMLParser
#help from https://docs.python.org/2/library/htmlparser.html





class URLS(HTMLParser) :#webcrawling to get urls of html page containing
#data

    def handle_starttag(self, tag, attrs):#getting urls and titles of job links
        if tag == "a" :
            for (resttag, val) in attrs :
                if resttag == "href" and len(val.split("/")) >0 :
                    url = val
                    a =val.split("/")
                    for k in a :
                       if k != "" : 
                        self.urls += [self.base + url]
                        self.titles += [k]
        
    def getURLS(self, url, path) :
        self.urls,self.titles = [],[]
        self.base = path
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'FIREFOX LOL')#tricking website into 
        #thinking we are a browser
        opener = urllib2.build_opener()
        data = opener.open(request).read()
        self.feed(data)
        return (self.titles, self.urls)

def getText(page) :
    soup = BeautifulSoup(page) #getting particular data
    file = []
    for hit in soup.findAll("div"):
       #converting unicode str to text string (keys stored in json file as
       #unicode str
        file += [unicodedata.normalize('NFKD', hit.text).encode('ascii','ignore') +"\n"]
    file = file[1]
    index = file.find("Dear")
    file = file[index:]
    finish = file.find("Ad Injection")#stripping useless data
    file = file[:finish]
    return(file)


def findJob(jobname) :
    parser = URLS()
    titles,urls  = parser.getURLS('http://www.jobhero.com/sample-cover-letters/',"http://www.jobhero.com") 
    #print(len(titles))
    if jobname in titles :
        index = titles.index(jobname) 
        url = urls[index]
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'FIREFOX LOL')
        opener = urllib2.build_opener()
        page = opener.open(request).read()
        text = getText(page) 
        return text
    else: return "found nothing"
        
 ############################
 ##Test
 ##############################3
#req = 'http://www.jobhero.com/sample-cover-letters/'
#response = urllib.urlopen(req)
#the_page = response.read()
#print(the_page)

#request = urllib2.Request('http://www.jobhero.com/sample-cover-letters/')
#request.add_header('User-Agent', 'FIREFOX LOL')
#opener = urllib2.build_opener()
#data = opener.open(request).read()
#print (data)      
#findJob("youth-worker-cover-letter")        
#parser = URLS()
#titles,urls  = parser.getURLS('http://www.jobhero.com/sample-cover-letters/',"http://www.jobhero.com" ) 
#i = titles.index('3d-artist-cover-letter')
#i2 = titles.index('zookeeper-cover-letter')
#titles = titles[i:i2+1]
#print(len(titles))
#print(titles)
                            
#url = "http://www.jobhero.com/3d-artist-cover-letter/"                       
#request = urllib2.Request(url)
#request.add_header('User-Agent', 'FIREFOX LOL')
#opener = urllib2.build_opener()
#page = opener.open(request).read()
#print(getText(page))

#for hit in hello.findAll(attrs ={"style": str.startswith(attrs[1], "border")}):
#    print hit.text
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
