# exercising

### Theoretical Questions

1. Qué entiende por Arquitectura de Software 
   **R:** Arquitectura de Software se refiere al conjunto de artefactos que se relacionan entre si para conformar e implementar una solución de software funcional.
2. ¿Cuáles son los 4 aspectos de Arquitectura que hemos trabajado?
   **R:** Requerimientos, Operacional, Funcional, Viabilidad
3. ¿Qué diagrama permite mostrar la frontera del sistema, las entidades externas con las que la solución debe interactuar y los actores que interactúan con el mismo? 
   **R:** Diagrama de Contexto
4. ¿Para qué sirve un diagrama de contexto?
   **R:** Sirve para representar al sistema como una entidad, en donde ademas se muestran las relaciones e interacciones con los actores externos como usuarios u otros sistemas. 
5. ¿Qué debería contener un template que documente un Diagrama de Contexto?
   **R:** Aplicación, Actores, Relaciones
6. ¿En qué se diferencian los atributos de calidad y las restricciones?
   **R:** Los atributos de calidad son cualidades que el sistema debe poseer, tales como performance, seguridad, operabilidad y disponibilidad.
7. Nombrar los atributos de calidad claves 
   **R:** Seguridad, Performance, Operabilidad, Disponibilidad   
8. En la siguiente clasificación de NFRs (atributos de calidad, restricciones técnicas y restricciones de negocio) clasifique los siguientes requerimientos no funcionales: 
	1. a. Performance 
	2. b. Disponibilidad 
	3. c. Presupuesto es de USD 4M 
	4. d. Deberá integrarse con el core a través de colas asincrónicas 
	5. e. Nuestro estándar de desarrollo es Java 
	6. f. El plazo para tener la solución funcionando es de 8 meses
	   **R:** 
	   *Atributos de calidad*: Disponibilidad, Performance.
	   *Restricciones Técnicas*: Estándar de desarrollo en Java, Integración con el core via colas asíncronas.
	   *Restricciones de Negocio*: Plazo de 8 meses, Presupuesto de USD 4 Millones.
9. ¿Qué se considera como un requerimiento funcional arquitecturalmente significativo?
   **R:** Un requerimiento funcional arquitecturalmente significativo es aquel cuyo impacto es determinante en la arquitectura del sistema, es decir, que una parte o total de
   la arquitectura sea de alguna manera dependiente del mismo.
10. Describa en qué consiste el proceso de construcción de una arquitectura
    **R:** El proceso consiste en varios pasos que deben seguirse si se quiere llegar a una solución óptima (o al menos lo mejor posible), los pasos son los siguientes:
	1. Obtención de requerimientos
	2. Diseño de arquitectura
	3. Documentación
	4. Evaluación
	5. Prototipado
	6. Implementación


## Architecture Decisions

11. ¿Qué ventajas presenta documentar las elecciones críticas que se tomaron en la definición de una solución?
    **R:** Las ventajas de documentar las elecciones son varias, entre ellas, consultar en cualquier momento las decisiones tomadas, en que contexto fueron realizadas y su explicación/justificación. También pueden verse las implicaciones de cada decision así como sus alternativas.
12. Presente un modelo/formato para documentar estas decisiones de arquitectura y proporcione dos ejemplos. 
    **R:** El modelo utilizado para esto es el ADR (Architecture Decision Record).
13. ¿Qué debería contener un template que documente las decisiones de Arquitectura?
    **R:** Decision, Motivo, Contexto, Alternativas planteadas, Asunciones, Implicaciones, Fecha.


## AOD Questions

14. ¿Qué es un "Architecture Overview Diagram" y cuál es su propósito principal en el contexto del diseño de una arquitectura? Si se utiliza una notación formal específica, descríbala.
    **R:** Es un diagrama que tiene como objetivo representar la arquitectura de la solución a un alto nivel y todos sus componentes así como también sus relaciones. Permite entender a los stakeholders el funcionamiento del sistema, así como también facilitar a los desarrolladores la toma de decisiones y una temprana validación.
15. ¿Qué elementos y relaciones componen un AOD?
    **R:** Componentes, relaciones entre componentes, sistemas y subsistemas, tiers de componentes.
