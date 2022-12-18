from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import urllib
import time

options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-notifications')

def get_product_links(url):
    links=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(url)
        time.sleep(5)
        prev_height=driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            products_section=driver.find_element(By.XPATH,'//*[@id="usf_container"]/div[2]')
            # get all the anchor tags
            products=products_section.find_elements(By.TAG_NAME,"a")
            for product in products:
                link=product.get_attribute("href")
                if 'page' in link or 'contact' in link:
                    continue
                links.append(link)
            links=list(set(links))
            print(f"Status: {len(links)} links found")

            new_height=driver.execute_script("return document.body.scrollHeight")
            if new_height==prev_height:
                break
            prev_height=new_height

        driver.quit()
        links=list(set(links))
        return links
    except Exception as e:
        print(e)
        driver.quit()
        return links


def get_product_details(links,type,gender):
    details=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        for link in links:
            driver.get(link)
            time.sleep(5)
            try:
                product_title=driver.find_element(By.CLASS_NAME,'t4s-product__title').text
            except:
                product_title='No title'
            try:
                product_price=driver.find_element(By.CLASS_NAME,'t4s-product-price')
                product_price=product_price.find_element(By.TAG_NAME,'ins').text
            except:
                try:
                    product_price=driver.find_element(By.CLASS_NAME,'t4s-product-price').text
                except:
                    product_price='No price'

            try:
                product_sku=driver.find_element(By.CLASS_NAME,'t4s-sku-wrapper').text
                product_sku=product_sku.split(':')[1]
            except:
                product_sku='No sku'

            try:
                product_description=driver.find_element(By.XPATH,'/html/body/div[2]/main/section[1]/div/div/div/div/div[2]/div[2]/div[4]/p').text
            except:
                product_description='No description'

            try:

                # get all div tags with attribute data-swatch-item
                swatches=driver.find_elements(By.XPATH,'//div[@data-swatch-item]')
                sizes=[]
                for swatch in swatches:
                    try:
                        # get the data-availability attribute of li tag
                        value=swatch.get_attribute('data-value')
                        if value:
                            # append size to sizes list
                            sizes.append(value)
                    except:
                        continue
                sizes=','.join(sizes)
                    
            except:
                sizes='No sizes'
            colors='Not available'

            try:
                images=[]
                # get all div tags with attribute data-product-single-media-wrapper
                img=driver.find_elements(By.XPATH,'//div[@data-product-single-media-wrapper]')
                # get src attribute of img
                for i in img:
                    i=i.find_element(By.TAG_NAME,'img')
                    src=i.get_attribute('srcset')
                    # split srcset attribute
                    src=src.split(',')[0]
                    # get first image from srcset attribute
                    src=src.split(' ')[0]
                    src=src.split('.jpg')[0]
                    src=src.split('_')
                    src='_'.join(src[:-1])+'.jpg'
                    src='https:'+src
                    # append image to images list
                    images.append(src)
                images=list(set(images))
                images=', '.join(images)
            except:
                images='No images'

            data={
                'title':product_title,
                'price':product_price,
                'sku':product_sku,
                'description':product_description,
                'sizes':sizes,
                'colors':colors,
                'images':images,
                'type':type,
                'product_link':link,

            }
            print(data)
            details.append(data)
        driver.quit()


    except Exception as e:
        print(e)
        driver.quit()

    return details


def main():
    url="https://monark.com.pk/collections/formal-shirts"
    links=get_product_links(url)
    print('Total links: ',len(links))
    print(links)
    details=get_product_details(links,'formal-shirt','Men')
    print('Total details: ',len(details))
    df=pd.DataFrame(details)
    df.to_csv('monark.csv',index=False)
    print('Done')
    print('Done')

if __name__=="__main__":
    main()