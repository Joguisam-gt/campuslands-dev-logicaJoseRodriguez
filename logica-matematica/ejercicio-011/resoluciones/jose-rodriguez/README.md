# Plantilla de solucion

## Analisis

- Entrada:
    - `cantidad_punos` (int): Numero de tecnicas distintas de mano que el peleador domina en su arsenal/
    - `cantidad_patadas` (int): Numero de tecnicas distintas de pierna que el peleador domina en su arsenal.

- Proceso:
1. Aplicar el principio multiplicativo fundamental del conteo combinatorio para determinar el espacio muestral de combinaciones de dos golpes (un golpe de puno seguido estrictamente por una patada): $Combinaciones = Punos \times Patadas$.
2. Evaluar mediante una estructura de control condicional simple (`if-else`) si el total de combinaciones resultantes es mayor o igual al limite normativo de 12 variantes tacticas fijado por el reglamento del torneo.

- Salida:
    - `total_combinaciones_dos_golpes` (int).
    - `veredicto` (cadena de texto con la resolucion de inscripcion del atleta).
    - `cumple_requisito` (booleano: `True` o `False`).

## Reglas identificadas

1. **Principio multiplicativo del conteo:** En analisis combinatorio, si un evento A occure de $n$ maneras y evento B ocurre de $m$ maneras, el numero total de formas en que ocurren ambos eventos de manera secuencial es el producto directo ($n \times m$).
2. **Restriccion en nulidad cooperativa:** Si cualquiera de las dos entradas es equivalente a cero, el resultado combinatorio se reduce a cero de forma automatica, demostrando que el kickboxing requiere obligatoriamente de la coexistencia de ambos estilos de ataque. 
3. **Umbral de predictibilidad tactica:** La regla de negocio exige un minimo de 12 combinaciones posibles ($\ge 12$). Si el arsenal combinatorio del competidor esta por debajo, el algoritmo deniega el alta debido a que el atleta presentaria un patron de pelea excesivamente facil de bloquear.

## Pruebas

### Caso normal

Entrada:
- `cantidad_punos`: 4 *(ej. Jab, Cross, Hook, Upper)*
- `cantidad_patadas`: 3 *(ej. Low, Middle, High)*

Resultado esperado:
- `Combinaciones posibles`: 12 *(Cálculo manual: 4 * 3 = 12)*
- `Veredicto`: "Estrategia Aprobada (Suficiente variabilidad táctica para el torneo)" *(Cálculo lógico: 12 >= 12 es Verdadero, aprueba exactamente en el límite)*

### Caso borde

Entrada:
- `cantidad_punos`: 5
- `cantidad_patadas`: 2

Resultado esperado:
- `Combinaciones posibles`: 10 *(Cálculo manual: 5 * 2 = 10)*
- `Veredicto`: "Estrategia Rechazada (Arsenal muy predecible. Requiere añadir más variantes)" *(Cálculo lógico: A pesar de dominar muchos golpes de puño, la baja cantidad de patadas reduce el espectro combinatorio a 10. Como 10 >= 12 es Falso, el sistema rechaza la estrategia)*

## Explicacion final 

Esta solucion funciona porque automatiza el principio multiplicativo elementeal de la combinatoria sin necesidad de recurrir a bucles o factoriales complejos, resolviendo el problema en complejidad temporal constante $0(1)$. Al validar los datos de manera previa y cruzarlos con un comparador inclusivo (`>=`), el script grantiza un diagnostico matematico exacto y predecible, ideal para los sistemas de arbitraje digital de Campuslands