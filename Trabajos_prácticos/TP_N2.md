
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## TP2: Evaluación in silico de propiedades ADMET y filtros de selección de candidatos a fármaco

**Profesora**: Dra. Ana Julia Velez Rueda

En el diseño de fármacos, una de las principales causas de fracaso en fases clínicas es la falta de propiedades farmacocinéticas adecuadas o la aparición de toxicidad inesperada. Para minimizar costos y tiempo, se aplican métodos in silico que permiten predecir la Absorción, Distribución, Metabolismo, Excreción y Toxicidad (ADMET) de moléculas candidatas.

Además, se utilizan filtros de “drug-likeness”, como las reglas de Lipinski y Veber, junto con los filtros de PAINS, para descartar compuestos con baja probabilidad de éxito o con estructuras problemáticas.

### CONSIGNAS PRÁCTICOS
1. Selección de compuestos:
    a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov)[https://pubchem.ncbi.nlm.nih.gov]. 
    Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

    b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:
    a. Peso molecular

    b. LogP (índice de lipofilicidad)

    c. H-bond acceptors

    d. H-bond donors

    e. TPSA (Superficie polar)

    f. Rotatable bonds

3. Identificar subestructuras indeseables de los compuestos del punto 1.ay 1.b usando la plataforma FAF-Drugs4 (http://fafdrugs4.rpbs.univ-paris-diderot.fr)

4. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta admetSAR 2.0 (http://lmmd.ecust.edu.cn/admetsar2/). Obtener para las moléculas del punto 1.a y 1.b:
    a. Absorption (intestinal, Caco-2).

    b. Distribution (BBB penetration, plasma binding).

    c. Metabolism (CYP interactions).

    d. Excretion (renal clearance).

    e. Toxicity (mutagenicidad, hepatotoxicidad, carcinogenicidad).

    RESPONDER: ¿Qué diferencias se observan en la absorción intestinal entre moléculas conocidas y experimentales? 
    Si una molécula muestra buen perfil ADMET pero tiene alertas PAINS, ¿la descartarías o la estudiarías igual?

5. Realizar la predicción de toxicidad in silico utilizando ProTox-II (https://tox-new.charite.de/protox_II/). Utilizando los SMILES de moléculas del punto 1.a y 1.b, obtener: 

    a. Predicted LD50 (mg/kg) y clase de toxicidad (I–VI).

    b. Riesgo de hepatotoxicidad, mutagenicidad, carcinogenicidad.

    ¿Cuál de las moléculas seleccionadas muestra menor toxicidad según ProTox-II?

6. Construir una ficha técnica de cada compuesto que considere las respuestas a lassiguientes preguntas: ¿Qué compuestos cumplen mejor con los filtros de Lipinski y Veber? ¿Aparecieron moléculas con alertas PAINS? ¿Cuál es su toxicidad?
