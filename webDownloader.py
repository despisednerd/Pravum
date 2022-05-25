# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.9.7 (default, Oct  6 2021, 01:34:26) 
# [GCC 11.1.0]
# Embedded file name: /home/mmnoa/p/p/.buildozer/android/app/webDownloader.py
# Compiled at: 2021-11-30 04:32:17
# Size of source mod 2**32: 6638 bytes
import requests, random, bs4, os, re, time, validators, urllib3, urllib.request, shutil, threading, plyer
from pathlib import Path
from kivy.utils import platform
urllib3.disable_warnings()
average_img_time = 2.5
androidAllowedLength = 127
delayTime = 0.0
downloadSections = 15
infoFileName = '/_info.txt'
if platform == 'android':
    from android.storage import primary_external_storage_path
    primary_ext_storage = primary_external_storage_path()
    androidFilePath = primary_ext_storage + '/.Pravum/'
else:
    androidFilePath = ''
GeneralSettings = 'generalsettings.txt'
GeneralSettings = androidFilePath + GeneralSettings
fileCheckList = [
 GeneralSettings]
for file in fileCheckList:
    try:
        file = open(file, 'r')
        file.close()
    except:
        file = open(file, 'w')
        file.close()

else:
    downloadDir = open(GeneralSettings, 'r')
    downloadDir = downloadDir.read()
    if not os.path.exists(downloadDir):
        open(GeneralSettings, 'w').close()
        if platform == 'android':
            androidDownloadPath = plyer.storagepath.get_downloads_dir()
        else:
            androidDownloadPath = 'downloads/'
    else:
        androidDownloadPath = downloadDir
    nHLink = 'https://nhentai.net/g/'
    maxFolderNameLength = androidAllowedLength - len(androidDownloadPath)
    replaceList = [
     '<span class=', '</span>', '"', 'before>', 'pretty>', 'after>', ']', '[', '}', '{', '(', ')', '|', ',', "'", '"', chr(92), '?', '<', '>', ' ', ';', ':', '*', '+']

    def imgDownload(url, pageNum, path):
        url = url.replace('//t', '//i')
        url = url.replace('t.png', '.png')
        url = url.replace('t.jpg', '.jpg')
        i = re.split('[/.]', url)[(-2)]
        i = i.replace('t', '')
        pathLocation = path + '/' + str(i) + '.jpg'
        try:
            response = requests.get(url, stream=True, verify=False)
            file = open(pathLocation, 'wb')
            shutil.copyfileobj(response.raw, file)
            file.close()
        except:
            pass


    def imgDirLocate(page, global_requests):
        imageLocate = global_requests
        soupImageLocate = bs4.BeautifulSoup(imageLocate.text, 'html.parser')
        soupImagePath = str(soupImageLocate.find_all('img')[3:page * 2 + 3])
        soupImagePath = re.split('([^(data-src=")]*")', soupImagePath)
        soupImagePathtmp = []
        for i in soupImagePath:
            if validators.url(i):
                soupImagePathtmp.append(i)
            soupImagePath = soupImagePathtmp
            for i in range(len(soupImagePath) - 1):
                if len(soupImagePath) > i:
                    soupImagePath.pop(i)
                return soupImagePath


    def linkFolderCreation(global_requests, sid):
        folderName = androidDownloadPath
        imageLocate = global_requests
        soupTitleLocate = bs4.BeautifulSoup(imageLocate.text, 'html.parser')
        sauceTagsLOL = soupTitleLocate.find_all(class_='name')
        sauceTagsLOLText = []
        for i in sauceTagsLOL:
            sauceTagsLOLText.append(i.get_text() + '|')
        else:
            soupTitleNameBefore = soupTitleLocate.find(class_='before')
            soupTitleName = str(soupTitleLocate.find(class_='pretty'))
            soupTitleNamePretty = soupTitleLocate.find(class_='pretty')
            soupTitleNameAfter = soupTitleLocate.find(class_='after')
            for character in replaceList:
                soupTitleName = soupTitleName.replace(character, '')
            else:
                folderName = folderName + soupTitleName
                if len(folderName) > maxFolderNameLength:
                    tmpNumLen = 0
                    tmpString = ''
                    for i in folderName:
                        if tmpNumLen <= maxFolderNameLength:
                            tmpString = tmpString + ''.join(i)
                        tmpNumLen += 1
                    else:
                        folderName = tmpString

                elif not os.path.exists(folderName):
                    os.makedirs(folderName)
                    f = open(folderName + infoFileName, 'w')
                    endText = 'Name: ' + soupTitleNameBefore.get_text() + soupTitleNamePretty.get_text() + soupTitleNameAfter.get_text() + '\nSauce ID: ' + sid.replace('https://nhentai.net/g/', '') + '\nTags: '
                    for i in sauceTagsLOLText[:-1]:
                        endText = endText + i
                    else:
                        endText = endText + '\nPages: ' + sauceTagsLOLText[(-1)]
                        f.write(endText)
                        f.close()

                else:
                    folderName = folderName + str(random.randint(1, 1000))
                    os.makedirs(folderName)
                    f = open(folderName + infoFileName, 'w')
                    endText = 'Name: ' + soupTitleNameBefore.get_text() + soupTitleNamePretty.get_text() + soupTitleNameAfter.get_text() + '\nSauce ID: ' + sid.replace('https://nhentai.net/g/', '') + '\nTags: '
                    for i in sauceTagsLOLText[:-1]:
                        endText = endText + i
                    else:
                        endText = endText + '\nPages: ' + sauceTagsLOLText[(-1)]
                        f.write(endText)
                        f.close()

                return folderName


    def pages(global_requests):
        nameClass = 'name'
        imageLocate = global_requests
        soupPagesLocate = bs4.BeautifulSoup(imageLocate.text, 'html.parser')
        soupPagesNumber = str(soupPagesLocate.find_all(class_='name')[(-1)])
        soupPagesNumber = soupPagesNumber.replace('<span', '')
        soupPagesNumber = soupPagesNumber.replace('</span>', '')
        soupPagesNumber = soupPagesNumber.replace('"', '')
        soupPagesNumber = soupPagesNumber.replace('class=name>', '')
        return int(soupPagesNumber)


    def websiteIncrement(url, actualDownload):
        if len(url) <= 6:
            url = nHLink + url
        elif actualDownload == 'True':
            global_requests = requests.get(url)
            page = pages(global_requests)
            path = linkFolderCreation(global_requests, url)
            imgLinks = imgDirLocate(page, global_requests)
            threads = []
            chunks = [imgLinks[i:i + downloadSections] for i in range(0, len(imgLinks), downloadSections)]
            for i in chunks:
                for k in i:
                    t = threading.Thread(target=imgDownload, args=[k, page, path])
                    t.start()
                    threads.append(t)
                    time.sleep(delayTime)

            else:
                for thread in threads:
                    thread.join()

        else:
            tmpCount = 0
            global_requests = requests.get(url)
            page = pages(global_requests)
            imgLinks = imgDirLocate(page, global_requests)
            for i in imgLinks:
                i = i.replace('//t', '//i')
                i = i.replace('t.png', '.png')
                i = i.replace('t.jpg', '.jpg')
                imgLinks[tmpCount] = i
                tmpCount += 1
            else:
                return imgLinks