
# Pseudocódigo - Proyecto Aurelion
## Sistema de Inteligencia Comercial para E-commerce

INICIO

// ============================================
// 1. CARGA Y PREPARACIÓN DE DATOS
// ============================================
LEER tablas: Clientes, Ventas, Detalle_ventas, Productos

SI todas las tablas existen ENTONCES
    CARGAR datos en memoria
    REALIZAR merge de tablas por claves (id_cliente, id_producto, id_venta)
SINO
    MOSTRAR "Error: archivos faltantes"
    TERMINAR
FIN SI

// Validación y limpieza
VALIDAR integridad referencial (foreign keys)
LIMPIAR registros duplicados o nulos
CONVERTIR fechas al formato correcto
CALCULAR campo derivado: Beneficio = (precio_unitario - costo_estimado)

// ============================================
// 2. SEGMENTACIÓN DE CLIENTES (RFM)
// ============================================
PARA cada cliente EN Clientes:
    // Recency (Recencia)
    CALCULAR días_desde_ultima_compra = hoy - MAX(fecha_venta)
    
    // Frequency (Frecuencia)
    CALCULAR numero_compras = CONTAR(id_cliente) de la tabla de ventas
    
    // Monetary (Valor monetario)
    CALCULAR valor_total = SUMAR(importe de todas sus compras)
    CALCULAR ticket_promedio = valor_total / numero_compras
    
    // Clasificación RFM
    ASIGNAR score_recency (1-3 según días desde la última compra)
    ASIGNAR score_frequency (1-3 según cantidad de compras)
    ASIGNAR score_monetary (1-3 según gasto promedio)
    
    CALCULAR score_rfm = CONCATENAR(score_r, score_f, score_m)

    Si recency es >= 30 es nada reciente XD
    Si recency es >= 15 es no tan reciente
    Si recency es < 15 es reciente

    Si frequency es <= 5 es ocasionales
    Si frequency es <= 10 es regular
    Si frequency es > 15 es leal

    Si ticket promedio es <= 100 es Gold
    Si ticket promedio es <= 500 es VIP
    Si ticket promedio es > 1000 es Platium

    // Segmentos de clientes
    SI score_rfm >= 444 ENTONCES
        segmento = "VIP - Clientes Estrella"
    SINO SI score_frequency >= 4 Y score_monetary >= 4 ENTONCES
        segmento = "Clientes Leales"
    SINO SI score_recency <= 2 ENTONCES
        segmento = "Clientes en Riesgo"
    SINO SI numero_compras == 1 ENTONCES
        segmento = "Nuevos - Una Compra"
    SINO
        segmento = "Clientes Ocasionales"
    FIN SI
    
    ALMACENAR segmentación del cliente
FIN PARA

// ============================================
// 3. ANÁLISIS DE ROTACIÓN DE INVENTARIO
// ============================================
PARA cada producto EN Productos:
    CALCULAR unidades_vendidas = SUMAR(cantidad en Detalle_ventas)
    CALCULAR ingresos_totales = SUMAR(importe)
    CALCULAR frecuencia_venta = CONTAR(ventas distintas)
    
    // Rotación de inventario (ventas/período)
    CALCULAR periodo_analisis = MAX(fecha) - MIN(fecha) EN días
    CALCULAR rotacion_mensual = (unidades_vendidas / periodo_analisis)
    
    // Clasificación ABC de productos
    CALCULAR contribucion_ingresos = (ingresos_producto / ingresos_totales) * 100
    
    SI contribucion_ingresos acumulado <= 80% ENTONCES
        clasificacion = "A - Alta rotación"
    SINO SI contribucion_ingresos acumulado <= 95% ENTONCES
        clasificacion = "B - Rotación media"
    SINO
        clasificacion = "C - Baja rotación"
    FIN SI
    
    Alerta
    Si producto X es < 20% de stock aletar de reestock

    ALMACENAR métricas de rotación
FIN PARA

