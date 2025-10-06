# Título del Proyecto
Proyecto Aurelion

## 1. Tema
Análisis del comportamiento de ventas y clientes de la Tienda Arurelión mediante el procesamiento de datos transaccionales para identificar patrones de compra, productos más rentables y segmentación de clientes.

## 2. Problema
La tienda carece de información consolidada sobre el rendimiento comercial, no identifica claramente a sus clientes más valiosos, desconoce las tendencias de ventas por temporada y no tiene visibilidad sobre qué productos o categorías generan mayor rentabilidad, lo que dificulta la toma de decisiones estratégicas.

## 3. Solución
Desarrollo de un script en Python que consolida las tablas de clientes, ventas, detalle_ventas y productos para generar métricas clave como: evolución mensual de ingresos, top 10 clientes por gasto, productos más vendidos por categoría y preferencias de medios de pago.

## 4. Bases de datos

    **Tabla: Clientes**
        Estructura: Estructurada
        Registros: 100
        Campos: 5

        Campo: id_cliente (Primary key)
        Tipo: Entero (int)
        Escala: Nominal
        
        Campo: nombre_cliente
        Tipo: Texto (str)
        Escala: Nominal

        Campo: email
        Tipo: Texto (str)
        Escala: Nominal

        Campo: ciudad
        Tipo: Texto (str)
        Escala: Nominal

        Campo: fecha_alta
        Tipo: Fecha (date/timelap)
        Escala: Intervalo

    ###########################################################################

    **Tabla: Ventas**
        Estructura: Estructurada
        Registros: 120
        Campos: 6

        Campo: id_venta (Primary key)
        Tipo: Entero (int)
        Escala: Nominal

        Campo: fecha
        Tipo: Fecha (date/timelap)
        Escala: Intervalo
        
        Campo: id_cliente (Foreging key)
        Tipo: Entero (int)
        Escala: Nominal

        Campo: nombre_cliente
        Tipo: Texto (str)
        Escala: Nominal

        Campo: email
        Tipo: Texto (str)
        Escala: Nominal

        Campo: medio_pago
        Tipo: Texto (str)
        Escala: Nominal

    ###########################################################################

    **Tabla: Detalle_ventas**
        Estructura: Estructurada
        Registros: 343
        Campos: 6

        Campo: id_venta (Primary key)
        Tipo: Entero (int)
        Escala: Nominal

        Campo: id_producto (Foreging key)
        Tipo: Entero (int)
        Escala: Nominal

        Campo: nombre_producto
        Tipo: Texto (str)
        Escala: Nominal

        Campo: cantidad
        Tipo: Entero (int)
        Escala: Razón

        Campo: Precio_unitario
        Tipo: Decimal (float)
        Escala: Razón

        Campo: Importe
        Tipo: Decimal (float)
        Escala: Razón
        
     ###########################################################################

    **Tabla: Productos**
        Estructura: Estructurada
        Registros: 100
        Campos: 4

        Campo: id_producto (Primary key)
        Tipo: Entero (int)
        Escala: Nominal

        Campo: nombre_producto
        Tipo: Texto (str)
        Escala: Nominal

        Campo: Categoria
        Tipo: Texto (str)
        Escala: Nominal

        Campo: Precio_unitario
        Tipo: Decimal (float)
        Escala: Razón

        
## 5. Pseudocódigo

Información:
-Evolución mensual de ingresos
- Top 10 clientes por gasto
- Productos más vendidos por categoría
- Preferencias de medios de pago

Pasos
Psudocódigo
