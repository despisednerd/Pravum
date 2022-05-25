# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.9.7 (default, Oct  6 2021, 01:34:26) 
# [GCC 11.1.0]
# Embedded file name: /home/mmnoa/p/p/.buildozer/android/app/preferenceManager.py
# Compiled at: 2021-11-30 04:32:17
# Size of source mod 2**32: 3213 bytes
import re, requests, time, bs4, glob, threading
from kivy.clock import Clock
from kivy.utils import platform
delayTime = 0.4
if platform == 'android':
    androidFilePath = '/sdcard/.Pravum/'
else:
    androidFilePath = ''
favorites = 'favorites.txt'
orderSauce = 'orderSauce.txt'
preferences = 'preferences.txt'
preferencesBak = 'preferencesBak.txt'
tmpFileDef = 'tmp.txt'
saucesFileDef = 'sauces.txt'
outputFileDef = 'output.txt'
orderSauce = androidFilePath + orderSauce
preferences = androidFilePath + preferences
preferencesBak = androidFilePath + preferencesBak
tmpFileDef = androidFilePath + tmpFileDef
saucesFileDef = androidFilePath + saucesFileDef
outputFileDef = androidFilePath + outputFileDef
favorites = androidFilePath + favorites
orderSauceSeperator = '|'
ENDLIST = []
preferences = open(androidFilePath + 'preferences.txt', 'r')
PreferenceList = []
for line in preferences:
    line = line.strip('\n')
    line = re.split('[?/]', line)
    PreferenceList.append(line)
else:
    PreferenceList = sorted(PreferenceList, key=len, reverse=True)

    def filtration(num):
        global ENDLIST
        score = 0
        sorted_ = []
        tmpList = []
        endList = []
        tagIdentifier = 'name'
        dateClass = 'nobold'
        baseWebsite = 'https://nhentai.net/g/' + str(num)
        sauceWebCode = requests.get(baseWebsite)
        sauceHTML = bs4.BeautifulSoup(sauceWebCode.text, 'html.parser')
        tagName = sauceHTML.find_all(class_=tagIdentifier)
        for i in tagName:
            tmpList.append(i.get_text())
        else:
            for line in PreferenceList:
                in_list = all((item in tmpList[:-1] for item in line[:-1]))
                been_sorted = all((item in sorted_ for item in line[:-1]))

        if in_list == True:
            if not been_sorted == False:
                if in_list == True:
                    if len(sorted_) == 0:
                        for i in line[:-1]:
                            sorted_.append(i)
                        else:
                            score += int(line[(-1)])

                    if score != 0:
                        endList.append(num)
                        endList.append(score / len(sorted_))
                        for i in tmpList:
                            endList.append(i)

        else:
            endList.append(num)
            endList.append(score)
            for i in tmpList:
                endList.append(i)
            else:
                ENDLIST.append(endList)


    def filtrationManager(numbers):
        global ENDLIST
        ENDLIST = []
        threads = []
        tmpList = []
        for i in numbers:
            if len(tmpList) == 0:
                tmpList.append(i)
            elif i in tmpList:
                pass
            else:
                tmpList.append(i)
        else:
            numbers = tmpList
            for i in numbers:
                t = threading.Thread(target=filtration, args=[i])
                t.start()
                threads.append(t)
                time.sleep(delayTime)
            else:
                for thread in threads:
                    thread.join()
                else:
                    ENDLIST = sorted(ENDLIST, key=(lambda x: x[1]), reverse=True)
                    f = open(orderSauce, 'w')
                    f.close()
                    f = open(orderSauce, 'a')
                    for i in ENDLIST:
                        tmpString = ''
                        for k in i[:-1]:
                            tmpString = tmpString + str(k) + orderSauceSeperator
                        else:
                            tmpString = tmpString + i[(-1)]
                            f.write(tmpString + '\n')

                    else:
                        f.close()
                        return ENDLIST