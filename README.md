# MCOC2021-P0

# Mi computador principal

* Marca/modelo: MacBook Pro
* Tipo: Notebook
* Año adquisición: 2012
* Procesador:
  * Marca/Modelo: Intel Core i7-4790K
  * Velocidad Base: 2.8 GHz
  * Velocidad Máxima: 2.8 GHz
  * Numero de núcleos: 2 
  * Numero de hilos: 2
  * Arquitectura: x86_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * Caché de nivel 2 (por nucle0): 256KB
  * Caché de nivel 3: 4MB
* Memoria 
  * Total: 12 GB
  * Tipo memoria: DDR3
  * Velocidad 1067 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: ntel HD Graphics 3000
  * Memoria dedicada: 512 MB
  * Resolución: 1280 x 800
* Disco 1: 
  * Marca: Macintosh
  * Tipo: SSD
  * Tamaño: 525 GB
  * Particiones: 1
  * Sistema de archivos: APFS
  
* Dirección MAC de la tarjeta wifi:  192.168.10.37
* Dirección IP (Interna, del router): 192.168.10.1
* Dirección IP (Externa, del ISP): 255.255.255.0
* Proveedor internet: VTR S.A.


* Desempeño MATMUL:

se cargo la imagen en otro archivo



* ¿Cómo difiere del gráfico del profesor/ayudante?
se puede ver que mi grafica es mas lineal que la del ayudante, esto puede yaque moi computador no puestra mucha diferencia en las variaciones de tiempo para cada una de las multiplicaciones. de todas maneras se observa que los tiempos del programa del profesor son menores a los mios.

* ¿A qué se pueden deber las diferencias en cada corrida?
 se ve representado de una manera explicita, al moemtno de aumentar el tamaño de cada una de las matrices, en donde se ve el incremento de tiempo al aumentar estas al igual que el aumento de consumo de memoria

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
* ¿Qué versión de python está usando?
3.7

* ¿Qué versión de numpy está usando?

1.16.4

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
en el caso del tiempo la frafica no es linal ya que esta depende de la memoria que se utilizaen en el moemtno para la multiplicacion de matrices y para el caso de la memoria utilizada para cada multiplicacion se observa que se van sumando por lo que todos los incrementos seran lineales.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

ENTREGA 3

Para esta entrega se programo y luego se analiso el desempeño de el calculo de la inversa de una matriz tipo de diferentes tamaños, esto se llevo a cabo con dos librerias, la primera fue niumpy en donde se presentaron problemas con que corriera el half(float16) y el longdouble(float128) y la otra libreria fue scipy donde se pusieron a prueba dos casos; overwrite_a=true y overwrite_a=false, esn donde no hubo mayior problema con la corride de los codigos pero se noto un mejor desempeño en el caso del overwrtite_a=true.
Se puede notar que scipy es una libreria mas efectiva que el numpy ya que esta calcula la inversa en menos tiempo y usa la misma memoria.

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.

Para la libreira de scipy.linalg.inv() el programa calcula la inversa mediante el metodo de pivoteo y factorizacion LU, se tiene el caso de scipy overwrite true y false en donde al ser false se calcula la matriz siempre desde cero y al usar true se trabaja con los datos de la matriz ingresada al programa. al usar true se suele tener un proceso mas eficiente.
el metodo de numpy.linalg.inv() usa un solve en donde se tiene (a,I) siendo "a" la matris e "i" la matriz identidad y se calcula mediente procesos de factorizacion LU de lapacks.


¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas. 


Al utilizar todos los recursos del pc los programas se lograron desarrollar de una manera rapida. esto se puede ver refeljado en la imagen de desempeño ingresada en el mismo github


