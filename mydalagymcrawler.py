import requests
import lxml.html
import csv
from lxml import etree
from lxml import html



with open('test.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    url = []
    for x in range(1,34):

            a = "http://www.mydala.com/delhi/gym-k?sort=latest&filter=sort&page="+str(x)
            url.append(a)
            print a

            response = requests.get(a)
            html = response.content
            item = etree.HTML(html)
            name = item.xpath('//*[@class="fltLeft bottom-spacing-10 clearLeft clearfix"]/a/@href')
            print name

            for x in name:
                url.append(x)
                # print '\n'
                print x
                response = requests.get(x)
                html = response.content
                item = etree.HTML(html)
                name = item.xpath('//*[@class="merchant-name"]/h1/text()')
                contact = item.xpath('//*[@class="text-13 font-bold margin-bottom-spacing-5"]/span/text()')

                if not contact : 
                    for x in range(0,len(name)):
                        row = [(name[x].strip()).encode('ascii','ignore')]+["Not available"]
                        
                            
                else:
                    for x in range(0,len(name)):
                        row = [(name[x].strip()).encode('ascii','ignore')]+[(contact[x].strip()).encode('ascii','ignore')]

                print row
                spamwriter.writerow(row)