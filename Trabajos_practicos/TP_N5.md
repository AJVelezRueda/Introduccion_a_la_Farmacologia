
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

# TP5: ACOMPLAMIENTO MOLECULAR

**Profesora**: Dra. Ana Julia Velez Rueda


## Actividades Teóricas

El docking molecular es una técnica computacional utilizada para predecir la orientación y afinidad de unión entre una molécula pequeña (ligando) y una macromolécula receptora (target), como una proteína. Esta herramienta es fundamental en el diseño racional de fármacos, ya que permite estimar la energía de interacción entre el ligando y el sitio activo de la proteína, ayudando a identificar posibles compuestos con actividad biológica.

### 1T. Investigar sobre las técnicas de acoplamiento molecular
Usando el libro [Bioinformática con Ñ](https://zenodo.org/records/1066358) describir los siguientes métodos y/o conceptos:
  a. Docking Flexible
  b. Docking Rígido
  c. Virtual Screening

## Actividades prácticas

### 1P. Caracterización del Target

Vamos a utilizar como Target la Anhydrasa Carbonica II humana. Descargá la estructura PDB ID = 3HS4 (CAII con acetazolamida co-cristalizada).
    a) ¿Qué caracterización estructural podemos hacer de la proteína? Describir la batería de herramientas usadas
    b) Usando la herramienta [PockDrug](https://pockdrug.rpbs.univ-paris-diderot.fr/cgi-bin/index.py?page=Druggability) predecir los pockets drogables. ¿Coinciden con sitios anotados en Uniprot?
    c)  Extraer el ligando asociado a la estructura acetazolamida y obtener las estructuras de dorzolamida o brinzolamida (desde ZINC o PubChem).

### 2P. Preparación de la corrida
Eliminar moléculas de agua y el ligando original si corresponde. [Agregar hidrógenos](http://newbiophysics.cs.vt.edu/H++/) al receptor (pH fisiológico). Guardar receptor en formato compatible (.pdbqt o equivalente) Preparar los ligandos: minimización + conversión a formato compatible.

Herramientas: [Propka](https://propka.readthedocs.io/en/latest/), [H++](http://newbiophysics.cs.vt.edu/H++/), [Fpocket](https://durrantlab.pitt.edu/fpocketweb-download/),

### 3P. [Docking](https://durrantlab.pitt.edu) comparativo

a. Definir la [caja de docking](https://durrantlab.pitt.edu/) alrededor del Zn²⁺ y el sitio donde se une acetazolamida.
b. Usando el programa  dockear en el sitio activo:
- acetazolamida (control)
- dorzolamida 
- brinzolamida

software alternativo: [SwissDock](https://www.swissdock.ch)

c. Registrar:
Energía de unión (kcal/mol), Poses obtenidas, Principales interacciones (puentes H, interacción con Zn²⁺, contactos hidrofóbicos)

<details>
<summary>Instrucciones de Corridas</summary>

**1. Preparación del receptor**
 a. Descargar la estructura: Ir a RCSB PDB --> Descargar el archivo PDB de la Human Carbonic Anhydrase II (CAII) co-cristalizada con acetazolamida.

**2. Quitar agua y ligando**
Cargar el archivo 3HS4.pdb en [Mol](https://molstar.org/viewer/) o Pymol, eliminar las aguas y exportar la estructura de la proteína y del ligando por separado (File → Export → Structure → .pdb).

**3.Agregar hidrógenos a pH fisiológico**
Usando el servidos [pdb2pqr](https://server.poissonboltzmann.org/pdb2pqr) (Elegir pH = 7.0, seleccionar la opción “Add hydrogens” y descargar el archivo resultante CAII_H.pdb) o el software [OpenBabel](https://openbabel.org/index.html) localmente para agregar los hidrógenos.

**4. Convertir a formato .pdbqt las estructuras pdb**
Podés usar [Mol](https://molstar.org/viewer/), [NGL](https://nglviewer.org/ngl/) o [PLIP](https://plip-tool.biotec.tu-dresden.de)

**5. Correr el docking**
Usando Webina, centrando la caja alrededor del átomo de Zn²⁺ (usá un tamaño de caja de aprox. 20 × 20 × 20 Å y verificar que incluye el sitio donde estaba la acetazolamida original), y descargar los resultados para analizar

</details>
