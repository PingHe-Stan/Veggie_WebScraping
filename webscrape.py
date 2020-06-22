#This is a Web Scraping Script

from bs4 import BeautifulSoup
import json
import requests
import os


def my_webscrape():
    x = 0 # Image Number Counter
    y = 0 # Failed Attempt to Scrape Image
    for i in range(1,4):
        #URL = "https://www.instacart.ca/t-t/aisles/63205-fresh-vegetables/page/" + str(i) #Five pages for Veggie Section
        URL = "https://www.instacart.ca/t-t/aisles/63202-fresh-fruits/page/" + str(i) #Five pages for Veggie Section
        #hdrs = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        hdrs = {'User-Agent':'Chrome/78.0.3904.70'}
        html = requests.get(URL,headers=hdrs).text
        soup = BeautifulSoup(html, 'lxml')
        #img_ul = soup.find_all('ul', {"class": "img_list"})
        img_ul = soup.find_all('script', {"type":"application/ld+json"})
        os.makedirs('./img_fruits/', exist_ok=True)
        for img in img_ul[1:]:
            try:
                json_str = json.loads(img.text)
                image_url = json_str['image'].replace('primary','large')
                image_name = json_str['name'] + '.jpg'
                print(image_url,type(image_url))
                print(image_name)
                x = x + 1
                r = requests.get(image_url, stream=True)
                with open('./img_fruits/%s' % image_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=128):
                        f.write(chunk)
                print('Saved %s' % image_name)
                print(f'--------------------------------------No.({x}) Image Scraped in Veggie category-----------------------------------')
            except Exception as e:
                errmsg = type(e).__name__ + " " + str(e)
                y = y + 1
                print(f'{errmsg},total failed attempts = {y}')
                print(f'failed at {img} due to json formatting, please download it manually.')


if __name__ == "main":
    my_webscrape()
