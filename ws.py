from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as soup

productName_list = []
date_list = []
DropDown_list = []
oriPrice_list = []
nowPrice_list = []
plate_list = []
ratePercent_list = []
user_list = []
overall_reviewlist = []
containerAmount = 0

for counter in range(22, 23):
    my_url = 'https://store.steampowered.com/search/?specials=1&page=' + str(counter)
    print(counter)
    uPage = uo(my_url)
    my_html = uPage.read()
    uPage.close()
    pageParse = soup(my_html, 'html.parser')
    myContainers = pageParse.find_all("div", {'class', 'responsive_search_name_combined'})
    containerAmount += len(myContainers)
    # print(containerAmount)
    # ---------------------------------brandName, price,review
    for m in myContainers:
        s = m.text.split('\n')
        if len(s) < 19:
            DropDown_list.append(s[11])
            p1 = s[len(s)-2][0:-7].split('$')
            if len(p1) < 3:
                oriPrice_list.append(s[len(s)-2][0:-7])
                nowPrice_list.append(s[len(s)-2][0:-7])
            else:
                op = p1[1]
                np = p1[2]
                oriPrice_list.append('$' + op)
                nowPrice_list.append('$' + np)
        else:
            p1 = s[16][0:-7].split('$')
            if len(p1) < 3:
                oriPrice_list.append(s[16][0:-7])
                nowPrice_list.append(s[16][0:-7])
            else:
                op = p1[1]
                np = p1[2]
                oriPrice_list.append('$' + op)
                nowPrice_list.append('$' + np)
            # print(p)
            # object = s[2] + ',' + s[6] + ',' + s[13] + ',' + s[16][0:-7]

        print(s[2])
        productName_list.append(s[2])

        DropDown_list.append(s[13])