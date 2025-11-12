# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

print("=== ANÁLISIS DE DATOS DE VENTAS ===")
print("Procesando datos, por favor espera...\n")

# Definir la ruta de la carpeta de base de datos
ruta_base = 'Base de datos'

# Crear carpeta de resultados si no existe
ruta_resultados = 'resultados'
if not os.path.exists(ruta_resultados):
    os.makedirs(ruta_resultados)

# ============================================================
# 1. LIMPIEZA DE TABLA: CLIENTE
# ============================================================

# Leer el archivo Excel
clientes = pd.read_excel(os.path.join(ruta_base, 'Clientes.xlsx'))
filas_originales_clientes = len(clientes)

# Convertir todo a texto, excepto las fechas
for col in clientes.columns:
    if 'fecha' in col.lower() or 'date' in col.lower():
        clientes[col] = pd.to_datetime(clientes[col], errors='coerce')
    else:
        clientes[col] = clientes[col].astype(str)

# Ordenar por fecha (más reciente primero)
fecha_cols = [col for col in clientes.columns if 'fecha' in col.lower() or 'date' in col.lower()]
if fecha_cols:
    clientes = clientes.sort_values(by=fecha_cols[0], ascending=False)

# Eliminar duplicados (conservar los más nuevos = primeros después de ordenar)
clientes = clientes.drop_duplicates(keep='first')

# Limpiar emails que contengan "2" en el medio del nombre
# Ejemplo: agustina.martinez2@mail.com -> agustina.martinez@mail.com
email_cols = [col for col in clientes.columns if 'email' in col.lower() or 'correo' in col.lower() or 'mail' in col.lower()]
emails_corregidos = 0
for email_col in email_cols:
    # Contar emails con "2" antes de limpiar
    emails_con_2 = clientes[email_col].str.contains('2', na=False).sum()
    # Eliminar el "2" de los emails
    clientes[email_col] = clientes[email_col].str.replace('2', '', regex=False)
    emails_corregidos += emails_con_2

filas_eliminadas_clientes = filas_originales_clientes - len(clientes)

# Guardar tabla limpia en formato Excel
clientes.to_excel(os.path.join(ruta_resultados, 'cliente_limpio.xlsx'), index=False, engine='openpyxl')


# ============================================================
# 2. LIMPIEZA DE TABLA: PRODUCTOS
# ============================================================

# Leer el archivo Excel
productos = pd.read_excel(os.path.join(ruta_base, 'Productos.xlsx'))
filas_originales_productos = len(productos)

# Convertir a los tipos correctos
for col in productos.columns:
    # Si es una columna numérica (precio, costo, cantidad, etc.)
    if any(palabra in col.lower() for palabra in ['precio', 'costo', 'cantidad', 'price', 'cost']):
        productos[col] = pd.to_numeric(productos[col], errors='coerce')
    # Si es una columna de ID numérico
    elif 'id' in col.lower():
        try:
            productos[col] = pd.to_numeric(productos[col], errors='coerce').astype('Int64')
        except:
            productos[col] = productos[col].astype(str)
    else:
        productos[col] = productos[col].astype(str)

# Eliminar filas con valores nulos en columnas importantes
productos = productos.dropna()

# Calcular BENEFICIO y MARGEN DE BENEFICIO
# Buscar las columnas de precio y costo (pueden tener nombres variados)
precio_col = [col for col in productos.columns if 'precio' in col.lower() or 'unitario' in col.lower()]
costo_col = [col for col in productos.columns if 'costo' in col.lower()]

if precio_col and costo_col:
    productos['beneficio'] = productos[precio_col[0]] - productos[costo_col[0]]
    productos['margen_de_beneficio'] = productos['beneficio'] / productos[costo_col[0]]
    campos_nuevos = True
else:
    campos_nuevos = False

filas_eliminadas_productos = filas_originales_productos - len(productos)

# Guardar tabla limpia en formato Excel
productos.to_excel(os.path.join(ruta_resultados, 'productos_limpio.xlsx'), index=False, engine='openpyxl')


# ============================================================
# 3. LIMPIEZA DE TABLA: VENTAS
# ============================================================

