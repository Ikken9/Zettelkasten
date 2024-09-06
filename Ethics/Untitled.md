# COMPAS

Correctional Offender Management Profiling for Alternative Sanctions, es una herramienta para el manejo de casos y la toma de decisiones desarrollado por Northpointe, utilizado por los Estados Unidos para evaluar la probabilidad de que la persona defendida se vuelva un reincidente.

Para evaluar el riesgo de reincidencia COMPAS utiliza un algoritmo que toma como referencia una serie de escalas de reincidencia general y violenta. Las escalas son hechas con datos provenientes de perfiles de delincuentes.

## Criticas
El algoritmo utilizado por COMPAS es secreto, lo que implica que un acusado no puede ver como es que su caso es evaluado, simplemente conoce el resultado.

Otra critica, es que el algoritmo es dependiente de datos para funcionar, si los datos con los que se entrena al algoritmo son erróneos o manipulados, los resultados de las evaluaciones pueden ser incorrectos.

## Precision
En 2016, una [investigación realizada por ProPublica](https://www.propublica.org/espanol), una organización periodística sin ánimo de lucro, reveló que **COMPAS tendía a sobreestimar el riesgo de reincidencia** entre las personas de raza negra, mientras que subestimaba el riesgo para las personas de raza blanca. El estudio demostró que las personas negras etiquetadas como de “alto riesgo” tenían casi el doble de probabilidades de no reincidir en comparación con las personas blancas con la misma clasificación. Del mismo modo, las personas blancas etiquetadas como de “bajo riesgo” tenían más probabilidades de reincidir que las personas negras clasificadas de la misma forma.

El problema del sesgo en COMPAS tiene sus raíces en los datos históricos que se usaron para entrenar el algoritmo. El sistema se alimentó de datos que reflejaban la discriminación racial y las desigualdades históricas en el sistema judicial estadounidense. Estos datos, inherentemente sesgados, **generaron un algoritmo que perpetúa las mismas desigualdades que pretendía combatir**.

