![Logo UCN](images/60x60-ucn-negro.png)
# Laboratorio 01: Cálculo de frecuencia peatonal 


## 1. Introducción 
<div style="text-align: justify;">
El problema se enmarca en un interesante experimento que busca analizar cómo la densidad de personas y el ancho de las puertas afectan el tiempo de evacuación en un corredor con dos accesos, correspondientes a puerta 1 y puerta 2. 

La experimentacion plantea realizar nueve carreras, donde se variarán diferentes parámetros para obtener resultados significativos y generalizables. El corredor utilizado en el experimento ha sido diseñado cuidadosamente para asegurar la simetría entre ambos lados. Esto significa que las condiciones en los lados izquierdo y derecho del corredor son iguales, permitiendo la realización de carreras desde ambas puertas en una secuencia alterna. La simetría del corredor ofrece varias ventajas, entre ellas, reducir el tiempo de preparación entre carreras individuales y minimizar la interferencia de factores externos que puedan sesgar los resultados.
Cada carrera en el corredor experimental representa un escenario único de densidad de personas y ancho de las puertas. Se variarán las cantidades de individuos presentes en el corredor y se ajustarán los anchos de las puertas 1 y 2 para recrear diferentes situaciones de alta densidad. La densidad de personas se define como la cantidad de individuos por unidad de área del corredor y se manipula cuidadosamente en cada carrera para representar diversos escenarios realistas.
El tiempo de evacuación se medirá desde el momento en que se dé la señal de inicio hasta que el último peatón haya abandonado completamente el corredor. Durante la evacuación, se registrarán diversos parámetros para analizar el flujo de personas, como la velocidad de desplazamiento a través de las puertas y el espacio que ocupan en el corredor.
Además de analizar los tiempos de evacuación, el experimento también se enfoca en evaluar la eficiencia en el uso del espacio del corredor durante la evacuación. Esto implica observar si la densidad de personas influye en la formación de congestiones o atascos en algún punto del corredor. Estos datos serán fundamentales para comprender cómo el ancho de las puertas y la cantidad de personas en el corredor impactan en la fluidez de la evacuación y en la seguridad de los peatones.
Los resultados obtenidos de las nueve carreras serán analizados y comparados exhaustivamente para identificar tendencias y relaciones significativas entre los factores estudiados. El análisis de los datos permitirá obtener conclusiones valiosas sobre cómo la densidad de personas y el ancho de las puertas interactúan para influir en el tiempo de evacuación y en la eficiencia del proceso.
Este tipo de investigación es esencial para mejorar el diseño y la gestión de espacios públicos, especialmente en áreas con alta afluencia de personas, como estadios, centros comerciales o eventos masivos. Además, los resultados podrían tener implicaciones prácticas en la planificación de medidas de seguridad y evacuación en caso de emergencias o desastres naturales.
En resumen, el experimento busca estudiar cómo la densidad de personas y el ancho de las puertas influyen en el tiempo de evacuación en un corredor simétrico con dos puertas. Se realizarán nueve carreras con diferentes escenarios de densidad y anchos de puertas para obtener resultados significativos. Los datos recopilados serán analizados minuciosamente para obtener conclusiones relevantes para el diseño de espacios públicos y medidas de seguridad en situaciones de alta afluencia de personas.

