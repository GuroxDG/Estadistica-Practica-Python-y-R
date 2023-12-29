
# Elementos de datos estructurados

## Términos clave de los tipos de datos

__Númericos__

Datos que se expresan en una escala númerica
* __Continuos__: Datos sque pueden adoptar cualquier valor dentro de un intervalo (Sinónimos: intervalo, flotante).
* __Discretos__: Datos que solo pueden adoptar valores enteros, como valores contables.

__Categóricos__
Datos que solo pueden adoptar un conjunto específico de valores que representan un conjunto de categorías posibles.
* __Binarios__: Son un caso especial de dato categóricos con solo dos categorías de valores, por ejemplo verdadero/falso
* __Ordinales__: Datos categóricos que tienen un orden explícito

la identificación explícita de datos como categóricos, como algo diferente al texto, ofrece algunas ventajas:
* Los datos ordinales se pueden representar mediante _ordered.factor_ en __R__, conservando el orden específico por el usuario en gráficos, tablas y modelos.
* El almacenamiento y la indexación se pueden oprimizar,
* Los posibles valores que puede adoptar una variable categórica dada, se aplican al software.

## Ideas clave
* Los datos se clasifican generalmente por tipos
* En los tipos de datos están incluidos los númericos y categóricos

# Datos rectangulares

Los datos rectangulares son el término general asociado a una matriz bidimensional con filas que indican registros (casos) y columnas que indican características (variables).

## Términos clave de los datos rectangulares

__Marco de datos__
Los datos rectangulares son la estructura básica de datos para modelos estadísticos y de aprendizaje automático

__Característica__
Una columna de una tabla se denomina generalmente característica (atributo, entrada, predictor, variable)

__Resultado__
Muchos proectos implican pronosticar un resultado (outcome) (variable dependiente, respuesta, objetivo, salida)

__Registros__
Una fila dentro de una tabla (caso, ejemplo, isntancia, observación, muestra)

## Estructura de datos no rectangulares

* Los datos de serie de tiempo registran mediciones sucesivas de la misma variable. Es la materia prima de los métodos de pronóstico estadístico.
* Las estructuras de datos espaciales, que se utilizan en cartografía y análisis de la localización.
* Las estructuras de datos en forma de gráfico se utilizan para representar relaciones físicas, sociales y abstractas.

# Estimación de la localización

## Términos clave de la estimación de la localización

__Media__ 
Suma de todos los valores dividida por el número de valores (promedio)

__Media ponderada__ 
Suma de todos los valores multiplicados por cada ponderación y dividida por la suma de las ponderaciones

__Mediana__ Valor tal que la mitad del número de datos se encuentra por encima y la otra mitad por debajo de dicho valor (percentil 50)

__Percentil__ Valor tal que el __P__ por ciento de los datos se encuentran por debako del mismo (cuantil)

__Mediana ponderada__ Valor tal que la mitad de la suma de las ponderaciones se encuentra por encima y la otra mitad por debajo de los datos ordenados

__Media recortada__ El promedio de todos los valores después de eliminar un número fijo de valores extremos (media truncada)

__Robusto__ insensible a valores extremos

__Atípico__ Valor de un dato que es muy diferente de la mayoría de los valores de los datos (valor extremo)

