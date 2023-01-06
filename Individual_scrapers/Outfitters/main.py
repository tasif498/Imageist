from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
def get_product_links_outfitters(url):
    links=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get(url)
        driver.maximize_window()
        ## record the current document height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            # get all the a tags with class name product-link-main
            products=driver.find_elements(By.XPATH,"//a[@class='product-link-main']")
            for product in products:
                links.append(product.get_attribute("href"))
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        links=list(set(links))
        print('Total links:',len(links))
        # print(links)

        ## close the browser
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
    return links


def get_product_details_outfitters(links,type):

    details=[]
    try:
        driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.maximize_window()
        print('Scraping the product details...')
        for link in links:
            driver.get(link)
            time.sleep(5)
            # get the product name using class name product__title
            try:
                product_name=driver.find_element(By.CLASS_NAME,"product__title").text
            except:
                product_name='Not Found'
            # get the product sku using class name pro-sku
            try:
                product_sku=driver.find_element(By.CLASS_NAME,"pro-sku").text
            except:
                product_sku='Not Found'
            # get the product price using class name price-item
            try:
                product_price=driver.find_element(By.CLASS_NAME,"price-item").text
            except:
                product_price='Not Found'
            # get the product color using lables in class name color-wrapper
            try:
                product_color=driver.find_element(By.CLASS_NAME,"color-wrapper")
                product_color=product_color.find_elements(By.TAG_NAME,"label")
                product_color=[color.get_attribute("title") for color in product_color]
                product_color=','.join(product_color)
            except:
                product_color='Not Found'
            # get the product size using input tags in class name size-wrapper
            try:
                product_size=driver.find_element(By.CLASS_NAME,"size-wrapper")
                product_size=product_size.find_elements(By.TAG_NAME,"input")
                product_size=[size.get_attribute("value") for size in product_size]
                product_size=','.join(product_size)
            except:
                product_size='Not Found'
            # get the product gender using class gender-wrapper
            try:
                gender=driver.find_element(By.CLASS_NAME,'gender-wrapper').text
            except:
                gender='Not Found'
            # get the product description using class name product__description
            try:
                product_description=driver.find_element(By.CLASS_NAME,"product__description").text
            except:
                product_description='Not Found'
            # get the all img tags with class name zoomImg
            imgs=[]
            try:
                img=driver.find_elements(By.CLASS_NAME,"zoomImg")
                for i in img:
                    imgs.append(i.get_attribute("src"))
                imgs=','.join(imgs)
            except:
                imgs='Not Found'
            print('-------------------------------------------------------------------------------')
            print('Product Name:',product_name)
            print('Product SKU:',product_sku)
            print('Product Price:',product_price)
            print('Product Color:',product_color)
            print('Product Size:',product_size)
            print('Gender:',gender)
            print('Product Description:',product_description)
            print('Product Images:',imgs)
            print('Product Link:',link)
            print('PRODUCT TYPE:',type)
            product_data={
                'Product Name':product_name,
                'Product SKU':product_sku,
                'Product Price':product_price,
                'Product Color':product_color,
                'Product Size':product_size,
                'Gender':gender,
                'Product Description':product_description,
                'Product Images':imgs,
                'Product Link':link,
                'Type':type
            }
            details.append(product_data)

        ## close the browser

        driver.close()
    except Exception as e:
        print(e)
        driver.close()

    return details
details=[]
links=[]
url='https://outfitters.com.pk/collections/men-t-shirts'
links.extend(get_product_links_outfitters(url))
url='https://outfitters.com.pk/collections/men-shirts'
links.extend(get_product_links_outfitters(url))
details.extend(get_product_details_outfitters(links,'t-shirt'))
details.extend(get_product_details_outfitters(links,'shirt'))
print('Total products:',len(details))
df=pd.DataFrame(details)
df.to_csv('outfitters.csv',index=False)


time.sleep(120)