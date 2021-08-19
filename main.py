from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


#Get into the page!!!!!!!!!!

driver = webdriver.Chrome(executable_path="E:\\Datos\\Escritorio\\Proyectos\\Proyectos2021\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.cbti-bkvt.org/en/directory")
sleep(1)


#Scrolling down untill the end!!!!!!!!!

for i in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

#Creating an array with all the profiles!!!!!!!!

container = driver.find_element_by_id("main-and-sidebar").find_element_by_css_selector("div.container")
container = container.find_element_by_css_selector("div.row").find_element_by_css_selector("div.col-md-9").find_element_by_css_selector("div.translators")
links=[]

for item in container.find_elements_by_css_selector("div.infinite"):
    for link in item.find_elements_by_css_selector("div.team-member-wrap"):
        url = link.find_element_by_tag_name("a").get_attribute("href")
        links.append(url)
        print(url)

print(len(links))



#Extracting info from each link !!!!!!!!!!!!!




lista = []

for link in links:
    diccionario = {
        "nombre": "-",
        "mail": "-"
    }
    driver.get(link)
    sleep(1.15)
    name = driver.find_element_by_css_selector("div.col-sm-6").text.split("\n")[0]
    email = driver.find_element_by_id("collapse-1").find_element_by_tag_name("a").get_attribute("href")
    email = email.split(":")[1]
    print(name)
    print(email)
    diccionario["nombre"] = name
    diccionario["mail"] = email
    print(diccionario)
    lista.append(diccionario)

print(lista)

dataFrame = pd.DataFrame(lista)
dataFrame.to_excel("outputposta.xlsx")













