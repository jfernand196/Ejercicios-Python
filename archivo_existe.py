## Comprobar si un archivo existe

import pathlib
import os

print(pathlib.Path(__file__).parent.absolute())
nombre_archivo = "prueba.py"
print(os.path.isfile(nombre_archivo))