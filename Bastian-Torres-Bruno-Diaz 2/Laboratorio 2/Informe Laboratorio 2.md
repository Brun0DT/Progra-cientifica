![Logo UCN](images/60x60-ucn-negro.png)
# Laboratorio 01: Cálculo de frecuencia peatonal 
## 1. Introducción 
<div style="text-align: justify;">
El problema se enmarca en un interesante experimento que busca analizar cómo la densidad de personas y el ancho de las puertas afectan el tiempo de evacuación en un corredor con dos accesos, correspondientes a puerta 1 y puerta 2. 
La experimentacion plantea realizar nueve carreras, donde se variarán diferentes parámetros para obtener resultados significativos y generalizables. El corredor del experimento presenta una simetría entre ambos lados, permitiendo la realización de carreras desde ambas puertas afectando positivamente reduciendo el sesgo en lo resultados.
Cada carrera en el corredor experimental representa un escenario único de densidad de personas y ancho de las puertas. Se variarán las cantidades de individuos presentes en el corredor y se ajustarán los anchos de las puertas 1 y 2 para recrear diferentes situaciones de alta densidad. La densidad de personas se define como la cantidad de individuos por unidad de área del corredor y se manipula cuidadosamente en cada carrera para representar diversos escenarios realistas.
Los resultados obtenidos de las nueve carreras serán analizados y comparados exhaustivamente para identificar tendencias y relaciones significativas entre los factores estudiados. El análisis de los datos permitirá obtener conclusiones valiosas sobre cómo la densidad de personas y el ancho de las puertas interactúan para influir en el tiempo de evacuación y en la eficiencia del proceso. En el presente informa se tendran en cuenta 2 carreras, las cuales tendran una direccion de derecha a izquierda y ademas las medidas de las puertas para cada una corresponderan a 1 metro para la primera puerta y 5 para la segunda, por otro lado el segundo experimento presentara unas medidas de 5 y 4 metros


### 1.1 Justificación 
La programación científica desempeña un papel fundamental en el cálculo de la frecuencia peatonal, especialmente en el campo de la investigación urbana y la ingeniería de transporte. El estudio y análisis sistemático de la cantidad de personas que caminan por diferentes áreas urbanas proporciona información valiosa para la toma de decisiones basadas en evidencia y la planificación efectiva de la movilidad urbana.
Una de las principales ventajas de utilizar la programación científica en el cálculo de la frecuencia peatonal es la capacidad de procesar grandes cantidades de datos de manera rápida y eficiente. Con el crecimiento de las ciudades y el aumento de la población, la cantidad de información recolectada sobre el flujo peatonal ha aumentado significativamente. La programación científica permite manejar esta gran cantidad de datos y realizar análisis complejos para identificar patrones y tendencias en el movimiento de peatones.
Además, la programación científica facilita la implementación de modelos matemáticos y algoritmos de aprendizaje automático para predecir la frecuencia peatonal en diferentes escenarios. Mediante la simulación computacional, es posible proyectar el impacto de cambios urbanos propuestos, como la construcción de nuevos edificios o la implementación de nuevos sistemas de transporte, en la movilidad peatonal. Esto es especialmente relevante en la planificación de infraestructuras y en la adopción de medidas para mejorar la seguridad y accesibilidad peatonal en áreas urbanas congestionadas.
La integración de datos provenientes de diversas fuentes también es un aspecto clave que la programación científica facilita. Sensores de conteo de personas, sistemas de transporte público y datos demográficos pueden combinarse y analizarse en conjunto para obtener una visión integral de la movilidad peatonal en un área específica. Esta visión holística permite a los urbanistas y planificadores tomar decisiones informadas y basadas en datos para optimizar la infraestructura y los servicios urbanos, mejorando la calidad de vida de los ciudadanos.
La precisión y la velocidad de la programación científica también juegan un papel crucial en el cálculo de la frecuencia peatonal. Los modelos matemáticos y algoritmos implementados pueden ajustarse y optimizarse rápidamente, lo que permite a los investigadores realizar múltiples escenarios y evaluar diferentes estrategias de planificación con eficiencia. Esto contribuye a una toma de decisiones más ágil y efectiva en la mejora de la movilidad urbana.
En conclusión, la programación científica se presenta como una herramienta poderosa en el cálculo de la frecuencia peatonal. Su capacidad para procesar grandes volúmenes de datos, modelar escenarios futuros y facilitar la integración de diversas fuentes de información, hace posible tomar decisiones más informadas en la planificación urbana. La programación científica impulsa la creación de ciudades más amigables con los peatones, mejorando la calidad de vida de los ciudadanos y promoviendo una movilidad urbana más sostenible y eficiente.

