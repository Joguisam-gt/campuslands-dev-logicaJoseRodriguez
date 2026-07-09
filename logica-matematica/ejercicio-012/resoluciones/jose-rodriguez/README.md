# Plantilla de solucion

## Analisis

- Entrada:
    - `puntos_ganados_saque` (int): Cantidad de jugadas donde el servidor obtuvo el punto de forma directa o indirecta tras poner la bola en juego.
    - `total_saques` (int): Universo total de saques ejecutados por el jugador durante el set o partido.

- Proceso:
1. Validar que el denominador de la fraccion no sea cero para blindar el algoritmo contra indeterminaciones matematicas.
2. Aplicar la formmula de la probabilidad clasica/ empirica: Dividir los casos favorables (`puntos_ganados_saque`) entre el total de casos posibles (`total_saques`) y multiplicar el cociente por 100 para estandarizar la metrica en un porcentaje.
3. Evaluar mediante una estructura de control condicional (`if-else`) si la probabilidad resultante alcanza o supera la frontera critica del 60.0% de efectividad.

- Salida:
    - `probabilidad_porcentaje` (float redondeado a 1 decimal).
    - `diagnostico` (cadena de texto con la interpretacion del rendimiento).
    - `tiene_ventaja` (booleano: `True` o `False`)..

## Reglas identificadas

1. **Restriccion de espacio muestral:** Los casos favorables jamas pueden exceder el tamano total del espacio muestal ($Ganados \le Saques$). Intentar ingresar un dato inverso corrompe el principio axiomatico de la probabilidad (la cual oscila estrictamente entre 0 y 1, o 0% y 100%).
2. **Blindaje de indeterminacion (`ZeroDivisionError`):** Si la variable del total de saques es 0, la division matematica es impracticable. El flujo logico debe capturar este estado y desviar el resultado hacia una salida segura por defecto.
3. **Umbral de dominio de juego:** La regla de negocio estipula que una efectividad $\ge 60\%$ otroga una "Ventaja competitiva alta". Al ser un comparador inclusivo, el valor exacto de 60% se clasifica dentro de la zona de dominio del partido.

## Pruebas

### Caso normal 

Entrada:
- `puntos_ganados_saque`: 15
- `total_saques`: 20

Resultado esperado:
- `Probabilidad de éxito`: 75.0% *(Cálculo manual: (15 / 20) * 100 = 0.75 * 100 = 75.0%)*
- `Diagnóstico`: "Ventaja Competitiva Alta (Dominio total del servicio)"
- `¿Tiene ventaja?`: `True` *(Cálculo lógico: 75.0 >= 60.0 es Verdadero)*

### Caso borde

Entrada:
- `puntos_ganados_saque`: 3
- `total_saques`: 5

Resultado esperado:
- `Probabilidad de éxito`: 60.0% *(Cálculo manual: (3 / 5) * 100 = 0.6 * 100 = 60.0%)*
- `Diagnóstico`: "Ventaja Competitiva Alta (Dominio total del servicio)"
- `¿Tiene ventaja?`: `True` *(Cálculo lógico: Al tocar exactamente el límite de la frontera mediante el operador `>=`, el sistema lógico valida el estado positivo por el margen mínimo de la regla)*

## Explicacion final 

Esta solucion funciona porque reduce un escenario deportivo dinamico a una proporcion matematica estricta y predecible bajo el modelo de la probabilidad empirica. Al implementar validacion jerarquicas cruzadas (que impiden que los casos favorables superen a los totales o que el denominador caiga o cero), el software garantiza que el veredicto logico sea robusto, libre de fallos en tiempo de ejecucion y perfectamente auditable para los retos de Campuslands.