from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://techwithtim.net/") #Sitio web al que quiero acceder
search = driver.find_element_by_name("s") #el elemento "s" es la barra de busqueda 
search.send_keys("test") #busco "test" en google
search.send_keys(Keys.RETURN) #accion de presionar la tecla enter para buscar
#print(driver.page_source)
#main = driver.find_element_by_id("rcnt")

#las siguientres lineas sirven para que el driver espere a que exixstan elementos que extraer luego de realizar la busqueda, 
#si no se implementan es posible que la extraccion se ejecute antes de que hayan elementos obteniendose una lista vacia
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")    
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()