### 1.3 Objetivos 

**Objetivo General**:
Realizar un análisis de patrones de concentración de personas en un entorno monitoreado a través del procesamiento y análisis de datos de coordenadas capturados por una cámara, utilizando programación científica en Python.

**Objetivos específicos**

1. Cargar y preprocesar el conjunto de datos "UNI_CORR_500_01.txt" en el entorno de Visual Studio Code utilizando el lenguaje de programación Python.
2. Almacenar las coordenadas X, Y y Z de las muestras capturadas en estructuras de datos apropiadas para su posterior análisis.
3. Identificar las coordenadas que se repiten con mayor frecuencia en las muestras capturadas, lo que permitirá determinar las áreas de mayor concentración de personas en el entorno monitoreado.

Estos objetivos permitirán llevar a cabo un análisis detallado de la frecuencia de aparición de coordenadas y la identificación de patrones de concentración de personas, contribuyendo así a una mejor comprensión de la distribución espacial de las personas en el área monitoreada.
## 2. Marco teórico (800 caracteres)
**Librearia:**

**Matplotlib**: Librería para gráficos y visualización de datos.

**Time**: Medición de tiempo en ejecución.

**Pandas**: Análisis y manipulación de datos con DataFrames y Series.

**Estructuras:**

**Listas**: Colecciones ordenadas y mutables.

**Cadenas de Texto**: Secuencias de caracteres.

**Herramientas:**

**Anaconda**: Plataforma con librerías y ambientes separados.

**Visual Studio**: IDE completo para desarrollo de software.

**GitHub**: Plataforma de alojamiento y colaboración para desarrollo de código.

## 3. Materiales y métodos

En este laboratorio se utilizarán diversos elementos para llevar a cabo el análisis de patrones de concentración de personas a partir de un conjunto de datos capturados por una cámara. A continuación, se detallará cada elemento y la metodología a seguir.
En el desarrollo de este laboratorio, se hará uso de diversos elementos esenciales para llevar a cabo un análisis detallado de patrones de concentración de personas. En primera instancia, se utilizará un archivo de texto denominado "UNI_CORR_500_01.txt", el cual contiene una colección de 25.535 muestras de coordenadas. Estas coordenadas han sido capturadas mediante una cámara en un entorno específico, permitiendo obtener información detallada sobre la ubicación de las personas en dicho espacio. Es importante resaltar que cada observación contenida en el dataset abarca no solo las coordenadas en los ejes X, Y y Z, sino que también incorpora datos fundamentales como el ID de la persona enfocada y el número de Frame de la cámara correspondiente. Esta combinación de información brinda una visión completa de las posiciones de las personas en relación con su identificación y el momento de captura. 
Por otro lado la representacion grafica de el espacio existente para el paso peatonal se evidencian en la siguiente ilustraciones, la cual presenta un largo de 18 metros, siendo el medio el punto (0,0).
<center>
<img src="images/Dimensiones.jpeg" width="400">

*Ilustracion 1: Dimensiones paso peatonal*
</center>
Para el procedimiento de este laboratorio se realizarán varias etapas cruciales. En primer lugar, emplearemos la plataforma Visual Studio Code junto con el lenguaje de programación Python para cargar el archivo "UNI_CORR_500_01.txt". Una vez completado el proceso de carga extraeremos las coordenadas X e Y del conjunto de datos y las almacenaremos en estructuras de listas de Python, lo que simplificará su manipulación y análisis subsiguiente. A continuación, procederemos al análisis de frecuencia para determinar qué conjuntos de coordenadas X, Y y (X, Y) se repiten con mayor frecuencia, lo que permitirá identificar patrones significativos de concentración de personas en el entorno observado. A continuación, se realizará la conversión de las coordenadas de metros a pixeles, lo cual nos brindará una representación más precisa de la distribución espacial. Posteriormente, emplearemos estos datos transformados en una matriz la cual será utilizada para generar un mapa de calor, visualizando claramente las zonas de mayor afluencia de personas. Este mapa de calor será una herramienta valiosa para comprender de manera intuitiva los patrones de movimiento y concentración en el entorno monitoreado, lo que proporcionará información clave para la toma de decisiones en la planificación urbana y la optimización de la movilidad peatonal. En resumen, este laboratorio fusiona el poder de la programación científica con la visualización de datos para obtener conocimientos profundos sobre la frecuencia peatonal y su distribución en un entorno específico.
En resumen, la secuencia de pasos sería la siguiente:
1. Cargar el archivo "UNI_CORR_500_01.txt" en el entorno de Visual Studio Code para su acceso y manipulación.
2. Extraer minuciosamente las coordenadas X e Y de cada observación registrada en el conjunto de datos, y almacenar estas coordenadas en listas o diccionarios apropiados.
3. Calcular rigurosamente la frecuencia de aparición de cada conjunto único de coordenadas (X, Y) en el conjunto de datos, lo que permitirá comprender qué patrones son más comunes en el entorno monitoreado.

