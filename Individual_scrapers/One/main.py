from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
# Note: I have to fix the price capturing and the size data

def get_links_one(url):
    links=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(url)
        time.sleep(5)   
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            # get all a tags with class ='full-unstyled-link'
            a=driver.find_elements(By.XPATH,'//a[@class="full-unstyled-link"]')
            for i in a:
                links.append(i.get_attribute('href'))
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(5)

        driver.quit()
        links=list(set(links))
        return links
    except Exception as e:
        print(e)
        driver.quit()
        return links
        



def get_data_monark(urls,type,gender):
    details=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        for link in urls:
            driver.get(link)
            time.sleep(5)
            try:
                # get product name from class 'product__title'
                name=driver.find_element(By.XPATH,'//h1[@class="product__title"]').text
            except:
                name='No Name Found'
            try:
                # get product price from span with class 'money'
                price=driver.find_element(By.XPATH,'//*[@id="price-template--15591320846487__main"]/div/div/div[2]/span[4]/span').text
            except:
                try:
                    price=driver.find_element(By.XPATH,'//*[@id="price-template--15591320846487__main"]/div/div/div[2]/span[2]/s/span').text
                except:
                    price='No Price Found'

            try:
                # get product sku from div class 'product-sku'
                sku=driver.find_element(By.XPATH,'//div[@class="product-sku"]').text
            except:
                sku='No Sku Found'
            try:
                # get product description from /html/body/main/section[1]/section/div[1]/div[3]/div/div[5]/p
                description=driver.find_element(By.XPATH,'/html/body/main/section[1]/section/div[1]/div[3]/div/div[5]/p').text
            except:
                description='No Description Found'
            try:
                # get product color from input with name 'color'
                color=driver.find_element(By.XPATH,'//input[@name="Color"]').get_attribute('value')
            except:
                color='No Color Found'
            try:
            # get product size from input tags with name='size'
                sizes=driver.find_elements(By.NAME,'Size')
                size_list=[]
                for i in sizes:
                    c=i.get_attribute('class')
                    if c!='sold-out':
                        size=i.get_attribute('value')
                        size_list.append(size)
                size=','.join(size_list)
            except:
                size='No Size Found'
            try:
                # get all img tags with attribute 'data-fancybox'='media-gallery'
                img=driver.find_elements(By.XPATH,'//img[@data-fancybox="media-gallery"]')
                img=[i.get_attribute('src') for i in img]
                img=', '.join(img)

            except:
                img='No Image Found'

            print('---------------------------------------------------------------------------------')
            print('Name: ',name)
            print('Price: ',price)  
            print('SKU: ',sku)
            print('Description: ',description)
            print('Color: ',color)
            print('Size: ',size)
            print('Gender:',gender)
            print('Type:',type)
            print('Image: ',img)
            print('Product Link: ',link)
            print('---------------------------------------------------------------------------------')
            data={
                'title':name,
                'price':price,
                'sku':sku,
                'description':description,
                'colors':color,
                'sizes':size,
                'gender':gender,
                'type':type,
                'images':img,
                'product_link':link
            }
            details.append(data)
        driver.quit()
        return details
    except Exception as e:
        print(e)
        driver.quit()
        return details








url='https://beoneshopone.com/collections/men-tops-t-shirts'

links=get_links_one(url)
print(len(links))
print(links)
details=get_data_monark(links,'T-Shirt','Men')

url='https://beoneshopone.com/collections/men-bottoms-jeans'

links=get_links_one(url)
print(len(links))
print(links)
details=get_data_monark(links,'jeans','Men')
df=pd.DataFrame(details)
df.to_csv('beoneshopone.csv',index=False)