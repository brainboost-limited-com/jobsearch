from urllib.error import URLError
from urllib.request import Request, urlopen
import mechanize
import urllib.parse
import re
from tinydb import Query, TinyDB
import validators



def extract_application_link(url):
    req = Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    page = urlopen(req)
    html = page.read().decode("utf8")
    m = re.findall(r'https:\/\/(t(?:elegram)?\.(?:org|me|dog))\/(?:(joinchat\/[a-zA-Z0-9\-_]{22})|([a-zA-Z0-9\-_]+))', html,flags=re.I)
    result = []
    for match in m:
        result.append('https://' + (('/'.join(match)).replace('//','/')))
    return result



client = TinyDB('jobs.json')

browser = mechanize.Browser()
browser.set_handle_robots(False)

user_agent = [('User-agent',
        'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01'
        )]
browser.addheaders=user_agent




search = ["python jobs remote","remote python developer jobs","remote python jobs entry level","django remote jobs","python developer remote","junior python developer remote","remote python","entry level python jobs remote","python developer work from home","django developer remote jobs","python entry level jobs remote","remote django developer jobs","python developer part time jobs","junior python developer remote jobs","junior django developer remote","entry level python developer jobs remote","part time python jobs remote","python remote jobs for beginners","junior python developer jobs remote","python jobs remote entry level","remote jobs for python developer","remote junior python developer jobs","remote entry level python jobs","python remote jobs worldwide","remote jobs python developer","python contract jobs remote","python developer jobs work from home","python remote jobs for freshers","python apprenticeship remote","python remote work","python coding jobs from home","part time remote python jobs","work from home jobs for python developer","python jobs entry level remote","remote python programming jobs","junior python remote","remote work python","junior python jobs remote","junior python remote jobs","django developer jobs remote","python developer part time","remote junior python developer","python entry level remote jobs","django developer remote","python programming remote jobs","python junior jobs remote","python wfh jobs","freelance python jobs remote","part time python developer jobs remote","python django remote jobs","python developer work from home jobs","entry level remote python jobs","django remote","remote junior python jobs","python remote jobs entry level","entry level python remote jobs","python junior developer jobs remote","python coding jobs remote","python part time jobs remote","fully remote python jobs","python part time remote jobs","python data analyst remote jobs","python programming jobs remote","django junior remote jobs","remote jobs for python programmers","remote python django jobs","python junior developer remote","jobs python remote","python remote developer jobs","remote python entry level jobs","remote jobs python django","python jobs remote part time","django remote jobs worldwide","junior django developer remote jobs","python junior remote","entry level python developer remote","flask jobs remote","remote job python junior","remote python web scraping jobs","work from home python developer jobs","flask remote jobs"] 

good_words = []
bad_words = []

for q in search:
    base_url = "http://duckduckgo.com/html/?q="
    query_url = base_url + q
    visit_link = urllib.parse.unquote(query_url)
    page = browser.open(visit_link)


    source_code = page.read()
    results = []
    results.extend(browser.links())
    for i in results:
        current_link = urllib.parse.unquote(i.url)
        if 'uddg=' in current_link:
            current_link = current_link.split('uddg=')[1].split('&rut=')[0]
            if validators.url(current_link):
                try:
                    print("Extract application links  " + current_link)
                    channels_found_in_website = extract_application_link(current_link)
                    print("Done")
                    for c in channels_found_in_website:
                        channel_exists = Query()
                        if len(client.search(channel_exists.channel==c)) == 0:
                            client.insert({'channel': c})
                            print("Inserted: " + c)
                except URLError:
                    print("Website " + current_link + " is not good. Continuing with others..")
    results = []

    

