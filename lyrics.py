import requests #匯入request 
import re #匯入re
from bs4 import BeautifulSoup #匯入beautiful soup
file=open("test.txt",mode="w",encoding="utf-8") #開啟一個文檔

rs = requests.session()
res = rs.get('https://mojim.com/twzhot-song.htm') #取得網址 

soup = BeautifulSoup(res.text, 'html.parser') #將抓回的HTML頁面傳入BeautifulSoup，使用html.parser解析

# 使用 find_all()
td_tags = soup.find_all('td') #找到網頁中全部的 <td>
for td_tag in td_tags:
    a_tag = td_tag.find('a') #找到 <td> 下的 <a>
    if a_tag is not None: #或歌詞被刪除會是None，要排除None
        
       

        # 抓取每首歌詞使用
        rs2 = requests.session()
        res2 = rs2.get('http://www.mojim.com//'+ a_tag.get('href')) #獲得每一首歌的網址
        soup2 = BeautifulSoup(res2.text, 'html.parser')
        words = soup2.find(id="fsZx3").text #找到網頁中全部id=fsZx3 
        #清理文字
        pretext=words.split('[')[0] #清理歌詞後提供的秒數對照
        lyrics=re.sub(r'更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網','',pretext) #將中間置入非歌詞的句子用空白取代
        file.write(a_tag.text + "\n" + lyrics + "\n" ) #寫入檔案


file.close() #關閉文檔
#以上爬蟲程式參考老師的程式 bsb.py

import matplotlib.pyplot as plt #匯入matplotlib 模組
print("請輸入想查詢的字詞類別：地點，顏色或是情緒")
x=input() #使用者輸入想查詢的字詞類別

if x=="地點":
    image1= plt.imread("C:\pyc\地點.png") #讀取圖片路徑
    plt.imshow(image1)
    plt.show() #顯示圖片
elif x=="顏色":
    image2= plt.imread("C:\pyc\顏色文字雲.png") 
    plt.imshow(image2)
    plt.show()
elif x=="情緒":
    image3= plt.imread("C:\pyc\圓餅圖.png") 
    plt.imshow(image3)
    plt.show()