16. ¿Cuál es el público objetivo principal de los AOD? ¿Podrían existir varios AOD? ¿Por qué es relevante comunicar la arquitectura de esta manera?
    **R:** El publico objetivo pueden ser tanto el equipo de desarrollo como los stakeholders y todo aquel que se vea involucrado en el proceso de desarrollo. Comunicar la arquitectura de esta manera es bastante sencilla y facilita la comprensión del sistema a aquellos que lo construyen y a quienes lo van a utilizar.
17. Describe cómo un AOD puede ser útil en las etapas iniciales de un proyecto y en las discusiones con los stakeholders.
    **R:** Un AOD puede resultar muy util para detectar posibles problemas en el desarrollo temprano y por lo tanto ser corregidos a tiempo, pueden evaluarse multiples posibles soluciones y optar por la mejor de ellas. Ademas ayudan a que los stakeholders puedan entender mas fácilmente como es la estructura de su sistema.
18. ¿Qué debería contener un template que documente un Diagrama General de Arquitectura (AOD)?
    **R:** Componentes, relaciones entre componentes (conexiones), sistemas y subsistemas, tiers de componentes.


## Components

19. ¿Los aspectos funcionales de una arquitectura cómo se pueden modelar?
    **R:** Los aspectos funcionales pueden modelarse mediante una serie de diagramas complementarios que son: Diagrama de Casos de Uso, Diagrama de Actividades, Diagrama de Secuencia, Diagrama de Clases, Diagrama de Componentes y Diagrama de Despliegue.
20. ¿A través de qué diagrama se representa la relación estática de los componentes? ¿Y la relación dinámica?
    **R:** La relación estática pueden representarse mediante un diagrama de relación, mientas que la relación dinámica puede representarse mediante un diagrama de interacción.
21. ¿Qué representa un diagrama de relación de componentes? ¿Cómo se documenta?
    **R:** Un diagrama de relación de componentes representa como se relacionan los componentes de un sistema sin tener en cuenta la interacción durante el funcionamiento del mismo, no se tiene en cuenta el orden o tiempo, por lo tanto es estático. Similar a los diagramas de clases.
22. ¿Qué representa un diagrama de interacción de componentes? ¿Cómo se documenta?
    **R:** Este tipo de diagrama representa la interacción de los componentes de un sistema a lo largo del tiempo, es decir, de una forma dinámica. Se representan de la misma forma que un diagrama de secuencia.
23. ¿Cómo ayuda un diagrama de relaciones de componentes a mejorar la comprensión del diseño arquitectónico del sistema?
24. ¿Qué debería tener un template que documenta el modelo de componentes?
    **R:** Diagrama de Relación de componentes y Diagrama de Interacción de componentes.
25. ¿Qué se entiende por Alta Cohesión?
    **R:** La cohesion es la medida en que los componentes de una misma clase se mantienen unidos, por lo tanto una alta cohesion indica que los componentes involucrados cumplen con un mismo propósito.
26. ¿Qué se entiende por Bajo Acoplamiento?
    **R:** El acoplamiento es la medida en que los componentes de un sistema dependen el uno del otro, por lo tanto un bajo acoplamiento indica una baja dependencia entre componentes, lo cual es beneficioso.
27. ¿Qué se entiende por Componente? 
    **R:** Un componente es una parte bien diferenciable que conforma un sistema, disponibilizando sus funciones por medio de una interfaz.
28. ¿Qué diagrama UML se utiliza para modelar un diagrama de interacción de componentes?
    **R:** Diagrama de Secuencia.
29. ¿Qué diagrama UML se utiliza para modelar un diagrama de relación de componentes?
    **R:** Diagrama de Clases.
30. ¿Qué input se toma para representar un diagrama de interacción de componentes?
    **R:** El flujo de datos entre componentes producto de su caso de uso.
31. ¿Cuál es la única relación entre componentes que se representa en un diagrama de relación de componentes?
    **R:** Entre los componentes se establece una relación de uso.
32. ¿Qué se debe describir para cada componente en un modelo de componentes?
    **R:** Responsabilidad, Interfaz 
33. Pensar un caso de uso para una compra de entradas para el cine y un conjunto de componentes que participan de la solución; realizar un diagrama de interacción de componentes para este ejemplo.