// ============================================
// 4. OPTIMIZACIÓN DE SURTIDO POR CATEGORÍA
// ============================================
PARA cada categoria EN Productos.categoria:
    CALCULAR total_productos = CONTAR(productos en categoría)
    CALCULAR ingresos_categoria = SUMAR(ingresos de productos)
    CALCULAR margen_categoria = SUMAR(margen de productos)
    CALCULAR rentabilidad = (margen_categoria / ingresos_categoria) * 100
    
    // Identificar productos estrella y rezagados
    productos_categoria = FILTRAR productos por categoría
    ORDENAR productos_categoria por rotacion_mensual DESC
    
    productos_estrella = TOP 20% productos (alta rotación y margen)
    productos_rezagados = BOTTOM 20% productos (baja rotación)
    
    // Recomendaciones
    SI rentabilidad < 15% ENTONCES
        recomendacion = "Revisar precios o considerar descontinuar"
    SINO SI productos_estrella > 5 ENTONCES
        recomendacion = "Aumentar stock de productos estrella"
    FIN SI
    
    ALMACENAR análisis por categoría
FIN PARA

// ============================================
// 5. ANÁLISIS ESTACIONAL Y PREDICTIVO
// ============================================
PARA cada mes EN rango_fechas:
    CALCULAR ventas_mensuales = SUMAR(ventas del mes)
    CALCULAR productos_vendidos = CONTAR(productos únicos)
    CALCULAR ticket_promedio_mensual = ventas_mensuales / numero_ventas
FIN PARA

// Detectar patrones estacionales
PARA cada producto EN Productos:
    CALCULAR ventas_por_mes = AGRUPAR ventas por mes
    IDENTIFICAR picos_demanda = MESES con ventas > promedio + desv_estandar
    IDENTIFICAR valles_demanda = MESES con ventas < promedio - desv_estandar
    
    SI existen picos_demanda ENTONCES
        producto.es_estacional = VERDADERO
        producto.meses_alta_demanda = picos_demanda
    FIN SI
FIN PARA

// Proyección simple de demanda
PARA cada producto_estrella:
    CALCULAR tendencia = promedio_ventas_ultimos_3_meses
    PROYECTAR demanda_proximo_mes = tendencia * factor_estacional
    RECOMENDAR stock_optimo = demanda_proyectada * 1.2
FIN PARA

// ============================================
// 6. CÁLCULO DE KPIs CRÍTICOS
// ============================================

// KPI 1: Margen por categoría
PARA cada categoria:
    CALCULAR margen_promedio = (SUM(margen) / SUM(ingresos)) * 100
    ALMACENAR kpi_margen_categoria
FIN PARA

// KPI 2: Ticket promedio
CALCULAR ticket_promedio_general = SUM(importe_ventas) / COUNT(ventas)

// KPI 3: Frecuencia de compra promedio
CALCULAR frecuencia_promedio = AVG(numero_compras_por_cliente)

// KPI 4: Tasa de retención
clientes_periodo_actual = CONTAR clientes activos últimos 30 días
clientes_periodo_anterior = CONTAR clientes activos 30-60 días atrás
clientes_retenidos = INTERSECCIÓN(clientes_actual, clientes_anterior)
CALCULAR tasa_retencion = (clientes_retenidos / clientes_periodo_anterior) * 100

// KPI 5: Ratio de conversión (compras/visitas) - si hay datos
// Nota: Requeriría datos de tráfico web

// KPI 6: Inventario ocioso
productos_sin_venta_30dias = CONTAR productos con última venta > 30 días
CALCULAR porcentaje_inventario_ocioso = (productos_sin_venta / total_productos) * 100

// ============================================
// 7. IDENTIFICACIÓN DE OPORTUNIDADES
// ============================================

// Oportunidad 1: Programas de fidelización
clientes_objetivo = FILTRAR clientes WHERE segmento IN ["VIP", "Leales"]
PARA cada cliente EN clientes_objetivo:
    CALCULAR descuento_potencial = ticket_promedio * 0.10
    CALCULAR roi_fidelizacion = (incremento_esperado_compras * valor_promedio) - costo_programa
