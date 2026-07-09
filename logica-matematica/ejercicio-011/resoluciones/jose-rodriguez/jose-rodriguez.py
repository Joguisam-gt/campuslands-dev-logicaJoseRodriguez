def analizar_combinatoria_kickboxing(cantidad_punos, cantidad_patadas):
    # Umbral de variabilidad exigido por el torneo
    MIN_COMBINACIONES_ESTRATEGIA = 12
    
    # 1. Aplicar el Principio Multiplicativo del Conteo Combinatorio
    # Si una acción se puede hacer de 'n' formas y otra de 'm' formas, 
    # ambas se pueden hacer consecutivamente de 'n * m' formas.
    total_combinaciones_dos_golpes = cantidad_punos * cantidad_patadas
    
    # 2. Evaluar reglas de negocio condicionales
    if total_combinaciones_dos_golpes >= MIN_COMBINACIONES_ESTRATEGIA:
        veredicto = "Estrategia Aprobada (Suficiente variabilidad táctica para el torneo)"
        cumple_requisito = True
    else:
        veredicto = "Estrategia Rechazada (Arsenal muy predecible. Requiere añadir más variantes)"
        cumple_requisito = False
        
    return total_combinaciones_dos_golpes, veredicto, cumple_requisito


if __name__ == "__main__":
    print("=== SISTEMA DE ANÁLISIS TÁCTICO: KICKBOXING COMBINATORIO ===")
    print("Por favor, ingresa el arsenal de movimientos disponibles del peleador:\n")
    
    try:
        # Captura de datos interactiva dentro del bloque de control de excepciones
        punos = int(input("Cantidad de tipos de golpes de puño dominados (ej. 4): "))
        patadas = int(input("Cantidad de tipos de patadas dominadas (ej. 3): "))
        
        if punos < 0 or patadas < 0:
            print("\nError: No se pueden registrar cantidades negativas de movimientos.")
        elif punos == 0 or patadas == 0:
            print("\nAlerta: Un arsenal en cero no permite generar combinaciones válidas de kickboxing.")
        else:
            # Procesamiento de la lógica combinatoria
            combinaciones, reporte_tactico, aprobado = analizar_combinatoria_kickboxing(punos, patadas)
            
            print("\n=============================================")
            print("REPORTE DE ANÁLISIS COMBINATORIO:")
            print(f"-> Golpes de puño base: {punos}")
            print(f"-> Patadas base: {patadas}")
            print(f"-> Combinaciones posibles (Puño + Patada): {combinaciones}")
            print("---------------------------------------------")
            print(f"-> Veredicto del Comité: {reporte_tactico}")
            print("=============================================")
            
    except ValueError:
        # Control para interceptar entradas de texto no numéricas en la terminal
        print("\nError: Por favor, introduce únicamente números enteros válidos.")