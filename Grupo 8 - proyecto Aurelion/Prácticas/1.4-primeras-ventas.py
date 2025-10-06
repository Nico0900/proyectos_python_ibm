"""
Script para análisis de las primeras 10 ventas de una tienda
Permite evaluar el arranque del negocio con estadísticas detalladas
"""

def solicitar_ventas():
    """Solicita al usuario el monto de las primeras 10 ventas"""
    ventas = []
    
    print("=" * 60)
    print("  ANÁLISIS DE PRIMERAS 10 VENTAS DEL NEGOCIO  ")
    print("=" * 60)
    print("\nIngrese el monto de cada venta (en la moneda de su preferencia)")
    print("Puede usar decimales (ejemplo: 150.50)\n")
    
    for i in range(10):
        while True:
            try:
                venta = float(input(f"Venta #{i+1}: $"))
                if venta < 0:
                    print(" El monto no puede ser negativo. Intente nuevamente.")
                else:
                    ventas.append(venta)
                    break
            except ValueError:
                print(" Por favor, ingrese un número válido.")
    
    return ventas

def calcular_promedio(ventas):
    """Calcula el promedio de las ventas iniciales"""
    if len(ventas) == 0:
        return 0
    return sum(ventas) / len(ventas)

def identificar_ventas_sobre_promedio(ventas, promedio):
    """Identifica cuáles ventas estuvieron por encima del promedio"""
    ventas_sobre_promedio = []
    
    for i, venta in enumerate(ventas, 1):
        if venta > promedio:
            ventas_sobre_promedio.append({
                'numero': i,
                'monto': venta,
                'diferencia': venta - promedio
            })
    
    return ventas_sobre_promedio

def calcular_total(ventas):
    """Calcula el total recaudado en las primeras ventas"""
    return sum(ventas)

def determinar_mejor_peor_venta(ventas):
    """Determina cuál fue la mejor y peor venta inicial"""
    if not ventas:
        return None, None, None, None
    
    mejor_venta = max(ventas)
    peor_venta = min(ventas)
    indice_mejor = ventas.index(mejor_venta) + 1
    indice_peor = ventas.index(peor_venta) + 1
    
    return mejor_venta, indice_mejor, peor_venta, indice_peor

def generar_grafico_barras(ventas, promedio):
    """Genera un gráfico de barras ASCII para visualizar las ventas"""
    if not ventas:
        return
    
    max_venta = max(ventas)
    
    print("\n GRÁFICO DE VENTAS:")
    print("-" * 50)
    
    for i, venta in enumerate(ventas, 1):
        # Calcular longitud de la barra (máximo 30 caracteres)
        if max_venta > 0:
            longitud = int((venta / max_venta) * 30)
        else:
            longitud = 0
        
        # Determinar color/símbolo según relación con promedio
        if venta > promedio:
            barra = "█" * longitud
            indicador = " ⬆"
        elif venta < promedio:
            barra = "▓" * longitud
            indicador = " ⬇"
        else:
            barra = "█" * longitud
            indicador = " ="
        
        print(f"  Venta #{i:2d} |{barra:<30} ${venta:,.2f}{indicador}")
    
    print(f"\n  Línea promedio: ${promedio:,.2f}")
    print("  ⬆ = Sobre promedio  ⬇ = Bajo promedio  = = En promedio")

