
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
* Otras métricas son menos sensibles a valores atípicos y a distribuciones inusuales y, por lo tanto, son más robustas

# Estimación de la variabilidad

La localización es sola una dimensión para extraer el resumen de una característica. Una segunda dimensión, la variabilidad, también conocida como una dispesión, mide el grado de agrupación o dispesión de los valores de los datos.


## Términos clave de métricas de variabilidad

__Desviaciones__ Diferencias entre los valores observados y la estimación de la localización (errores, residuales).
__Varianza__ Suma de los cuadrados de la desviaciones de la media al cuadrafo y dividida por n-1, donde n es el número de valores de datos.(error cuadrático medio)
__Desviación estándar__ Raíz cuadrada de la varianza.
__Desviación media absoluta__ Media de los valores absolutos de las desviaciones de la media.(normal L1, norma Manhattan)
__Desviación absoluta mediana de la mediana__ Media de los valores absolutos de las desviaciones de la mediana.
__Rango__ La diferencia entre el mayor y el menor valor de un conjunto de datos.
__Estadísticos ordinales__ Métricas basadas en los valores de datos ordenados de menor a mayor.(rangos)
__Percentil__ Valor tal que le _P_ por ciento de los valores toma este valor o un valor inferior y para (100-P) el porcentaje toma este valor o un valor superior. (cuantil)
__Rango intercuartil__ Diferencia entre el percentil 75 y el percentil 25. (IQR)

## Desviación estándar y estimaciones relacionadas

La estimación de variabilidad más conocidas son la varianza y la desviación estándar, la  desviación estándar es mucho más fácil de interpretar que la varianza, ya que está en la misma escala que los datos originales.

La varianza, la desviación estándar y la desviación absoluta mediana son robustas a valores atípicos y extremos. La varianza y la desviación estándar son especialmente sensibles a los valores atípicos, ya que se basan en las desviaciones al cuadrado.

Una estimación robusta de la variabilidad es la desviación absoluta mediana de la mediana o MAD.

## Estimación basada en percentiles

Un enfoque diferente para estimar la dispersión se centra en observar la distribución de los datos ordenados. Los esdísticos que tienen como base los datos ordenados(clasificados) se denominan estadísticos de orden(order statistics)

La desviación estándar es casi dos veces mayor que la MAD(en R por defecto, la escala MAD se ajusta para estar en la misma escala que la de la media). Esta hecho no es sorprendente, ya que la desviación estándar es sensible a valores atípicos.

## Ideas clave

* La varianza y la desviación estándar son los estadísticos de variabilidad más difundidos y de los que más se informa de manera rutinaria.
* Ambos son sensibles a los valores atípicos.
* Entre las métricas más robustas se encuentran la desviación absoluta media, la MAD y los percentiles

# Exproración de la distribución de datos

## Términos clave de la exploración de la distribución

__Diagrama de caja__ Permite visualizar de forma rápida la distribución de datos.(diagrama de caja y bigotes)
__Tabla de frecuencias__ Registro del recuento de valores de datos númericos que caen en un conjunto de intervalos.(contenedores)
__Histograma__ El diagrama de la tabla de frecuencias con los contenedores o intervalos en el eje x y el recuento (proporción) en el eje y. Aunque los gráficos de barra son visualmente similares, no deben confundirse con los histogramas.
__Diagrama de densidad__ Versión suavisada del histograma, a menudo basada en una estimación de la densidad del núcleo (Estimador de densidad de Kernel)

## Percentiles y diagramas de caja
La cultura popular ha acuñado el término de los uno por ciento para referirse a las personas con una riqueza superior al percentil 99

## Tablas de frecuencias e histogramas

La tabla de frecuencias de una variable divide el rango de la variable en segmentos igualmente espaciados y nos dice cuántos valores caen dentro de cada segmento.

Tanto las tablas de frecuencias como los percentiles, extraen el resumen de los datos mediante la creación de contenedores. En general, los cuartiles y deciles tendrán el mismo número de valores en cada contenedor, pero los tamaños de los contenedores serán diferentes. La tabla de frecuencias por el contrario, tendrá diferente número de valores en los contenedores y el tamaño de los contenedores será el mismo para todos.

El histograma es un modo de visualizar la tabla de frecuencias, con contenedores en el eje x y los valores de los datos en el eje y.

Los histogramas se representan gráficamente teniendo en cuenta que:
* Los contenedores vacíos se incluyen en el gráfico
* Los contenedores tienen la misma anchura
* El número de contenedores(o, de manera equivalente, el tamaño del contenedor) depende del usuario.
* Las barras son contiguas: no se muestran espacios vacíos entre las barras, a menos que hay aun contenedor vacío

## Momentos de la distribución estadística

En teoría esta estadística, la localización y la variabilidad se conocen como el primer y segundo momentos (moments) de una distribución. Los momentos tercero y cuarto se denominan asimetría (skewness) y curtosis (kurtosis).

La asimetría se refiere a si los datos están sesgados hacia valores mayores o menores, y la curtosis indica la propensión de los datos a tener valores extremos.

# Diagramas y estimación de la curva de densidad

Muestra la distribución de los valores de los datos mediante una línea continua. Se puede considerar como un histograma suavisado, aunque normalmente se calcula directamente a partir de los datos a través de una estimación de la densidad del núcleo.

## Ideas clave

* El diagrama de densidad es una versión estimada del histograma. Requiere una función para estimar el diagrama basado en datos.
* Un diagrama de caja también da una idea rápida de la distribución de los datos. A menudo se utiliza en visualizaciones paralelas para comparar distribuciones
* La tabla de frecuencias es una versión tabular de las frecuencias de lso resultados que se encuentran en un histograma
* EL histograma de frecuencias proporciona de un vistazo una idea de la distribución de los datos

# Exploración de datos binarios y categóricos

## Términos clave de la exploración de datos categóricos

__Moda:__ Categoría o valor que ocurre con más frecuencia en un conjunto de datos
__Valor esperado:__ Cuando las categorías se pueden asociar con un valor númerico, el valor esperado propociona un valor promedio basado en la probalidad de ocurrencia de una categoría
__Gráficos de barras:__ frecuencia o proporción de cada categoría representada en barras
__Gráficos en forma de la tarta:__ frecuencia o proporción de cada categoría representada en forma de cuña de un pastel.

