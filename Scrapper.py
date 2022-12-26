from selenium import webdriver  # Importing the webdriver   from selenium
from selenium.webdriver.common.keys import Keys # Importing the Keys class  to use the keys like ENTER, ESC etc
from selenium.webdriver.common.by import By # Importing the By class to use the locator
from selenium.webdriver.support.ui import WebDriverWait # Importing the WebDriverWait class to use the wait function
from webdriver_manager.chrome import ChromeDriverManager    # Importing the ChromeDriverManager class to install the chrome driver
import pandas as pd # Importing the pandas library to use the dataframes
import urllib   # Importing the urllib library to use the url functions
import time # Importing the time library to use the time functions

options=webdriver.ChromeOptions()   # Options to be passed to the webdriver
options.add_argument('--disable-blink-features=AutomationControlled') # to disable the webdriver detection in the website

class Scrapper: # Scrapper class used to scrape data from the web
    
    def get_product_links_diners(self,url):
        '''
        This function is used to get the product links from the diners website
        '''
        links=[]    # List to store the product links
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the webdriver object
            driver.get(url) # Getting the url
            time.sleep(5)   # Waiting for 5 seconds to load the page
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling down to load all the products
            #get ul tag with class name 'pagination-page'   
            page_links= driver.find_element(By.XPATH,"//ul[@class='pagination-page']")  #  Getting the ul tag with class name 'pagination-page'
            products=driver.find_elements(By.XPATH,"//a[@class='product-title']")   # Getting all the a tags with class name 'product-title'
            for product in products:    # Loop to get the href attribute of all the a tags
                links.append(product.get_attribute('href')) # Appending the href attribute to the links list
            #get all a tags inside ul tag
            page_links=page_links.find_elements(By.TAG_NAME,"a")    # Getting all the a tags inside the ul tag
            #get href attribute of all a tags
            page_links=[link.get_attribute('href') for link in page_links]  # Getting the href attribute of all the a tags
            page_links=list(set(page_links))    # Removing the duplicate links
            page_links.sort()   # Sorting the links
            # print(page_links)
            for link in page_links: # Loop to get the product links from all the pages
                driver.get(link)    # Getting the link
                time.sleep(5)   # Waiting for 5 seconds to load the page
                #scrolling down to load all the products
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling down to load all the products
                #getting all a tags with class name 'product-title'
                products=driver.find_elements(By.XPATH,"//a[@class='product-title']")   # Getting all the a tags with class name 'product-title'
                for product in products:
                    links.append(product.get_attribute('href')) # Appending the href attribute to the links list
            driver.quit()   # Quitting the driver
            links=list(set(links))  # Removing the duplicate links
            return links    # Returning the links
        except Exception as e:  # Exception block to handle the exceptions if any
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver
            return links    # Returning the links

    def get_product_details_diners(self,links,type,gender): 
        '''
        This function is used to get the product details from the diners website
        '''
        details=[]  # List to store the product details
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the webdriver object
            for link in links:  # Loop to get the product details from all the links
                driver.get(link)    # Getting the link  
                time.sleep(5)   # Waiting for 5 seconds to load the page
                try:
                    product_title=driver.find_element(By.XPATH,"//h1[@class='product-title']").text # Getting the product title
                except:
                    product_title='No title'    # If the product title is not found then assigning 'No title' to the product title
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[3]/span[2]/span').text # Getting the product price
                except:
                    try:    # Try block to handle the exceptions
                        product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[3]/span[1]/span').text # Getting the product price
                    except:
                        product_price='No price'    # If the product price is not found then assigning 'No price' to the product price

                try:
                    product_sku=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[2]/div[1]/span').text    # Getting the product sku
                except:
                    product_sku='No sku'    # If the product sku is not found then assigning 'No sku' to the product sku

                try:
                    product_description=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[2]/div[4]').text    # Getting the product description
                except:
                    product_description='No description'    # If the product description is not found then assigning 'No description' to the product description

                try:
                    # get div tag with class name 'swatch'
                    swatches=driver.find_element(By.CLASS_NAME,'swatch')    # Getting the div tag with class name 'swatch'
                    # get all input tags inside with type 'radio'
                    swatches=swatches.find_elements(By.XPATH,"//input[@type='radio']")  # Getting all the input tags inside the div tag with type 'radio'
                    sizes=[]    # List to store the sizes
                    for swatch in swatches: # Loop to get the sizes
                        # check if swatch is disabled
                        if swatch.is_enabled(): # Checking if the swatch is disabled
                            sizes.append(swatch.get_attribute('value'))  # Appending the value attribute to the sizes list
                    sizes=','.join(sizes)   # Joining the sizes list with comma
                        
                except:
                    sizes='No sizes'    # If the sizes are not found then assigning 'No sizes' to the sizes

                try:
                    colors=[]   # List to store the colors
                    # get div tag with //*[@id="product-variants"]/div[4]
                    swatches=driver.find_element(By.XPATH,'//*[@id="product-variants"]/div[4]') # Getting the div tag with //*[@id="product-variants"]/div[4]
                    # get all input tags inside with type 'radio'
                    swatches=swatches.find_elements(By.XPATH,"//input[@type='radio']")  # Getting all the input tags inside the div tag with type 'radio'
                    for swatch in swatches: # Loop to get the colors
                        colors.append(swatch.get_attribute('value'))    # Appending the value attribute to the colors list
                    colors=','.join(colors) # Joining the colors list with comma
                except: # Exception block to handle the exceptions if any
                    colors='No colors'

                try:
                    #get image slider
                    slider=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-default"]/div/div[1]/div[1]/div/div[2]')  # Getting the image slider
                    #get all img tags inside slider
                    images=slider.find_elements(By.TAG_NAME,'img')  # Getting all the img tags inside the image slider
                    #get src attribute of all img tags  
                    images=[image.get_attribute('src') for image in images] # Getting the src attribute of all the img tags
                    images=','.join(images) # Joining the images list with comma
                except:
                    images='No images'  # If the images are not found then assigning 'No images' to the images

                data={ # Dictionary to store the product details
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
                print(data) # Printing the data
                details.append(data)    # Appending the data to the details list
            driver.quit()   # Quitting the driver
            # save data to csv file
            df=pd.DataFrame(details)    # Converting the details list to pandas dataframe
            df.to_csv('products.csv',index=False)   # Saving the dataframe to csv file


        except Exception as e:  # Exception block to handle the exceptions if any
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver

        return details  # Returning the details list


    def get_product_links_equator(self,url):  
        '''
        Function to get the product links from the Equator website
        '''  # Function to get the product links from the Equator website
        links=[]    # List to store the product links
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.get(url) # Getting the url
            time.sleep(5)   # Waiting for 5 seconds
            prev_height=driver.execute_script("return document.body.scrollHeight")  # Getting the previous height of the page
            while True: # Loop to scroll the page
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling the page
                time.sleep(5)       # Waiting for 5 seconds
                products_section=driver.find_element(By.XPATH,"//div[@class='row']")    # Getting the div tag with class name 'row'
                # get all the anchor tags
                products=products_section.find_elements(By.TAG_NAME,"a")    # Getting all the anchor tags
                for product in products:  # Loop to get the product links
                    link=product.get_attribute("href")  # Getting the href attribute of the anchor tag
                    links.append(link)  # Appending the link to the links list
                links=list(set(links))  # Removing the duplicates from the links list
                print(f"Status: {len(links)} links found")  # Printing the number of links found

                new_height=driver.execute_script("return document.body.scrollHeight")   # Getting the new height of the page
                if new_height==prev_height: # Checking if the new height is equal to the previous height
                    break   # If the new height is equal to the previous height then breaking the loop
                prev_height=new_height  # Assigning the new height to the previous height

            driver.quit()   # Quitting the driver   
            links=list(set(links))  # Removing the duplicates from the links list
            return links    # Returning the links list
        except Exception as e:      
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver
            return links    # Returning the links list


    def get_product_details_equator(self,links,type,gender):
        '''
        Function to get the product details from the Equator website    
        '''
        details=[]  # List to store the product details
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            for link in links:  # Loop to get the product details
                driver.get(link)    # Getting the link
                time.sleep(5)   # Waiting for 5 seconds
                try:
                    product_title=driver.find_element(By.XPATH,'//*[@id="shopify-section-pr_summary"]/h1').text # Getting the product title
                except:
                    product_title='No title'    # If the product title is not found then assigning 'No title' to the product title
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="price_ppr"]/ins').text # Getting the product price
                except:
                    try:
                        product_price=driver.find_element(By.XPATH,'//*[@id="price_ppr"]').text # Getting the product price
                    except:
                        product_price='No price'    # If the product price is not found then assigning 'No price' to the product price

                try:
                    product_sku=driver.find_element(By.XPATH,'//*[@id="pr_sku_ppr"]').text  # Getting the product sku
                except:
                    product_sku='No sku'        # If the product sku is not found then assigning 'No sku' to the product sku

                try:
                    product_description=driver.find_element(By.XPATH,'//*[@id="shopify-section-pr_summary"]/div[4]').text   # Getting the product description
                except:
                    product_description='No description'    # If the product description is not found then assigning 'No description' to the product description

                try:
                    # get div tag with data-opname="size"
                    swatches=driver.find_element(By.XPATH,'//*[@data-opname="size"]')   # Getting the div tag with data-opname="size"
                    # print("swatches: ",swatches)
                    # get all input tags inside with li tag
                    swatches=swatches.find_elements(By.TAG_NAME,'li')   # Getting all the li tags inside the div tag
                    sizes=[]
                    for swatch in swatches: # Loop to get the sizes
                        sizes.append(swatch.get_attribute('data-escape'))   # Appending the size to the sizes list
                    sizes=','.join(sizes)   # Joining the sizes list with comma
                        
                except: # If the sizes are not found then assigning 'No sizes' to the sizes
                    sizes='No sizes'    # If the sizes are not found then assigning 'No sizes' to the sizes
                colors='Not available'  # Assigning 'Not available' to the colors

                try:
                    images=[]   # List to store the images
                    # get all div tags with data-mdtype="image"
                    img=driver.find_elements(By.XPATH,'//*[@data-mdtype="image"]')  # Getting all the div tags with data-mdtype="image"
                    for i in img:   # Loop to get the images
                        # get img tag inside div tag
                        img=i.find_element(By.TAG_NAME,'img')   # Getting the img tag inside the div tag
                        # get srcset attribute of img tag
                        img=img.get_attribute('srcset') # Getting the srcset attribute of the img tag
                        img=img.split(',')  # Splitting the srcset attribute by comma
                        img=img[0].split(' ')[0]    # Splitting the first element of the list by space and getting the first element
                        img=img.split('.jpg')[0]    # Splitting the image by .jpg and getting the first element
                        img=img.split('_')  # Splitting the image by _
                        img='_'.join(img[:-1])+'.jpg'   # Joining the list with _ and appending .jpg to the end
                        img='https:'+img    # Adding https: to the image url
                        images.append(img)  # Appending the image to the images list
                    images=list(set(images))    # Removing the duplicates from the images list
                    images=', '.join(images)    # Joining the images list with comma
                except:
                    images='No images'  # If the images are not found then assigning 'No images' to the images

                data={  # Dictionary to store the product details
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
                print(data) # Printing the data
                details.append(data)    # Appending the data to the details list
            driver.quit()   # Quitting the driver
            # save data to csv file
            df=pd.DataFrame(details)    # Creating the dataframe
            df.to_csv('products.csv',index=False)   # Saving the dataframe to csv file


        except Exception as e:  # If any exception occurs then printing the exception and quitting the driver
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver

        return details  # Returning the details

    def get_product_links_monark(self,url):
        '''
        This function is used to get the product links from the given url of monark
        '''
        links=[]    # List to store the links
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.get(url) # Getting the url
            time.sleep(5)   # Waiting for 5 seconds
            prev_height=driver.execute_script("return document.body.scrollHeight")  # Getting the previous height of the page
            while True: # Loop to scroll the page
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling the page
                time.sleep(5)   # Waiting for 5 seconds
                products_section=driver.find_element(By.XPATH,'//*[@id="usf_container"]/div[2]')    # Getting the products section
                # get all the anchor tags
                products=products_section.find_elements(By.TAG_NAME,"a")    # Getting all the anchor tags
                for product in products:    # Loop to get the links
                    link=product.get_attribute("href")  # Getting the link
                    if 'page' in link or 'contact' in link:  # If the link is not a product link then
                        continue    # Continue to the next iteration
                    links.append(link)  # Appending the link to the links list
                links=list(set(links))  # Removing the duplicates from the links list
                print(f"Status: {len(links)} links found")  # Printing the number of links found

                new_height=driver.execute_script("return document.body.scrollHeight")   # Getting the new height of the page
                if new_height==prev_height: # If the new height is equal to the previous height then
                    break   # Break the loop
                prev_height=new_height  # Assigning the new height to the previous height

            driver.quit()       # Quitting the driver
            links=list(set(links))  # Removing the duplicates from the links list
            return links    # Returning the links
        except Exception as e:  # If any exception occurs then printing the exception and quitting the driver
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver
            return links    # Returning the links


    def get_product_details_monark(self,links,type,gender):
        '''
        This function is used to get the product details from the given links for monark
        '''
        details=[]  # List to store the details
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            for link in links:  # Loop to get the product details
                driver.get(link)    # Getting the link
                time.sleep(5)   # Waiting for 5 seconds
                try:
                    product_title=driver.find_element(By.CLASS_NAME,'t4s-product__title').text  # Getting the product title
                except:
                    product_title='No title'    # If the product title is not found then assigning 'No title' to the product title
                try:
                    product_price=driver.find_element(By.CLASS_NAME,'t4s-product-price')    # Getting the product price
                    product_price=product_price.find_element(By.TAG_NAME,'ins').text    # Getting the product price
                except:
                    try:
                        product_price=driver.find_element(By.CLASS_NAME,'t4s-product-price').text   # Getting the product price
                    except:
                        product_price='No price'    # If the product price is not found then assigning 'No price' to the product price

                try:
                    product_sku=driver.find_element(By.CLASS_NAME,'t4s-sku-wrapper').text   # Getting the product sku
                    product_sku=product_sku.split(':')[1]   # Getting the product sku
                except: 
                    product_sku='No sku'        # If the product sku is not found then assigning 'No sku' to the product sku

                try:
                    product_description=driver.find_element(By.XPATH,'/html/body/div[2]/main/section[1]/div/div/div/div/div[2]/div[2]/div[4]/p').text   # Getting the product description
                except:
                    product_description='No description'    # If the product description is not found then assigning 'No description' to the product description

                try:

                    # get all div tags with attribute data-swatch-item
                    swatches=driver.find_elements(By.XPATH,'//div[@data-swatch-item]')      # Getting all the swatches
                    sizes=[]
                    for swatch in swatches:    # Loop to get the sizes
                        try:
                            # get the data-availability attribute of li tag
                            value=swatch.get_attribute('data-value')    # Getting the size
                            if value:
                                # append size to sizes list
                                sizes.append(value)    # Appending the size to the sizes list
                        except:
                            continue    # Continue to the next iteration
                    sizes=','.join(sizes)   # Joining the sizes list with comma
                        
                except:
                    sizes='No sizes'    # If the sizes are not found then assigning 'No sizes' to the sizes
                colors='Not available'  # Assigning 'Not available' to the colors

                try:
                    images=[]   # List to store the images
                    # get all div tags with attribute data-product-single-media-wrapper
                    img=driver.find_elements(By.XPATH,'//div[@data-product-single-media-wrapper]')  # Getting all the images
                    # get src attribute of img
                    for i in img:   # Loop to get the images
                        i=i.find_element(By.TAG_NAME,'img') # Getting the image
                        src=i.get_attribute('srcset')   # Getting the srcset attribute
                        # split srcset attribute
                        src=src.split(',')[0]   # Getting the first image from the srcset attribute
                        # get first image from srcset attribute
                        src=src.split(' ')[0]   # Getting the first image from the srcset attribute
                        src=src.split('.jpg')[0]    # Getting the first image from the srcset attribute
                        src=src.split('_')
                        src='_'.join(src[:-1])+'.jpg'   # Getting the first image from the srcset attribute
                        src='https:'+src
                        # append image to images list
                        images.append(src)  # Appending the image to the images list
                    images=list(set(images))    # Removing the duplicates from the images list
                    images=', '.join(images)    # Joining the images list with comma
                except:
                    images='No images'  # If the images are not found then assigning 'No images' to the images

                data={  # Dictionary to store the details
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
                print(data) # Printing the data
                details.append(data)    # Appending the data to the details list
            driver.quit()


        except Exception as e:  # Exception block to handle the exceptions
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver

        return details

    def get_product_links_outfitters(self,url): # Function to get the product links
        '''
        This function is used to get the product links
        '''
        links=[]        # List to store the links
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.get(url)    # Getting the url
            driver.maximize_window()    # Maximizing the window
            ## record the current document height
            last_height = driver.execute_script("return document.body.scrollHeight")    # Getting the document height
            while True:    # Loop to scroll the page
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scrolling the page
                time.sleep(5)   # Waiting for 5 seconds
                # get all the a tags with class name product-link-main
                products=driver.find_elements(By.XPATH,"//a[@class='product-link-main']")   # Getting all the products
                for product in products:    # Loop to get the links
                    links.append(product.get_attribute("href"))   # Appending the link to the links list
                new_height = driver.execute_script("return document.body.scrollHeight")     # Getting the document height
                if new_height == last_height:       # Checking if the document height is changed
                    break   # Break the loop if the document height is not changed
                last_height = new_height    # Assigning the new document height to the last height
            links=list(set(links))  # Removing the duplicates from the links list
            print('Total links:',len(links))    # Printing the total links
            # print(links)

            ## close the browser
            driver.close()  # Closing the driver
        except Exception as e:
            print(e)    # Printing the exception
            driver.close()      # Closing the driver
        return links    # Returning the links list


    def get_product_details_outfitters(self,links,type):    
        '''
        This function is used to get the product details from outfitters
        '''

        details=[]  # List to store the details
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.maximize_window()    # Maximizing the window
            print('Scraping the product details...')    # Printing the message
            for link in links:  # Loop to get the details
                driver.get(link)    # Getting the link
                time.sleep(5)   # Waiting for 5 seconds
                # get the product name using class name product__title
                try:
                    product_name=driver.find_element(By.CLASS_NAME,"product__title").text   # Getting the product name
                except:
                    product_name='Not Found'    # If the product name is not found then assigning 'Not Found' to the product name
                # get the product sku using class name pro-sku  
                try:
                    product_sku=driver.find_element(By.CLASS_NAME,"pro-sku").text   # Getting the product sku
                except:
                    product_sku='Not Found' # If the product sku is not found then assigning 'Not Found' to the product sku
                # get the product price using class name price-item
                try:
                    product_price=driver.find_element(By.CLASS_NAME,"price-item").text  # Getting the product price
                except:
                    product_price='Not Found'   # If the product price is not found then assigning 'Not Found' to the product price
                # get the product color using lables in class name color-wrapper
                try:
                    product_color=driver.find_element(By.CLASS_NAME,"color-wrapper")    # Getting the product color
                    product_color=product_color.find_elements(By.TAG_NAME,"label")  # Getting the product color
                    product_color=[color.get_attribute("title") for color in product_color]   # Getting the product color
                    product_color=','.join(product_color)   # Joining the product color with comma
                except:
                    product_color='Not Found'   # If the product color is not found then assigning 'Not Found' to the product color
                # get the product size using input tags in class name size-wrapper
                try:
                    product_size=driver.find_element(By.CLASS_NAME,"size-wrapper")  # Getting the product size
                    product_size=product_size.find_elements(By.TAG_NAME,"input")    # Getting the product size
                    product_size=[size.get_attribute("value") for size in product_size]  # Getting the product size
                    product_size=','.join(product_size) # Joining the product size with comma
                except:
                    product_size='Not Found'        # If the product size is not found then assigning 'Not Found' to the product size
                # get the product gender using class gender-wrapper
                try:
                    gender=driver.find_element(By.CLASS_NAME,'gender-wrapper').text # Getting Gender
                except: 
                    gender='Not Found'  # If the product
                # get the product description using class name product__description
                try:
                    product_description=driver.find_element(By.CLASS_NAME,"product__description").text  # Getting the product description
                except:
                    product_description='Not Found' # If the product description is not found then assigning 'Not Found' to the product description
                # get the all img tags with class name zoomImg
                imgs=[]
                try:
                    img=driver.find_elements(By.CLASS_NAME,"zoomImg")   # Getting the product images
                    for i in img:
                        imgs.append(i.get_attribute("src")) # Appending the product images to the imgs list
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
                product_data={  # Creating the dictionary to store the details
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
                details.append(product_data)    # Appending the dictionary to the details list

            ## close the browser

            driver.close()
        except Exception as e:
            print(e)    # Printing the exception
            driver.close()    # Closing the driver

        return details


    def get_product_links_royaltag(self,url):
        links=[]    # List to store the links
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.get(url) # Getting the url
            time.sleep(5)   # Waiting for 5 seconds
            prev_height=driver.execute_script("return document.body.scrollHeight")  # Getting the previous height
            while True:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling the page    
                time.sleep(5)   # Waiting for 5 seconds
                products_section=driver.find_element(By.XPATH,'//*[@id="shopify-section-collection-template-no-sidebar"]/div/div[2]')   # Getting the products section
                # get all the anchor tags
                products=products_section.find_elements(By.TAG_NAME,"a")    # Getting the anchor tags
                for product in products:    # Iterating through the anchor tags
                    link=product.get_attribute("href")      # Getting the href attribute
                    if 'page' in link or 'contact' in link: # If the link is not a product link then
                        continue    # Continue
                    links.append(link)  # Appending the link to the links list
                links=list(set(links))  # Removing the duplicates
                print(f"Status: {len(links)} links found")  # Printing the status

                new_height=driver.execute_script("return document.body.scrollHeight")   # Getting the new height
                if new_height==prev_height: # If the new height is equal to the previous height then
                    break   # Break
                prev_height=new_height  # Assigning the new height to the previous height

            driver.quit()   # Quitting the driver
            links=list(set(links))  # Removing the duplicates
            return links
        except Exception as e:  # If any exception occurs
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver
            return links    # Returning the links


    def get_product_details_royaltag(self,links,type,gender):
        '''
        This function is used to get the product details from Royaltag
        '''
        details=[]  # List to store the details
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            for link in links:      # Iterating through the links
                driver.get(link)    # Getting the link
                time.sleep(5)       # Waiting for 5 seconds
                try:
                    product_title=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[2]/h1').text  # Getting the product title
                except:
                    product_title='No title'    # If the product title is not found then assigning 'No title' to the product title
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[2]/div[3]/span[2]').text  # Getting the product price
                except:
                    try:
                        product_price=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[2]/div[3]/span').text # Getting the product price
                    except: 
                        product_price='No price'    # If the product price is not found then assigning 'No price' to the product price

                try:
                    product_sku=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[2]/div[2]/div[2]/span').text    # Getting the product sku
                except:
                    product_sku='No sku'        # If the product sku is not found then assigning 'No sku' to the product sku

                try:
                    product_description=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[2]/div[4]').text    # Getting the product description
                except:
                    product_description='No description'    # If the product description is not found then assigning 'No description' to the product description

                try:
                    swatches=driver.find_element(By.XPATH,'//*[@id="product-variants"]/div[3]')   # Getting the swatches
                    # get all the div tags inside swatches
                    swatches=swatches.find_elements(By.TAG_NAME,'div')  # Getting the div tags
                    sizes=[]    # List to store the sizes
                    for swatch in swatches:
                        try:
                            # get the data-availability attribute of li tag
                            value=swatch.get_attribute('data-value')    
                            if value:
                                # append size to sizes list
                                sizes.append(value)
                        except:
                            continue
                    sizes=','.join(sizes)   # Joining the sizes with comma
                        
                except:
                    sizes='No sizes'    # If the sizes are not found then assigning 'No sizes' to the sizes
                colors='Not available'  # Assigning 'Not available' to the colors

                try:
                    images=[]   # List to store the images
                    # get all div tags with id='smallGallery'
                    slider=driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-grouped"]/div/div[1]/div[1]/div/div[2]/div/div')  
                    # get all the img tags inside slider
                    img=slider.find_elements(By.TAG_NAME,'img')
                    # get src attribute of img
                    for i in img:   # Iterating through the img tags
                        src=i.get_attribute('src')
                        # get first image from srcset attribute
                        src=src.split(' ')[0]   # Splitting the src attribute with space
                        src=src.split('.jpg')[0]    # Splitting the src attribute with .jpg
                        src=src.split('_')  # Splitting the src attribute with _
                        src='_'.join(src[:-1])+'.jpg'   # Joining the src attribute with _
                        # append image to images list
                        images.append(src)  # Appending the src to the images list
                    images=list(set(images))        # Removing the duplicates
                    images=', '.join(images)    # Joining the images with comma
                except:
                    images='No images'  # If the images are not found then assigning 'No images' to the images

                data={  # Dictionary to store the data
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
                print(data)    # Printing the data
                details.append(data)    # Appending the data to the details list
            driver.quit()   # Quitting the driver
            # save data to csv file
            df=pd.DataFrame(details)    # Creating the dataframe
            df.to_csv('products.csv',index=False)   # Saving the dataframe to csv file


        except Exception as e:  # If any exception occurs then printing the exception
            print(e)            # Printing the exception
            driver.quit()    # Quitting the driver

        return details  # Returning the details


    def get_product_links_breakout(self,url):
        '''
        This function is used to get the product links from the given url
        '''
        links=[]        # List to store the links
        try:    # Try block to handle the exceptions
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            driver.get(url)    # Getting the url    
            time.sleep(5)   # Waiting for 5 seconds 
            prev_height=driver.execute_script("return document.body.scrollHeight")  # Getting the previous height
            while True:    # Infinite loop
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # Scrolling to the bottom of the page
                time.sleep(5)   # Waiting for 5 seconds
                products_section=driver.find_element(By.XPATH,'//*[@id="pt-pageContent"]/div[1]/div/div/div')       # Getting the products section
                # get all the anchor tags
                products=products_section.find_elements(By.TAG_NAME,"a")    # Getting the anchor tags
                for product in products:    # Iterating through the products
                    link=product.get_attribute("href")  # Getting the href attribute of the product
                    if 'page' in link or 'contact' in link:  # If the link is not a product link then continue
                        continue
                    links.append(link)  # Appending the link to the links list
                links=list(set(links))  # Removing the duplicates
                print(f"Status: {len(links)} links found")  # Printing the status

                new_height=driver.execute_script("return document.body.scrollHeight")   # Getting the new height
                if new_height==prev_height: # If the new height is equal to the previous height then break
                    break   # Breaking the loop
                prev_height=new_height  # Assigning the new height to the previous height

            driver.quit()   # Quitting the driver
            links=list(set(links))  # Removing the duplicates
            return links    # Returning the links
        except Exception as e:  # If any exception occurs then printing the exception
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver
            return links    # Returning the links


    def get_product_details_breakout(self,links,type,gender):
        '''
        This function is used to get the product details from the given links
        '''
        details=[]      # List to store the details
        try:
            driver=webdriver.Chrome(ChromeDriverManager().install(),options=options)    # Creating the driver
            for link in links:  # Iterating through the links
                driver.get(link)        # Getting the link
                time.sleep(5)   # Waiting for 5 seconds
                try:
                    product_title=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/h1').text # Getting the product title
                except:
                    product_title='No title'    # If the product title is not found then assigning 'No title' to the product title
                try:
                    product_price=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[2]/div/span[2]').text # Getting the product price
                except: 
                    try:
                        product_price=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[2]/div/span[2]').text # Getting the product price
                    except:
                        product_price='No price'    # If the product price is not found then assigning 'No price' to the product price

                try:
                    product_sku=driver.find_element(By.XPATH,'//*[@id="sku"]/div/ul/li[1]/span[2]').text    # Getting the product sku
                except:
                    product_sku='No sku'    # If the product sku is not found then assigning 'No sku' to the product sku

                try:
                    product_description=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[5]/span[2]').text   # Getting the product description
                except:
                    product_description='No description'    # If the product description is not found then assigning 'No description' to the product description

                try:
                    swatches=driver.find_element(By.XPATH,'//*[@id="shopify-section-product-template"]/div/div[2]/div/div[2]/div/div[3]/div[1]/ul') # Getting the swatches
                    # get all the li tags 
                    swatches=swatches.find_elements(By.TAG_NAME,'li')   # Getting the li tags
                    sizes=[]    # List to store the sizes
                    for swatch in swatches:    # Iterating through the swatches
                        try:    # Try block to handle the exceptions
                            # get the data-availability attribute of li tag
                            availability=swatch.get_attribute('data-availability')  # Getting the data-availability attribute
                            if availability:    # If the data-availability attribute is not None then
                                continue
                            else:
                                # get the text of li tag
                                size=swatch.text    # Getting the text of the li tag
                                # append size to sizes list
                                sizes.append(size)      # Appending the size to the sizes list
                        except:
                            continue
                    sizes=','.join(sizes)   # Joining the sizes list with comma
                        
                except:
                    sizes='No sizes'        # If the sizes are not found then assigning 'No sizes' to the sizes
                colors='Not available'  # Assigning 'Not available' to the colors

                try:
                    images=[]   # List to store the images
                    # get all div tags with id='smallGallery'
                    slider=driver.find_element(By.XPATH,'//*[@id="smallGallery"]/div/div')  # Getting the div tag with id='smallGallery'
                    # get all the img tags inside slider
                    img=slider.find_elements(By.TAG_NAME,'img') # Getting the img tags
                    # get src attribute of img
                    for i in img:   
                        src=i.get_attribute('src')
                        # get first image from srcset attribute
                        src=src.split(' ')[0]   # Splitting the src with space
                        src=src.split('.jpg')[0]    # Splitting the src with '.jpg'
                        src=src.split('_')  # Splitting the src with '_'
                        src='_'.join(src[:-1])+'.jpg'       # Joining the src with '_'
                        # append image to images list
                        images.append(src)  # Appending the src to the images list
                    images=list(set(images))    # Removing the duplicates
                    images=', '.join(images)    # Joining the images list with comma
                except:
                    images='No images'  # If the images are not found then assigning 'No images' to the images

                data={  # Dictionary to store the data
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
                print(data)    # Printing the data
                details.append(data)    # Appending the data to the details list
            driver.quit()   # Quitting the driver
            # save data to csv file
            df=pd.DataFrame(details)    # Creating the dataframe
            df.to_csv('products.csv',index=False)   # Saving the dataframe to csv file


        except Exception as e:  # If any exception occurs then printing the exception
            print(e)    # Printing the exception
            driver.quit()   # Quitting the driver

        return details  # Returning the details

