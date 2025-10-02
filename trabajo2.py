"""
Script para registro y análisis de temperaturas
Este programa solicita temperaturas de 5 días consecutivos y genera estadísticas
"""

def solicitar_temperaturas():
    """Solicita al usuario las temperaturas de 5 días consecutivos"""
    temperaturas = []
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    
    print("=" * 50)
    print("REGISTRO DE TEMPERATURAS (5 DÍAS)")
    print("=" * 50)
    
    for i in range(5):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dias_semana[i]} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("❌ Por favor, ingrese un número válido.")
    
    return temperaturas, dias_semana

def calcular_estadisticas(temperaturas):
    """Calcula estadísticas de las temperaturas"""
    temp_promedio = sum(temperaturas) / len(temperaturas)
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)
    
    return temp_promedio, temp_maxima, temp_minima

def contar_dias_calurosos(temperaturas, umbral=25):
    """Cuenta cuántos días tuvieron temperatura alta (mayor a 25°C)"""
    dias_calurosos = sum(1 for temp in temperaturas if temp > umbral)
    return dias_calurosos

def mostrar_resumen(temperaturas, dias_semana, promedio, maxima, minima, dias_calurosos):
    """Muestra un resumen completo de los datos registrados"""
    print("\n" + "=" * 50)
    print("RESUMEN COMPLETO DE TEMPERATURAS")
    print("=" * 50)
    
    # Mostrar temperaturas registradas
    print("\n📊 TEMPERATURAS REGISTRADAS:")
    print("-" * 30)
    for dia, temp in zip(dias_semana, temperaturas):
        # Agregar indicador visual para temperaturas altas
        indicador = " 🔥" if temp > 25 else ""
        print(f"  {dia:12s}: {temp:6.1f}°C{indicador}")
    
    # Mostrar estadísticas
    print("\n📈 ESTADÍSTICAS DE LA SEMANA:")
    print("-" * 30)
    print(f"  Temperatura Promedio: {promedio:.2f}°C")
    print(f"  Temperatura Máxima:   {maxima:.1f}°C")
    print(f"  Temperatura Mínima:   {minima:.1f}°C")
    print(f"  Rango de temperatura: {maxima - minima:.1f}°C")
    
    # Mostrar días calurosos
    print("\n🌡️  ANÁLISIS DE DÍAS CALUROSOS:")
    print("-" * 30)
    print(f"  Días con temperatura > 25°C: {dias_calurosos}")
    
    if dias_calurosos > 0:
        print(f"  Porcentaje de días calurosos: {(dias_calurosos/5)*100:.1f}%")
        print("  Días calurosos:")
        for dia, temp in zip(dias_semana, temperaturas):
            if temp > 25:
                print(f"    • {dia}: {temp:.1f}°C")
    else:
        print("  No hubo días con temperatura superior a 25°C")
    
    # Gráfico de barras simple
    print("\n📊 GRÁFICO DE TEMPERATURAS:")
    print("-" * 30)
    
    # Normalizar para el gráfico (máximo 40 caracteres de ancho)
    max_temp_graf = max(temperaturas)
    min_temp_graf = min(0, min(temperaturas))
    rango = max_temp_graf - min_temp_graf
    
    for dia, temp in zip(dias_semana, temperaturas):
        # Calcular longitud de la barra
        if rango > 0:
            longitud = int((temp - min_temp_graf) / rango * 30)
        else:
            longitud = 15
        
        barra = "█" * longitud
        print(f"  {dia:10s} |{barra} {temp:.1f}°C")
    
    print("\n" + "=" * 50)

def main():
    """Función principal del programa"""
    print("\n🌡️  PROGRAMA DE REGISTRO DE TEMPERATURAS 🌡️")
    print("Este programa registra y analiza las temperaturas de 5 días\n")
    
    try:
        # 1. Solicitar temperaturas
        temperaturas, dias_semana = solicitar_temperaturas()
        
        # 2. Calcular estadísticas
        promedio, maxima, minima = calcular_estadisticas(temperaturas)
        
        # 3. Contar días calurosos
        dias_calurosos = contar_dias_calurosos(temperaturas)
        
        # 4. Mostrar resumen completo
        mostrar_resumen(temperaturas, dias_semana, promedio, maxima, minima, dias_calurosos)
        
        # Mensaje final
        print("\n✅ Análisis completado exitosamente")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()