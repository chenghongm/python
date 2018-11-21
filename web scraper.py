import bs4
from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as soup

# my target
counter = 1
#for counter in range(1, 36):
my_url = 'https://store.steampowered.com/search/?specials=1&page=22' #+ str(counter)
    #print(my_url)
#my_url = 'https://store.steampowered.com/'

#open this URL, read it, and close
uPage = uo(my_url)
my_html = uPage.read()
uPage.close()

#parsing this page with the tool of beautifulSoup
pageParse = soup(my_html, 'html.parser')
#get header
#print(pageParse.h2)
#print(pageParse.p)
#from the feature of Inspect,
# I found all item info all under the tag of 'div' with class of'responsive_search_name_combined'


myContainers = pageParse.find_all("div", {'class','responsive_search_name_combined'})
#in order to check if I got all 25 item each page
print(len(myContainers)) #24
mylist =[]
for i in myContainers:
    s = i.text.split('\n')
    #print(len(s),"***********",s,'------------------',s[14])

    if len(s) < 19:

        object = s[2] + ',' + s[6] + ',' + s[11] + ',' + s[len(s)-2][0:-7]


    else:
        object = s[2] + ',' + s[6] + ',' + s[13] + ',' + s[16][0:-7]

    #print(s)
    #print(len(s))
    '''
    if len(s)<19:
        while len(s) !=19:
           s.append('-')
    '''
    #print(len(s))
    #get prices
    p = s[15].split('$')
    #print(p)
    #while len(p) !=3:
     #   p.append('-')
    #print(len(p))
    #print(p)


   # mylist.append(object)
    print(object,"----------", len(s))

'''
# to analysis each item info
item1 = myContainers[1]
# to see the content between all tags

#--------------------------brand, price
content = item1.text

#print(content) #we can many space here

for i in content:
    if len(str(i))>1 and len(i)==1:
        print("--------", str(i)[38: -16])
    if len(i)>1:
        print("----------", str(i)[0: 6])

s = content.split('\n')# we try space ' ', and '\t',and '\n'
print(s)

mylist = []
for i in s:
    if i !='':
        mylist.append(i)

print(mylist)
#print(len(mylist))
#-----------------------------platform
# to get the platform info, it is a class name, can't not be scrap from text
plate = item1.div.p
#
print(len(plate))
for i in plate:
    if len(i) !=1:
    #print("------",i)
    #print("--------", len(i))
       print(str(i)[26:29])




-------------------------------------rating

rateContainer = pageParse.find_all('div', {'class','col search_reviewscore responsive_secondrow'})
rate1 = rateContainer[0]
print(len(rate1))
print('66666666666666',len(rateContainer))
counter = 0
if len(rateContainer) < 25:
    while len(rateContainer) != 25:
        rateContainer.append("---")
print("+++++++++",len(rateContainer))
counter =0

for m in rateContainer:

    p=''
    u=''

   # print(len(m),'---------\n', m)
    if len(m) == 3:
        counter +=1
        r = str(m).split(' ')
        #print(r)
        # print('))))',r)
        pr = r[6]+r[7]+r[8]
        p = pr[pr.index('%') - 2:pr.index('%') + 1]
        user = r[9]+r[10] + r[11]

        for us in user:
            if us.isdigit():
                u = u + us
        #print(p, "-------", u)
    else:
        counter += 1
        p='0%'
        u='0'
    print(p, "-------", u)
            #print("----",len(str(i).split(' ')))




            #print('---', r[2], r[3][:-3],r[6])
            #print( "---------",len(r))
print("has data ",counter)
#file = open('steam video games analysis.csv')

header = ('Product_Name', 'PlatForm' 'Price_Down', 'Original_Price','Price', 'Overall_Review', 'RatePercent', 'User_Amount')
'''