## Styles and Architectural Patterns

34. ¿En qué se diferencia un estilo y un patrón de arquitectura?
    **R:** Un estilo es un un conjunto de reglas y restricciones de como organizar los componentes de un sistema, restringiendo sus roles, características y relaciones. Un patron de arquitectura es una solución a un problema común que viene dada por una serie de decisiones o pasos a seguir que establecen las interacciones entre subsistemas de un sistema mayor.
35. Explica la importancia de utilizar patrones y estilos de arquitectura
36. ¿Qué ventajas presenta una arquitectura monolítica frente a una distribuida?
    **R:** Una arquitectura monolítica es mas fácil de trabajar que una distribuida, debido a que los componentes están en un mismo lugar. Por el mismo motivo, también es mas fácil de testear y desplegar.
37. ¿Qué ventajas presenta una arquitectura distribuida frente a una monolítica?
    **R:** Una arquitectura distribuida escala mejor que una monolítica, es mas flexible y ofrece una mayor resiliencia, por lo tanto es mucho mas tolerante a fallos y fácil de mantener.
38. ¿Es posible combinar distintos patrones de arquitectura en una misma solución? Si es así, brinde un ejemplo.
    **R:** Es posible.
39. Enumere y describa al menos 3 falacias de la computación distribuida.
40. ¿En qué se diferencian los niveles/tiers de las capas/layers? 
41. Explique en qué consiste el patrón de arquitectura “MVC” 
42. Explique en qué consiste el patrón de arquitectura “Three-tier” 
43. Explique en qué consiste el patrón de arquitectura “Microservicios” 
44. Explique en qué consiste el patrón de arquitectura “Saga” 
45. ¿Qué patrón de arquitectura utilizaría en una aplicación bancaria donde se requiera garantizar la ejecución completa de transacciones al utilizar varios servicios?
    **R:** Saga


## Deployment Diagrams

46. ¿Qué diagrama UML se utiliza para comprender la arquitectura física de un sistema? Enumere y describa los elementos que utiliza en la notación.
    **R:** Diagrama de Despliegue
47. Explica la diferencia entre nodos y componentes en un diagrama de despliegue. ¿Cómo se relacionan estos elementos?
    **R:** Los nodos de un diagrama de despliegue son unidades que pueden procesar, almacenar o transportar datos. Son items en donde reside el software que se quiere desplegar. Los componentes de un diagrama de despliegue pueden son piezas de software o partes del sistema que pueden ser desplegadas dentro de un nodo.
48. Explica cómo se indican los artefactos en un diagrama de despliegue y cómo se relacionan con los nodos.
    **R:** Los artefactos se indican mediante un rectángulo con la notación *\<\<artifact\>\>*, estos están contenidos dentro de los nodos.
49. ¿En qué casos sería útil utilizar un diagrama de despliegue en un proyecto de desarrollo de software? ¿Qué información puede proporcionar a los desarrolladores y otros stakeholders?
    **R:** Siempre que se quiera realizar un despliegue.
50. Dibuje un diagrama de despliegue con los elementos necesarios para una aplicación de mensajería instantánea que utiliza una arquitectura three-tier.


## ANDISTORE

#### Actores:
  - Personal,
  - Usuarios web
  - Usuarios mobile
  
#### Sistemas adyacentes:
  - Mercado Pago
  - DAC
  - Auth0
  - Pasarela de pagos
  - Correo

#### Casos de Uso:
- Usuario se autentica (\*) 
- Usuario realiza compra (incluyendo el pago) (\*)
- Usuario visualiza productos
- Usuario visualiza su historial de compras
- Personal gestiona productos (\*)
- Personal gestiona promociones
- Usuario rastrea pedido en tiempo real (\*)
- Usuario filtra producto
- Usuario busca producto
- Usuario recibe recomendaciones basadas en su historial de compra

#### NFRs
Seguridad TLS 1.3
Compatibilidad Android y iOS
Alto nivel de rendimiento
Alta escalabilidad
Alta disponibilidad
Redundancia de datos
Balanceo de Carga
UI/UX


### AOD

![andistore_aod](andistore_aod.png)
