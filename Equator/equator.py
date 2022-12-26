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

def get_product_links_equator(url):
    links=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(url)
        time.sleep(5)
        prev_height=driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            products_section=driver.find_element(By.XPATH,"//div[@class='row']")
            # get all the anchor tags
            products=products_section.find_elements(By.TAG_NAME,"a")
            for product in products:
                link=product.get_attribute("href")
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


def get_product_details_equator(links,type,gender):
    details=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        for link in links:
            driver.get(link)
            time.sleep(5)
            try:
                product_title=driver.find_element(By.XPATH,'//*[@id="shopify-section-pr_summary"]/h1').text
            except:
                product_title='No title'
            try:
                product_price=driver.find_element(By.XPATH,'//*[@id="price_ppr"]/ins').text
            except:
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="price_ppr"]').text
                except:
                    product_price='No price'

            try:
                product_sku=driver.find_element(By.XPATH,'//*[@id="pr_sku_ppr"]').text
            except:
                product_sku='No sku'

            try:
                product_description=driver.find_element(By.XPATH,'//*[@id="shopify-section-pr_summary"]/div[4]').text
            except:
                product_description='No description'

            try:
                # get div tag with data-opname="size"
                swatches=driver.find_element(By.XPATH,'//*[@data-opname="size"]')
                print("swatches: ",swatches)
                # get all input tags inside with li tag
                swatches=swatches.find_elements(By.TAG_NAME,'li')
                sizes=[]
                for swatch in swatches:
                    sizes.append(swatch.get_attribute('data-escape'))
                sizes=','.join(sizes)
                    
            except:
                sizes='No sizes'
            colors='Not available'

            try:
                images=[]
                # get all div tags with data-mdtype="image"
                img=driver.find_elements(By.XPATH,'//*[@data-mdtype="image"]')
                for i in img:
                    # get img tag inside div tag
                    img=i.find_element(By.TAG_NAME,'img')
                    # get srcset attribute of img tag
                    img=img.get_attribute('srcset')
                    # split srcset attribute by comma
                    img=img.split(',')
                    # get first image from srcset attribute
                    img=img[0].split(' ')[0]
                    img=img.split('.jpg')[0]
                    img=img.split('_')
                    img='_'.join(img[:-1])+'.jpg'
                    # add https: to image url
                    img='https:'+img
                    # append image to images list
                    images.append(img)
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
    url="https://equatorstores.com/collections/t-shirts"
    links=get_product_links_equator(url)
    print('Total links: ',len(links))
    details=get_product_details_equator(links,'t-shirt','Men')
    print('Total details: ',len(details))
    df=pd.DataFrame(details)
    df.to_csv('equator.csv',index=False)
    print('Done')
    print('Done')
    # print(links)

if __name__=="__main__":
    main()