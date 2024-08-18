# data_processors.py
"""
Functions for processing and extracting specific data from article content.
This module contains various functions to analyze and categorize article content.
"""

import re

def extract_location(text):
    """Extract the location mentioned in the article text."""
    locations = [
        'Rio de Janeiro', 'Niterói', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu',
        'Belford Roxo', 'São João de Meriti', 'Magé', 'Itaboraí', 'Mesquita',
        'Nilópolis', 'Queimados', 'Maricá', 'Itaguaí', 'Japeri', 'Seropédica',
        'Guapimirim', 'Paracambi', 'Rio Bonito', 'Tanguá',
        'Copacabana', 'Ipanema', 'Leblon', 'Barra da Tijuca', 'Tijuca', 'Maracanã',
        'Centro', 'Botafogo', 'Flamengo', 'Laranjeiras', 'Catete', 'Glória',
        'Santa Teresa', 'Lapa', 'Urca', 'Jardim Botânico', 'Gávea', 'São Conrado',
        'Recreio dos Bandeirantes', 'Jacarepaguá', 'Méier', 'Madureira', 'Penha',
        'Ilha do Governador', 'Ramos', 'Olaria', 'Bonsucesso', 'Pavuna', 'Irajá',
        'Bangu', 'Campo Grande', 'Santa Cruz', 'Realengo'
    ]
    for loc in locations:
        if loc.lower() in text.lower():
            return loc
    return 'Rio de Janeiro'  # Default to Rio de Janeiro if no specific location found

def extract_police_involvement(text):
    """Determine if there's police involvement mentioned in the article."""
    police_keywords = ['polícia', 'policial', 'PM', 'Polícia Militar']
    return 1 if any(keyword in text.lower() for keyword in police_keywords) else 0

def extract_gang_involvement(text):
    """Determine if there's gang involvement mentioned in the article."""
    gang_keywords = ['gangue', 'facção', 'crime organizado', 'milícia']
    return 1 if any(keyword in text.lower() for keyword in gang_keywords) else 0

def extract_victims(text):
    """Extract the number of victims mentioned in the article."""
    victim_match = re.search(r'(\d+)\s+vítimas?', text, re.IGNORECASE)
    return int(victim_match.group(1)) if victim_match else 0

def extract_gender(text):
    """Extract gender information from the article text."""
    male_keywords = ['homem', 'homens', 'masculino']
    female_keywords = ['mulher', 'mulheres', 'feminino']
    male_count = sum(text.lower().count(word) for word in male_keywords)
    female_count = sum(text.lower().count(word) for word in female_keywords)
    return f"{male_count}M, {female_count}F"

def determine_violence_level(text):
    """Determine the level of violence based on keywords in the article."""
    high_keywords = ['assassinato', 'homicídio', 'morte']
    medium_keywords = ['ferido', 'agressão', 'tiro']
    low_keywords = ['ameaça', 'roubo', 'furto']
    
    if any(keyword in text.lower() for keyword in high_keywords):
        return 'High'
    elif any(keyword in text.lower() for keyword in medium_keywords):
        return 'Medium'
    elif any(keyword in text.lower() for keyword in low_keywords):
        return 'Low'
    return 'Unknown'

def determine_violence_type(text):
    """Determine the type of violence mentioned in the article."""
    types = {
        'Homicídio': ['assassinato', 'homicídio', 'morte'],
        'Roubo': ['roubo', 'assalto'],
        'Agressão': ['agressão', 'espancamento'],
        'Tiroteio': ['tiroteio', 'troca de tiros'],
        'Sequestro': ['sequestro', 'cárcere privado']
    }
    for vtype, keywords in types.items():
        if any(keyword in text.lower() for keyword in keywords):
            return vtype
    return 'Unknown'

def is_violence_related(text):
    """Determine if the article is related to violence based on keywords."""
    violence_keywords = [
        'crime', 'violência', 'assassinato', 'homicídio', 'morte', 'tiro', 'bala',
        'assalto', 'roubo', 'furto', 'sequestro', 'agressão', 'briga', 'confronto',
        'operação policial', 'milícia', 'tráfico', 'drogas', 'arma', 'fuzil', 'pistola'
    ]
    return any(keyword in text.lower() for keyword in violence_keywords)

def extract_journalist(text):
    """Extract the journalist's name from the article text."""
    journalist_match = re.search(r'Por\s+([^\n]+)', text)
    return journalist_match.group(1) if journalist_match else 'Unknown'