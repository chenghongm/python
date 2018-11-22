from urllib.request import urlopen as uo
from bs4 import BeautifulSoup as soup

productName_list = []
DropDown_list = []
oriPrice_list = []
nowPrice_list = []
plate_list = []
ratePercent_list = []
user_list = []

containerAmount = 0

for counter in range(1, 29):
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
            p1 = s[14][0:-7].split('$')
            if len(p1) < 3:
                oriPrice_list.append(s[14][0:-7])
                nowPrice_list.append(s[14][0:-7])
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
    # -----------------------------------plate
    for m in myContainers:
        p2 = m.div.p
        # print('--------',p)
        pl = []
        for i in p2:
            if len(i) != 1:
                # print("------",i)
                # print("--------", len(i))
                plate = str(i)[26:29]
                pl.append(plate)
        # print('>>>>',pl)
        plate_list.append(pl)

        # -------------------------rating

    rateContainer = pageParse.find_all('div', {'class', 'col search_reviewscore responsive_secondrow'})
    # in order to check if I got all 25 item each page'

    if len(rateContainer) != len(myContainers):
        while len(rateContainer) != len(myContainers):
            rateContainer.append("---")

    for m in rateContainer:

        p3 = ''
        u = ''

        # print(len(m),'---------\n', m)
        if len(m) == 3:

            r = str(m).split(' ')
            # print(r)
            # print('))))',r)
            pr = r[6] + r[7] + r[8]
            p3 = pr[pr.index('%') - 2:pr.index('%') + 1]
            ratePercent_list.append(p3)
            user = r[9] + r[10] + r[11]

            for us in user:
                if us.isdigit():
                    u = u + us
            user_list.append(u)
            # print(p, "-------", u)
        else:
            p3 = '0%'
            ratePercent_list.append(p3)
            u = '0'
            user_list.append(u)

            # print(p,"-------",u )

# print(len(myContainers)) #24


# for i in range(25):
#   print(productName_list[i],date_list[i],DropDown_list[i],oriPrice_list[i],nowPrice_list[i])


# item1=myContainers[0]
# print(item1.div.p)

# ------------plate


# print(len(plate_list))


# rate1 = rateContainer[0]
# print(len(rate1))


# print(len(overall_reviewlist),len(ratePercent_list), len(user_list))
import io

with io.open('data.csv', "w", encoding="utf-8") as file:
    header = "Product_Name, PlatForm, Price_Down, Original_Price,Price, RatePercent, User_Amount\n"

    file.write(header)

    for j in range(0, containerAmount):
        file.write(str(productName_list[j]) + ',' + str(plate_list[j]).replace(',', '/') + ',' + str(
            DropDown_list[j]) + ',' + str(oriPrice_list[j]) + ',' + str(nowPrice_list[j]) + ',' + str(
            ratePercent_list[j]) + ',' + str(user_list[j]) + '\n')
        print(productName_list[j], plate_list[j], DropDown_list[j], oriPrice_list[j], nowPrice_list[j],
              ratePercent_list[j], user_list[j])
        print(j)
    file.close()

print(len(productName_list), len(plate_list), len(DropDown_list), len(oriPrice_list), len(nowPrice_list),
      len(ratePercent_list), len(user_list))
print(containerAmount)
