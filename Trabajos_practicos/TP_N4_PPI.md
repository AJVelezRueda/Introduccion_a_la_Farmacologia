
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## TP3: Interacción Proteína Proteína

**Profesora**: Dra. Ana Julia Velez Rueda

### **Ejercicio 1: Construcción y Visualización de la Red PPI**

Accedé a [STRING-db.org](https://string-db.org). Ingresá a la lista de genes dada:
 ```
    IL1B
    IL6
    TNF
    PTGS2
    NFkB1
    CXCL8
    TLR4
    STAT3
    MAPK14
    RELA
 ```
 proporcionada y configurá organismo como _Homo sapiens_.
1. Describí la topología de la red: ¿es densa o dispersa? Calculá el "degree"o cantidad de conexiones en la red según el score actual. 
2. ¿Cuántas proteínas "Hub" identificás? 
3. ¿Cómo afecta el ajuste de confianza a la red? ¿Por qué es importante este filtro?


### **Ejercicio 2: Análisis de Enriquecimiento Funcional**

Explorar pestaña "Functional Enrichment" y  analizar resultados en KEGG, Process y Function
1. Listá las 3 vías KEGG más enriquecidas (nombre y valor FDR)
2. ¿Qué procesos biológicos aparecen? ¿Coinciden con contexto de cáncer?
3. Se llama **targets combinatorios** si dos o más proteínas están en la misma vía y son mediadores clave ¿Existen en la red proteínas que puedan ser targets combinatorios para una terapia más efectiva?
4. Según GO Molecular Function ¿hay actividades o dominios específicos que sean aprovechables para diseñar inhibidores o activadores?


### **Ejercicio 3: Identificación y Priorización de Dianas**

Completar tabla de evaluación para 2 candidatos:

| Criterio | Candidato 1 | Candidato 2 |
|----------|-------------|-------------|
| Posición en red | | |
| Evidencia en enfermedad | | |
| Drogabilidad | | |
| Participación en vías clave | | |


1. Justifique la elección de sus 2 candidatos
2. Seleccione UNO como diana principal y explique su decisión