4. Identificar con precisión las coordenadas que presentan mayor frecuencia de aparición, lo que nos brindará una visión clara de las áreas de mayor concentración de personas en el espacio observado.
5. Generar visualizaciones gráficas como mapas de calor, utilizando una matriz con las coordenadas transformadas en unidades de píxeles, para ilustrar de manera efectiva los patrones de concentración peatonal en el entorno. Estas representaciones visuales facilitarán la interpretación y comprensión intuitiva de los resultados obtenidos.
Al llevar a cabo esta secuencia de pasos, lograremos analizar y visualizar de manera precisa la frecuencia peatonal en el entorno estudiado, proporcionando valiosa información para la toma de decisiones en la planificación urbana y la mejora de la movilidad peatonal.

*3. Descripción del experimento:*
El experimento consiste en analizar las coordenadas capturadas por una cámara en un entorno específico para identificar patrones de concentración de personas. A través del uso de programación científica en Python y herramientas de análisis de datos, se pretende determinar las áreas en las que las personas se agrupan con mayor frecuencia. Este análisis proporcionará información valiosa para la toma de decisiones en la planificación urbana y la mejora de la movilidad en áreas de alta concentración peatonal. El experimento busca contribuir a la comprensión de los patrones de comportamiento de las personas en espacios urbanos, lo que puede tener implicaciones significativas en el diseño de infraestructuras y la implementación de medidas de seguridad y accesibilidad.

## 4. Resultados obtenidos

Para obtener una conclusion certera sobre la realizacion del experimento se realizaron 2 archivos .py donde se utilizaron distintos metodos de obtencion y graficado de los datos, en el archivo "Codigo pandas.py", se utilizo la libreria pandas, para el cargado y visualizacion de los datos, donde se realizaron filtros correspondientes para las columnas a utilizar (x e y), en el caso del segundo codigo, se extrajo la informacion de los datos, y se utilizaron listas y variables, en conjunto con ciclos for para el cargado de la informacion en los graficos.

En la tabla a continuacion se puede observar como el primero archivo "Codigo pandas.py", presenta una mayor eficiencia computacional, evidenciandose que genera un menor tiempo de utilizacion, en comparacion al codigo que no utiliza la libreria pandas. Por otro lado, se observa como el uso de la libreria pandas genera una mayor utilizacion de memoria que el no uso de esta.
<center>

| Tipo de Experimento   | Tiempo de ejecucion (mseg) |  Memoria utilizada (MB) |
|-----------------------|----------------------------|-------------------------|
| Programa Uno (Codigo 1.py) |        255.5286            |           31.777        |
| Programa Dos (Codigo 2.py) |        303.28607           |           44.515        |

*Tabla 1: Tiempos de ejecucion*
</center>

En cuanto a los resultados obtenidos, se puede concluir que se logro obtener los dos mapas de calor  revelaría cómo se distribuyen las frecuencias de tránsito a lo largo de dicho pasillo correspondientes a cada experimentacion realizada, donde para el caso de la carrera numero 1 se tiene la primera puerta, con un tamaño de puerta de entrada de 1 metro y de salida con 5 metros, se pudo observar como las personas, al entrar por la derecha, se van separando entre ellas debido a que una persona se encuentra detenida en la mitad del camino y todas la evitan manteniendo asi su espacio personal y a medida que estan se van acercando a la puerta de salida que se encuentra en la izquierda con el tamaño de 5 metros, se nota como las personas mantienen su separacion ademas de una distancia prudente con las paredes a su alrededor, por otro lado tambien se concluye que como la entrada es de un tamaño pequeño, se produce que entre una cantidad de personas que no sea suficiente para el llenado completo del pasillo ademas de que el espacio ocupado por la persona en el centro reduce el area por donde podrian entrar las personas dejando disponible solo los costados.

