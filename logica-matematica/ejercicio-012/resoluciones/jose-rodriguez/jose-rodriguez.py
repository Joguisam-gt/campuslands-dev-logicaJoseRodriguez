def analizar_probabilidad_pingpong(puntos_ganados_saque, total_saques):
    # Regla de control: Evitar división por cero si no se han realizado saques
    if total_saques == 0:
        return 0.0, "Indeterminado (El partido no ha iniciado)", False
        
    # Umbral de ventaja competitiva según las reglas del torneo
    UMBRAL_VENTAJA = 60.0
    
    # 1. Calcular la Probabilidad Básica Empírica (Casos favorables / Casos totales)
    probabilidad_porcentaje = (puntos_ganados_saque / total_saques) * 100
    
    # 2. Evaluar reglas de negocio condicionales
    if probabilidad_porcentaje >= UMBRAL_VENTAJA:
        diagnostico = "Ventaja Competitiva Alta (Dominio total del servicio)"
        tiene_ventaja = True
    else:
        diagnostico = "Rendimiento Estándar (Servicio vulnerable bajo presión)"
        tiene_ventaja = False
        
    return round(probabilidad_porcentaje, 1), diagnostico, tiene_ventaja


if __name__ == "__main__":
    print("=== SISTEMA DE ANÁLISIS PROBABILÍSTICO: PINGPONG ===")
    print("Por favor, ingresa las estadísticas de servicio del jugador:\n")
    
    try:
        # Captura de datos interactiva dentro del bloque de control de excepciones
        ganados = int(input("Puntos ganados con el propio saque: "))
        saques_totales = int(input("Total de saques realizados en el partido: "))
        
        if ganados < 0 or saques_totales < 0:
            print("\nError: No se pueden registrar estadísticas con valores negativos.")
        elif ganados > saques_totales:
            print("\nError lógico: Los puntos ganados no pueden superar al total de saques.")
        else:
            # Procesamiento de la lógica de probabilidad básica
            prob, reporte, ventaja = analizar_probabilidad_pingpong(ganados, saques_totales)
            
            print("\n=============================================")
            print("REPORTE DE RENDIMIENTO PROBABILÍSTICO:")
            print(f"-> Probabilidad de ganar el punto al saque: {prob}%")
            print(f"-> Diagnóstico técnico: {reporte}")
            print("---------------------------------------------")
            
            if ventaja:
                print("ESTRATEGIA: Mantener saques profundos y con efecto. El control es tuyo.")
            else:
                print("ESTRATEGIA: Variar el ángulo de servicio. El rival está descifrando el patrón.")
            print("=============================================")
            
    except ValueError:
        # Control de excepciones para entradas de texto accidentales en la terminal
        print("\nError: Por favor, introduce únicamente números enteros válidos.")