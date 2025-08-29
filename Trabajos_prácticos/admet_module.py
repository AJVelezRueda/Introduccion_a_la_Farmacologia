import warnings
import sys
import os
from io import StringIO

warnings.filterwarnings("ignore")
os.environ['PYTHONWARNINGS'] = 'ignore'

old_stderr = sys.stderr
sys.stderr = StringIO()

try:
    import pandas as pd
    from rdkit import Chem
    from rdkit.Chem import Descriptors, Lipinski
    from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
finally:
    sys.stderr = old_stderr


def calculate_properties(smiles_dict):
    """
    Calcula propiedades fisicoquímicas para moléculas
    uso:
        smiles_dict (dict): {nombre: SMILES}
    """
    properties_list = []
    
    for name, smiles in smiles_dict.items():
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            hba = Lipinski.NumHAcceptors(mol)
            hbd = Lipinski.NumHDonors(mol)
            logp = Descriptors.MolLogP(mol)
            mw = Descriptors.MolWt(mol)

            lipinski_violations = 0
            if mw > 500: lipinski_violations += 1
            if logp > 5: lipinski_violations += 1
            if hbd > 5: lipinski_violations += 1
            if hba > 10: lipinski_violations += 1
            
            props = {
                'Name': name,
                'SMILES': smiles,
                'MW': mw,
                'LogP': logp,
                'HBA': hba,
                'HBD': hbd,
                'TPSA': Descriptors.TPSA(mol),
                'RotatableBonds': Lipinski.NumRotatableBonds(mol),
                'Lipinski_Violations': lipinski_violations
            }
            properties_list.append(props)
        else:
            pass
    
    return pd.DataFrame(properties_list)

def predict_admet(smiles):
    """
    Predice propiedades ADMET para una molécula
    """
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    tpsa = Descriptors.TPSA(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    rotatable_bonds = Lipinski.NumRotatableBonds(mol)

    absorption = 'High' if tpsa < 140 and logp < 5 and rotatable_bonds < 10 else 'Medium' if tpsa < 180 else 'Low'
    bbb_penetration = 'Yes' if mw < 450 and logp < 3.5 and tpsa < 90 and hbd < 3 else 'No'
    plasma_binding = 'High' if logp > 3 else 'Medium' if logp > 1 else 'Low'
    cyp_inhibition = 'High' if logp > 3 and mw > 250 and (hba + hbd) < 8 else 'Low'
    renal_clearance = 'High' if mw < 300 and logp < 1 else 'Low'
    
    return {
        'Absorption': absorption,
        'BBB_Penetration': bbb_penetration,
        'Plasma_Binding': plasma_binding,
        'CYP_Inhibition': cyp_inhibition,
        'Renal_Clearance': renal_clearance
    }

def run_admet_predictions(smiles_dict):
    """
    Ejecuta predicciones ADMET para un diccionario de moleculas (SMILES)
    INPUT:
        moleculas = {'molecula': 'COc1ccccc1C=O'}
    """
    results = []
    for name, smiles in smiles_dict.items():
        admet = predict_admet(smiles)
        if admet:
            results.append({'Name': name, **admet})
        else:
            pass
    return pd.DataFrame(results)

def check_undesirable_substructures(smiles_dict):
    """
    Detecta subestructuras indeseables (PAINS)
    """
    results = []
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS)
    catalog = FilterCatalog(params)
    
    for name, smiles in smiles_dict.items():
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            pain_matches = catalog.GetMatches(mol)
            results.append({
                'Name': name,
                'PAINS_Alerts': len(pain_matches),
                'PAINS_Details': [match.GetDescription() for match in pain_matches]
            })
        else:
            results.append({
                'Name': name,
                'PAINS_Alerts': 0,
                'PAINS_Details': ['Invalid SMILES']
            })
    
    return pd.DataFrame(results)

