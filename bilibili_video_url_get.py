from selenium import webdriver  
from selenium.webdriver.edge.options import Options  
from bs4 import BeautifulSoup  
import random
from selenium import webdriver  
from selenium.webdriver.edge.service import Service  #导入 Service 类
import time
import csv
# 配置Edge浏览器选项  
options = Options()  
options.use_chromium = True  
total_vedio=0
message_url=[]
message_name=[]
# 初始化Edge浏览器  
s = Service('D:\\浏览器下载\\edgedriver_win64\\msedgedriver.exe')
# 创建 Edge 的选项  
options = webdriver.EdgeOptions()   
# 使用 Service 对象和选项来初始化 Edge WebDriver  
driver = webdriver.Edge(service=s, options=options) 

# 打开目标网页  
url = 'https://www.bilibili.com/v/animal/cat/'
driver.get(url)  
  
# 滚动指定次数加载更多内容  
scroll_times = 3 
for _ in range(scroll_times):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待页面加载新内容
    wait=random.randint(30,40)/10
    time.sleep(wait)
    
# 获取滚动后的页面HTML  
html = driver.page_source

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'html.parser')
h3_tags=soup.find_all('h3',{'class':'bili-video-card__info--tit'})
# 假设视频名称在一个class为"video-name"的元素中  
#video_names = soup.find_all('a', {'target':'_blank','data-mod':'sub_channel', 'data-idx':'latest_video','data-ext':'click'})
for h3 in h3_tags:
    if h3.a:
        vedio_name=h3.a.get_text(strip=True)
        url_vedio=h3.a['href']
        print(vedio_name,url_vedio)
        total_vedio+=1
        message_url.append(url_vedio)
        message_name.append(vedio_name)
print(f'总共爬取视频{total_vedio}')
# 提取并打印视频名称
#for name in video_names:
#    print(name.text)
#导出url和视频名
with open ('name_url.csv','w',newline='',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['视频名','视频url'])
    for name_csv,url_csv in zip(message_name,message_url):
        writer.writerow([name_csv,url_csv])
# 关闭浏览器
driver.quit()
