# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.9.7 (default, Oct  6 2021, 01:34:26) 
# [GCC 11.1.0]
# Embedded file name: /home/mmnoa/p/p/.buildozer/android/app/main.py
# Compiled at: 2021-11-30 04:32:17
# Size of source mod 2**32: 33031 bytes
from kivy.config import Config
Config.set('kivy', 'log_dir', '/sdcard/.Pravum/')
import re, bs4, glob, requests, os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.utils import platform
from kivymd.theming import ThemeManager
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.config import Config
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import plyer, webbrowser, threading, time, random, datetime
updateBomb = '2021-09-04'
updateBomb = updateBomb.split('-')
date = str(str(datetime.datetime.now()).split()[0]).split('-')
addSymbol = '+'
remSymbol = '-'
wipSymbol = '--'
resSymbol = '++'
delayTime = 0.2
outputText = ''
platformName = ''
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    from android.storage import primary_external_storage_path
    primary_ext_storage = primary_external_storage_path()
    Config.set('kivy', 'log_dir', primary_ext_storage + '/.Pravum/')
    androidFilePath = primary_ext_storage + '/.Pravum/'
    platformName = 'android'
    from android.storage import secondary_external_storage_path
    secondary_ext_storage = secondary_external_storage_path()
else:
    androidFilePath = ''
    androidDownloadPath = ''
    platformName = 'windows'
try:
    os.mkdir(androidFilePath)
except:
    pass
else:
    import webDownloader
    orderSauce = 'orderSauce.txt'
    preferences = 'preferences.txt'
    preferencesBak = 'preferencesBak.txt'
    tmpFileDef = 'tmp.txt'
    saucesFileDef = 'sauces.txt'
    outputFileDef = 'output.txt'
    GeneralSettings = 'generalsettings.txt'
    favorites = 'favorites.txt'
    adminFile = '9lmxaoB2X3PGPeNdgcK1qGTYGs7i.txt'
    adminFile = androidFilePath + adminFile
    orderSauce = androidFilePath + orderSauce
    preferences = androidFilePath + preferences
    preferencesBak = androidFilePath + preferencesBak
    tmpFileDef = androidFilePath + tmpFileDef
    saucesFileDef = androidFilePath + saucesFileDef
    outputFileDef = androidFilePath + outputFileDef
    GeneralSettings = androidFilePath + GeneralSettings
    favorites = androidFilePath + favorites
    kvFileName = 'box.kv'
    orderSauceSeperator = '|'
    fileCheckList = [
     preferences, preferencesBak, tmpFileDef, saucesFileDef, outputFileDef, GeneralSettings, orderSauce, favorites]
for file in fileCheckList:
    try:
        file = open(file, 'r')
        file.close()
    except:
        file = open(file, 'w')
        file.close()