# Leer el archivo Excel
ventas = pd.read_excel(os.path.join(ruta_base, 'Ventas.xlsx'))
filas_originales_ventas = len(ventas)

# Convertir todo a texto, excepto las fechas
for col in ventas.columns:
    if 'fecha' in col.lower() or 'date' in col.lower():
        ventas[col] = pd.to_datetime(ventas[col], errors='coerce')
    else:
        ventas[col] = ventas[col].astype(str)

# Eliminar el número "2" de los correos electrónicos
email_cols = [col for col in ventas.columns if 'email' in col.lower() or 'correo' in col.lower() or 'mail' in col.lower()]
for email_col in email_cols:
    ventas[email_col] = ventas[email_col].str.replace('2', '', regex=False)

# Reemplazar IDs duplicados por el mismo email asociado
id_cols = [col for col in ventas.columns if 'id' in col.lower() and 'cliente' not in col.lower()]
if email_cols and id_cols:
    ventas[id_cols[0]] = ventas.groupby(email_cols[0])[id_cols[0]].transform('first')

# Ordenar por fecha o ID
fecha_cols = [col for col in ventas.columns if 'fecha' in col.lower() or 'date' in col.lower()]
if fecha_cols:
    ventas = ventas.sort_values(by=fecha_cols[0])
elif id_cols:
    ventas = ventas.sort_values(by=id_cols[0])


# Guardar tabla limpia en formato Excel
ventas.to_excel(os.path.join(ruta_resultados, 'ventas_limpio.xlsx'), index=False, engine='openpyxl')


# ============================================================
# 4. LIMPIEZA DE TABLA: DETALLE_VENTAS
# ============================================================

# Leer el archivo Excel
detalle_ventas = pd.read_excel(os.path.join(ruta_base, 'Detalle_ventas.xlsx'))
filas_originales_detalle = len(detalle_ventas)

# Convertir a los tipos correctos según el campo
for col in detalle_ventas.columns:
    if 'fecha' in col.lower() or 'date' in col.lower():
        detalle_ventas[col] = pd.to_datetime(detalle_ventas[col], errors='coerce')
    elif any(palabra in col.lower() for palabra in ['precio', 'importe', 'cantidad', 'total', 'costo']):
        # Limpiar símbolos y convertir a número
        if detalle_ventas[col].dtype == 'object':
            detalle_ventas[col] = detalle_ventas[col].astype(str).str.replace('[\$,]', '', regex=True)
        detalle_ventas[col] = pd.to_numeric(detalle_ventas[col], errors='coerce')
    elif 'id' in col.lower():
        try:
            detalle_ventas[col] = pd.to_numeric(detalle_ventas[col], errors='coerce').astype('Int64')
        except:
            detalle_ventas[col] = detalle_ventas[col].astype(str)
    else:
        detalle_ventas[col] = detalle_ventas[col].astype(str)


# Guardar tabla limpia en formato Excel
detalle_ventas.to_excel(os.path.join(ruta_resultados, 'detalle_ventas_limpio.xlsx'), index=False, engine='openpyxl')


# ============================================================
# 5. GENERACIÓN DE GRÁFICOS
# ============================================================

