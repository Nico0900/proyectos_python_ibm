# Título del Proyecto
Proyecto Aurelion

## 1. Tema
Optimización del e-comerce "Tienda Aurelión" para maximizar su rentabilidad y eficiencia operativa

Este proyecto se centra en transformar el e-comerce "Tienda Aurelión" en un negocio altamente rentable mediante el análisis estratégico de datos. Nos enfocaremos en identificar oportunidades de crecimiento, segmentar a los clientes habituales de mayor valor y optimizar la gestión de inventario y surtido para maximizar el margen de beneficio en el competitivo sector de comercio electrónico.

El análisis considerará métricas críticas del negocio como rotación de productos, comportamiento de compra por temporada, lealtad del cliente y eficiencia en la gestión de perecederos, integrando estos insights con los datos transaccionales del punto de venta.

## 2. Problema
Gestión ineficiente y pérdida de oportunidades en el negocio

Aurelión enfrenta desafíos específicos de un abasto tradicional:

- Desconocimiento del cliente habitual: No identifica quiénes son sus compradores más frecuentes ni sus patrones de consumo.
- Gestión de inventario subóptima: Incertidumbre sobre qué productos rotan más rápido y cuáles generan mayor rentabilidad.
- Surtido no estratégico: Falta de análisis data-driven para determinar la combinación ideal de productos que maximice ventas y margen.
- Oportunidades de fidelización desaprovechadas: Ausencia de programas dirigidos a clientes frecuentes que incrementen su lealtad y gasto promedio.

Estos problemas limitan la rentabilidad del abasto y afectan su competitividad frente a cadenas organizadas.

## 3. Solución
Sistema de inteligencia comercial para abasto de alta rentabilidad

Implementaremos una solución práctica y efectiva que transforme datos en ventajas competitivas:

- Segmentación por frecuencia y valor: Identificación de clientes habituales y de alto gasto para programas de fidelización personalizados.
- Optimización de surtido y espacio: Análisis de rotación de inventrario y rentabilidad por producto para determinar el mix ideal y asignación de espacio en góndolas.
- Gestión predictiva de inventario: Sistema para anticipar demanda estacional y optimizar niveles de stock, reduciendo mermas y rupturas.
- Dashboard gerencial: Monitoreo de KPIs críticos: margen por categoría, rotación de productos, ticket promedio y frecuencia de compra.

Resultado Esperado: Incremento de la rentabilidad operativa, reducción del inventario ocioso y aumento de la lealtad de clientes habituales.

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
