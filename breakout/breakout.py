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
            products_section=driver.find_element(By.XPATH,'//*[@id="pt-pageContent"]/div[1]/div/div/div')
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
                product_title=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/h1').text
            except:
                product_title='No title'
            try:
                product_price=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[2]/div/span[2]').text
            except:
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[2]/div/span[2]').text
                except:
                    product_price='No price'

            try:
                product_sku=driver.find_element(By.XPATH,'//*[@id="sku"]/div/ul/li[1]/span[2]').text
            except:
                product_sku='No sku'

            try:
                product_description=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[5]/span[2]').text
            except:
                product_description='No description'

            try:
                swatches=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[3]/div[1]/ul')
                # get all the li tags 
                swatches=swatches.find_elements(By.TAG_NAME,'li')
                sizes=[]
                for swatch in swatches:
                    try:
                        # get the data-availability attribute of li tag
                        availability=swatch.get_attribute('data-availability')
                        if availability:
                            continue
                        else:
                            # get the text of li tag
                            size=swatch.text
                            # append size to sizes list
                            sizes.append(size)
                    except:
                        continue
                sizes=','.join(sizes)
                    
            except:
                sizes='No sizes'
            colors='Not available'

            try:
                images=[]
                # get all div tags with id='smallGallery'
                slider=driver.find_element(By.XPATH,'//*[@id="smallGallery"]/div/div')
                # get all the img tags inside slider
                img=slider.find_elements(By.TAG_NAME,'img')
                # get src attribute of img
                for i in img:
                    src=i.get_attribute('src')
                    # get first image from srcset attribute
                    src=src.split(' ')[0]
                    src=src.split('.jpg')[0]
                    src=src.split('_')
                    src='_'.join(src[:-1])+'.jpg'
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
        # save data to csv file
        df=pd.DataFrame(details)
        df.to_csv('products.csv',index=False)


    except Exception as e:
        print(e)
        driver.quit()

    return details


def main():
    url="https://breakout.com.pk/collections/men-tees"
    links=get_product_links(url)
    print('Total links: ',len(links))
    # print(links)
    details=get_product_details(links,'t-shirt','Men')
    print('Total details: ',len(details))
    df=pd.DataFrame(details)
    df.to_csv('breakout.csv',index=False)
    print('Done')
    print('Done')
    # print(links)

if __name__=="__main__":
    main()