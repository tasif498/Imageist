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

def get_product_links_diners(url):
    links=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #get ul tag with class name 'pagination-page'
        page_links= driver.find_element(By.XPATH,"//ul[@class='pagination-page']")
        products=driver.find_elements(By.XPATH,"//a[@class='product-title']")
        for product in products:
            links.append(product.get_attribute('href'))
        #get all a tags inside ul tag
        page_links=page_links.find_elements(By.TAG_NAME,"a")
        #get href attribute of all a tags
        page_links=[link.get_attribute('href') for link in page_links]
        page_links=list(set(page_links))
        page_links.sort()
        # print(page_links)
        for link in page_links:
            driver.get(link)
            time.sleep(5)
            #scrolling down to load all the products
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            #getting all a tags with class name 'product-title'
            products=driver.find_elements(By.XPATH,"//a[@class='product-title']")
            for product in products:
                links.append(product.get_attribute('href'))
        driver.quit()
        links=list(set(links))
        return links
    except Exception as e:
        print(e)
        driver.quit()
        return links

def get_product_details_diners(links,type,gender):
    details=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        for link in links:
            driver.get(link)
            time.sleep(5)
            try:
                product_title=driver.find_element(By.XPATH,"//h1[@class='product-title']").text
            except:
                product_title='No title'
            try:
                product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[3]/span[2]/span').text
            except:
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[3]/span[1]/span').text
                except:
                    product_price='No price'

            try:
                product_sku=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[2]/div[1]/span').text
            except:
                product_sku='No sku'

            try:
                product_description=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[4]').text
            except:
                product_description='No description'

            try:
                # get div tag with class name 'swatch'
                swatches=driver.find_element(By.CLASS_NAME,'swatch')
                # get all input tags inside with type 'radio'
                swatches=swatches.find_elements(By.XPATH,"//input[@type='radio']")
                sizes=[]
                for swatch in swatches:
                    # check if swatch is disabled
                    if swatch.is_enabled():
                        sizes.append(swatch.get_attribute('value'))
                sizes=','.join(sizes)
                    
            except:
                sizes='No sizes'

            try:
                colors=[]
                # get div tag with //*[@id="product-variants"]/div[4]
                swatches=driver.find_element(By.XPATH,'//*[@id="product-variants"]/div[4]')
                # get all input tags inside with type 'radio'
                swatches=swatches.find_elements(By.XPATH,"//input[@type='radio']")
                for swatch in swatches:
                    colors.append(swatch.get_attribute('value'))
                colors=','.join(colors)
            except:
                colors='No colors'

            try:
                #get image slider
                slider=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[1]/div/div[2]')
                #get all img tags inside slider
                images=slider.find_elements(By.TAG_NAME,'img')
                #get src attribute of all img tags
                images=[image.get_attribute('src') for image in images]
                images=','.join(images)
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
    url="https://diners.com.pk/collections/t-shirts"
    links=get_product_links_diners(url)
    print('Total links: ',len(links))
    details=get_product_details_diners(links,'t-shirt','Men')
    print('Total details: ',len(details))
    df=pd.DataFrame(details)
    df.to_csv('diners.csv',index=False)
    print('Done')
    # convert chrismas.data to json    
    print('Done')
    # print(links)

if __name__=="__main__":
    main()