Para los resultados de la segunda carrera, se realizar variacion en el tamaño de las puertas donde la primera presenta un tamaño de 5 metros y la segunda de 4 metros, observandose en el mapa de calor como las personas entran con un mayor flujo y el pasillo se mantiene lleno, estando mucho mas cercas una de las otras, debido a que en la ilustracion no se evidencian separaciones entre los puntos. En cuanto a la salida, se observa como a medida que se acercan al final las personas se van juntando a causa del menor tamaño de la puerta lo que podria ralentizar el paso de estas, ya que la agrupacion repercutiria a las personas que esten detras de estas.

Por otro lado, también se puede observar cómo los datos se muestrean únicamente hasta ciertas coordenadas en el eje x, lo que indica que la cámara no captura una vista completa del pasillo. Además, en el mapa de calor se puede apreciar cómo las personas se desplazan a lo largo del tiempo.

<center>


<img src="images/Mapa_de_calor.png" width="400">

*Ilustracion 3: Mapa de calor*
</center>

## 5. Conclusiones

Basándonos en los resultados obtenidos, es posible extraer valiosas inferencias que contribuyen al conocimiento. Por ejemplo, al emplear un bucle 'for' para buscar el valor máximo justo antes de un comando 'print', se identifica una desaceleración en la ejecución del código. En contraste, la realización de la búsqueda del valor máximo con antelación al comando 'print' demuestra ser más óptima en términos de tiempo de ejecución.
Estos descubrimientos enfatizan la relevancia de la optimización en la programación y cómo decisiones aparentemente pequeñas en la estructura del código pueden tener un impacto significativo en el rendimiento general. La experimentación y análisis minucioso de diferentes enfoques son esenciales para identificar las mejores prácticas que garanticen una ejecución eficiente y un uso optimizado de recursos computacionales. En última instancia, la inferencia de nuevo conocimiento a partir de los resultados refuerza la importancia de la constante revisión y mejora de los procesos de programación.

Por otro lado tambien se logra identificar que la creacion de variables adicionales y ciclos for adicionales, generan que se demore mucho mas el sistema en procesar el codigo, esto se observa en el codigo 2 debido a que la lectura del archivo corresponde a variables auxiliares, que no son tan necesarias para luego ser leidas en un ciclo for apartado del inicial, cosa que no pasa en el codigo 1 ya que todo es obtenido en el primer ciclo for.

Finalmente podemos concluir que se lograros los objetivos especificos y generales, debido a que se pude extraer la informacion del archivo entregado, logrando representar los puntos criticos mas utilizados por los peatones, pudiendo representar esto en la matriz de frecuencias para lograr obtener un mapa de calor, que nos muestre visualmente como se distribuyen estos puntos criticos, a lo largo del pasillo.

Con respecto al tiempo y memoria de procesamiento se pudo concluir que el uso de la libreria pandas produce que una
menor utilizacion de tiempo para el procesamiento de la impresion y calculo, esto se puede deber a que la accesibilidad a los datos es mucho mas directa, porque de la tabla entregada por pandas se puede obtener todo tipo de informacion sin realizar algun tipo de ciclo o implementar objetos auxiliares, por otro lado en el segundo codigo se deberan utilizar ciclos for para poder alamacenar los datos en las listas respectivas, lo que generaria un mayor tiempo de procesamiento al realizar el recorrido de todas las filas presentes en los dos archivos. En cuanto a la utilizacion de la memoria se logro identificar que el uso de pandas, implica utilizar una mayor cantidad de memoria para almacenar toda la informacion extraida (Tabla completa) por otro lado, en el caos del segundo codigo, solo se almacenan en 2 listas los datos mas releveantes correspondientes al eje x e y sin necesidad de extraer usuarios, frames o algun otro dato sin relevancia, que genere uso de memoria adicional.

## 6. Referencias
OpenAI. (2021). GPT-3.5 [Modelo de lenguaje AI]. Recuperado de https://openai.com/gpt-3.5

</div>