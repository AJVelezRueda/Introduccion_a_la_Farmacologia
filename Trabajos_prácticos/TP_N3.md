
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


# Trabajo Práctico: Diseño de Fármacos Asistido por Computadora

**Profesora**: Dra. Ana Julia Velez Rueda

## Datos del Ensayo Biológico
Se midió la actividad inhibidora (IC₅₀) de 6 compuestos análogos contra una enzima diana:

| Compuesto | Estructura (SMILES) | IC₅₀ (nM) | Actividad |
|-----------|---------------------|-----------|-----------|
| CMP-1 | `C1=CC(=CC=C1CCO)O` | 1000 | Baja |
| CMP-2 | `C1=CC(=CC=C1CCN)O` | 100 | Media |
| CMP-3 | `C1=CC(=CC=C1CCN)C(F)(F)F` | 10 | Alta |
| CMP-4 | `C1=CC(=CC=C1CCO)C(F)(F)F` | 500 | Baja |
| CMP-5 | `C1=CC(=CC=C1CCN)C#N` | 25 | Alta |
| CMP-6 | `C1=CC(=CC=C1CCN)CCl` | 50 | Alta |

## Fase 1: Visualización y Comparación de Estructuras

### 1. Dibujar las moléculas
- Utilizar **PubChem Sketcher** (https://pubchem.ncbi.nlm.nih.gov/edit3/index.html) o **MolView** (https://molview.org/)
- Dibujar cada uno de los 6 compuestos usando sus códigos SMILES

### 2. Identificar características comunes
- ¿Qué motivo estructural comparten todos los compuestos? ("andamiaio" o scaffold común)

### 3. Identificar diferencias
- ¿Qué sustituyentes (grupos químicos) están presentes en diferentes posiciones?

## Fase 2: Análisis de la Relación Estructura-Actividad (SAR)

### Comparemos por pares
1. **CMP-1 vs CMP-2**: ¿Qué diferencia estructural hay? ¿Qué grupo parece crucial para aumentar la actividad?
2. **CMP-2 vs CMP-3**: ¿Qué nuevo grupo añade CMP-3? ¿Qué efecto tiene en la actividad?
3. **CMP-4**: Tiene el nuevo grupo de CMP-3 pero el grupo problemático de CMP-1. ¿Confirma esto sus ideas?
4. **CMP-5 y CMP-6**: ¿Qué tienen en común sus sustituciones con la de CMP-3?

### Definir el Farmacóforo
Proponer un modelo farmacofórico simple que incluya al menos:
- Un grupo funcional específico necesario para la unión
- Una región hidrofóbica o área que tolere sustituciones voluminosas con carácter electrónico-atrayente (halógenos, nitrilo)

## Fase 3: Diseño y Evaluación de un Nuevo Análogo

### 1. Diseñar un nuevo compuesto (CMP-7)
- Debe contener:
  - Scaffold común
  - Grupo funcional crucial
  - Nuevo sustituyente que boostea la actividad

### 2. Predecir propiedades (ADME)
- Dibujar CMP-7 en PubChem Sketcher y copiar su SMILES
- Pegar en **SwissADME** [http://www.swissadme.ch/](http://www.swissadme.ch/)
- Analizar resultados:
  - ¿Cumple con la Regla de Lipinski?
  - ¿Tiene buena solubilidad?
  - ¿Es probable que sea absorbida por vía oral?

## 4. Resultados y Discusión

Presentar un informe breve con:

### SAR Resumida
Descripción clara de las conclusiones de la Fase 2

### Diagrama del Farmacóforo
Dibujo simple de la molécula, señalando las partes esenciales para la actividad

### Estructura de CMP-7
Incluir dibujo o SMILES de la molécula diseñada

### Propiedades Predichas de CMP-7
Tabla o párrafo resumiendo los resultados de SwissADME

### Discusión
- ¿Por qué CMP-7 sería más activo?
- ¿Sería un buen fármaco oral basándose en las predicciones? Justificar

## 5. Preguntas para Reflexión

1. ¿Cuáles son las ventajas principales de este enfoque (basado en ligando) frente a uno que requiere la estructura de la proteína?
2. ¿Cuál es la gran limitación de este método? (Pista: ¿Qué pasa si no tenemos compuestos activos para empezar?)
3. Si tuvieran que probar solo 2 compuestos en un costoso ensayo biológico, ¿elegirían probar CMP-1 y CMP-2? ¿Por qué sí o por qué no?