# --- GRÁFICO 1: Línea temporal de importes promedio ---
try:
    # Buscar columnas de ID de venta
    venta_id_col_detalle = [col for col in detalle_ventas.columns if 'venta' in col.lower() and 'id' in col.lower()]
    venta_id_col_ventas = [col for col in ventas.columns if 'id' in col.lower() and 'venta' in col.lower()]

    # Si no encuentra específico de venta, usa el primer ID
    if not venta_id_col_detalle:
        venta_id_col_detalle = [col for col in detalle_ventas.columns if 'id' in col.lower()]
    if not venta_id_col_ventas:
        venta_id_col_ventas = [col for col in ventas.columns if 'id' in col.lower()]

    # Buscar columna de importe
    importe_col = [col for col in detalle_ventas.columns if 'importe' in col.lower() or 'total' in col.lower() or 'monto' in col.lower()]

    # Buscar columna de fecha en ventas
    fecha_col_ventas = [col for col in ventas.columns if 'fecha' in col.lower() or 'date' in col.lower()]

    if venta_id_col_detalle and venta_id_col_ventas and importe_col and fecha_col_ventas:
        # Asegurar que ambas columnas ID tengan el mismo tipo
        detalle_ventas_temp = detalle_ventas.copy()
        ventas_temp = ventas.copy()
        detalle_ventas_temp[venta_id_col_detalle[0]] = detalle_ventas_temp[venta_id_col_detalle[0]].astype(str)
        ventas_temp[venta_id_col_ventas[0]] = ventas_temp[venta_id_col_ventas[0]].astype(str)

        # Combinar detalle_ventas con ventas
        detalle_con_fecha = detalle_ventas_temp.merge(
            ventas_temp[[venta_id_col_ventas[0], fecha_col_ventas[0]]],
            left_on=venta_id_col_detalle[0],
            right_on=venta_id_col_ventas[0],
            how='left'
        )

        # Extraer el día del mes
        detalle_con_fecha['dia'] = pd.to_datetime(detalle_con_fecha[fecha_col_ventas[0]]).dt.day

        # Calcular promedio de importe por día
        promedio_por_dia = detalle_con_fecha.groupby('dia')[importe_col[0]].mean()

        # Crear figura individual
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(promedio_por_dia.index, promedio_por_dia.values, marker='o', color='#2E86AB', linewidth=2, markersize=8)
        ax1.set_xlabel('Día del mes', fontsize=12)
        ax1.set_ylabel('Importe promedio ($)', fontsize=12)
        ax1.set_title('Importes promedio por día del mes', fontsize=14, fontweight='bold', pad=20)
        ax1.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(ruta_resultados, 'grafico_1_linea_temporal.png'), dpi=300, bbox_inches='tight')
        plt.close()
except Exception as e:
    pass


# --- GRÁFICO 2: Distribución de importes por categoría ---
try:
    # Buscar columnas necesarias
    producto_id_col_detalle = [col for col in detalle_ventas.columns if 'producto' in col.lower() and 'id' in col.lower()]
    producto_id_col_productos = [col for col in productos.columns if col.lower() == 'id_producto' or (col.lower() == 'id' and col not in ['id'])]
    if not producto_id_col_productos:
        producto_id_col_productos = [productos.columns[0]]  # Usar primera columna si no encuentra
    categoria_col = [col for col in productos.columns if 'categoria' in col.lower() or 'category' in col.lower()]

    if producto_id_col_detalle and producto_id_col_productos and categoria_col and importe_col:
        # Asegurar que ambas columnas ID tengan el mismo tipo
        detalle_ventas_temp = detalle_ventas.copy()
        productos_temp = productos.copy()
        detalle_ventas_temp[producto_id_col_detalle[0]] = detalle_ventas_temp[producto_id_col_detalle[0]].astype(str)
        productos_temp[producto_id_col_productos[0]] = productos_temp[producto_id_col_productos[0]].astype(str)

        # Combinar detalle_ventas con productos
        detalle_con_categoria = detalle_ventas_temp.merge(
            productos_temp[[producto_id_col_productos[0], categoria_col[0]]],
            left_on=producto_id_col_detalle[0],
            right_on=producto_id_col_productos[0],
            how='left'
        )

        # Sumar importes por categoría
        suma_por_categoria = detalle_con_categoria.groupby(categoria_col[0])[importe_col[0]].sum()

        # Colores personalizados
        colores = ['#A23B72', '#F18F01', '#C73E1D', '#6A994E', '#2E86AB', '#BC4B51']

        # Crear figura individual
        fig2, ax2 = plt.subplots(figsize=(10, 8))
        ax2.pie(suma_por_categoria.values, labels=suma_por_categoria.index,
               autopct='%1.1f%%', startangle=90, colors=colores, textprops={'fontsize': 11})
        ax2.set_title('Distribución de ventas por categoría', fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig(os.path.join(ruta_resultados, 'grafico_2_distribucion_categoria.png'), dpi=300, bbox_inches='tight')
        plt.close()
except Exception as e:
    pass


# --- GRÁFICO 3: Comparativa por producto ---
try:
    # Buscar columna de nombre de producto
    nombre_col = [col for col in productos.columns if 'nombre' in col.lower() or 'name' in col.lower()]
    # Si no hay columna de nombre, filtrar 'producto' que no sea 'id_producto'
    if not nombre_col:
        nombre_col = [col for col in productos.columns if 'producto' in col.lower() and 'id' not in col.lower()]

    if producto_id_col_detalle and producto_id_col_productos and nombre_col and importe_col:
        # Asegurar que ambas columnas ID tengan el mismo tipo
        detalle_ventas_temp = detalle_ventas.copy()
        productos_temp = productos[[producto_id_col_productos[0], nombre_col[0]]].copy()
        detalle_ventas_temp[producto_id_col_detalle[0]] = detalle_ventas_temp[producto_id_col_detalle[0]].astype(str)
        productos_temp[producto_id_col_productos[0]] = productos_temp[producto_id_col_productos[0]].astype(str)

        # Combinar detalle_ventas con productos usando suffixes para evitar duplicados
        detalle_con_producto = detalle_ventas_temp.merge(
            productos_temp,
            left_on=producto_id_col_detalle[0],
            right_on=producto_id_col_productos[0],
            how='left',
            suffixes=('', '_prod')
        )

        # Sumar importes por producto
        suma_por_producto = detalle_con_producto.groupby(nombre_col[0])[importe_col[0]].sum().sort_values()

        # Tomar los top 10 productos
        top_productos = suma_por_producto.tail(10)

        # Crear figura individual
        fig3, ax3 = plt.subplots(figsize=(10, 8))
        ax3.barh(range(len(top_productos)), top_productos.values, color='#6A994E')
        ax3.set_yticks(range(len(top_productos)))
        ax3.set_yticklabels(top_productos.index, fontsize=10)
        ax3.set_xlabel('Importe total ($)', fontsize=12)
        ax3.set_title('Top 10 productos por ventas', fontsize=14, fontweight='bold', pad=20)
        ax3.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(ruta_resultados, 'grafico_3_top_productos.png'), dpi=300, bbox_inches='tight')
        plt.close()
