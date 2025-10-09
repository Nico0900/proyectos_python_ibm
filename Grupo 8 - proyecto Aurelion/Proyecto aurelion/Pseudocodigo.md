# Pseudocódigo - Proyecto Aurelion

## Análisis de Ventas y Clientes (Versión Simplificada)

```pseudocode
INICIO

// 1. CARGAR DATOS
LEER archivo_datos
SI archivo_datos existe ENTONCES
    CARGAR datos en memoria
SINO
    MOSTRAR "Error: archivo no encontrado"
    FIN
FIN SI

// 2. VALIDAR DATOS
SI datos están completos ENTONCES
    CONTINUAR
SINO
    LIMPIAR datos incompletos
FIN SI

// 3. PROCESAR ANÁLISIS
PARA cada registro en datos
    CALCULAR total_ventas
    IDENTIFICAR cliente
    IDENTIFICAR producto
    REGISTRAR medio_pago
FIN PARA

// 4. GENERAR RESULTADOS
CALCULAR ingresos_mensuales
IDENTIFICAR mejores_clientes (Top 10)
IDENTIFICAR productos_populares
CALCULAR estadísticas_medios_pago

// 5. CREAR REPORTES
GENERAR gráfico_ventas
GENERAR tabla_clientes
GENERAR reporte_productos

// 6. GUARDAR RESULTADOS
GUARDAR reportes en archivos
EXPORTAR gráficos

FIN
```

## Estructura del Programa

1. **Entrada**: Archivos de datos (clientes, ventas, productos)
2. **Validación**: Verificación de datos completos
3. **Procesamiento**: Cálculos y análisis
4. **Salida**: Reportes y gráficos

## Información Generada

- Ingresos mensuales
- Top 10 clientes por gasto
- Productos más vendidos
- Estadísticas de medios de pago
