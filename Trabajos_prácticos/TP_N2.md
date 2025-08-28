
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
    a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov). 
    Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

    b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:
    a. Peso molecular

    b. LogP (índice de lipofilicidad)

    c. H-bond acceptors

    d. H-bond donors

    e. TPSA (Superficie polar)

    f. Rotatable bonds

3. Identificar subestructuras indeseables de los compuestos del punto 1.ay 1.b usando la la siguiente módulo de python creado para tal fin siguiendo el tutorial:

```python
$ pip install rdkit-pypi molvs requests pandas numpy matplotlib seaborn
$ pip install deepchem 
$ python
Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from admet_module import analisis_completo
>>> mis_moleculas = {'molecula': 'COc1ccccc1C=O'}
>>> resultados = analisis_completo(mis_moleculas)
>>> print(resultados.keys())
>>> print(resultados['propiedades'])
```

4. Realizar la predicción de toxicidad in silico utilizando ProTox-II (https://tox-new.charite.de/protox_II/). Utilizando los SMILES de moléculas del punto 1.a y 1.b, obtener: 

    a. Predicted LD50 (mg/kg) y clase de toxicidad (I–VI).

    b. Riesgo de hepatotoxicidad, mutagenicidad, carcinogenicidad.

    ¿Cuál de las moléculas seleccionadas muestra menor toxicidad según ProTox-II?

5. Construir una ficha técnica de cada compuesto que considere las respuestas a las siguientes preguntas: ¿Qué compuestos cumplen mejor con los filtros de Lipinski y Veber? ¿Aparecieron moléculas con alertas PAINS? ¿Cuál es su toxicidad?