else:
    try:
        open(adminFile, 'r')
        isAdmin = True
    except:
        isAdmin = False
    else:
        if isAdmin == False:
            keySearchDefaults = [
             'random:', 'getpages:', 'tagsearch=tag: language:english range:', 'tagsearchrandompages=tag: language:english range:', '']
        else:
            keySearchDefaults = [
             'random:', 'getpages:', 'tagsearch=tag: language:english range:', 'tagsearchrandompages=tag: language:english range:', 'YTMP3@', '']
        import preferenceManager as pm
        userTagFormattingSeperatorInput = ','
        savedFileFormattingSeperator = '?'
        savedFileFormattingScoreSeperator = '/'
        reModuleTagSeperator01 = '([' + savedFileFormattingSeperator + '])'
        reModuleTagSeperator02 = '([^' + savedFileFormattingSeperator + ']*' + chr(92) + savedFileFormattingSeperator + ')'
        preferenceScreenTagSeperator = ', '
        tagScoreSeperator = ': '
        httpsSeperators = [
         '(', ')', 'https://', 'http://', 'nhentai', '.net', '/g/', '-', '~']

        class FileSelectorInternalWindow(Screen):
            defaultpath01 = open(GeneralSettings, 'r')
            defaultpath = str(defaultpath01.read())
            if not os.path.exists(defaultpath):
                if platformName == 'android':
                    defaultpath = primary_ext_storage + '/'
                elif platformName == 'windows':
                    defaultpath = ''
            else:
                defaultpath = defaultpath
            defaultpath01.close()

            def selected(self, filename):
                try:
                    dataStoreDownload = open(GeneralSettings, 'w')
                    if platformName == 'windows':
                        tmpSymbol = chr(92) + chr(92)
                    else:
                        if platformName == 'android':
                            tmpSymbol = '/'
                    filename = ''.join(filename[0])
                    filename = filename.replace(chr(92), tmpSymbol)
                    filename = filename + tmpSymbol
                    dataStoreDownload.write(str(filename))
                    dataStoreDownload.close()
                except:
                    pass


        class FileSelectorExternalWindow(Screen):
            defaultpath01 = open(GeneralSettings, 'r')
            defaultpath = str(defaultpath01.read())
            if not os.path.exists(defaultpath):
                if platformName == 'android':
                    defaultpath = '/sdcard/'
                elif platformName == 'windows':
                    defaultpath = ''
            else:
                defaultpath = str(plyer.storagepath.get_sdcard_dir()) + '/'
            defaultpath01.close()

            def selected(self, filename):
                try:
                    dataStoreDownload = open(GeneralSettings, 'w')
                    if platformName == 'windows':
                        tmpSymbol = chr(92) + chr(92)
                    else:
                        if platformName == 'android':
                            tmpSymbol = '/'
                    filename = ''.join(filename[0])
                    filename = filename.replace(chr(92), tmpSymbol)
                    filename = filename + tmpSymbol
                    dataStoreDownload.write(str(filename))
                    dataStoreDownload.close()
                except:
                    pass


        class InAppView(Screen):
            page = 0
            link = StringProperty()
            links_ = []
            links__ = []

            def preload(sauce):
                links = webDownloader.websiteIncrement(str(sauce), 'False')
                InAppView.links_ = links
                for i in links[0:4]:
                    AsyncImage(source=i)
                else:
                    InAppView.source = links[0]

            def next(self):
                if self.page + 1 <= len(self.links_):
                    self.page += 1
                    self.link = self.links_[(self.page - 1)]
                    try:
                        AsyncImage(source=(self.links_[(self.page + 3)]))
                    except:
                        pass

            def previous(self):
                if self.page != 1:
                    if self.page != 0:
                        self.page -= 1
                        self.link = self.links_[(self.page - 1)]

            def exit(self):
                self.page = 0


        class Favorites(Screen):
            favoritesText = ObjectProperty(None)
            f = open(favorites, 'r')
            tmpList = []
            for i in f:
                i = i.replace('\n', '')
                tmpList.append(i)
            else:
                favoritesText = tmpList

                def renderFavorites(self):
                    f = open(favorites, 'r')
                    tmpList = []
                    for i in f:
                        i = i.replace('\n', '')
                        btn = Button(Text=(str(i)))

                def remove(self, sauce, placeHolder):
                    try:
                        f = open(favorites, 'r')
                        tmpList = []
                        for i in f:
                            i = i.replace('\n', '')
                            tmpList.append(i)
                        else:
                            f.close()
                            tmpList.remove(sauce)
                            f = open(favorites, 'w')
                            f.close()
                            f = open(favorites, 'a')
                            for i in tmpList:
                                f.write(i + '\n')
                            else:
                                f.close()
                                plyer.notification.notify(title='Restart App', message='Please restart app to update this page', toast=True)

                    except:
                        plyer.notification.notify(title='Already Deleted', message='This item has already been removed', toast=True)

                def runFavorite(self, sauce, placeHolder):
                    if sauce.split('@')[0] == 'external_link':
                        webbrowser.open_new_tab(str(sauce.split('@')[1]))
                    else:
                        webbrowser.open_new_tab(f"https://nhentai.net/g/{sauce}")


        class PreferencesWindow(Screen):
            settings_text = StringProperty()
            settings_file = open(preferences, 'r')
            settings_score = StringProperty()
            settings_count = StringProperty()
            settings_count01 = StringProperty()
            tagAddRemove = ObjectProperty(None)
            tagAddRemoveScore = ObjectProperty(None)

            def toast_message(self):
                plyer.notification.notify(title='Pravum External File Download', message='Comming Soon!', toast=True)

            def backup_run(self):
                open(preferencesBak, 'w').close()
                settingsBakFile = open(preferencesBak, 'w')
                settingsFileCopy = open(preferences, 'r')
                for i in settingsFileCopy:
                    settingsBakFile.write(i)
                else:
                    settingsBakFile.close()

            def settings(self):
                tmpY = False
                tag_list = []
                settingsWrite = []
                settingsWrite1 = self.ids.tagAddRemove.text
                settingsWriteScore = self.ids.tagAddRemoveScore.text
                settingsWrite.append(settingsWrite1)
                if len(settingsWrite1) == 0 and len(settingsWriteScore) == 0:
                    pass
                elif len(settingsWriteScore) == 0:
                    settingsWrite = ''.join(settingsWrite)
                    tmpY = True
                if len(settingsWriteScore) != 0:
                    self.backup_run()
                    settingsWrite.append(savedFileFormattingScoreSeperator + settingsWriteScore + '\n')
                    settingsWrite[0] = settingsWrite[0].replace(userTagFormattingSeperatorInput, savedFileFormattingSeperator)
                    settingsFile = open(preferences, 'a')
                    settingsFile.write(''.join(settingsWrite))
                else:
                    if not settingsWrite[0] == remSymbol:
                        if not tmpY == True or settingsWrite.replace('.', '').isdigit() == True:
                            tmpList = []
                            self.backup_run()
                            count = 0
                            settingsFile = open(preferences, 'r')
                            tmpFile = open(tmpFileDef, 'w')
                            for i in settingsFile:
                                tmpFile.write(i)
                                count += 1
                            else:
                                settingsFile.close()
                                tmpFile.close()

                            if int(settingsWrite.replace('.', '')) <= count:
                                settingsFile = open(preferences, 'w')
                                tmpFile = open(tmpFileDef, 'r')
                                for line in tmpFile:
                                    line = re.split(reModuleTagSeperator02, line)
                                    tmpList.append(line)
                                else:
                                    tmpList = sorted(tmpList, key=len, reverse=True)
                                    if tmpY == True:
                                        if settingsWrite.replace('.', '').isdigit() == True:
                                            tmpList.remove(tmpList[(int(str(settingsWrite).replace('.', '')) - 1)])
                                            tmpFile = open(tmpFileDef, 'w')
                                            tmpString = ''
                                            for i in tmpList:
                                                tmpString = tmpString + ''.join(i)
                                            else:
                                                tmpList = tmpString
                                                tmpFile.write(tmpList)
                                                tmpFile.close()
                                                tmpFile = open(tmpFileDef, 'r')

                                        for line in tmpFile:
                                            lineBreak = line.split(savedFileFormattingScoreSeperator)
                                            if lineBreak[0] != settingsWrite[1]:
                                                settingsFile.write(line)
                                            settingsFile.close()
                                            tmpFile.close()

                                    else:
                                        pass

                                if settingsWrite == wipSymbol:
                                    self.backup_run()
                                    open(preferences, 'w').close()
                    elif settingsWrite == resSymbol:
                        resFile = open(preferencesBak, 'r')
                        file = open(preferences, 'r+')
                        tmpText = ''
                        for i in file:
                            tmpText = tmpText + i
                        else:
                            open(preferences, 'w').close()
                            for i in resFile:
                                file.write(i)
                            else:
                                file.close()
                                resFile.close()
                                open(preferencesBak, 'w').close()
                                resFile = open(preferencesBak, 'w')
                                for i in tmpText:
                                    resFile.write(i)

            def settingUpdate(self):
                f = open(preferences, 'r')
                tmpList = []
                score = ''
                for line in f:
                    line = re.split(reModuleTagSeperator01, line)
                    tmpList.append(line)
                else:
                    tmpList = sorted(tmpList, key=len, reverse=True)
                    contents = ''
                    count = 0
                    count_string = ''
                    for i in tmpList:
                        for t in i:
                            t = t.strip(savedFileFormattingScoreSeperator)
                            if t.isdigit() == False:
                                t = t + ' '
                        else:
                            for i in tmpList:
                                count += 1
                                count_string = count_string + (str(count) + '.\n')
                                tmpText = ''.join(i)
                                tmpText = tmpText.split(savedFileFormattingScoreSeperator)
                                score = score + str(tmpText[(-1)])
                                tmpText.remove(tmpText[(-1)])
                                contents = contents + ''.join(tmpText)
                                contents = contents + '\n'
                            else:
                                contents = contents.replace(savedFileFormattingSeperator, preferenceScreenTagSeperator)
                                self.ids.settings_text.text = contents
                                self.ids.settings_score.text = score
                                self.ids.settings_count.text = count_string
                                self.ids.settings_count01.text = count_string
                                plyer.notification.notify(title='Pravum Preference Edit', message='Please restart app to apply changes', toast=True)


        class WindowManager(ScreenManager):
            pass


        class MyGridWindow(Screen):
            sauces = ObjectProperty(None)
            text = StringProperty()
            if not updateBomb == date:
                if not int(date[0]) > int(updateBomb[0]):
                    if not int(date[1]) > int(updateBomb[1]):
                        if int(date[2]) > int(updateBomb[2]):
                            pass

            def tagSearchRandomPages(self, tagset):
                tagset = tagset.split('\n')
                tagset[-1] = tagset[(-1)].replace('range:', '')
                tmp = 0
                for i in tagset:
                    tagset[tmp] = i.replace(':', '%3A')
                    tmp += 1
                else:
                    if len(tagset) == 1:
                        res = 'https://nhentai.net/search/?q=' + tagset[0]
                    else:
                        res = 'https://nhentai.net/search/?q=' + tagset[0]
                        for i in tagset[1:-1]:
                            res = res + '+' + i
                        else:
                            res = res + '&sort=popular'
                            res = res + '&page='

                    lastPage = self.randomSauce(1, res)
                    for i in range(int(tagset[(-1)])):
                        ranPage = random.randint(1, lastPage)
                        self.pageSearch(ranPage, res)

            def randomSauce(self, num, link):
                res = requests.get(link + '1')
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                soup = str(soup.find_all(class_='last'))
                soup = soup.split('href="')
                soup = soup[1].split('page=')
                tmplist = []
                for i in soup:
                    i = i.replace('/', '')
                    i = i.replace('g', '')
                    i = i.split('"')
                    if i[0].isdigit() == True:
                        tmplist.append(i[0])
                    tmplist = int(tmplist[0])
                    if link != 'https://nhentai.net/?page=':
                        return tmplist

                for i in range(int(num)):
                    ranPage = random.randint(1, tmplist)
                    self.pageSearch(ranPage, link)
                else:
                    f = open(tmpFileDef, 'r')
                    tmplist = []
                    for i in f:
                        tmplist.append(i)
                    else:
                        f.close()
                        f = open(tmpFileDef, 'w')
                        f.close()
                        f = open(tmpFileDef, 'a')
                        for i in range(int(num)):
                            ranEntry = random.randint(0, len(tmplist) - 2)
                            f.write(tmplist[ranEntry])
                        else:
                            f.close()

            def pageSearch(self, num, link):
                res = requests.get(link + str(num))
                soup = bs4.BeautifulSoup(res.text, 'html.parser')
                soup = str(soup.find_all(class_='cover'))
                soup = soup.split('href="')
                tmplist = []
                for i in soup:
                    i = i.replace('/', '')
                    i = i.replace('g', '')
                    i = i.split('"')
                    if i[0].isdigit() == True:
                        tmplist.append(i[0])
                else:
                    f = open(tmpFileDef, 'a')

                for i in tmplist:
                    f.write(i + '\n')
                else:
                    f.close()

            def tagSearch(self, tagset):
                tagset = tagset.split('\n')
                if re.search('range:.*', tagset[(-1)]):
                    tagset[-1] = tagset[(-1)].replace('range:', '')
                    tmpinp = tagset[(-1)].split('-')
                    if len(tmpinp) == 1:
                        tmppageset = '&page=' + tmpinp[0]
                        tmp = 0
                        for i in tagset:
                            tagset[tmp] = i.replace(':', '%3A')
                            tmp += 1
                        else:
                            if len(tagset) == 1:
                                res = 'https://nhentai.net/search/?q=' + tagset[0]
                            else:
                                res = 'https://nhentai.net/search/?q=' + tagset[0]
                                for i in tagset[1:-1]:
                                    res = res + '+' + i
                                else:
                                    res = res + '&sort=popular'
                                    res = res + tmppageset

                            res = requests.get(res)
                            soup = bs4.BeautifulSoup(res.text, 'html.parser')
                            soup = str(soup.find_all(class_='cover'))
                            soup = soup.split('href="')
                            tmplist = []
                            for i in soup:
                                i = i.replace('/', '')
                                i = i.replace('g', '')
                                i = i.split('"')
                                if i[0].isdigit() == True:
                                    tmplist.append(i[0])
                            else:
                                f = open(tmpFileDef, 'a')
                                for i in tmplist:
                                    f.write(i + '\n')
                                else:
                                    f.close()

                    else:
                        pagesetrange = int(tmpinp[1]) - int(tmpinp[0])
                        for t in range(pagesetrange + 1):
                            t += int(tmpinp[0])
                            tmp = 0
                            for i in tagset:
                                tagset[tmp] = i.replace(':', '%3A')
                                tmp += 1

                        else:
                            if len(tagset) == 1:
                                res = 'https://nhentai.net/search/?q=' + tagset[0]
                            else:
                                res = 'https://nhentai.net/search/?q=' + tagset[0]
                                for i in tagset[1:-1]:
                                    res = res + '+' + i
                                else:
                                    res = res + '&sort=popular'
                                    res = res + '&page=' + str(t)

                            res = requests.get(res)
                            soup = bs4.BeautifulSoup(res.text, 'html.parser')
                            soup = str(soup.find_all(class_='cover'))
                            soup = soup.split('href="')
                            tmplist = []
                            for i in soup:
                                i = i.replace('/', '')
                                i = i.replace('g', '')
                                i = i.split('"')
                                if i[0].isdigit() == True:
                                    tmplist.append(i[0])
                                f = open(tmpFileDef, 'a')
                                for i in tmplist:
                                    f.write(i + '\n')
                                else:
                                    f.close()

            def run_pressed(self):
                pagesDict = []
                sauceWrite = self.sauces.text
                sauceWrite = sauceWrite.replace(' ', '\n')
                if sauceWrite != '':
                    try:
                        if platformName != 'windows':
                            plyer.notification.notify(title='Score Sauce Set', message='Running...', toast=True)
                        if sauceWrite.split(':')[0] == 'getpages' and len(sauceWrite.split(':')) == 2:
                            sauceWrite = sauceWrite.split(':')
                            open(tmpFileDef, 'w').close()
                            if len(sauceWrite[1].split('-')) == 1:
                                self.pageSearch(sauceWrite[1], 'https://nhentai.net/?page=')
                            else:
                                sauceWrite = sauceWrite[1].split('-')
                                threads = []
                                i = int(sauceWrite[0]) - 1
                                for i in range(int(sauceWrite[1])):
                                    i += 1
                                    t = threading.Thread(target=(self.pageSearch), args=[str(i), 'https://nhentai.net/?page='])
                                    t.start()
                                    threads.append(t)
                                    time.sleep(delayTime)
                                else:
                                    for thread in threads:
                                        thread.join()
                                    else:
                                        f = open(tmpFileDef, 'r')
                                        sauceWrite = []
                                        for i in f:
                                            i = i.replace('\n', '')
                                            sauceWrite.append(i)
                                        else:
                                            outputObjects = pm.filtrationManager(sauceWrite)

                        else:
                            if sauceWrite.split(':')[0] == 'random' and len(sauceWrite.split(':')) == 2:
                                sauceWrite = sauceWrite.split(':')
                                self.randomSauce(sauceWrite[1], 'https://nhentai.net/?page=')
                                f = open(tmpFileDef, 'r')
                                sauceWrite = []
                                for i in f:
                                    i = i.replace('\n', '')
                                    sauceWrite.append(i)
                                else:
                                    outputObjects = pm.filtrationManager(sauceWrite)

                            else:
                                if sauceWrite.split('=')[0] == 'tagsearch' and len(sauceWrite.split('=')) == 2:
                                    f = open(tmpFileDef, 'w')
                                    f.close()
                                    sauceWrite = sauceWrite.split('=')
                                    self.tagSearch(sauceWrite[1])
                                    f = open(tmpFileDef, 'r')
                                    sauceWrite = []
                                    for i in f:
                                        i = i.replace('\n', '')
                                        sauceWrite.append(i)
                                    else:
                                        outputObjects = pm.filtrationManager(sauceWrite)

                                else:
                                    if sauceWrite.split('=')[0] == 'tagsearchrandompages' and len(sauceWrite.split('=')) == 2:
                                        f = open(tmpFileDef, 'w')
                                        f.close()
                                        sauceWrite = sauceWrite.split('=')
                                        self.tagSearchRandomPages(sauceWrite[1])
                                        f = open(tmpFileDef, 'r')
                                        sauceWrite = []
                                        for i in f:
                                            i = i.replace('\n', '')
                                            sauceWrite.append(i)
                                        else:
                                            outputObjects = pm.filtrationManager(sauceWrite)

                                    else:
                                        for i in httpsSeperators:
                                            sauceWrite = sauceWrite.replace(i, '')
                                        else:
                                            sauceFile = open(saucesFileDef, 'w')
                                            sauceFile.write(sauceWrite)
                                            sauceFile.close()
                                            sauceWrite = sauceWrite.split('\n')
                                            outputObjects = pm.filtrationManager(sauceWrite)

                        NameString = ''
                        PageString = ''
                        for i in outputObjects:
                            NameString += str(i[0]) + tagScoreSeperator + str(i[1]) + '\n'
                            PageString += str(i[(-1)]) + '\n'
                        else:
                            self.ids.display_text.text = NameString
                            self.ids.pages.text = PageString

                    except:
                        pass

            def downloadDojin(self):
                tmpNum = 0
                saucesWrite = self.sauces.text
                saucesWriteNotif = saucesWrite.replace('\n', ' ')
                for i in httpsSeperators:
                    saucesWriteNotif = saucesWriteNotif.replace(i, '')
                else:
                    if saucesWrite != '':
                        plyer.notification.notify(title='Download', message='Downloading...', toast=True)
                        saucesWrite = re.split('[\\n ]', saucesWrite)
                        for numberSauce in saucesWrite:
                            saucesWrite01 = ''.join(numberSauce)
                            for i in httpsSeperators:
                                numberSauce = numberSauce.replace(i, '')
                            else:
                                webDownloader.websiteIncrement(str(numberSauce), 'True')
                                tmpNum += 1

                        else:
                            plyer.notification.notify(title='Pravum Download', message=f"Your download of {saucesWriteNotif} is done!")

            def openInBrowser(self):
                saucesWrite = self.sauces.text
                if saucesWrite != '':
                    saucesWrite = re.split('[\\n ]', saucesWrite)
                    for numberSauce in saucesWrite:
                        for i in httpsSeperators:
                            numberSauce = numberSauce.replace(i, '')
                        else:
                            webbrowser.open_new_tab(f"https://nhentai.net/g/{numberSauce}")

                else:
                    webbrowser.open_new_tab('https://nhentai.net/')

            def inappviewpreload(self):
                saucesWrite = self.sauces.text
                if saucesWrite != '':
                    saucesWrite = re.split('[\\n ]', saucesWrite)
                    if len(saucesWrite) == 1:
                        for numberSauce in saucesWrite:
                            for i in httpsSeperators:
                                numberSauce = numberSauce.replace(i, '')
                            else:
                                InAppView.preload(numberSauce)

                    else:
                        plyer.notification.notify(title='InAppView', message='Please Enter Only 1 Sauce', toast=True)

            def nextSauce(self):
                f = open(orderSauce, 'r')
                saucesWrite = self.sauces.text
                tmplist = []
                for i in f:
                    i = i.split(orderSauceSeperator)
                    i[-1] = i[(-1)].replace('\n', '')
                    tmplist.append(i)
                else:
                    tmpcount = 0
                    nextcount = tmpcount - 1
                    for i in tmplist:
                        if i[0] == saucesWrite:
                            nextcount = tmpcount + 1
                        tmpcount += 1
                    else:
                        if nextcount == -1 or nextcount > len(tmplist) - 1:
                            nextcount = 0
                        if len(tmplist) != 0:
                            self.ids.sauces.text = str(tmplist[nextcount][0])
                            plyer.notification.notify(title='Next Sauce', message=('Score: ' + str(tmplist[nextcount][1]) + ' Pages: ' + str(tmplist[nextcount][(-1)])), toast=True)

            def prevSauce(self):
                f = open(orderSauce, 'r')
                saucesWrite = self.sauces.text
                tmplist = []
                for i in f:
                    i = i.split(orderSauceSeperator)
                    i[-1] = i[(-1)].replace('\n', '')
                    tmplist.append(i)
                else:
                    tmpcount = 0
                    nextcount = tmpcount - 1
                    for i in tmplist:
                        if i[0] == saucesWrite:
                            nextcount = tmpcount - 1
                        tmpcount += 1
                    else:
                        if nextcount == -1:
                            nextcount = len(tmplist) - 1
                        if len(tmplist) != 0:
                            self.ids.sauces.text = str(tmplist[nextcount][0])
                            plyer.notification.notify(title='Previous Sauce', message=('Score: ' + str(tmplist[nextcount][1]) + ' Pages: ' + str(tmplist[nextcount][(-1)])), toast=True)

            def keyChange(self):
                saucesWrite = self.sauces.text
                tmpcount = 0
                nextcount = tmpcount - 1
                for i in keySearchDefaults:
                    if i == saucesWrite:
                        nextcount = tmpcount + 1
                    tmpcount += 1
                else:
                    if nextcount == -1 or nextcount > len(keySearchDefaults) - 1:
                        nextcount = 0
                    if len(keySearchDefaults) != 0:
                        self.ids.sauces.text = str(keySearchDefaults[nextcount])

            def addToFavorites(self):
                sauceWrite = self.sauces.text
                sauceWrite = sauceWrite.replace(' ', '\n')
                for i in httpsSeperators:
                    sauceWrite = sauceWrite.replace(i, '')
                else:
                    f = open(favorites, 'r')
                    tmpList = []
                    for i in f:
                        i = i.replace('\n', '')
                        tmpList.append(i)
                    else:
                        f.close()
                        f = open(favorites, 'a')
                        sauceWrite = sauceWrite.split('\n')
                        for i in sauceWrite:
                            if i in tmpList:
                                pass
                            else:
                                f.write(i + '\n')
                        else:
                            f.close()
                            plyer.notification.notify(title='Add To Favorites', message='Added To Favorites', toast=True)


        class HelpWindow(Screen):
            pass


        f = open(preferences, 'r')
        tmpList = []
        score = ''
        for line in f:
            line = re.split(reModuleTagSeperator01, line)
            tmpList.append(line)
        else:
            tmpList = sorted(tmpList, key=len, reverse=True)
            contents = ''
            count = 0
            count_string = ''
            for i in tmpList:
                for t in i:
                    t = t.strip(savedFileFormattingScoreSeperator)
                    if t.isdigit() == False:
                        t = t + ' '
                else:
                    for i in tmpList:
                        count += 1
                        count_string = count_string + (str(count) + '.\n')
                        tmpText = ''.join(i)
                        tmpText = tmpText.split(savedFileFormattingScoreSeperator)
                        score = score + str(tmpText[(-1)])
                        tmpText.remove(tmpText[(-1)])
                        contents = contents + ''.join(tmpText)
                        contents = contents + '\n'
                    else:
                        contents = contents.replace(savedFileFormattingSeperator, preferenceScreenTagSeperator)
                        PreferencesWindow.settings_text = contents
                        PreferencesWindow.settings_score = score
                        PreferencesWindow.settings_count = count_string
                        PreferencesWindow.settings_count01 = count_string

                        class HomeApp(MDApp):

                            def build(self):
                                self.theme_cls.theme_style = 'Dark'
                                kv = Builder.load_file(kvFileName)
                                return kv


                        if __name__ == '__main__':
                            HomeApp().run()