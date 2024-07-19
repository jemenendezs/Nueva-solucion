# Nueva-solucion
Este código está diseñado para ayudar a mezclar dos soluciones con concentraciones diferentes para obtener una solución final con una concentración y volumen deseados. Permite calcular exactamente la cantidad de cada solución que debe mezclarse. Si las concentraciones iniciales son iguales, el código informa al usuario que no es posible realizar la mezcla. Aquí está un desglose de lo que hace el código:

1. **Entrada del Usuario**:
   - Solicita al usuario las concentraciones de dos soluciones que se van a mezclar (`c1` y `c2` en porcentaje).
   - Solicita la concentración final deseada (`cf`) y el volumen final deseado (`vf`) en mililitros.

2. **Sistema de Ecuaciones**:
   - Utiliza un sistema de ecuaciones con dos incógnitas para calcular cuánto de cada solución debe mezclarse para obtener la concentración final deseada:
     - La primera ecuación es $\( c1 \cdot x + c2 \cdot y = cf \cdot vf \)$, donde $\( x \)$ es el volumen de la primera solución y $\( y \)$ es el volumen de la segunda solución.
     - La segunda ecuación es $\( x + y = vf \)$.

   - Resuelve el sistema de ecuaciones para obtener los volúmenes necesarios de cada solución:
     - $\( x = \frac{(cf - c2) \cdot vf}{(c1 - c2)} \)$
     - $\( y = vf - x \)$

3. **Validación y Resultados**:
   - **Cálculo**: Calcula los volúmenes $\( x \)$ y $\( y \)$ necesarios.
   - **Validación**: Verifica si alguno de los volúmenes calculados es negativo, lo que indicaría que la mezcla no es posible con las concentraciones proporcionadas. Si esto ocurre, se genera un error.
   - **Excepciones**:
     - Maneja el caso en que las concentraciones de las soluciones (`c1` y `c2`) son iguales, lo cual causaría una división por cero.
     - Captura y muestra cualquier otro error generado (por ejemplo, si los volúmenes resultantes son negativos).

4. **Impresión de Resultados**:
   - Imprime el volumen de cada solución que debe mezclarse para obtener la solución final deseada, con dos decimales de precisión.