except Exception as e:
    pass


# ============================================================
# 6. RESUMEN DE RESULTADOS
# ============================================================
print("\n" + "="*50)
print("=== RESUMEN DE RESULTADOS ===")
print("="*50)

print(f"\n📁 Filas procesadas:")
print(f"  • Clientes: {len(clientes)}")
print(f"  • Productos: {len(productos)}")
print(f"  • Ventas: {len(ventas)}")
print(f"  • Detalle ventas: {len(detalle_ventas)}")

print(f"\n🔧 Limpieza realizada:")
print(f"  • Duplicados eliminados en clientes: {filas_eliminadas_clientes}")
print(f"  • Emails corregidos (sin '2'): {emails_corregidos}")
print(f"  • Productos con nulos eliminados: {filas_eliminadas_productos}")

if campos_nuevos:
    print(f"\n➕ Campos nuevos creados:")
    print(f"  • beneficio (en productos)")
    print(f"  • margen_de_beneficio (en productos)")

print(f"\n📊 Estadísticas importantes:")
if campos_nuevos:
    print(f"  • Beneficio promedio: ${productos['beneficio'].mean():.2f}")
    print(f"  • Margen de beneficio promedio: {productos['margen_de_beneficio'].mean():.1%}")

if importe_col:
    print(f"  • Importe total de ventas: ${detalle_ventas[importe_col[0]].sum():.2f}")
    print(f"  • Importe promedio por venta: ${detalle_ventas[importe_col[0]].mean():.2f}")

print(f"\n💾 Archivos generados en carpeta 'resultados/':")
print(f"  📊 Bases de datos limpias (Excel):")
print(f"     • cliente_limpio.xlsx (Limpio)")
print(f"     • productos_limpio.xlsx (Limpio)")
print(f"     • ventas_limpio.xlsx (Limpio)")
print(f"     • detalle_ventas_limpio.xlsx (Limpio)")
print(f"  📈 Gráficos (PNG):")
print(f"     • grafico_1_linea_temporal.png (Completo)")
print(f"     • grafico_2_distribucion_categoria.png (Completo)")
print(f"     • grafico_3_top_productos.png (Completo)")

print("\n" + "="*50)
print("✅ ¡Análisis completado exitosamente!")
print("="*50)
