
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

## Media

La estimación más elemental para la localización es el valor medio o  promedio(average). La media es la suma de todos los valores dividida por el número de valores.

La variación de la media se conoce como __media truncada(trimmed mean)__, que se calcula ignorando un número fijo, en cada extremo, de valores ordenados y a continuación se calcula el promedio de los valores restantes. La media truncada elimina la influencia de los valores extremos.

Otro tipo de media es la __media ponderada (weighted mean)__, que se calcula multiplicando cada valor de datos _xi_ por el peso _wi_ especificado por el usuario y dividiendo su suma por la suma de las ponderaciones.

Hay dos motivos fundamentales para usar una media ponderada:
* Algunos valores son intrinsecamente más variables que otros, y las observaciones muy variables reciben un peso menor.
* Los datos recopilados no representan por igual a los diferentes grupos que nos interesa medir.

## Estimación de medianas robustas

La mediana es el valor central de una lista de datos ordenados de menor a mayor.

### Valores atípicos

A la mediana se la conoce como una estimación robusta de la localización, ya que no está influenciada por valores atípicos (outliers) que podrían sesgar los resultados. 

* Cuando los valores atípicos son el resultado de datos incorrectos, la media dará como resultado una estimación deficiente de la localización, mientras que la mediana seguirá siendo válida.

La mediana no es la única estimación robusta de la localización, de hecho la media truncada se usa habitualmente para evitar la influencia de valores atípicos.

## Ideas clave

* La métrica básica para la localización es la media, pero puede ser sensible a valores atípicos
* Otras métricas son menos sencibles a valores atípicos y a distribuciones inusuales y, por lo tanto, son más robustas