def calcular_estadisticas_adicionales(ventas):
    """Calcula estadísticas adicionales útiles"""
    if not ventas:
        return {}
    
    ventas_ordenadas = sorted(ventas)
    n = len(ventas_ordenadas)
    
    # Mediana
    if n % 2 == 0:
        mediana = (ventas_ordenadas[n//2 - 1] + ventas_ordenadas[n//2]) / 2
    else:
        mediana = ventas_ordenadas[n//2]
    
    # Desviación estándar
    promedio = calcular_promedio(ventas)
    varianza = sum((x - promedio) ** 2 for x in ventas) / n
    desviacion_estandar = varianza ** 0.5
    
    return {
        'mediana': mediana,
        'desviacion_estandar': desviacion_estandar,
        'rango': max(ventas) - min(ventas)
    }

def mostrar_resumen_completo(ventas):
    """Muestra un resumen completo del análisis de ventas"""
    print("\n" + "=" * 60)
    print(" RESUMEN COMPLETO DEL ANÁLISIS")
    print("=" * 60)
    
    # 2. Calcular promedio
    promedio = calcular_promedio(ventas)
    
    # 3. Identificar ventas sobre el promedio
    ventas_sobre_promedio = identificar_ventas_sobre_promedio(ventas, promedio)
    
    # 4. Calcular total
    total = calcular_total(ventas)
    
    # 5. Determinar mejor y peor venta
    mejor_venta, indice_mejor, peor_venta, indice_peor = determinar_mejor_peor_venta(ventas)
    
    # Estadísticas adicionales
    stats_adicionales = calcular_estadisticas_adicionales(ventas)
    
    # Mostrar todas las ventas
    print("\n DETALLE DE VENTAS REGISTRADAS:")
    print("-" * 50)
    for i, venta in enumerate(ventas, 1):
        diferencia = venta - promedio
        simbolo = "✓" if venta > promedio else "✗" if venta < promedio else "="
        print(f"  Venta #{i:2d}: ${venta:>10,.2f} [{simbolo}] (Dif: ${diferencia:+,.2f})")
    
    # Estadísticas principales
    print("\n ESTADÍSTICAS PRINCIPALES:")
    print("-" * 50)
    print(f"  • Promedio de ventas:     ${promedio:,.2f}")
    print(f"  • Total recaudado:        ${total:,.2f}")
    print(f"  • Mediana:                ${stats_adicionales['mediana']:,.2f}")
    print(f"  • Desviación estándar:    ${stats_adicionales['desviacion_estandar']:,.2f}")
    print(f"  • Rango (max - min):      ${stats_adicionales['rango']:,.2f}")
    
    # Ventas sobre el promedio
    print("\n  VENTAS SOBRE EL PROMEDIO:")
    print("-" * 50)
    if ventas_sobre_promedio:
        print(f"  Total: {len(ventas_sobre_promedio)} ventas ({len(ventas_sobre_promedio)*10}%)")
        for venta_info in ventas_sobre_promedio:
            print(f"  • Venta #{venta_info['numero']:2d}: ${venta_info['monto']:>10,.2f} "
                  f"(+${venta_info['diferencia']:,.2f} sobre promedio)")
    else:
        print("  No hubo ventas sobre el promedio")
    
    # Mejor y peor venta
    print("\n MEJOR Y PEOR VENTA:")
    print("-" * 50)
    print(f"   Mejor venta:  Venta #{indice_mejor:2d} con ${mejor_venta:,.2f}")
    print(f"   Peor venta:   Venta #{indice_peor:2d} con ${peor_venta:,.2f}")
    print(f"   Diferencia:   ${mejor_venta - peor_venta:,.2f}")
    
    # Análisis de rendimiento
    print("\n ANÁLISIS DE RENDIMIENTO:")
    print("-" * 50)
    
    # Tendencia
    primera_mitad = calcular_promedio(ventas[:5])
    segunda_mitad = calcular_promedio(ventas[5:])
    
    if segunda_mitad > primera_mitad:
        tendencia = " POSITIVA - Las ventas mejoraron en la segunda mitad"
        diferencia_mitades = segunda_mitad - primera_mitad
        print(f"  Tendencia: {tendencia}")
        print(f"  Mejora: +${diferencia_mitades:,.2f} en promedio")
    elif segunda_mitad < primera_mitad:
        tendencia = " NEGATIVA - Las ventas disminuyeron en la segunda mitad"
        diferencia_mitades = primera_mitad - segunda_mitad
        print(f"  Tendencia: {tendencia}")
        print(f"  Disminución: -${diferencia_mitades:,.2f} en promedio")
    else:
        print("  Tendencia:  ESTABLE - Las ventas se mantuvieron constantes")
    
    print(f"\n  Promedio primera mitad (1-5):  ${primera_mitad:,.2f}")
    print(f"  Promedio segunda mitad (6-10): ${segunda_mitad:,.2f}")
    
    # Consistencia
    if stats_adicionales['desviacion_estandar'] < promedio * 0.2:
        print("\n   Ventas muy consistentes (baja variabilidad)")
    elif stats_adicionales['desviacion_estandar'] < promedio * 0.5:
        print("\n   Ventas moderadamente consistentes")
    else:
        print("\n   Alta variabilidad en las ventas")

    # Generar gráfico
    generar_grafico_barras(ventas, promedio)
    
    print("\n" + "=" * 60)
    print(" Análisis completado exitosamente")
    print("=" * 60)

def main():
    """Función principal del programa"""
    print("\n SISTEMA DE ANÁLISIS DE VENTAS INICIALES ")
    print("Analice el arranque de su negocio con las primeras 10 ventas\n")
    
    try:
        # 1. Solicitar las 10 ventas
        ventas = solicitar_ventas()
        
        # Mostrar resumen completo
        mostrar_resumen_completo(ventas)
        
        # Recomendaciones finales
        print("\n RECOMENDACIONES:")
        print("-" * 50)
        promedio = calcular_promedio(ventas)
        if promedio < 100:
            print("  • Considere estrategias para aumentar el ticket promedio")
        if max(ventas) > promedio * 2:
            print("  • Identifique qué hizo especial en su mejor venta")
        if min(ventas) < promedio * 0.5:
            print("  • Analice las causas de las ventas más bajas")
        print("  • Mantenga registro detallado para futuras comparaciones")
        
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n  Error inesperado: {e}")

if __name__ == "__main__":
    main()