#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-10-19 11:06
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org

import xml.etree.cElementTree as ET
import csv


def main():
    tree = ET.parse('./MicrosoftTermCollection.tbx')
    root = tree.getroot()

    list = []

    for termEntry in root.iter('termEntry'):
        listRow = []
        for i, langSet in enumerate(termEntry.findall('langSet')):
            # print(i)
            # print(langSet)
            # input()
            # 缩写不翻译、不添加进术语库
            if i == 0:
                en = langSet.find('ntig').find('termGrp').find('term').text
                listRow.append(en)
            elif i == 1:
                zh = langSet.find('ntig').find('termGrp').find('term').text
                listRow.append(zh)
            else:
                listRow.append(langSet.find('ntig').find(
                    'termGrp').find('term').text)
        if en != zh:
            list.append(listRow)

    with open('Termbase.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerow(['en', 'zh_CN', 'pos', 'description'])
        a.writerows(list)


if __name__ == "__main__":
    main()