### 1.1 Justificación 
La programación científica desempeña un papel fundamental en el cálculo de la frecuencia peatonal, especialmente en el campo de la investigación urbana y la ingeniería de transporte. El estudio y análisis sistemático de la cantidad de personas que caminan por diferentes áreas urbanas proporciona información valiosa para la toma de decisiones basadas en evidencia y la planificación efectiva de la movilidad urbana.
Una de las principales ventajas de utilizar la programación científica en el cálculo de la frecuencia peatonal es la capacidad de procesar grandes cantidades de datos de manera rápida y eficiente. Con el crecimiento de las ciudades y el aumento de la población, la cantidad de información recolectada sobre el flujo peatonal ha aumentado significativamente. La programación científica permite manejar esta gran cantidad de datos y realizar análisis complejos para identificar patrones y tendencias en el movimiento de peatones.
Además, la programación científica facilita la implementación de modelos matemáticos y algoritmos de aprendizaje automático para predecir la frecuencia peatonal en diferentes escenarios. Mediante la simulación computacional, es posible proyectar el impacto de cambios urbanos propuestos, como la construcción de nuevos edificios o la implementación de nuevos sistemas de transporte, en la movilidad peatonal. Esto es especialmente relevante en la planificación de infraestructuras y en la adopción de medidas para mejorar la seguridad y accesibilidad peatonal en áreas urbanas congestionadas.
La integración de datos provenientes de diversas fuentes también es un aspecto clave que la programación científica facilita. Sensores de conteo de personas, sistemas de transporte público y datos demográficos pueden combinarse y analizarse en conjunto para obtener una visión integral de la movilidad peatonal en un área específica. Esta visión holística permite a los urbanistas y planificadores tomar decisiones informadas y basadas en datos para optimizar la infraestructura y los servicios urbanos, mejorando la calidad de vida de los ciudadanos.
La precisión y la velocidad de la programación científica también juegan un papel crucial en el cálculo de la frecuencia peatonal. Los modelos matemáticos y algoritmos implementados pueden ajustarse y optimizarse rápidamente, lo que permite a los investigadores realizar múltiples escenarios y evaluar diferentes estrategias de planificación con eficiencia. Esto contribuye a una toma de decisiones más ágil y efectiva en la mejora de la movilidad urbana.
En conclusión, la programación científica se presenta como una herramienta poderosa en el cálculo de la frecuencia peatonal. Su capacidad para procesar grandes volúmenes de datos, modelar escenarios futuros y facilitar la integración de diversas fuentes de información, hace posible tomar decisiones más informadas en la planificación urbana. La programación científica impulsa la creación de ciudades más amigables con los peatones, mejorando la calidad de vida de los ciudadanos y promoviendo una movilidad urbana más sostenible y eficiente.

### 1.3 Objetivos 

**Objetivo General**

Decribir objetivo general

**Objetivos específicos**

1. Primer objetivo
2. Segundo objetivo
3. Tercer objetivo

## 2. Marco teórico (800 caracteres)

Librerias:

**Matplotlib**: 

Estructuras a utilizar:

**Listas**: Las listas son colecciones ordenadas y mutables de elementos que pueden contener diferentes tipos de datos. Se definen utilizando corchetes "[]", y los elementos se separan por comas. Para la experimentacion, se hara uso de listas con el fin de poder extraer y almacenar las diversas coordenadas e informacion sobre los datos existentes en la base de datos entregada

**Diccionarios**: Los diccionarios son colecciones de pares clave-valor no ordenadas. Cada elemento del diccionario tiene una clave única asociada a un valor. Se definen utilizando llaves "{}". La importancia de esta estructura radica en la capacidad de poder asociar un dato obtenido con las frecuencias que se obtienen de este.

**Cadenas de Texto**: Las cadenas son secuencias de caracteres y se pueden tratar como estructuras de datos en Python. Se definen utilizando comillas simples o dobles. Por ejemplo: mi_cadena = "Hola, mundo!".

Herramientas:

**Anaconda**: Anconda representa una de las muchas aplicaciones que permiten la interacion con el lenguaje de programacion python, la cual entrega un entorno de visualizacion amigable para el usuario, ademas de una gran cantidad de librerias y funciones, por otro lado tambien permite la creacion de diversos ambiente para diferenciar entre proyectos.

**Visual Studio**: Visual Studio es un entorno de desarrollo integrado (IDE), el cual brinda una plataforma completa y versátil para construir, depurar y desplegar aplicaciones de software. Con soporte multiplataforma y para diversos lenguajes de programación entre los que se descataca Python, por otro lado tambien ofrece una interfaz gráfica de usuario intuitiva que facilita la creación de proyectos. Además, cuenta con herramientas de depuración y pruebas, por otro lado tambien integra interacciones con la nube como lo seria Github. Para esta experimentacion se hara el desarrollo de la aplicacion en lenguaje python, para luego ser exportada a gihub.

**Ipython**: IPython es un entorno interactivo de Python que proporciona una experiencia de shell mejorada en comparación con la consola de Python estándar. IPython se ejecuta en la línea de comandos y ofrece características adicionales, como autocompletado, historial de comandos, capacidades avanzadas de visualización de datos y soporte para la ejecución de comandos de sistema operativo. Esta se encuentra relacionada con Visual studio, debido a que  IPython se puede utilizar en conjunción con el entorno de desarrollo integrado de visual studio, obteniendo una experiencia mas completa.

