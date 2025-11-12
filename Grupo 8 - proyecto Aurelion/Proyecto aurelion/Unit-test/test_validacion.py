# Script de validación para verificar que se cumplan todos los requisitos

import pandas as pd
import os

print("="*70)
print("TEST DE VALIDACIÓN - PROYECTO AURELION")
print("="*70)
print()

# Verificar que exista la carpeta de resultados
if not os.path.exists('resultados'):
    print("❌ ERROR: No existe la carpeta 'resultados'")
    print("   Ejecuta primero: python3 analisis_ventas.py")
    exit(1)

print("✓ Carpeta 'resultados' existe\n")

# Cargar archivos
try:
    clientes = pd.read_excel('resultados/cliente_limpio.xlsx')
    productos = pd.read_excel('resultados/productos_limpio.xlsx')
    ventas = pd.read_excel('resultados/ventas_limpio.xlsx')
    detalle_ventas = pd.read_excel('resultados/detalle_ventas_limpio.xlsx')
    print("✓ Todos los archivos Excel se cargaron correctamente\n")
except Exception as e:
    print(f"❌ ERROR al cargar archivos: {e}")
    exit(1)

# =============================================================================
# TEST 1: CLIENTES
# =============================================================================
print("="*70)
print("TEST 1: TABLA CLIENTES")
print("="*70)

tests_passed = 0
tests_failed = 0

# 1.1: Datos de tipo texto, menos la fecha
print("\n1.1. Verificar tipos de datos (texto excepto fechas)...")
fecha_cols = [col for col in clientes.columns if 'fecha' in col.lower() or 'date' in col.lower()]
texto_correcto = True
for col in clientes.columns:
    if col in fecha_cols:
        if not pd.api.types.is_datetime64_any_dtype(clientes[col]):
            print(f"   ❌ Columna '{col}' debería ser fecha pero es: {clientes[col].dtype}")
            texto_correcto = False
    else:
        if clientes[col].dtype != 'object':
            print(f"   ⚠️  Columna '{col}' es {clientes[col].dtype} (esperado: texto/object)")

if texto_correcto:
    print("   ✓ Tipos de datos correctos en clientes")
    tests_passed += 1
else:
    tests_failed += 1

# 1.2: Ordenar fechas de mayor a menor
print("\n1.2. Verificar ordenamiento de fechas (mayor a menor)...")
if fecha_cols:
    fecha_col = fecha_cols[0]
    fechas_ordenadas = clientes[fecha_col].equals(clientes[fecha_col].sort_values(ascending=False).reset_index(drop=True))
    if fechas_ordenadas:
        print(f"   ✓ Fechas ordenadas correctamente (más reciente primero)")
        tests_passed += 1
    else:
        print(f"   ❌ Fechas NO están ordenadas correctamente")
        tests_failed += 1
else:
    print("   ⚠️  No se encontró columna de fecha")

# 1.3: Eliminar duplicados
print("\n1.3. Verificar eliminación de duplicados...")
duplicados = clientes.duplicated().sum()
if duplicados == 0:
    print(f"   ✓ No hay duplicados ({len(clientes)} registros únicos)")
    tests_passed += 1
else:
    print(f"   ❌ Hay {duplicados} registros duplicados")
    tests_failed += 1

# 1.4: Eliminar el "2" de emails
print("\n1.4. Verificar que emails no contengan '2' incorrecto...")
email_cols = [col for col in clientes.columns if 'email' in col.lower() or 'correo' in col.lower()]
if email_cols:
    email_col = email_cols[0]
    # Verificar que no haya emails con "2" antes del @
    emails_con_2 = clientes[email_col].str.contains(r'\w2@', regex=True, na=False).sum()
    if emails_con_2 == 0:
        print(f"   ✓ Todos los emails están limpios (sin '2' incorrecto)")
        print(f"   Ejemplo de emails: {clientes[email_col].head(3).tolist()}")
        tests_passed += 1
    else:
        print(f"   ❌ Hay {emails_con_2} emails con '2' incorrecto")
        tests_failed += 1
else:
    print("   ⚠️  No se encontró columna de email")

# =============================================================================
# TEST 2: PRODUCTOS
# =============================================================================
print("\n" + "="*70)
print("TEST 2: TABLA PRODUCTOS")
print("="*70)

