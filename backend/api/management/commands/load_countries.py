from django.core.management.base import BaseCommand
from api.models import Country, City
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        countries_df = pd.read_csv('data/country.csv')

        replacements = {
            "Côte d’Ivoire": "Côte_d%27Ivoire",
            "Congo - Brazzaville": "Republic_of_the_Congo",
            "Congo - Kinshasa": "Democratic_Republic_of_the_Congo",
            "Heard & McDonald Islands": "Heard_Island_and_McDonald_Islands",
            "Hong Kong SAR China": "Hong_Kong",
            "Macao SAR China": "Macau",
            "Myanmar (Burma)": "Myanmar",
            "South Georgia & South Sandwich Islands": "South_Georgia_and_the_South_Sandwich_Islands",
            "Timor-Leste": "East_Timor",
        }

        
        countries_df['value'] = countries_df['value'].str.replace('St.', 'Saint')

        for old, new in replacements.items():
            countries_df['value'] = countries_df["value"].replace(old, new)

        countries_df['value'] = countries_df['value'].str.replace(' ', '_').str.replace('&', 'and').str.replace('"', '')
        countries_df['value'] = countries_df['value'].apply(lambda x: f'"{x}"')


        for country in countries_df['value']:
            if not Country.objects.filter(name=country).exists():
                country = (country.replace('"', ""))
                #self.scrape_country_info2(country)
                print(country)




    def scrape_country_info2(self, country):
        level7 = None
        cityExists = True
        driver = webdriver.Edge()
        driver.get(f"https://en.wikivoyage.org/wiki/{country}")
        driver.implicitly_wait(2)
        
        try:
            content = driver.find_element(By.ID, "Villages")
            print(content.get_attribute("innerHTML"))
        except:
            cityExists = False

        if (cityExists):
            try:
                ancestor_element = content.find_element(By.XPATH, "./following::div")
                ul = content.find_element(By.XPATH, "./following::ul")
            except NoSuchElementException:
                print("nothing")
            
                


            """ if (cityExists):
            try:
                ancestor_element = content.find_element(By.XPATH, "./ancestor::h2")
                ancestor_div = ancestor_element.find_element(By.XPATH, "parent::div")
                ul = ancestor_div.find_element(By.TAG_NAME, "ul")
            except NoSuchElementException:
                ancestor_element = content.find_element(By.XPATH, "parent::div")
                ancestor_div = ancestor_element.find_element(By.XPATH, "parent::div")
                ul = ancestor_div.find_element(By.TAG_NAME, "ul") """


            #print(ancestor_element.get_attribute("outerHTML"))
            #print(ancestor_div.get_attribute("outerHTML"))


            print(ul.get_attribute("outerHTML"))
            try:
                level7 = ul.find_elements(By.TAG_NAME, "li")
                sub = level7[0].find_element(By.CSS_SELECTOR, ".fn.org.listing-name")
                print(f"Element found: {sub.get_attribute('outerHTML')}")
            except NoSuchElementException:
                level7 = None
                print("No list found")


            if (level7):
                country_obj = Country.objects.create(
                    name=json.dumps(country, ensure_ascii=False)
                )

                for sublevel7 in level7:
                    result = sublevel7.find_element(By.CSS_SELECTOR, ".fn.org.listing-name")
                    result = result.text
                    print(result)
                    City.objects.create(
                        name=json.dumps(result, ensure_ascii=False),
                        name_type="Village",
                        country = country_obj)
        else:
            print("No city found")