# Plantilla de solucion

## Analisis

- Entrada:
  - `puntos_ganados_saque` (entero): Cantidad de jugadas donde el servidor obtuvo el punto de forma directa o indirecta tras poner la bola en juego.
  - `total_saques` (entero): Universo total de saques ejecutados por el jugador durante el set o partido.

- Proceso:
  1. Validar que el denominador de la fracción no sea cero para blindar el algoritmo contra indeterminaciones matemáticas.
  2. Aplicar la fórmula de la probabilidad clásica/empírica: Dividir los casos favorables (`puntos_ganados_saque`) entre el total de casos posibles (`total_saques`) y multiplicar el cociente por 100 para estandarizar la métrica en un porcentaje.
  3. Evaluar mediante una estructura de control condicional (`if-else`) si la probabilidad resultante alcanza o supera la frontera crítica del 60.0% de efectividad.

- Salida:
  - `probabilidad_porcentaje` (flotante redondeado a 1 decimal).
  - `diagnostico` (cadena de texto con la interpretación del rendimiento).
  - `tiene_ventaja` (booleano: `True` o `False`).

## Reglas identificadas

1. **Restricción de Espacio Muestral:** Los casos favorables jamás pueden exceder el tamaño total del espacio muestral ($Ganados \le Saques$). Intentar ingresar un dato inverso corrompe el principio axiomático de la probabilidad (la cual oscila estrictamente entre 0 y 1, o 0% y 100%).
2. **Blindaje de Indeterminación (`ZeroDivisionError`):** Si la variable del total de saques es 0, la división matemática es impracticable. El flujo lógico debe capturar este estado y desviar el resultado hacia una salida segura por defecto.
3. **Umbral de Dominio de Juego:** La regla de negocio estipula que una efectividad $\ge 60\%$ otorga una "Ventaja Competitiva Alta". Al ser un comparador inclusivo, el valor exacto de 60% se clasifica dentro de la zona de dominio del partido.

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

Esta solución funciona porque reduce un escenario deportivo dinámico a una proporción matemática estricta y predecible bajo el modelo de la probabilidad empírica. Al implementar validaciones jerárquicas cruzadas (que impiden que los casos favorables superen a los totales o que el denominador caiga a cero), el software garantiza que el veredicto lógico sea robusto, libre de fallos en tiempo de ejecución y perfectamente auditable para los retos de Campuslands.

## Sugerencia

Verifica cada operacion con calculos manuales antes de confiar en el codigo.