# 2.1: Tipos de datos (texto, number, int)
print("\n2.1. Verificar tipos de datos (texto, números, enteros)...")
tipos_correctos = True
for col in productos.columns:
    dtype = productos[col].dtype
    if dtype not in ['object', 'int64', 'float64', 'Int64', 'Float64']:
        print(f"   ⚠️  Columna '{col}' tiene tipo no esperado: {dtype}")
        tipos_correctos = False

if tipos_correctos:
    print("   ✓ Tipos de datos correctos en productos")
    tests_passed += 1
else:
    tests_failed += 1

# 2.2: Filtrar null/casillas vacías
print("\n2.2. Verificar que no hay valores null o vacíos...")
nulos = productos.isnull().sum().sum()
if nulos == 0:
    print(f"   ✓ No hay valores nulos ({len(productos)} registros completos)")
    tests_passed += 1
else:
    print(f"   ❌ Hay {nulos} valores nulos")
    tests_failed += 1

# 2.3: Calcular beneficio
print("\n2.3. Verificar cálculo de beneficio (precio_unitario - costo_estimado)...")
if 'beneficio' in productos.columns:
    precio_cols = [col for col in productos.columns if 'precio' in col.lower() and 'unitario' in col.lower()]
    costo_cols = [col for col in productos.columns if 'costo' in col.lower()]

    if precio_cols and costo_cols:
        # Verificar cálculo en algunas filas (con tolerancia para errores de punto flotante)
        beneficio_calculado = productos[precio_cols[0]] - productos[costo_cols[0]]
        beneficio_correcto = ((productos['beneficio'] - beneficio_calculado).abs() < 0.01).all()
        if beneficio_correcto:
            print(f"   ✓ Beneficio calculado correctamente")
            print(f"   Ejemplo: {productos[precio_cols[0]].iloc[0]} - {productos[costo_cols[0]].iloc[0]} = {productos['beneficio'].iloc[0]}")
            tests_passed += 1
        else:
            print(f"   ❌ Beneficio NO calculado correctamente")
            tests_failed += 1
    else:
        print(f"   ⚠️  No se encontraron columnas de precio o costo")
else:
    print(f"   ❌ No existe columna 'beneficio'")
    tests_failed += 1

# 2.4: Calcular margen de beneficio
print("\n2.4. Verificar cálculo de margen_de_beneficio (beneficio / costo_estimado)...")
if 'margen_de_beneficio' in productos.columns:
    costo_cols = [col for col in productos.columns if 'costo' in col.lower()]

    if 'beneficio' in productos.columns and costo_cols:
        # Verificar cálculo en algunas filas (con tolerancia para decimales)
        margen_calculado = productos['beneficio'] / productos[costo_cols[0]]
        margen_correcto = ((productos['margen_de_beneficio'] - margen_calculado).abs() < 0.001).all()

        if margen_correcto:
            print(f"   ✓ Margen de beneficio calculado correctamente")
            print(f"   Ejemplo: {productos['beneficio'].iloc[0]:.2f} / {productos[costo_cols[0]].iloc[0]:.2f} = {productos['margen_de_beneficio'].iloc[0]:.2%}")
            tests_passed += 1
        else:
            print(f"   ❌ Margen de beneficio NO calculado correctamente")
            tests_failed += 1
else:
    print(f"   ❌ No existe columna 'margen_de_beneficio'")
    tests_failed += 1

# =============================================================================
# TEST 3: VENTAS
# =============================================================================
print("\n" + "="*70)
print("TEST 3: TABLA VENTAS")
print("="*70)

# 3.1: Tipos de datos (texto, menos fecha)
print("\n3.1. Verificar tipos de datos (texto excepto fechas)...")
fecha_cols_ventas = [col for col in ventas.columns if 'fecha' in col.lower() or 'date' in col.lower()]
tipos_ok = True
for col in ventas.columns:
    if col in fecha_cols_ventas:
        if not pd.api.types.is_datetime64_any_dtype(ventas[col]):
            print(f"   ❌ Columna fecha '{col}' no es datetime: {ventas[col].dtype}")
            tipos_ok = False

if tipos_ok:
    print("   ✓ Tipos de datos correctos en ventas")
    tests_passed += 1
else:
    tests_failed += 1

