from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
#browser = webdriver.Chrome("D:/Area de Trabalho/whitehatjr/Pro Versão 2 - Python/c127")
#browser.get(START_URL)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(START_URL)


time.sleep(10)


planets_data = []



headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Defina o dataframe do pandas
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Converta para CSV
#para adicionar a primeira coluna com os numeros de serie o atributo index com a eitqueta id
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