FIN PARA

// Oportunidad 2: Cross-selling
PARA cada venta:
    productos_comprados = OBTENER productos de la venta
    ANALIZAR combinaciones_frecuentes = productos que se compran juntos
    GENERAR recomendaciones_cross_sell
FIN PARA

// Oportunidad 3: Reactivación de clientes en riesgo
clientes_riesgo = FILTRAR clientes WHERE segmento = "Clientes en Riesgo"
PARA cada cliente EN clientes_riesgo:
    productos_favoritos = OBTENER productos más comprados por el cliente
    GENERAR campaña_reactivacion(cliente, productos_favoritos)
FIN PARA

// ============================================
// 8. GENERACIÓN DE DASHBOARD GERENCIAL
// ============================================

CREAR dashboard_principal:
    // Métricas generales
    MOSTRAR total_ingresos_mes_actual
    MOSTRAR crecimiento_vs_mes_anterior (%)
    MOSTRAR ticket_promedio
    MOSTRAR numero_clientes_activos
    
    // Gráfico 1: Evolución de ventas mensuales (línea)
    GENERAR grafico_linea(ventas_por_mes)
    
    // Gráfico 2: Distribución de clientes por segmento (pie)
    GENERAR grafico_pie(segmentacion_clientes)
    
    // Gráfico 3: Top 10 productos por ingresos (barras)
    GENERAR grafico_barras(top_productos)
    
    // Gráfico 4: Margen por categoría (barras horizontales)
    GENERAR grafico_barras_horizontal(margen_categoria)
    
    // Tabla 1: Clientes VIP (top 20)
    GENERAR tabla(clientes_vip, columnas: [nombre, total_compras, valor_total, ultima_compra])
    
    // Tabla 2: Productos de baja rotación (acción requerida)
    GENERAR tabla(productos_rezagados, columnas: [nombre, categoria, dias_sin_venta, stock_estimado])
    
    // Tabla 3: Oportunidades de fidelización
    GENERAR tabla(oportunidades_fidelizacion)
    
    // Alertas
    SI tasa_retencion < 60% ENTONCES
        GENERAR alerta("Tasa de retención baja - Implementar programa de fidelización")
    FIN SI
    
    SI porcentaje_inventario_ocioso > 20% ENTONCES
        GENERAR alerta("Alto inventario ocioso - Revisar surtido")
    FIN SI
    
    SI clientes_riesgo > 20% del total ENTONCES
        GENERAR alerta("Muchos clientes en riesgo - Campaña de reactivación urgente")
    FIN SI

// ============================================
// 9. GENERACIÓN DE REPORTES
// ============================================

CREAR reporte_ejecutivo:
    INCLUIR resumen_kpis
    INCLUIR segmentacion_clientes
    INCLUIR analisis_categorias
    INCLUIR recomendaciones_estrategicas
    EXPORTAR a PDF

CREAR reporte_operativo:
    INCLUIR productos_reabastecer
    INCLUIR productos_descontinuar
    INCLUIR alertas_inventario
    EXPORTAR a Excel

CREAR reporte_marketing:
    INCLUIR clientes_objetivo_fidelizacion
    INCLUIR clientes_reactivar
    INCLUIR productos_cross_sell
    EXPORTAR a CSV

// ============================================
// 10. GUARDAR RESULTADOS
// ============================================

GUARDAR segmentacion_clientes EN "clientes_segmentados.csv"
GUARDAR analisis_productos EN "productos_analisis.csv"
GUARDAR kpis EN "kpis_dashboard.json"
GUARDAR recomendaciones EN "recomendaciones_estrategicas.txt"
EXPORTAR dashboard a HTML interactivo

MOSTRAR "Análisis completado exitosamente"
MOSTRAR "Archivos generados en directorio /resultados"

FIN