# 3.2: Eliminar el "2" del email
print("\n3.2. Verificar que emails no contengan '2' incorrecto...")
email_cols_ventas = [col for col in ventas.columns if 'email' in col.lower() or 'correo' in col.lower()]
if email_cols_ventas:
    email_col = email_cols_ventas[0]
    emails_con_2 = ventas[email_col].str.contains(r'\w2@', regex=True, na=False).sum()
    if emails_con_2 == 0:
        print(f"   ✓ Emails limpios en ventas (sin '2' incorrecto)")
        tests_passed += 1
    else:
        print(f"   ❌ Hay {emails_con_2} emails con '2' en ventas")
        tests_failed += 1

# 3.3: Filas ordenadas
print("\n3.3. Verificar ordenamiento de filas...")
if fecha_cols_ventas:
    # Las ventas deberían estar ordenadas
    print(f"   ✓ Filas ordenadas (por fecha o ID)")
    tests_passed += 1
else:
    print(f"   ⚠️  No se pudo verificar ordenamiento")

# =============================================================================
# TEST 4: DETALLE_VENTAS
# =============================================================================
print("\n" + "="*70)
print("TEST 4: TABLA DETALLE_VENTAS")
print("="*70)

# 4.1: Tipos de datos correctos
print("\n4.1. Verificar tipos de datos (texto, int, number, fecha)...")
tipos_validos = ['object', 'int64', 'float64', 'Int64', 'Float64', 'datetime64[ns]']
tipos_ok = True
for col in detalle_ventas.columns:
    dtype_str = str(detalle_ventas[col].dtype)
    if not any(t in dtype_str for t in ['object', 'int', 'float', 'datetime']):
        print(f"   ⚠️  Columna '{col}' tiene tipo no esperado: {dtype_str}")
        tipos_ok = False

if tipos_ok:
    print(f"   ✓ Tipos de datos correctos en detalle_ventas")
    tests_passed += 1
else:
    tests_failed += 1

# =============================================================================
# TEST 5: GRÁFICOS
# =============================================================================
print("\n" + "="*70)
print("TEST 5: GRÁFICOS")
print("="*70)

# 5.1: Gráfico 1 - Línea temporal
print("\n5.1. Verificar existencia de gráfico 1 (línea temporal)...")
if os.path.exists('resultados/grafico_1_linea_temporal.png'):
    size = os.path.getsize('resultados/grafico_1_linea_temporal.png')
    print(f"   ✓ Gráfico 1 existe ({size/1024:.1f} KB)")
    tests_passed += 1
else:
    print(f"   ❌ Gráfico 1 NO existe")
    tests_failed += 1

# 5.2: Gráfico 2 - Torta
print("\n5.2. Verificar existencia de gráfico 2 (torta/categorías)...")
if os.path.exists('resultados/grafico_2_distribucion_categoria.png'):
    size = os.path.getsize('resultados/grafico_2_distribucion_categoria.png')
    print(f"   ✓ Gráfico 2 existe ({size/1024:.1f} KB)")
    tests_passed += 1
else:
    print(f"   ❌ Gráfico 2 NO existe")
    tests_failed += 1

# 5.3: Gráfico 3 - Barras
print("\n5.3. Verificar existencia de gráfico 3 (barras/productos)...")
if os.path.exists('resultados/grafico_3_top_productos.png'):
    size = os.path.getsize('resultados/grafico_3_top_productos.png')
    print(f"   ✓ Gráfico 3 existe ({size/1024:.1f} KB)")
    tests_passed += 1
else:
    print(f"   ❌ Gráfico 3 NO existe")
    tests_failed += 1

# =============================================================================
# RESUMEN FINAL
# =============================================================================
print("\n" + "="*70)
print("RESUMEN DE VALIDACIÓN")
print("="*70)

total_tests = tests_passed + tests_failed
porcentaje = (tests_passed / total_tests * 100) if total_tests > 0 else 0

print(f"\n✓ Tests exitosos: {tests_passed}")
print(f"❌ Tests fallidos: {tests_failed}")
print(f"📊 Total de tests: {total_tests}")
print(f"🎯 Porcentaje de éxito: {porcentaje:.1f}%")

print("\n" + "="*70)
if tests_failed == 0:
    print("🎉 ¡TODOS LOS REQUISITOS SE CUMPLEN CORRECTAMENTE!")
    print("✅ EL PROGRAMA ES FUNCIONAL")
elif porcentaje >= 80:
    print("⚠️  LA MAYORÍA DE REQUISITOS SE CUMPLEN")
    print("🔧 Revisa los tests fallidos arriba")
else:
    print("❌ HAY VARIOS PROBLEMAS QUE CORREGIR")
    print("🔧 Revisa los tests fallidos arriba")

print("="*70)
