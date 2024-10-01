import sys
import os

# 1.Verificar si el usuario proporcionó un directorio
if len(sys.argv) < 2:
    print("Uso: python script.py <directorio>")
    sys.exit(1)

directorio = sys.argv[1]  # Obtener el directorio de la línea de comandos

# Verificar que el directorio existe
if not os.path.isdir(directorio):
    print(f"Error: El directorio {directorio} no existe.")
    sys.exit(1)

# 2.Buscar archivos .txt en el directorio
archivosTxt = [f for f in os.listdir(directorio) if f.endswith('.txt')]

# Si no hay archivos .txt, mostrar mensaje y salir
if not archivosTxt:
    informePath = os.path.join(directorio, 'informe.txt')
    informe = open(informePath, 'w')
    informe.write("No se encontraron archivos de texto.\n")
    print("No se encontraron archivos de texto.")
    sys.exit(0)

# Crear lista para almacenar los resultados del análisis
resumen = []

# Analizar cada archivo .txt
for archivo in archivosTxt:
    rutaArchivo = os.path.join(directorio, archivo)
    try:
        f = open(rutaArchivo, 'r')
        contenido = f.readlines()  # Leer todas las líneas del archivo
        numLineas = len(contenido)  # Contar el número de líneas
        palabras = ' '.join(contenido).split()  # Obtener todas las palabras
        numPalabras = len(palabras)  # Contar el número de palabras
        numPython = sum(1 for palabra in palabras if palabra.lower() == "python")  # Contar "Python"

        # Agregar el resultado a la lista resumen
        resumen.append({
            'archivo': archivo,
            'lineas': numLineas,
            'palabras': numPalabras,
            'python': numPython
            })
    except PermissionError:
        print(f"No tienes permiso para leer {archivo}.")
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error desconocido en {archivo}: {e}")

# 3.Generar el informe en informe.txt
informePath = os.path.join(directorio, 'informe.txt')
infrome = open(informePath, 'w')
for datos in resumen:
    informe.write(f"Archivo: {datos['archivo']}\n")
    informe.write(f"Número de líneas: {datos['lineas']}\n")
    informe.write(f"Número de palabras: {datos['palabras']}\n")
    informe.write(f"Veces que aparece 'Python': {datos['python']}\n\n")

print(f"Informe generado en {informePath}")