**Github**:
GitHub es una plataforma de alojamiento y colaboración para el desarrollo de software, donde los desarrolladores pueden almacenar, gestionar y compartir su código fuente y archivos de proyectos. Esta es reconocida por facilitar la colaboración en proyectos y la comunidad de código abierto. Sus características clave incluyen control de versiones con Git, repositorios públicos o privados, herramientas para colaboración efectiva, seguimiento de problemas y errores, ramas para desarrollo independiente y la integración continua para automatizar pruebas y despliegues. GitHub se ha convertido en una herramienta esencial para el desarrollo colaborativo y el acceso a una amplia gama de proyectos y recursos de desarrollo.

## 3. Materiales y métodos

*Materiales y Métodos*

*1. Descripción del dataset:*
El conjunto de datos utilizado en este laboratorio se denomina "UNI_CORR_500_01.txt". Este archivo de texto contiene un total de 25.536 muestras captadas por una cámara. Cada muestra está compuesta por los siguientes elementos:
- ID: Identificador único de la persona enfocada por la cámara.
- Frame: Número del frame correspondiente a la muestra.
- Coordenadas X, Y y Z: Posiciones espaciales de la persona..

*2. Procedimiento del laboratorio:*
El laboratorio se llevará a cabo en el entorno de desarrollo de Visual Studio Code, utilizando el lenguaje de programación Python. Los pasos para realizar el experimento son los siguientes:

   a. Carga de datos: Se leerá el archivo "UNI_CORR_500_01.txt" en Python utilizando las bibliotecas adecuadas para el manejo de archivos de texto.

   b. Almacenamiento de datos: Se almacenarán las coordenadas X, Y y Z de cada muestra en estructuras de datos apropiadas, como listas o diccionarios.

   c. Cálculo de repeticiones: Se identificarán las coordenadas X, Y y Z que más se repiten en el conjunto de datos.

   d. Identificación de patrones: Se analizará si existen patrones o tendencias en las coordenadas que se repiten con mayor frecuencia.

   e. Descripción de resultados: Se generará un resumen con las coordenadas X, Y y Z que tienen mayor frecuencia de aparición, identificando posibles áreas de concentración de personas en los frames capturados.

*3. Descripción del experimento:*
El objetivo principal del experimento es analizar y determinar qué coordenadas X, Y y Z tienen una mayor repetición en las muestras captadas por la cámara. Esto permitirá identificar áreas de mayor concentración de personas en el entorno monitoreado.

El experimento se llevará a cabo mediante la implementación de un código en Python en el entorno de Visual Studio Code. Se realizarán los cálculos estadísticos necesarios para determinar qué coordenadas son las más frecuentes en el conjunto de datos.

Los resultados obtenidos en el análisis de las coordenadas permitirán inferir sobre la posible existencia de áreas de mayor afluencia de personas, lo cual puede ser relevante para la planificación y toma de decisiones en el ámbito de la gestión del espacio urbano o la seguridad.

Es importante mencionar que el éxito del experimento depende de la correcta carga y procesamiento de los datos, así como de la precisión en los cálculos estadísticos realizados. La reproducibilidad de los resultados está garantizada por el uso de un lenguaje de programación y entorno de desarrollo específicos, lo que permite compartir y replicar el código para futuros análisis.

## 4. Resultados obtenidos

Indicar si el funcionamiento es correcto, agregar métricas de rendimiento como tiempo de ejecución y cantidad de memoria utilizada.

| Tipo de Experimento   | Tiempo de ejecucion (mseg) |  Memoria utilizada (Mb) |
|-----------------------|----------------------------|-------------------------|
| Programa Uno (p01.py) |                            |                         |
| Programa Dos (p02.py) |                            |                         |



<img src="images/column-chart.png" width="300">

## 5. Conclusiones

Apartir de los resultados inferir nuevo conocimiento. Por ejemplo, al ultilizar concatenación de listas cono "+" el programa es menos eficiente en términos de tiempo que utilizar 'append()'.





</div>