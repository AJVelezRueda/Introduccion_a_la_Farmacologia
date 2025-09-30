
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
| CMP-1 | `CC(CCCCC)C(O)CCCC(=O)O` | 1200 | Baja |
| CMP-2 | `CC(CC(CC)C)C(O)CCCC(=O)N` | 200 | Media |
| CMP-3 | `CC(C)CC(CCC)C(O)CCCC(F)(F)F` | 15 | Alta |
| CMP-4 | `CC(CCCCC)C(O)CCCC(=O)O[C@@H]1O[C@H](N)C(=O)C1` | 600 | Baja |
| CMP-5 | `CC(CCN)C(O)CCCC(=O)C#N` | 30 | Alta |
| CMP-6 | `CC(CCCl)C(O)CCCC(=O)Cl` | 45 | Alta |

### 1. Identificar características comunes
a. ¿Qué motivo estructural comparten todos los compuestos? ("andamiaio" o scaffold común) ¿Qué sustituyentes (grupos químicos) están presentes en diferentes posiciones?

### 2. Compareción de compuestos por pares

  a. **CMP-1 vs CMP-2**: ¿Qué diferencia estructural hay? ¿Qué grupo parece crucial para aumentar la actividad?

  b. **CMP-2 vs CMP-3**: ¿Qué nuevo grupo añade CMP-3? ¿Qué efecto tiene en la actividad?

  c. **CMP-4**: Tiene el nuevo grupo de CMP-3 pero el grupo problemático de CMP-1 

  d. **CMP-5 y CMP-6**: ¿Qué tienen en común sus sustituciones con la de CMP-3?

### 3. Diseñar un nuevo compuesto  análogo (CMP-7)
Proponer un modelo farmacofórico simple que incluya:

- Un grupo funcional específico necesario para la unión

- Una región hidrofóbica o área que tolere sustituciones voluminosas con carácter electrónico-atrayente (halógenos, nitrilo)

- Scaffold común

- Grupo funcional crucial

- Nuevo sustituyente que boostea la actividad

### 4. Predecir propiedades (ADME) del compuesto CMP-7
a. Dibujar CMP-7 en PubChem Sketcher y copiar su SMILES

b. Usando el módulo admet_module del TP2 analizar:

  * ¿Cumple con la Regla de Lipinski?

  * ¿Tiene buena solubilidad?

  * ¿Es probable que sea absorbida por vía oral?

## 5. Preguntas para Reflexión
a. ¿Cuáles son las ventajas principales del enfoque basado en ligando frente a uno que requiere la estructura de la proteína?

b. ¿Cuál es la gran limitación de este método?

c. Si tuvieran que probar solo 2 compuestos en un costoso ensayo biológico, ¿elegirían probar CMP-1 y CMP-2? ¿Por qué sí o por qué no?

## 6. Búsqueda de Blancos moleculares
Dada la secuencia:

```
>sp|P0A722|LPXA_ECOLI Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase OS=Escherichia coli (strain K12) GN=lpxA PE=1 SV=1
MIDKSAFVHPTAIVEEGASIGANAHIGPFCIVGPHVEIGEGTVLKSHVVVNGHTKIGRDNEIYQFASIGEVNQDLKYAGEPTRVEIGDRNRIRESVTIHRGTVQGGGLTKVGSDNLLMINAHIAHDCTVGNRCILANNATLAGHVSVDDFAIIGGMTAVHQFCIIGAHVMVGGCSGVAQDVPPYVIAQGNHATPFGVNIEGLKRRGFSREAITAIRNAYKLIYRSGKTLDEVKPEIAELAETYPEVKAFTDFFARSTRGLIR
```
Consignar todos los homólogos cercanos con estructura conocida. Responder

a- ¿Cuáles son las herramientas y configuraciones necesarias para tal fin?
b- ¿Existen regiones proteicas con mayor consevación?
c -¿Existen regiones proteicas con mayor consevación?¿Coinciden con regiones de relevancia biológica?

## 7. Cálculo de similitud química de los compuestos canónicos con los candidatos

Usando la biblioteca admet_module, calcular las similitud con los ligandos elegidos en el punto 1 y 2 y los ligandos canónicos de la proteína del punto 7:

```python
# Ejemplo de corrida
moleculas = {
    "CMP-1": "CC(CCCCC)C(O)CCCC(=O)O",
    "CMP-2": "CC(CC(CC)C)C(O)CCCC(=O)N"
}

ligando_canonico = "CCCCCCCCCCCCCC(O)C(=O)O"

df_tanimoto = calculate_tanimoto_similarity(moleculas, ligando_canonico)
print(df_tanimoto)
```