
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## TP3: ACOMPLAMIENTO MOLECULAR

**Profesora**: Dra. Ana Julia Velez Rueda

El docking molecular es una técnica computacional utilizada para predecir la orientación y afinidad de unión entre una molécula pequeña (ligando) y una macromolécula receptora (target), como una proteína. Esta herramienta es fundamental en el diseño racional de fármacos, ya que permite estimar la energía de interacción entre el ligando y el sitio activo de la proteína, ayudando a identificar posibles compuestos con actividad biológica.

En este trabajo práctico, los estudiantes realizarán un experimento de docking sobre un target proteico definido y compararán los resultados obtenidos entre diferentes ligandos, incluyendo un ligando canónico (conocido) y una molécula con potencial actividad farmacológica (droga candidata).

## 1. Caracterización del Target

Vamos a utilizar como Target la Anhydrasa Carbonica II humana. Descargá la estructura PDB ID = 3HS4 (CAII con acetazolamida co-cristalizada).
    a) ¿Qué caracterización estructural podemos hacer de la proteína? Describir la batería de herramientas usadas
    b) Usando la herramienta [PockDrug](https://pockdrug.rpbs.univ-paris-diderot.fr/cgi-bin/index.py?page=Druggability) predecir los pockets drogables. ¿Coinciden con sitios anotados en Uniprot?
    c)  Extraer el ligando asociado a la estructura acetazolamida y obtener las estructuras de dorzolamida o brinzolamida (desde ZINC o PubChem).

## 2. Preparación de la corrida
Eliminar moléculas de agua y el ligando original si corresponde. Agregar hidrógenos al receptor (pH fisiológico). Guardar receptor en formato compatible (.pdbqt o equivalente) Preparar los ligandos: minimización + conversión a formato compatible.

## 3. Definición del sitio activo
Definir la caja de docking alrededor del Zn²⁺ y el sitio donde se une acetazolamida.

## 4. Docking comparativo
    a. Usando el programa  dockear en el sitio activo:
    - acetazolamida (control)
    - dorzolamida 
    - brinzolamida

    b. Registrar:
    Energía de unión (kcal/mol), Poses obtenidas, Principales interacciones (puentes H, interacción con Zn²⁺, contactos hidrofóbicos)
		