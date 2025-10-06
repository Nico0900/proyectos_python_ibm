# Pseudocódigo - Proyecto Aurelion

## Análisis de Ventas y Clientes

```pseudocode
INICIO

// 1. CARGAR DATOS
CARGAR tabla_clientes desde CSV/JSON
CARGAR tabla_ventas desde CSV/JSON
CARGAR tabla_detalle_ventas desde CSV/JSON
CARGAR tabla_productos desde CSV/JSON

// 2. VALIDAR Y LIMPIAR DATOS
VERIFICAR valores nulos en campos críticos
CONVERTIR fecha a tipo datetime en tabla_ventas
VERIFICAR integridad referencial (foreign keys)

// 3. ANÁLISIS 1: EVOLUCIÓN MENSUAL DE INGRESOS
UNIR detalle_ventas CON ventas POR id_venta
EXTRAER mes y año de fecha
AGRUPAR POR mes y año
CALCULAR suma de importe POR grupo
ORDENAR POR fecha ascendente
ALMACENAR resultado en evolucion_mensual

// 4. ANÁLISIS 2: TOP 10 CLIENTES POR GASTO
UNIR ventas CON detalle_ventas POR id_venta
AGRUPAR POR id_cliente y nombre_cliente
CALCULAR suma total de importe POR cliente
ORDENAR POR gasto total descendente
SELECCIONAR primeros 10 registros
ALMACENAR resultado en top_10_clientes

// 5. ANÁLISIS 3: PRODUCTOS MÁS VENDIDOS POR CATEGORÍA
UNIR detalle_ventas CON productos POR id_producto
AGRUPAR POR categoria y nombre_producto
CALCULAR suma de cantidad POR grupo
PARA cada categoria:
    SELECCIONAR producto con mayor cantidad vendida
FIN PARA
ALMACENAR resultado en productos_mas_vendidos_por_categoria

// 6. ANÁLISIS 4: PREFERENCIAS DE MEDIOS DE PAGO
UNIR ventas CON detalle_ventas POR id_venta
AGRUPAR POR medio_pago
CALCULAR cantidad de transacciones POR medio_pago
CALCULAR monto total POR medio_pago
CALCULAR porcentaje de uso POR medio_pago
ORDENAR POR cantidad de transacciones descendente
ALMACENAR resultado en preferencias_medios_pago

// 7. GENERAR REPORTES
CREAR visualización de evolucion_mensual (gráfico de líneas)
CREAR visualización de top_10_clientes (gráfico de barras)
CREAR visualización de productos_mas_vendidos_por_categoria (gráfico de barras agrupadas)
CREAR visualización de preferencias_medios_pago (gráfico de pastel)

// 8. EXPORTAR RESULTADOS
EXPORTAR evolucion_mensual a CSV
EXPORTAR top_10_clientes a CSV
EXPORTAR productos_mas_vendidos_por_categoria a CSV
EXPORTAR preferencias_medios_pago a CSV
GUARDAR visualizaciones como imágenes PNG/PDF

FIN
```

## Información Generada

- **Evolución mensual de ingresos**: Tendencia de ventas mes a mes
- **Top 10 clientes por gasto**: Clientes más valiosos
- **Productos más vendidos por categoría**: Identificación de productos estrella
- **Preferencias de medios de pago**: Análisis de comportamiento de pago
