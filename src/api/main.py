import wget
import zipfile
import pandas as pd
import os
from os import remove
import os.path as path

# ---- Borrar archivo CSV original filtrado - por si no se reescribe
if path.exists("covidFiltradoOaxaca.csv"):
    remove("covidFiltradoOaxaca.csv")

# ---- Descarga del archivo 
url = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
wget.download(url, 'covidOaxaca.zip')

# ---- Descomprimir el archivo 
ruta_zip = "covidOaxaca.zip" #ruta del archivo
ruta_extraccion = os.getcwd() #ruta de extracción
archivo_zip = zipfile.ZipFile(ruta_zip, "r")
password=None
try:
    print(archivo_zip.namelist())
    archivo_zip.extractall(pwd=password, path=ruta_extraccion)
except ValueError as error:
    print("error",error)
f=str(archivo_zip.namelist()).strip('[]')
file= f[1:len(f)-1]

# ------------------- leer datos del archivo csv --------------------------------
# Leer archivo csv original
datos=pd.read_csv(file, header=0,encoding= 'unicode_escape')

# Ordenar datos por Estado
datos.set_index('ENTIDAD_RES', inplace=True)
# Filtrar datos, Oaxaca=20
df=datos.loc[20]
#print(df)

# Guardar datos en CSV filtrados x Municipio
df.reset_index().to_csv('covidFiltradoOaxaca.csv', header=True, index=False)


# ----- Eliminar archivos residuales

if path.exists(file):
    remove(file)

if path.exists("covidOaxaca.zip"):
    remove("covidOaxaca.zip")