def predict_toxicity(smiles):
    """
    Predice toxicidad para una molécula
    """
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None
    
    toxic_fragments = [
        '[S&!$(S=O)]', '[N+](=O)[O-]', 'c1ccc2c(c1)ccc3c2ccc4c3cccc4',
        'C#N', 'ClC=Cl', 'P(=O)(O)(O)'
    ]
    
    alerts = 0
    toxic_details = []
    
    for i, frag in enumerate(toxic_fragments):
        pattern = Chem.MolFromSmarts(frag)
        if pattern and mol.HasSubstructMatch(pattern):
            alerts += 1
            toxic_details.append(f'Alert_{i+1}')
    
    if alerts == 0:
        toxicity_class = 'Low'
        ld50_estimate = '>5000 mg/kg'
    elif alerts == 1:
        toxicity_class = 'Moderate' 
        ld50_estimate = '500-5000 mg/kg'
    else:
        toxicity_class = 'High'
        ld50_estimate = '<500 mg/kg'
    
    return {
        'Toxicity_Alerts': alerts,
        'Toxic_Fragments': ', '.join(toxic_details),
        'Predicted_Toxicity': toxicity_class,
        'Estimated_LD50': ld50_estimate
    }

def predict_toxicity_batch(smiles_dict):
    """
    Predice toxicidad para todas las moléculas en un diccionario de moléculas (SMILES)
    INPUT:
        moleculas = {'molecula': 'COc1ccccc1C=O'}
    """
    results = []
    for name, smiles in smiles_dict.items():
        tox = predict_toxicity(smiles)
        if tox:
            results.append({'Name': name, **tox})
        else:
            results.append({
                'Name': name,
                'Toxicity_Alerts': 0,
                'Toxic_Fragments': 'Invalid SMILES',
                'Predicted_Toxicity': 'Unknown',
                'Estimated_LD50': 'Unknown'
            })
    return pd.DataFrame(results)

def generate_compound_cards(smiles_dict):
    """
    Genera fichas técnicas bonitas para tus moléculas
    """
    cards = []
    properties_df = calculate_properties(smiles_dict)
    admet_df = run_admet_predictions(smiles_dict)
    toxicity_df = predict_toxicity_batch(smiles_dict)
    pains_df = check_undesirable_substructures(smiles_dict)
    
    for name in smiles_dict.keys():
        props = properties_df[properties_df['Name'] == name].iloc[0]
        admet = admet_df[admet_df['Name'] == name].iloc[0]
        tox = toxicity_df[toxicity_df['Name'] == name].iloc[0]
        pains = pains_df[pains_df['Name'] == name].iloc[0]
        
        card = f"""
        {'='*60}
        FICHA TÉCNICA: {name.upper()}
        {'='*60}
        SMILES: {props['SMILES']}

        PROPIEDADES:
        - Peso molecular: {props['MW']:.2f} Da
        - LogP: {props['LogP']:.2f}
        - Donores H: {props['HBD']}
        - Aceptores H: {props['HBA']}
        - TPSA: {props['TPSA']:.2f} Å²
        - Enlaces rotables: {props['RotatableBonds']}

        LIPINSKI:
        - Violaciones: {props['Lipinski_Violations']}/4
        - Cumplimiento: {'Sí' if props['Lipinski_Violations'] <= 1 else 'No'}

        ADMET:
        - Absorción: {admet['Absorption']}
        - Penetración BBB: {admet['BBB_Penetration']}
        - Unión a proteínas: {admet['Plasma_Binding']}
        - Inhibición CYP: {admet['CYP_Inhibition']}
        - Clearance renal: {admet['Renal_Clearance']}

        TOXICIDAD:
        - Alertas: {tox['Toxicity_Alerts']}
        - Toxicidad: {tox['Predicted_Toxicity']}
        - LD50: {tox['Estimated_LD50']}

        ALERTAS:
        - PAINS: {pains['PAINS_Alerts']} alertas
        {'='*60}
                """
        cards.append(card)
            
        return cards

def analisis_completo(smiles_dict):
    """
    Función de ejecución del análisis completo de un diccionario de moléculas
    
    Args:
        smiles_dict (dict): diccionario {nombre: SMILES}
    
    Returns:
        dict: Todos los resultados organizados
    """
    return {
        'propiedades': calculate_properties(smiles_dict),
        'admet': run_admet_predictions(smiles_dict),
        'toxicidad': predict_toxicity_batch(smiles_dict),
        'pains': check_undesirable_substructures(smiles_dict),
        'fichas': generate_compound_cards(smiles_dict)
    }

if __name__ == "__main__":
    print("¡Importa este módulo y usa analisis_completo(tus_moleculas)!")