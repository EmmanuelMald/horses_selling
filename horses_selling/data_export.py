from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

datos = {
    "Especie": ['juanito'],
#    "Raza": [respuestas[1]],
#    "Color": [respuestas[2]],
#    "Ojos": [respuestas[3]],
#    "Detalle extra": [respuestas[4]],
}

# Configure the WebDriver
wdriver = webdriver.Edge()

# Navigate to the forms page
wdriver.get('https://forms.monday.com/forms/893878d1a5de56ac58c4d5a4c17d8ccd?r=euc1')

# Fill species
f_especie = wdriver.find_element(By.NAME, 'form-input input_7ec7dfffa8') 
f_especie.send_keys(datos['Especie'])

f_especie.send_keys(Keys.RETURN)


"""
for i in datosssss

# Fill race
f_race = wdriver.find_element(By.NAME, 'Raza') 
f_race.send_keys(datos['Raza'])

# Fill color
f_color = wdriver.find_element(By.NAME, 'Color') 
f_color.send_keys(datos['Color'])

# Fill eyes
f_eyes = wdriver.find_element(By.NAME, 'Ojos') 
f_eyes.send_keys(datos['Ojos'])

# Fill extra details
f_detail = wdriver.find_element(By.NAME, 'Detalle extra') 
f_detail.send_keys(datos['Detalle extra'])
"""
