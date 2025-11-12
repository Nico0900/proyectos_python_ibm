#!/usr/bin/env python3
"""
Script simple para verificar que todo funciona correctamente
"""

import os
import sys

print("="*70)
print("VERIFICACIÓN DEL PROYECTO AURELION")
print("="*70)
print()

# Verificar Python
print("✓ Python está funcionando")
print(f"  Versión: {sys.version}")
print()

# Verificar librerías
print("Verificando librerías...")
try:
    import pandas as pd
    print("  ✓ pandas instalado")
except ImportError:
    print("  ❌ pandas NO instalado")
    print("     Instala con: pip3 install pandas")

try:
    import matplotlib.pyplot as plt
    print("  ✓ matplotlib instalado")
except ImportError:
    print("  ❌ matplotlib NO instalado")
    print("     Instala con: pip3 install matplotlib")

try:
    import openpyxl
    print("  ✓ openpyxl instalado")
except ImportError:
    print("  ❌ openpyxl NO instalado")
    print("     Instala con: pip3 install openpyxl")

print()

# Verificar archivos originales
print("Verificando archivos originales...")
archivos_necesarios = [
    'Base de datos/Clientes.xlsx',
    'Base de datos/Productos.xlsx',
    'Base de datos/Ventas.xlsx',
    'Base de datos/Detalle_ventas.xlsx'
]

for archivo in archivos_necesarios:
    if os.path.exists(archivo):
        print(f"  ✓ {archivo}")
    else:
        print(f"  ❌ {archivo} NO EXISTE")

print()

# Verificar carpeta de resultados
print("Verificando carpeta 'resultados'...")
if os.path.exists('resultados'):
    print("  ✓ Carpeta 'resultados' existe")
    archivos = os.listdir('resultados')
    print(f"  ✓ Contiene {len(archivos)} archivos:")
    for archivo in sorted(archivos):
        size = os.path.getsize(os.path.join('resultados', archivo))
        print(f"     • {archivo} ({size/1024:.1f} KB)")
else:
    print("  ⚠️  Carpeta 'resultados' NO existe")
    print("     Ejecuta primero: python3 analisis_ventas.py")

print()
print("="*70)
print("Para ejecutar el análisis:")
print("  python3 analisis_ventas.py")
print("="*70)
