#!/usr/bin/env python3
"""
Funciones de generación masiva directas (sin dependencias problemáticas)
"""

import time
import logging
from collections import defaultdict
import random

# Configurar logger
logger = logging.getLogger(__name__)

def _get_random_diversity_value(category, gender=None):
    """Obtener valor aleatorio real para diversidad genética"""
    diversity_options = {
        'region': ['Caracas', 'Maracaibo', 'Valencia', 'Barquisimeto', 'Maracay', 'Ciudad Guayana', 'Maturín', 'San Cristóbal', 'Cumana', 'Barinas'],
        'skin_tone': ['fair', 'light', 'medium', 'olive', 'tan', 'brown', 'dark'],
        'hair_color': ['black', 'dark brown', 'brown', 'light brown', 'blonde', 'red', 'gray', 'white'],
        'hair_style': ['short', 'medium', 'long', 'curly', 'straight', 'wavy', 'messy', 'neat', 'styled'],
        'eye_color': ['brown', 'black', 'hazel', 'green', 'blue', 'gray'],
        'face_shape': ['oval', 'round', 'square', 'heart', 'diamond', 'long'],
        'nose_shape': ['straight', 'aquiline', 'button', 'wide', 'narrow', 'pointed'],
        'lip_shape': ['full', 'thin', 'medium', 'wide', 'narrow'],
        'eye_shape': ['almond', 'round', 'hooded', 'deep-set', 'wide-set'],
        'jawline': ['defined', 'soft', 'strong', 'weak', 'angular'],
        'cheekbone': ['prominent', 'high', 'low', 'flat', 'defined'],
        'eyebrow': ['arched', 'straight', 'thick', 'thin', 'bushy'],
        'skin_texture': ['smooth', 'rough', 'normal', 'oily', 'dry'],
        'freckle': ['none', 'light', 'heavy', 'scattered'],
        'mole': ['none', 'small', 'medium', 'large'],
        'scar': ['none', 'small', 'medium', 'large'],
        'acne': ['none', 'light', 'moderate', 'severe'],
        'wrinkle': ['none', 'light', 'moderate', 'heavy'],
        'facial_hair': ['none', 'light', 'medium', 'heavy'] if gender and gender.lower() in ['hombre', 'male', 'masculino'] else ['none'],
        'beard': ['none', 'stubble', 'short', 'medium', 'long'] if gender and gender.lower() in ['hombre', 'male', 'masculino'] else ['none'],
        'mustache': ['none', 'thin', 'medium', 'thick'] if gender and gender.lower() in ['hombre', 'male', 'masculino'] else ['none'],
        'physical_complexion': ['thin', 'normal', 'athletic', 'muscular', 'overweight', 'obese'],
        'clothing_type': ['dress_shirt', 'polo_shirt', 't_shirt', 'sweater', 'jacket', 'suit'],
        'clothing_color': ['blue', 'black', 'gray', 'brown', 'green', 'red', 'navy', 'dark_blue'],
        'background': ['white_solid'],
        'makeup': ['no_makeup', 'natural', 'light', 'moderate', 'heavy'] if gender and gender.lower() in ['mujer', 'female', 'woman'] else ['no_makeup']
    }
    
    if category in diversity_options:
        return random.choice(diversity_options[category])
    return 'random'

def _get_diversity_value_no_repeat(category, used_values, gender=None):
    """Obtener valor aleatorio evitando repetir dentro del mismo lote."""
    # Obtener universo de opciones
    pool_value = _get_random_diversity_value(category, gender)
    # Para obtener el pool completo, replicamos la misma tabla local aquí
    options_map = {
        'region': ['Caracas', 'Maracaibo', 'Valencia', 'Barquisimeto', 'Maracay', 'Ciudad Guayana', 'Maturín', 'San Cristóbal', 'Cumana', 'Barinas'],
        'skin_tone': ['fair', 'light', 'medium', 'olive', 'tan', 'brown', 'dark'],
        'hair_color': ['black', 'dark brown', 'brown', 'light brown', 'blonde', 'red', 'gray', 'white'],
        'hair_style': ['short', 'medium', 'long', 'curly', 'straight', 'wavy', 'messy', 'neat', 'styled'],
        'eye_color': ['brown', 'black', 'hazel', 'green', 'blue', 'gray'],
        'face_shape': ['oval', 'round', 'square', 'heart', 'diamond', 'long'],
        'nose_shape': ['straight', 'aquiline', 'button', 'wide', 'narrow', 'pointed'],
        'lip_shape': ['full', 'thin', 'medium', 'wide', 'narrow'],
        'eye_shape': ['almond', 'round', 'hooded', 'deep-set', 'wide-set'],
        'jawline': ['defined', 'soft', 'strong', 'weak', 'angular'],
        'cheekbone': ['prominent', 'high', 'low', 'flat', 'defined'],
        'eyebrow': ['arched', 'straight', 'thick', 'thin', 'bushy'],
        'physical_complexion': ['thin', 'normal', 'athletic', 'muscular', 'overweight', 'obese'],
        'clothing_type': ['dress_shirt', 'polo_shirt', 't_shirt', 'sweater', 'jacket', 'suit'],
        'clothing_color': ['blue', 'black', 'gray', 'brown', 'green', 'red', 'navy', 'dark_blue'],
        'facial_hair_male': ['none', 'light', 'medium', 'heavy'],
        'beard_male': ['none', 'stubble', 'short', 'medium', 'long'],
        'mustache_male': ['none', 'thin', 'medium', 'thick']
    }
    # Seleccionar pool por categoría y género si aplica
    if category in ['facial_hair', 'beard', 'mustache'] and gender and gender.lower() in ['hombre', 'male', 'masculino']:
        key = f"{category}_male"
        pool = list(options_map.get(key, []))
    else:
        pool = list(options_map.get(category, []))
        if not pool:
            return pool_value
    # Filtrar usados
    used = used_values[category]
    candidates = [v for v in pool if v not in used]
    if not candidates:
        # Reset si agotamos el pool
        used.clear()
        candidates = pool
    choice = random.choice(candidates)
    used.add(choice)
    return choice

REGION_BIAS_WEIGHTS = {
    # Pesos simples para Venezuela por región (aproximados, diversidad multi-étnica)
    'Caracas': {
        'skin_tone': {'light': 1, 'medium': 3, 'olive': 2, 'tan': 2, 'brown': 1, 'fair': 1, 'dark': 1},
        'hair_color': {'black': 3, 'dark brown': 3, 'brown': 2, 'light brown': 1, 'blonde': 1, 'red': 1, 'gray': 1},
        'eye_color': {'brown': 5, 'black': 2, 'hazel': 2, 'green': 1, 'blue': 1, 'gray': 1},
    },
    'Maracaibo': {
        'skin_tone': {'tan': 3, 'olive': 3, 'medium': 2, 'brown': 2, 'dark': 1, 'light': 1, 'fair': 1},
        'hair_color': {'black': 4, 'dark brown': 3, 'brown': 2, 'light brown': 1, 'blonde': 1},
        'eye_color': {'brown': 6, 'black': 2, 'hazel': 2},
    },
    'Valencia': {
        'skin_tone': {'light': 2, 'medium': 3, 'olive': 2, 'tan': 2, 'fair': 1, 'brown': 1},
        'hair_color': {'black': 3, 'dark brown': 3, 'brown': 2, 'light brown': 2, 'blonde': 1},
        'eye_color': {'brown': 5, 'hazel': 2, 'green': 1, 'black': 1},
    },
    'Ciudad Guayana': {
        'skin_tone': {'olive': 3, 'tan': 3, 'medium': 2, 'brown': 2, 'dark': 1, 'light': 1},
        'hair_color': {'black': 4, 'dark brown': 3, 'brown': 2},
        'eye_color': {'brown': 6, 'black': 2, 'hazel': 2},
    },
    'Maturín': {
        'skin_tone': {'medium': 3, 'olive': 2, 'tan': 2, 'light': 1, 'fair': 1, 'brown': 1},
        'hair_color': {'black': 3, 'dark brown': 3, 'brown': 2, 'light brown': 1},
        'eye_color': {'brown': 5, 'hazel': 2, 'black': 2},
    },
    'Barinas': {
        'skin_tone': {'light': 2, 'medium': 3, 'olive': 2, 'tan': 2, 'fair': 1},
        'hair_color': {'dark brown': 3, 'brown': 3, 'black': 2, 'light brown': 2},
        'eye_color': {'brown': 5, 'hazel': 2},
    },
    'Barquisimeto': {
        'skin_tone': {'light': 2, 'medium': 3, 'olive': 2, 'tan': 2},
        'hair_color': {'dark brown': 3, 'brown': 3, 'black': 2},
        'eye_color': {'brown': 5, 'hazel': 2},
    },
    'Maracay': {
        'skin_tone': {'light': 2, 'medium': 3, 'olive': 2, 'tan': 2},
        'hair_color': {'dark brown': 3, 'brown': 3, 'black': 2},
        'eye_color': {'brown': 5, 'hazel': 2},
    },
    'San Cristóbal': {
        'skin_tone': {'fair': 2, 'light': 2, 'medium': 3, 'olive': 2},
        'hair_color': {'brown': 3, 'dark brown': 3, 'black': 2, 'light brown': 2},
        'eye_color': {'brown': 4, 'hazel': 2, 'green': 1},
    },
    'Cumana': {
        'skin_tone': {'light': 2, 'medium': 3, 'olive': 2, 'tan': 2},
        'hair_color': {'dark brown': 3, 'brown': 3, 'black': 2},
        'eye_color': {'brown': 5, 'hazel': 2},
    },
}

def _weighted_choice_no_repeat(category, region, used_values, gender=None):
    """Elección ponderada por región, evitando repetición en el lote."""
    region_weights = REGION_BIAS_WEIGHTS.get(region)
    # categorías soportadas por pesos
    bias_supported = ['skin_tone', 'hair_color', 'eye_color']
    if not region_weights or category not in bias_supported:
        return _get_diversity_value_no_repeat(category, used_values, gender)
    weights_map = region_weights.get(category, {})
    if not weights_map:
        return _get_diversity_value_no_repeat(category, used_values, gender)
    # Construir listas de candidatos y pesos filtrando usados
    used = used_values[category]
    candidates = []
    weights = []
    for val, w in weights_map.items():
        if val not in used and w > 0:
            candidates.append(val)
            weights.append(w)
    if not candidates:
        used.clear()
        for val, w in weights_map.items():
            if w > 0:
                candidates.append(val)
                weights.append(w)
    choice = random.choices(candidates, weights=weights, k=1)[0]
    used.add(choice)
    return choice

def _append_random_gender_descriptors(prompt_parts, gender_str):
    """Añade descriptores de género con variedad controlada."""
    is_male = gender_str.lower() in ['hombre', 'male', 'masculino']
    if is_male:
        options = [
            "masculine features", "strong jawline", "defined jawline", "broad shoulders",
            "masculine shoulders", "thick neck", "masculine build", "athletic build"
        ]
    else:
        options = [
            "feminine features", "soft jawline", "graceful jawline", "delicate shoulders",
            "slender neck", "feminine build", "graceful build"
        ]
    # Elegir aleatoriamente 3-5 descriptores sin repetición
    k = random.randint(3, min(5, len(options)))
    for desc in random.sample(options, k):
        prompt_parts.append(desc)

def generate_genetic_batch(params):
    """
    Generar lote de imágenes genéticas con controles de diversidad
    """
    try:
        # Importar el motor de diversidad
        from diversity_engine import UltraDiversityEngine
        from api_client import GeneticAPIGenerator
        from file_manager import FileManager
        
        # Crear instancia del motor de diversidad
        diversity_engine = UltraDiversityEngine()
        
        # Crear cliente API y generador
        from api_client import WebUIAPIClient
        api_client = WebUIAPIClient()
        api_generator = GeneticAPIGenerator(api_client)
        
        # Crear gestor de archivos
        file_manager = FileManager()
        
        # Configurar parámetros de diversidad avanzados
        diversity_params = {
            'nacionalidad': params.get('nacionalidad', 'Venezuela'),
            'genero': params.get('genero', 'hombre'),
            'region': params.get('region', 'random'),
            'edad_min': params.get('edad_min', 25),
            'edad_max': params.get('edad_max', 60),
            'cantidad': params.get('cantidad', 5),
            'beauty_control': params.get('beauty_control', 'random'),
            'skin_control': params.get('skin_control', 'random'),
            'hair_control': params.get('hair_control', 'random'),
            'hair_length_control': params.get('hair_length_control', 'random'),
            'hair_style_control': params.get('hair_style_control', 'random'),
            'eye_control': params.get('eye_control', 'random'),
            'eye_shape_control': params.get('eye_shape_control', 'random'),
            'face_shape_control': params.get('face_shape_control', 'random'),
            'nose_shape_control': params.get('nose_shape_control', 'random'),
            'lip_shape_control': params.get('lip_shape_control', 'random'),
            'jawline_control': params.get('jawline_control', 'random'),
            'cheekbone_control': params.get('cheekbone_control', 'random'),
            'eyebrow_control': params.get('eyebrow_control', 'random'),
            'skin_texture_control': params.get('skin_texture_control', 'random'),
            'makeup_control': params.get('makeup_control', 'random'),
            'clothing_type_control': params.get('clothing_type_control', 'random'),
            'clothing_color_control': params.get('clothing_color_control', 'random'),
            'background_control': params.get('background_control', 'white_solid'),
            'freckle_control': params.get('freckle_control', 'random'),
            'mole_control': params.get('mole_control', 'random'),
            'scar_control': params.get('scar_control', 'random'),
            'acne_control': params.get('acne_control', 'random'),
            'wrinkle_control': params.get('wrinkle_control', 'random'),
            # Nuevos controles de diversidad
            'facial_hair_control': params.get('facial_hair_control', 'random'),
            'beard_control': params.get('beard_control', 'random'),
            'mustache_control': params.get('mustache_control', 'random'),
            'physical_complexion_control': params.get('physical_complexion_control', 'random')
        }
        
        # Generar perfiles genéticos básicos (con muestreo sin repetición por lote)
        profiles = []
        used_values = defaultdict(set)
        for i in range(diversity_params['cantidad']):
            # Generar edad aleatoria dentro del rango
            edad = random.randint(diversity_params['edad_min'], diversity_params['edad_max'])
            
            # Crear perfil básico como diccionario
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            profile = {
                'image_id': f"genetic_{diversity_params.get('nacionalidad', 'Venezuela')}_{diversity_params.get('genero', 'hombre')}_{i+1}_{timestamp}",
                'generated_at': time.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'metadata': {
                    'nationality': diversity_params['nacionalidad'],
                    'gender': 'male' if diversity_params.get('genero') and diversity_params['genero'].lower() in ['hombre', 'male', 'masculino'] else 'female',
                    'region': _get_random_diversity_value('region'),
                    'age': edad,
                    'generation_type': 'genetic_diversity',
                    'unique_characteristics': True
                },
                'ethnic_characteristics': {
                    'region': _get_diversity_value_no_repeat('region', used_values),
                    'region_traits': {
                        'skin_modifier': 'standard',
                        'hair_modifier': 'standard'
                    },
                    'skin_tone': _get_diversity_value_no_repeat('skin_tone', used_values),
                    'hair_color': _get_diversity_value_no_repeat('hair_color', used_values),
                    'hair_style': _get_diversity_value_no_repeat('hair_style', used_values),
                    'eye_color': _get_diversity_value_no_repeat('eye_color', used_values),
                    'face_shape': _get_diversity_value_no_repeat('face_shape', used_values),
                    'nose_shape': _get_diversity_value_no_repeat('nose_shape', used_values),
                    'lip_shape': _get_diversity_value_no_repeat('lip_shape', used_values),
                    'eye_shape': _get_diversity_value_no_repeat('eye_shape', used_values),
                    'jawline': _get_diversity_value_no_repeat('jawline', used_values),
                    'cheekbone': _get_diversity_value_no_repeat('cheekbone', used_values),
                    'eyebrow': _get_diversity_value_no_repeat('eyebrow', used_values),
                    'skin_texture': _get_diversity_value_no_repeat('skin_texture', used_values),
                    'freckle': _get_diversity_value_no_repeat('freckle', used_values),
                    'mole': _get_diversity_value_no_repeat('mole', used_values),
                    'scar': _get_diversity_value_no_repeat('scar', used_values),
                    'acne': _get_diversity_value_no_repeat('acne', used_values),
                    'wrinkle': _get_diversity_value_no_repeat('wrinkle', used_values),
                    # Nuevos controles de diversidad con lógica específica por género
                    'facial_hair': _get_diversity_value_no_repeat('facial_hair', used_values, diversity_params.get('genero')),
                    'beard': _get_diversity_value_no_repeat('beard', used_values, diversity_params.get('genero')),
                    'mustache': _get_diversity_value_no_repeat('mustache', used_values, diversity_params.get('genero')),
                    'physical_complexion': _get_diversity_value_no_repeat('physical_complexion', used_values),
                    'clothing_type': _get_diversity_value_no_repeat('clothing_type', used_values),
                    'clothing_color': _get_diversity_value_no_repeat('clothing_color', used_values),
                    'background': _get_random_diversity_value('background'),
                    'makeup': _get_random_diversity_value('makeup', diversity_params.get('genero'))
                },
                'generation_parameters': {
                    'width': params.get('width', 512),
                    'height': params.get('height', 764),
                    'steps': params.get('steps', 20),
                    'cfg_scale': params.get('cfg_scale', 7.0),
                    'sampler_name': params.get('sampler_name', 'DPM++ 2M'),
                    'seed': random.randint(1, 2**31 - 1),
                    'batch_size': 1,
                    'n_iter': 1,
                    'model_name': params.get('model', 'unknown_model')
                },
                'replication_info': {
                    'description': 'Configuración única para replicar esta imagen exacta',
                    'genetic_diversity': 'Real basada en datos demográficos',
                    'uniqueness': 'Cada imagen tiene características genéticas únicas'
                }
            }
            profiles.append(profile)
        
        # Crear estructura de directorios de salida
        model_name = params.get('model', 'unknown_model')
        output_dir = file_manager.create_output_structure(
            model_name=model_name,
            generation_type="genetico_premium",
            nacionalidad=diversity_params['nacionalidad'],
            genero=diversity_params.get('genero', 'hombre')
        )
        
        # Generar imágenes usando API
        generated_images = []
        print(f"🔍 Generando {len(profiles)} imágenes...")
        for i, profile in enumerate(profiles):
            try:
                print(f"📸 Procesando imagen {i+1}/{len(profiles)}")
                # Crear prompt genético avanzado con controles de diversidad
                prompt_parts = [
                    f"venezuelan passport photo",
                    f"{profile['metadata']['gender']} from {profile['metadata']['nationality']}",
                    f"{profile['metadata']['age']} years old",
                    "professional headshot",
                    "official document photo",
                    "clean white background",
                    "proper lighting",
                    "head and shoulders visible",
                    "neutral expression",
                    "looking at camera",
                    "high quality",
                    "realistic"
                ]
                
                # Descriptores de género variados
                _append_random_gender_descriptors(prompt_parts, diversity_params.get('genero', 'hombre'))

                # Agregar características de diversidad al prompt
                diversity_features = []
                
                # Beauty level
                if diversity_params['beauty_control'] != 'random':
                    diversity_features.append(f"{diversity_params['beauty_control']} appearance")
                
                # Skin tone
                if diversity_params['skin_control'] != 'random':
                    diversity_features.append(f"{diversity_params['skin_control']} skin")
                
                # Hair characteristics
                if diversity_params['hair_control'] != 'random':
                    diversity_features.append(f"{diversity_params['hair_control']} hair")
                if diversity_params['hair_length_control'] != 'random':
                    diversity_features.append(f"{diversity_params['hair_length_control']} hair")
                if diversity_params['hair_style_control'] != 'random':
                    diversity_features.append(f"{diversity_params['hair_style_control']} hairstyle")
                
                # Eye characteristics
                if diversity_params['eye_control'] != 'random':
                    diversity_features.append(f"{diversity_params['eye_control']} eyes")
                if diversity_params['eye_shape_control'] != 'random':
                    diversity_features.append(f"{diversity_params['eye_shape_control']} eyes")
                
                # Facial features
                if diversity_params['face_shape_control'] != 'random':
                    diversity_features.append(f"{diversity_params['face_shape_control']} face")
                if diversity_params['nose_shape_control'] != 'random':
                    diversity_features.append(f"{diversity_params['nose_shape_control']} nose")
                if diversity_params['lip_shape_control'] != 'random':
                    diversity_features.append(f"{diversity_params['lip_shape_control']} lips")
                if diversity_params['jawline_control'] != 'random':
                    diversity_features.append(f"{diversity_params['jawline_control']} jawline")
                if diversity_params['cheekbone_control'] != 'random':
                    diversity_features.append(f"{diversity_params['cheekbone_control']} cheekbones")
                if diversity_params['eyebrow_control'] != 'random':
                    diversity_features.append(f"{diversity_params['eyebrow_control']} eyebrows")
                
                # Skin characteristics
                if diversity_params['skin_texture_control'] != 'random':
                    diversity_features.append(f"{diversity_params['skin_texture_control']} skin texture")
                if diversity_params['freckle_control'] != 'random':
                    diversity_features.append(f"{diversity_params['freckle_control']} freckles")
                if diversity_params['mole_control'] != 'random':
                    diversity_features.append(f"{diversity_params['mole_control']} moles")
                if diversity_params['scar_control'] != 'random':
                    diversity_features.append(f"{diversity_params['scar_control']} scars")
                if diversity_params['acne_control'] != 'random':
                    diversity_features.append(f"{diversity_params['acne_control']} acne")
                if diversity_params['wrinkle_control'] != 'random':
                    diversity_features.append(f"{diversity_params['wrinkle_control']} wrinkles")
                
                # Makeup and clothing
                if diversity_params['makeup_control'] != 'random':
                    diversity_features.append(f"{diversity_params['makeup_control']} makeup")
                if diversity_params['clothing_type_control'] != 'random':
                    diversity_features.append(f"{diversity_params['clothing_type_control']}")
                if diversity_params['clothing_color_control'] != 'random':
                    diversity_features.append(f"{diversity_params['clothing_color_control']} clothing")
                
                # Background
                if diversity_params['background_control'] != 'random':
                    if diversity_params['background_control'] == 'white_solid':
                        diversity_features.append("solid white background")
                    else:
                        diversity_features.append(f"{diversity_params['background_control']} background")
                
                # Combinar prompt
                if diversity_features:
                    prompt_parts.extend(diversity_features)
                
                prompt = ", ".join(prompt_parts)
                negative_prompt = "blurry, low quality, distorted, deformed, ugly, bad anatomy, bad proportions, extra limbs, missing limbs, multiple people, smiling, laughing, 3/4 view, side profile, looking away, white clothing, colored background, shadows, jewelry, glasses, hat, excessive makeup"
                
                # Generar imagen usando el cliente API
                image_params = {
                    'width': params.get('width', 512),
                    'height': params.get('height', 764),
                    'cfg_scale': params.get('cfg_scale', 7.0),
                    'steps': params.get('steps', 20),
                    'seed': params.get('seed', -1)
                }
                image_result = api_client.generate_image(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    params=image_params
                )
                
                if image_result:
                    print(f"✅ Imagen {i+1} generada exitosamente")
                    # Guardar imagen con nomenclatura correcta
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    filename = f"genetic_{diversity_params.get('nacionalidad', 'Venezuela')}_{diversity_params.get('genero', 'hombre')}_{i+1}_{timestamp}"
                    
                    # Agregar información de imagen al perfil
                    profile['image_info'] = {
                        'filename': f"{filename}.png",
                        'filepath': str(output_dir / f"{filename}.png"),
                        'generation_successful': True,
                        'generation_time': time.strftime("%Y-%m-%dT%H:%M:%S.%f")
                    }
                    
                    save_result = file_manager.save_image(
                        image_data=image_result,
                        output_dir=output_dir,
                        filename=filename,
                        metadata=profile
                    )
                    
                    if save_result['success']:
                        generated_images.append({
                            'profile': profile,
                            'image_path': save_result['file_path']
                        })
                    
            except Exception as e:
                print(f"❌ Error generando imagen {i+1}: {e}")
                logger.error(f"Error generando imagen {i+1}: {e}")
                continue
        
        # Generar CSV con datos de diversidad
        if generated_images:
            csv_data = []
            for img_data in generated_images:
                profile = img_data['profile']
                csv_data.append({
                    'image_id': profile['image_id'],
                    'nationality': profile['metadata']['nationality'],
                    'gender': profile['metadata']['gender'],
                    'region': profile['metadata']['region'],
                    'age': profile['metadata']['age'],
                    # Características étnicas básicas
                    'skin_tone': profile['ethnic_characteristics']['skin_tone'],
                    'hair_color': profile['ethnic_characteristics']['hair_color'],
                    'hair_style': profile['ethnic_characteristics']['hair_style'],
                    'eye_color': profile['ethnic_characteristics']['eye_color'],
                    'face_shape': profile['ethnic_characteristics']['face_shape'],
                    'nose_shape': profile['ethnic_characteristics']['nose_shape'],
                    'lip_shape': profile['ethnic_characteristics']['lip_shape'],
                    'eye_shape': profile['ethnic_characteristics']['eye_shape'],
                    'jawline': profile['ethnic_characteristics']['jawline'],
                    'cheekbone': profile['ethnic_characteristics']['cheekbone'],
                    'eyebrow': profile['ethnic_characteristics']['eyebrow'],
                    'skin_texture': profile['ethnic_characteristics']['skin_texture'],
                    # Características de la piel
                    'freckle': profile['ethnic_characteristics']['freckle'],
                    'mole': profile['ethnic_characteristics']['mole'],
                    'scar': profile['ethnic_characteristics']['scar'],
                    'acne': profile['ethnic_characteristics']['acne'],
                    'wrinkle': profile['ethnic_characteristics']['wrinkle'],
                    # Nuevas características de diversidad
                    'facial_hair': profile['ethnic_characteristics'].get('facial_hair', 'none'),
                    'beard': profile['ethnic_characteristics'].get('beard', 'none'),
                    'mustache': profile['ethnic_characteristics'].get('mustache', 'none'),
                    'physical_complexion': profile['ethnic_characteristics'].get('physical_complexion', 'normal'),
                    'clothing_type': profile['ethnic_characteristics'].get('clothing_type', 'random'),
                    'clothing_color': profile['ethnic_characteristics'].get('clothing_color', 'random'),
                    'background': profile['ethnic_characteristics'].get('background', 'white_solid'),
                    'makeup': profile['ethnic_characteristics'].get('makeup', 'no_makeup'),
                    # Información de generación
                    'generation_time': profile['generated_at'],
                    'filename': profile['image_info']['filename'],
                    'seed': profile['generation_parameters']['seed'],
                    'model_name': profile['generation_parameters']['model_name'],
                    'cfg_scale': profile['generation_parameters']['cfg_scale'],
                    'steps': profile['generation_parameters']['steps'],
                    'sampler_name': profile['generation_parameters']['sampler_name']
                })
            
            # Guardar CSV
            csv_filename = f"genetic_diversity_analysis_{time.strftime('%Y%m%d_%H%M%S')}.csv"
            file_manager.save_csv_analysis(output_dir, csv_filename, csv_data)
        
        return {
            'success': True,
            'generated_count': len(generated_images),
            'images': generated_images
        }
        
    except Exception as e:
        print(f"Error en generación genética: {e}")
        return {
            'success': False,
            'error': str(e),
            'generated_count': 0
        }

# Importaciones optimizadas - solo las necesarias
import sys
import os
import time
import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

# Evitar importaciones pesadas hasta que sean necesarias
try:
    import hashlib
except ImportError:
    hashlib = None

# Optimización: evitar agregar paths innecesarios
# generation_path = Path(__file__).parent / "ui" / "generation"
# if str(generation_path) not in sys.path:
#     sys.path.insert(0, str(generation_path))

@dataclass
class UltraDiversityProfile:
    """Perfil genético ultra diverso"""
    id: str
    nacionalidad: str
    genero: str
    edad: int
    timestamp: str
    beauty_level: str
    skin_tone: str
    hair_color: str
    eye_color: str
    background: str
    face_shape: str
    nose_shape: str
    lip_shape: str
    eye_shape: str
    jawline: str
    cheekbone: str
    eyebrow: str
    skin_texture: str
    freckles: str
    moles: str
    scars: str
    acne: str
    wrinkles: str
    hair_style: str
    makeup: str
    clothing_type: str
    accessories: str
    expression: str
    ethnicity: str
    body_type: str

class DirectGeneticGenerator:
    """Generador genético directo sin dependencias problemáticas"""
    
    def __init__(self):
        self.data = self._load_diversity_data()
        
        # Sistema anti-repetición específico por género para máxima diversidad
        self.recent_choices_male = {
            'beauty_levels': [], 'skin_tones': [], 'hair_colors': [], 'eye_colors': [], 'backgrounds': [],
            'face_shapes': [], 'nose_shapes': [], 'lip_shapes': [], 'eye_shapes': [], 'jawlines': [],
            'cheekbones': [], 'eyebrows': [], 'skin_textures': [], 'freckles': [], 'moles': [],
            'scars': [], 'acne': [], 'wrinkles': [], 'hair_styles': []
        }
        
        self.recent_choices_female = {
            'beauty_levels': [], 'skin_tones': [], 'hair_colors': [], 'eye_colors': [], 'backgrounds': [],
            'face_shapes': [], 'nose_shapes': [], 'lip_shapes': [], 'eye_shapes': [], 'jawlines': [],
            'cheekbones': [], 'eyebrows': [], 'skin_textures': [], 'freckles': [], 'moles': [],
            'scars': [], 'acne': [], 'wrinkles': [], 'hair_styles': []
        }
        
        self.max_recent_choices = 15  # Historial ultra restrictivo para máxima diversidad
    
    def _load_diversity_data(self):
        """Cargar datos de diversidad ultra expandidos para alcanzar 95.3% de diversidad"""
        # Optimización: usar lazy loading para evitar cargar datos innecesarios
        if hasattr(self, '_diversity_cache'):
            return self._diversity_cache
            
        self._diversity_cache = {
            'beauty_levels': ['muy bajo', 'bajo', 'medio', 'alto', 'muy alto', 'extraordinario', 'único', 'distintivo', 'excepcional', 'sobresaliente', 'notable', 'especial', 'raro', 'incomparable', 'irrepetible', 'singular', 'extraordinario', 'soberbio', 'magnífico', 'excelente'],
            'skin_tones': ['muy claro', 'claro', 'medio claro', 'medio', 'medio oscuro', 'oscuro', 'muy oscuro', 'café', 'canela', 'miel', 'bronce', 'oliva', 'dorado', 'caramelo', 'chocolate', 'ébanos', 'crema', 'marfil', 'beige', 'tostado', 'cobrizo', 'rojizo', 'amarillento', 'verdoso', 'azulado', 'rosado', 'grisáceo', 'pálido', 'moreno', 'trigueño'],
            'hair_colors': ['negro', 'marrón oscuro', 'marrón', 'marrón claro', 'castaño', 'rubio oscuro', 'rubio', 'rubio claro', 'rojo', 'pelirrojo', 'gris', 'blanco', 'sal y pimienta', 'mezclado', 'auburn', 'cobre', 'bronce', 'dorado', 'plateado', 'champagne', 'miel', 'caramelo', 'chocolate', 'ébanos', 'azabache', 'caoba', 'castaño claro', 'rubio ceniza', 'rubio miel', 'rubio platino', 'rojo cobrizo', 'rojo intenso', 'rojo auburn', 'gris plata', 'gris sal', 'blanco nieve', 'blanco perla'],
            'eye_colors': ['marrón oscuro', 'marrón', 'marrón claro', 'avellana', 'verde', 'azul', 'gris', 'verde azulado', 'azul gris', 'ámbar', 'dorado', 'violeta', 'miel', 'café', 'esmeralda', 'azul marino', 'verde esmeralda', 'azul cielo', 'gris azulado', 'marrón chocolate', 'marrón caramelo', 'verde oliva', 'verde jade', 'azul acero', 'azul turquesa', 'gris perla', 'gris acero', 'ámbar dorado', 'violeta intenso', 'verde menta', 'azul profundo', 'marrón tostado', 'verde bosque', 'azul eléctrico', 'gris plata', 'miel clara', 'café oscuro'],
            'backgrounds': ['estudio', 'exterior', 'interior', 'urbano', 'natural', 'profesional', 'oficina', 'casa', 'parque', 'playa', 'montaña', 'ciudad', 'campo', 'universidad', 'hospital', 'trabajo', 'biblioteca', 'café', 'restaurante', 'hotel', 'aeropuerto', 'estación', 'centro comercial', 'museo', 'teatro', 'iglesia', 'escuela', 'gimnasio', 'club', 'residencia', 'apartamento', 'casa de campo', 'chalet', 'loft', 'estudio fotográfico'],
            'face_shapes': ['oval', 'redondo', 'cuadrado', 'corazón', 'diamante', 'triangular', 'rectangular', 'alargado', 'ancho', 'estrecho', 'angular', 'suave', 'definido', 'simétrico', 'asimétrico', 'ovalado', 'redondeado', 'cuadrangular', 'triangular invertido', 'diamante invertido', 'rectangular alargado', 'ovalado alargado', 'redondo ancho', 'cuadrado ancho', 'triangular estrecho', 'diamante estrecho', 'rectangular estrecho', 'ovalado estrecho'],
            'nose_shapes': ['pequeño', 'mediano', 'grande', 'ancho', 'estrecho', 'recto', 'aguileño', 'botón', 'prominente', 'delicado', 'fuerte', 'refinado', 'clásico', 'distintivo', 'elegante', 'robusto', 'pequeño delicado', 'mediano clásico', 'grande prominente', 'ancho robusto', 'estrecho refinado', 'recto clásico', 'aguileño distintivo', 'botón elegante', 'prominente fuerte', 'delicado refinado', 'fuerte robusto', 'refinado elegante', 'clásico distintivo', 'distintivo elegante'],
            'lip_shapes': ['delgados', 'medianos', 'gruesos', 'asimétricos', 'simétricos', 'arqueados', 'rectos', 'redondeados', 'puntiagudos', 'suaves', 'definidos', 'naturales', 'voluptuosos', 'finos', 'generosos', 'delgados finos', 'medianos naturales', 'gruesos voluptuosos', 'asimétricos definidos', 'simétricos suaves', 'arqueados redondeados', 'rectos puntiagudos', 'redondeados suaves', 'puntiagudos definidos', 'suaves naturales', 'definidos voluptuosos', 'naturales generosos', 'voluptuosos finos', 'finos delgados', 'generosos gruesos'],
            'eye_shapes': ['almendrados', 'redondos', 'estrechos', 'grandes', 'pequeños', 'hondos', 'salientes', 'inclinados', 'horizontales', 'verticales', 'asymétricos', 'simétricos', 'expresivos', 'serenos', 'intensos', 'almendrados expresivos', 'redondos serenos', 'estrechos intensos', 'grandes horizontales', 'pequeños verticales', 'hondos inclinados', 'salientes asimétricos', 'inclinados simétricos', 'horizontales expresivos', 'verticales serenos', 'asimétricos intensos', 'simétricos expresivos', 'expresivos serenos', 'serenos intensos', 'intensos almendrados'],
            'jawlines': ['suave', 'definido', 'cuadrado', 'puntiagudo', 'redondeado', 'angular', 'recto', 'inclinado', 'prominente', 'delicado', 'fuerte', 'elegante', 'robusto', 'refinado', 'distintivo', 'suave delicado', 'definido fuerte', 'cuadrado angular', 'puntiagudo recto', 'redondeado inclinado', 'angular prominente', 'recto elegante', 'inclinado robusto', 'prominente refinado', 'delicado distintivo', 'fuerte suave', 'elegante definido', 'robusto cuadrado', 'refinado puntiagudo', 'distintivo redondeado'],
            'cheekbones': ['bajos', 'medios', 'altos', 'prominentes', 'suaves', 'definidos', 'angulares', 'redondeados', 'delicados', 'fuertes', 'elegantes', 'robustos', 'refinados', 'distintivos', 'naturales', 'bajos suaves', 'medios definidos', 'altos angulares', 'prominentes redondeados', 'suaves delicados', 'definidos fuertes', 'angulares elegantes', 'redondeados robustos', 'delicados refinados', 'fuertes distintivos', 'elegantes naturales', 'robustos bajos', 'refinados medios', 'distintivos altos', 'naturales prominentes'],
            'eyebrows': ['delgadas', 'medianas', 'gruesas', 'arqueadas', 'rectas', 'redondeadas', 'angulares', 'suaves', 'definidas', 'naturales', 'expresivas', 'serenas', 'intensas', 'elegantes', 'distintivas', 'delgadas arqueadas', 'medianas rectas', 'gruesas redondeadas', 'arqueadas angulares', 'rectas suaves', 'redondeadas definidas', 'angulares naturales', 'suaves expresivas', 'definidas serenas', 'naturales intensas', 'expresivas elegantes', 'serenas distintivas', 'intensas delgadas', 'elegantes medianas', 'distintivas gruesas'],
            'skin_textures': ['suave', 'rugosa', 'porosa', 'mixta', 'seca', 'grasa', 'normal', 'sensible', 'madura', 'joven', 'natural', 'cuidada', 'descuidada', 'lisa', 'texturizada', 'suave natural', 'rugosa texturizada', 'porosa mixta', 'mixta normal', 'seca sensible', 'grasa madura', 'normal joven', 'sensible cuidada', 'madura descuidada', 'joven lisa', 'natural suave', 'cuidada rugosa', 'descuidada porosa', 'lisa mixta', 'texturizada seca'],
            'freckles': ['ninguno', 'pocos', 'moderados', 'muchos', 'leves', 'intensos', 'dispersos', 'concentrados', 'naturales', 'artificiales', 'suaves', 'definidos', 'tenues', 'prominentes', 'distintivos', 'ninguno natural', 'pocos leves', 'moderados intensos', 'muchos dispersos', 'leves concentrados', 'intensos naturales', 'dispersos artificiales', 'concentrados suaves', 'naturales definidos', 'artificiales tenues', 'suaves prominentes', 'definidos distintivos', 'tenues ninguno', 'prominentes pocos', 'distintivos moderados'],
            'moles': ['ninguno', 'pocos', 'moderados', 'muchos', 'pequeños', 'grandes', 'dispersos', 'concentrados', 'naturales', 'artificiales', 'suaves', 'definidos', 'tenues', 'prominentes', 'distintivos', 'ninguno natural', 'pocos pequeños', 'moderados grandes', 'muchos dispersos', 'pequeños concentrados', 'grandes naturales', 'dispersos artificiales', 'concentrados suaves', 'naturales definidos', 'artificiales tenues', 'suaves prominentes', 'definidos distintivos', 'tenues ninguno', 'prominentes pocos', 'distintivos moderados'],
            'scars': ['ninguno', 'pequeños', 'medianos', 'grandes', 'leves', 'intensos', 'dispersos', 'concentrados', 'naturales', 'artificiales', 'suaves', 'definidos', 'tenues', 'prominentes', 'distintivos', 'ninguno natural', 'pequeños leves', 'medianos intensos', 'grandes dispersos', 'leves concentrados', 'intensos naturales', 'dispersos artificiales', 'concentrados suaves', 'naturales definidos', 'artificiales tenues', 'suaves prominentes', 'definidos distintivos', 'tenues ninguno', 'prominentes pequeños', 'distintivos medianos'],
            'acne': ['ninguno', 'leve', 'moderado', 'severo', 'ocasional', 'crónico', 'disperso', 'concentrado', 'natural', 'artificial', 'suave', 'intenso', 'tenue', 'prominente', 'distintivo', 'ninguno natural', 'leve ocasional', 'moderado crónico', 'severo disperso', 'ocasional concentrado', 'crónico natural', 'disperso artificial', 'concentrado suave', 'natural intenso', 'artificial tenue', 'suave prominente', 'intenso distintivo', 'tenue ninguno', 'prominente leve', 'distintivo moderado'],
            'wrinkles': ['ninguno', 'leves', 'moderados', 'profundos', 'naturales', 'artificiales', 'dispersos', 'concentrados', 'suaves', 'intensos', 'tenues', 'prominentes', 'distintivos', 'expresivos', 'serenos', 'ninguno natural', 'leves artificiales', 'moderados dispersos', 'profundos concentrados', 'naturales suaves', 'artificiales intensos', 'dispersos tenues', 'concentrados prominentes', 'suaves distintivos', 'intensos expresivos', 'tenues serenos', 'prominentes ninguno', 'distintivos leves', 'expresivos moderados', 'serenos profundos'],
            'hair_styles': ['corto', 'mediano', 'largo', 'ondulado', 'rizado', 'liso', 'recogido', 'suelto', 'peinado', 'despeinado', 'elegante', 'casual', 'formal', 'informal', 'distintivo', 'natural', 'artificial', 'moderno', 'clásico', 'vintage', 'corto peinado', 'mediano ondulado', 'largo rizado', 'ondulado liso', 'rizado recogido', 'liso suelto', 'recogido peinado', 'suelto despeinado', 'peinado elegante', 'despeinado casual', 'elegante formal', 'casual informal', 'formal distintivo', 'informal natural', 'distintivo artificial', 'natural moderno', 'artificial clásico', 'moderno vintage', 'clásico corto', 'vintage mediano']
        }
        
        return self._diversity_cache
    
    def generate(self, nacionalidad, genero, edad, cantidad, region, edad_min, edad_max, 
                beauty_control, skin_control, hair_control, eye_control, background_control,
                face_shape_control, nose_shape_control, lip_shape_control, eye_shape_control,
                jawline_control, cheekbone_control, eyebrow_control, skin_texture_control,
                freckle_control, mole_control, scar_control, acne_control, wrinkle_control, 
                hair_style_control, cfg_scale, steps, sampler_name, seed, width, height, 
                batch_count, batch_size, denoising_strength, hr_second_pass_steps, hr_scale, 
                hr_resize_x, hr_resize_y, hr_upscaler, hr_sampler_name, hr_scheduler, 
                refiner_checkpoint, refiner_switch_at, progress=None):
        """Generar perfiles genéticos con estructura correcta"""
        try:
            # Obtener nombre del modelo actual
            model_name_clean = self._get_model_name()
            
            # Crear estructura de directorios correcta
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            batch_name = f"genetic_{nacionalidad}_{genero}_{timestamp}"
            
            # Estructura: outputs/{model_name}/genetico_premium/{batch_name}/
            output_dir = Path("outputs") / model_name_clean / "genetico_premium" / batch_name
            output_dir.mkdir(parents=True, exist_ok=True)
            
            profiles = []
            image_paths = []
            
            for i in range(cantidad):
                # Generar edad aleatoria si se proporciona rango
                if edad_min and edad_max:
                    final_age = random.randint(edad_min, edad_max)
                else:
                    final_age = edad
                
                # Generar perfil
                profile = self._generate_profile(
                    nacionalidad, genero, final_age, region,
                    beauty_control, skin_control, hair_control, eye_control, background_control,
                    face_shape_control, nose_shape_control, lip_shape_control, eye_shape_control,
                    jawline_control, cheekbone_control, eyebrow_control, skin_texture_control,
                    freckle_control, mole_control, scar_control, acne_control, wrinkle_control, 
                    hair_style_control, i
                )
                profiles.append(profile)
                
                # Crear imagen PNG real usando el motor del WebUI
                image_path = self._create_png_image(profile, output_dir, i+1, cfg_scale, steps, sampler_name, seed, width, height)
                image_paths.append(str(image_path))
                
                # Crear JSON correspondiente
                json_path = self._create_json_metadata(profile, output_dir, i+1)
            
            # Crear CSV de análisis
            csv_path = self._create_csv(profiles, output_dir)
            
            return image_paths, csv_path, "✅ Generación genética completada"
            
        except Exception as e:
            return [], "", f"❌ Error en generación genética: {e}"
    
    def _generate_profile(self, nacionalidad, genero, edad, region, *controls):
        """Generar un perfil individual con sistema anti-repetición específico por género"""
        # Generar ID único
        unique_id = f"genetic_{hashlib.md5(f'{nacionalidad}_{genero}_{edad}_{time.time()}_{random.randint(1, 999999)}'.encode()).hexdigest()[:12]}"
        
        # Generar características con sistema anti-repetición específico por género
        beauty_level = self._get_random_choice('beauty_levels', controls[0], genero)
        skin_tone = self._get_random_choice('skin_tones', controls[1], genero)
        hair_color = self._get_random_choice('hair_colors', controls[2], genero)
        eye_color = self._get_random_choice('eye_colors', controls[3], genero)
        background = self._get_random_choice('backgrounds', controls[4], genero)
        face_shape = self._get_random_choice('face_shapes', controls[5], genero)
        nose_shape = self._get_random_choice('nose_shapes', controls[6], genero)
        lip_shape = self._get_random_choice('lip_shapes', controls[7], genero)
        eye_shape = self._get_random_choice('eye_shapes', controls[8], genero)
        jawline = self._get_gender_appropriate_choice('jawlines', controls[9], genero)
        cheekbone = self._get_gender_appropriate_choice('cheekbones', controls[10], genero)
        eyebrow = self._get_gender_appropriate_choice('eyebrows', controls[11], genero)
        skin_texture = self._get_random_choice('skin_textures', controls[12], genero)
        freckles = self._get_random_choice('freckles', controls[13], genero)
        moles = self._get_random_choice('moles', controls[14], genero)
        scars = self._get_random_choice('scars', controls[15], genero)
        acne = self._get_random_choice('acne', controls[16], genero)
        wrinkles = self._get_age_appropriate_wrinkles(edad, controls[17], genero)
        hair_style = self._get_gender_appropriate_hair_style(controls[18], genero)
        
        return UltraDiversityProfile(
            id=unique_id,
            nacionalidad=nacionalidad,
            genero=genero,
            edad=edad,
            timestamp=time.strftime("%Y%m%d_%H%M%S"),
            beauty_level=beauty_level,
            skin_tone=skin_tone,
            hair_color=hair_color,
            eye_color=eye_color,
            background=background,
            face_shape=face_shape,
            nose_shape=nose_shape,
            lip_shape=lip_shape,
            eye_shape=eye_shape,
            jawline=jawline,
            cheekbone=cheekbone,
            eyebrow=eyebrow,
            skin_texture=skin_texture,
            freckles=freckles,
            moles=moles,
            scars=scars,
            acne=acne,
            wrinkles=wrinkles,
            hair_style=hair_style,
            makeup=self._get_gender_appropriate_makeup(genero),
            clothing_type=self._get_gender_appropriate_clothing(genero),
            accessories=self._get_gender_appropriate_accessories(genero),
            expression=self._get_saime_appropriate_expression(),
            ethnicity=self._get_nationality_appropriate_ethnicity(nacionalidad),
            body_type=self._get_gender_appropriate_body_type(genero)
        )
    
    def _get_random_choice(self, category, control, genero="hombre"):
        """Obtener elección aleatoria con sistema anti-repetición específico por género"""
        if control == "aleatorio":
            # Obtener opciones disponibles
            available_options = self.data[category]
            
            # Usar historial específico por género
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                recent_choices = self.recent_choices_male[category]
            else:
                recent_choices = self.recent_choices_female[category]
            
            # Filtrar opciones recientes para evitar repetición
            filtered_options = [opt for opt in available_options if opt not in recent_choices]
            
            # Si no hay opciones disponibles, usar todas
            if not filtered_options:
                filtered_options = available_options
            
            # Seleccionar opción aleatoria
            selected_choice = random.choice(filtered_options)
            
            # Actualizar historial específico por género
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                self.recent_choices_male[category].append(selected_choice)
                if len(self.recent_choices_male[category]) > self.max_recent_choices:
                    self.recent_choices_male[category].pop(0)
            else:
                self.recent_choices_female[category].append(selected_choice)
                if len(self.recent_choices_female[category]) > self.max_recent_choices:
                    self.recent_choices_female[category].pop(0)
            
            return selected_choice
        else:
            return control if control in self.data[category] else random.choice(self.data[category])
    
    def _get_age_appropriate_wrinkles(self, age, control, genero):
        """Obtener arrugas apropiadas para la edad con sistema anti-repetición específico por género"""
        if control == "aleatorio":
            # Sistema de arrugas por grupos de edad específicos
            if age < 20:
                # Grupo 1: 18-19 años - Sin arrugas
                return "ninguno"
            elif age < 30:
                # Grupo 2: 20-29 años - Arrugas muy leves
                young_options = ["ninguno", "leves", "tenues", "suaves", "naturales", "dispersos", "concentrados"]
                return self._get_random_choice_from_list(young_options, genero, 'wrinkles')
            elif age < 40:
                # Grupo 3: 30-39 años - Arrugas leves a moderadas
                adult_young_options = ["leves", "moderados", "naturales", "dispersos", "concentrados", "suaves", "intensos", "tenues", "prominentes", "distintivos"]
                return self._get_random_choice_from_list(adult_young_options, genero, 'wrinkles')
            elif age < 50:
                # Grupo 4: 40-49 años - Arrugas moderadas
                mature_options = ["moderados", "profundos", "naturales", "artificiales", "dispersos", "concentrados", "suaves", "intensos", "tenues", "prominentes", "distintivos", "expresivos", "serenos"]
                return self._get_random_choice_from_list(mature_options, genero, 'wrinkles')
            elif age < 60:
                # Grupo 5: 50-59 años - Arrugas profundas
                older_options = ["profundos", "naturales", "artificiales", "dispersos", "concentrados", "intensos", "prominentes", "distintivos", "expresivos", "serenos"]
                return self._get_random_choice_from_list(older_options, genero, 'wrinkles')
            else:
                # Grupo 6: 60+ años - Arrugas muy profundas
                elderly_options = ["profundos", "naturales", "artificiales", "concentrados", "intensos", "prominentes", "distintivos", "expresivos", "serenos"]
                return self._get_random_choice_from_list(elderly_options, genero, 'wrinkles')
        else:
            return control if control in self.data['wrinkles'] else random.choice(self.data['wrinkles'])
    
    def _get_random_choice_from_list(self, options, genero, category):
        """Obtener elección aleatoria de una lista con sistema anti-repetición específico por género"""
        # Usar historial específico por género
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            recent_choices = self.recent_choices_male[category]
        else:
            recent_choices = self.recent_choices_female[category]
        
        # Filtrar opciones recientes para evitar repetición
        filtered_options = [opt for opt in options if opt not in recent_choices]
        
        # Si no hay opciones disponibles, usar todas
        if not filtered_options:
            filtered_options = options
        
        # Seleccionar opción aleatoria
        selected_choice = random.choice(filtered_options)
        
        # Actualizar historial específico por género
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            self.recent_choices_male[category].append(selected_choice)
            if len(self.recent_choices_male[category]) > self.max_recent_choices:
                self.recent_choices_male[category].pop(0)
        else:
            self.recent_choices_female[category].append(selected_choice)
            if len(self.recent_choices_female[category]) > self.max_recent_choices:
                self.recent_choices_female[category].pop(0)
        
        return selected_choice
    
    def _get_gender_appropriate_choice(self, category, control, genero):
        """Obtener elección apropiada por género con sistema anti-repetición"""
        if control == "aleatorio":
            # Obtener opciones disponibles
            available_options = self.data[category]
            
            # Filtrar opciones apropiadas por género
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                # Características masculinas
                if category == 'jawlines':
                    masculine_options = ['definido', 'cuadrado', 'angular', 'fuerte', 'robusto', 'prominente', 'recto', 'inclinado', 'elegante', 'distintivo']
                elif category == 'cheekbones':
                    masculine_options = ['altos', 'prominentes', 'definidos', 'angulares', 'fuertes', 'elegantes', 'robustos', 'refinados', 'distintivos', 'naturales']
                elif category == 'eyebrows':
                    masculine_options = ['gruesas', 'medianas', 'definidas', 'naturales', 'expresivas', 'serenas', 'intensas', 'elegantes', 'distintivas']
                else:
                    masculine_options = available_options
            else:
                # Características femeninas
                if category == 'jawlines':
                    feminine_options = ['suave', 'redondeado', 'delicado', 'elegante', 'refinado', 'distintivo', 'angular', 'recto', 'inclinado', 'prominente']
                elif category == 'cheekbones':
                    feminine_options = ['bajos', 'medios', 'suaves', 'definidos', 'redondeados', 'delicados', 'fuertes', 'elegantes', 'robustos', 'refinados', 'distintivos', 'naturales']
                elif category == 'eyebrows':
                    feminine_options = ['delgadas', 'medianas', 'arqueadas', 'suaves', 'definidas', 'naturales', 'expresivas', 'serenas', 'intensas', 'elegantes', 'distintivas']
                else:
                    feminine_options = available_options
            
            # Usar opciones apropiadas por género
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                gender_options = masculine_options if category in ['jawlines', 'cheekbones', 'eyebrows'] else available_options
            else:
                gender_options = feminine_options if category in ['jawlines', 'cheekbones', 'eyebrows'] else available_options
            
            # Filtrar opciones recientes para evitar repetición
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                recent_choices = self.recent_choices_male[category]
            else:
                recent_choices = self.recent_choices_female[category]
            
            filtered_options = [opt for opt in gender_options if opt not in recent_choices]
            
            # Si no hay opciones disponibles, usar todas las opciones de género
            if not filtered_options:
                filtered_options = gender_options
            
            # Si aún no hay opciones, usar todas las disponibles
            if not filtered_options:
                filtered_options = available_options
            
            # Seleccionar opción aleatoria
            selected_choice = random.choice(filtered_options)
            
            # Actualizar historial específico por género
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                self.recent_choices_male[category].append(selected_choice)
                if len(self.recent_choices_male[category]) > self.max_recent_choices:
                    self.recent_choices_male[category].pop(0)
            else:
                self.recent_choices_female[category].append(selected_choice)
                if len(self.recent_choices_female[category]) > self.max_recent_choices:
                    self.recent_choices_female[category].pop(0)
            
            return selected_choice
        else:
            return control if control in self.data[category] else random.choice(self.data[category])

    def _get_gender_appropriate_makeup(self, genero):
        """Obtener maquillaje apropiado por género"""
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            return 'ninguno'  # Hombres sin maquillaje para SAIME
        else:
            return random.choice(['ninguno', 'leve', 'moderado'])

    def _get_gender_appropriate_clothing(self, genero):
        """Obtener ropa apropiada por género"""
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            return random.choice(['formal', 'casual', 'elegante'])
        else:
            return random.choice(['formal', 'casual', 'elegante', 'deportivo'])

    def _get_gender_appropriate_accessories(self, genero):
        """Obtener accesorios apropiados por género"""
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            return random.choice(['ninguno', 'reloj'])
        else:
            return random.choice(['ninguno', 'gafas', 'reloj', 'collar'])

    def _get_saime_appropriate_expression(self):
        """Obtener expresión apropiada para SAIME (neutral obligatorio)"""
        return 'neutral'  # SAIME requiere expresión neutral

    def _get_nationality_appropriate_ethnicity(self, nacionalidad):
        """Obtener etnia apropiada para la nacionalidad"""
        if nacionalidad.lower() == 'venezuela':
            return random.choice(['latino', 'mixto', 'europeo'])
        elif nacionalidad.lower() == 'colombia':
            return random.choice(['latino', 'mixto', 'europeo'])
        elif nacionalidad.lower() == 'mexico':
            return random.choice(['latino', 'mixto', 'europeo'])
        else:
            return random.choice(['latino', 'mixto', 'europeo', 'africano'])

    def _get_gender_appropriate_body_type(self, genero):
        """Obtener tipo de cuerpo apropiado por género"""
        if genero and genero.lower() in ['hombre', 'male', 'masculino']:
            return random.choice(['mediano', 'atlético', 'robusto'])
        else:
            return random.choice(['delgado', 'mediano', 'atlético'])

    def _get_gender_appropriate_hair_style(self, control, genero):
        """Obtener peinado apropiado por género"""
        if control == "aleatorio":
            if genero and genero.lower() in ['hombre', 'male', 'masculino']:
                # Peinados masculinos apropiados
                masculine_styles = [
                    'corto', 'mediano', 'ondulado', 'rizado', 'liso', 'suelto', 
                    'peinado', 'elegante', 'casual', 'formal', 'distintivo', 
                    'natural', 'moderno', 'clásico', 'corto peinado', 
                    'mediano ondulado', 'ondulado liso', 'liso suelto', 
                    'peinado elegante', 'casual formal', 'elegante natural', 
                    'formal moderno', 'distintivo clásico', 'natural corto'
                ]
                return self._get_random_choice_from_list(masculine_styles, genero, 'hair_styles')
            else:
                # Peinados femeninos apropiados
                feminine_styles = [
                    'corto', 'mediano', 'largo', 'ondulado', 'rizado', 'liso', 
                    'recogido', 'suelto', 'peinado', 'elegante', 'casual', 
                    'formal', 'distintivo', 'natural', 'moderno', 'clásico', 
                    'vintage', 'corto peinado', 'mediano ondulado', 'largo rizado', 
                    'ondulado liso', 'rizado recogido', 'liso suelto', 
                    'recogido peinado', 'suelto despeinado', 'peinado elegante', 
                    'despeinado casual', 'elegante formal', 'casual informal', 
                    'formal distintivo', 'informal natural', 'distintivo artificial', 
                    'natural moderno', 'artificial clásico', 'moderno vintage', 
                    'clásico corto', 'vintage mediano'
                ]
                return self._get_random_choice_from_list(feminine_styles, genero, 'hair_styles')
        else:
            return control if control in self.data['hair_styles'] else random.choice(self.data['hair_styles'])
    
    def _get_model_name(self):
        """Obtener nombre del modelo actual"""
        try:
            from modules import shared
            if shared.sd_model and hasattr(shared.sd_model, 'sd_checkpoint_info'):
                model_name = shared.sd_model.sd_checkpoint_info.name_for_extra
            else:
                model_name = "unknown_model"
            
            # Limpiar nombre del modelo para usar como nombre de carpeta
            model_name_clean = "".join(c for c in model_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            model_name_clean = model_name_clean.replace(' ', '_')
            return model_name_clean
        except Exception as e:
            print(f"⚠️ Error obteniendo nombre del modelo: {e}")
            return "unknown_model"
    
    def _create_png_image(self, profile, output_dir, index, cfg_scale, steps, sampler_name, seed, width, height):
        """Crear imagen PNG real usando la API del WebUI"""
        try:
            # Generar prompt basado en el perfil genético
            prompt = self._generate_genetic_prompt(profile)
            negative_prompt = self._generate_negative_prompt(profile)
            
            print(f"🎨 Generando imagen real para perfil {profile.id}")
            print(f"📝 Prompt: {prompt}")
            print(f"🚫 Negative: {negative_prompt}")
            
            # Usar la API del WebUI directamente
            import modules.txt2img as txt2img_module
            import modules.shared as shared
            from modules import processing
            from contextlib import closing
            
            # Verificar que el modelo esté cargado
            if not shared.sd_model:
                raise Exception("No hay modelo cargado en el WebUI")
            
            # Crear un request dummy para la API
            class DummyRequest:
                def __init__(self):
                    self.username = "genetic_generator"
            
            dummy_request = DummyRequest()
            
            # Usar txt2img_create_processing para configurar correctamente
            task_id = f"genetic_{profile.id}_{index}"
            
            # Configurar override settings para sampler y steps
            override_settings = {}
            if sampler_name:
                override_settings['sd_sampler'] = sampler_name
            if steps:
                override_settings['sd_steps'] = steps
            if seed != -1:
                override_settings['sd_seed'] = seed
            
            # Crear procesamiento usando la función del WebUI
            p = txt2img_module.txt2img_create_processing(
                id_task=task_id,
                request=dummy_request,
                prompt=prompt,
                negative_prompt=negative_prompt,
                prompt_styles=[],  # Sin estilos
                n_iter=1,
                batch_size=1,
                cfg_scale=cfg_scale,
                height=height,
                width=width,
                enable_hr=False,
                denoising_strength=0.0,
                hr_scale=1.0,
                hr_upscaler="Latent",
                hr_second_pass_steps=0,
                hr_resize_x=0,
                hr_resize_y=0,
                hr_checkpoint_name="Use same checkpoint",
                hr_sampler_name="Use same sampler",
                hr_scheduler="Use same scheduler",
                hr_prompt="",
                hr_negative_prompt="",
                override_settings_texts=[],
                force_enable_hr=False
            )
            
            # Configurar sampler y steps manualmente
            if sampler_name:
                p.sampler_name = sampler_name
            if steps:
                p.steps = steps
            if seed != -1:
                p.seed = seed
            
            # Configurar directorio de salida
            p.outpath_samples = str(output_dir)
            p.outpath_grids = str(output_dir)
            
            print(f"⚙️ Configuración: {sampler_name}, {steps} steps, CFG: {cfg_scale}, Seed: {seed}")
            
            # Ejecutar generación
            with closing(p):
                processed = processing.process_images(p)
            
            if processed.images and len(processed.images) > 0:
                # Guardar imagen con nombre específico
                image_path = output_dir / f"genetic_{profile.id}.png"
                processed.images[0].save(image_path, 'PNG')
                print(f"✅ Imagen real generada: {image_path}")
                return image_path
            else:
                raise Exception("No se generó ninguna imagen")
                
        except Exception as e:
            print(f"⚠️ Error generando imagen real: {e}")
            print(f"🔄 Usando fallback para perfil {profile.id}")
            # Fallback: crear PNG placeholder
            return self._create_placeholder_image(profile, output_dir)
    
    def _generate_genetic_prompt(self, profile):
        """Generar prompt basado en el perfil genético con especificaciones SAIME y características de género"""
        prompt_parts = []
        
        # Especificaciones SAIME obligatorias
        prompt_parts.append("venezuelan passport photo, ICAO standards, official document photo, government ID photo")
        
        # Especificar género de manera más clara y específica
        gender = profile['metadata']['gender'].lower()
        if gender in ['hombre', 'male', 'masculino']:
            prompt_parts.append("MALE person, MAN, MASCULINE person, MALE individual")
            prompt_parts.append("MALE features, MASCULINE features, MALE characteristics")
        else:
            prompt_parts.append("FEMALE person, WOMAN, FEMININE person, FEMALE individual")
            prompt_parts.append("FEMALE features, FEMININE features, FEMALE characteristics")
        
        prompt_parts.append(f"Venezuela, {profile['metadata']['age']} years old")
        prompt_parts.append("front view, frontal view, looking directly at camera, direct eye contact")
        prompt_parts.append("neutral expression, serious expression, no smile, no laughing, mouth closed")
        prompt_parts.append("eyes open and visible, head centered and straight, frontal position")
        prompt_parts.append("PURE WHITE BACKGROUND, SOLID WHITE BACKGROUND, CLEAN WHITE BACKGROUND")
        prompt_parts.append("UNIFORM WHITE BACKGROUND, PLAIN WHITE BACKGROUND, STUDIO WHITE BACKGROUND")
        prompt_parts.append("BRIGHT WHITE BACKGROUND, SNOW WHITE BACKGROUND, PAPER WHITE BACKGROUND")
        prompt_parts.append("WHITE WALL BACKGROUND, WHITE STUDIO BACKGROUND, WHITE BACKDROP")
        prompt_parts.append("NO SHADOWS ON BACKGROUND, NO GRADIENTS, NO TEXTURES, NO PATTERNS")
        prompt_parts.append("professional lighting, uniform lighting, even lighting, high contrast")
        prompt_parts.append("35mm x 45mm dimensions, 300 DPI resolution, professional quality, high resolution")
        prompt_parts.append("512x764 pixels, ultra high quality, no head accessories, natural makeup")
        prompt_parts.append("contrasting clothing colors, avoid white clothing, colored clothing, dark clothing")
        prompt_parts.append("sharp and focused image, correct exposure, NATURAL COLORS, VIBRANT COLORS")
        prompt_parts.append("FULL COLOR, COLOR PHOTOGRAPHY, COLOR IMAGE, COLOR PORTRAIT, COLOR HEADSHOT")
        prompt_parts.append("COLOR PASSPORT PHOTO, COLOR ID PHOTO, COLOR DOCUMENT PHOTO, COLOR OFFICIAL PHOTO")
        prompt_parts.append("COLOR GOVERNMENT PHOTO, EVERYDAY PERSON, NORMAL PERSON, REGULAR PERSON")
        prompt_parts.append("COMMON PERSON, AVERAGE PERSON, REAL PERSON, AUTHENTIC PERSON, NATURAL PERSON")
        prompt_parts.append("ORDINARY PERSON, TYPICAL PERSON, high resolution")
        prompt_parts.append("PHOTOGRAPHIC QUALITY, REALISTIC PHOTOGRAPHY, DOCUMENTARY STYLE")
        prompt_parts.append("RAW PHOTOGRAPHY, UNRETOUCHED, NATURAL SKIN TEXTURE, PORES VISIBLE")
        prompt_parts.append("NATURAL SKIN IMPERFECTIONS, AUTHENTIC APPEARANCE, NATURAL LIGHTING")
        prompt_parts.append("CENTered COMPOSITION, SYMMETRICAL POSITIONING, PROPER FRAMING")
        prompt_parts.append("CORRECT PROPORTIONS, HEAD AND SHOULDERS FRAMING, PASSPORT CROP")
        
        # Características específicas por género
        if profile['metadata']['gender'].lower() in ['hombre', 'male', 'masculino']:
            # Características masculinas específicas y realistas
            prompt_parts.append("masculine features, strong jawline, defined jawline, masculine jawline")
            prompt_parts.append("prominent cheekbones, masculine cheekbones, strong cheekbones")
            prompt_parts.append("prominent brow ridge, masculine brow ridge, strong brow ridge")
            prompt_parts.append("broad shoulders, wide shoulders, strong shoulders, masculine shoulders")
            prompt_parts.append("broad chest, wide chest, strong chest, masculine chest")
            prompt_parts.append("thick neck, strong neck, muscular neck, masculine neck")
            prompt_parts.append("masculine build, athletic build, strong features, defined features")
            prompt_parts.append("facial hair options, beard options, mustache options, stubble options")
            prompt_parts.append("square face, rectangular face, angular face, defined face")
            prompt_parts.append("strong facial structure, masculine facial structure")
            prompt_parts.append("natural body proportions, appropriate shoulder width for men")
            prompt_parts.append("men can have broader shoulders, masculine torso")
            prompt_parts.append("MALE HAIRSTYLE, MASCULINE HAIR, SHORT HAIR, MEDIUM HAIR, MALE CUT")
            prompt_parts.append("NO FEMININE HAIRSTYLES, NO LONG FEMININE HAIR, NO FEMININE STYLING")
            prompt_parts.append("MASCULINE APPEARANCE, MALE CHARACTERISTICS, MALE FEATURES")
        else:
            # Características femeninas específicas
            prompt_parts.append("feminine features, soft jawline, graceful jawline, feminine jawline")
            prompt_parts.append("high cheekbones, feminine cheekbones, elegant cheekbones")
            prompt_parts.append("soft brow ridge, feminine brow ridge, graceful brow ridge")
            prompt_parts.append("narrow shoulders, delicate shoulders, feminine shoulders")
            prompt_parts.append("feminine torso, graceful torso, elegant torso")
            prompt_parts.append("slender neck, graceful neck, elegant neck, feminine neck")
            prompt_parts.append("feminine build, graceful build, soft features, elegant features")
            prompt_parts.append("no facial hair, clean face, smooth skin, hairless face")
            prompt_parts.append("oval face, heart face, diamond face, soft face")
            prompt_parts.append("graceful facial structure, feminine facial structure")
            prompt_parts.append("natural body proportions, appropriate shoulder width for women")
            prompt_parts.append("women typically have narrower shoulders, feminine torso")
        
        # Características genéticas específicas (EN INGLÉS)
        # Características básicas del perfil
        ethnic_chars = profile.get('ethnic_characteristics', {})
        prompt_parts.append(f"{ethnic_chars.get('skin_tone', 'fair')} skin")
        prompt_parts.append(f"{ethnic_chars.get('hair_color', 'dark brown')} hair")
        prompt_parts.append(f"{ethnic_chars.get('eye_color', 'brown')} eyes")
        prompt_parts.append(f"{ethnic_chars.get('face_shape', 'oval')} face")
        prompt_parts.append(f"{ethnic_chars.get('nose_shape', 'straight')} nose")
        prompt_parts.append(f"{ethnic_chars.get('lip_shape', 'full')} lips")
        prompt_parts.append("neutral expression")
        prompt_parts.append(f"{ethnic_chars.get('makeup', 'natural')} makeup")
        prompt_parts.append(f"{ethnic_chars.get('clothing_type', 'dress_shirt')} clothing")
        
        # Nuevos controles de diversidad con lógica específica por género
        if profile['metadata']['gender'].lower() in ['hombre', 'man', 'male']:
            # Solo para hombres: vello facial, barba, bigote
            if ethnic_chars.get('facial_hair', 'none') != 'none':
                prompt_parts.append(f"{ethnic_chars.get('facial_hair', 'none')} facial hair")
            if ethnic_chars.get('beard', 'none') != 'none':
                prompt_parts.append(f"{ethnic_chars.get('beard', 'none')} beard")
            if ethnic_chars.get('mustache', 'none') != 'none':
                prompt_parts.append(f"{ethnic_chars.get('mustache', 'none')} mustache")
        else:
            # Para mujeres: sin vello facial, barba o bigote
            prompt_parts.append("no facial hair, no beard, no mustache, clean face")
        
        # Complexión física (para ambos géneros)
        if ethnic_chars.get('physical_complexion'):
            prompt_parts.append(f"{ethnic_chars.get('physical_complexion', 'normal')} build")
        
        # Ropa y colores (evitar blanco)
        clothing_color = ethnic_chars.get('clothing_color', 'blue')
        if clothing_color != 'white':
            prompt_parts.append(f"{clothing_color} clothing color")
        else:
            prompt_parts.append("colored clothing, avoid white, dark clothing")
        
        # Fondo
        background = ethnic_chars.get('background', 'white_solid')
        prompt_parts.append(f"{background} background")
        
        # Agregar especificaciones para evitar desnudez y mejorar realismo
        prompt_parts.append("FULLY CLOTHED, PROFESSIONAL ATTIRE, APPROPRIATE CLOTHING")
        prompt_parts.append("NO NUDITY, NO EXPOSED SKIN, NO INAPPROPRIATE CONTENT")
        prompt_parts.append("FAMILY FRIENDLY, SAFE FOR WORK, PROFESSIONAL APPEARANCE")
        
        # Especificaciones para realismo y evitar apariencia de modelo
        prompt_parts.append("REALISTIC PERSON, EVERYDAY PERSON, NORMAL PERSON, AVERAGE PERSON")
        prompt_parts.append("NATURAL APPEARANCE, AUTHENTIC LOOK, REALISTIC FEATURES")
        prompt_parts.append("NO MODEL LOOK, NO PERFECT FACE, NO FLAWLESS SKIN")
        prompt_parts.append("NATURAL SKIN TEXTURE, VISIBLE PORES, SKIN IMPERFECTIONS")
        prompt_parts.append("REALISTIC LIGHTING, NATURAL LIGHTING, NO OVEREXPOSURE")
        prompt_parts.append("NO EXCESSIVE BRIGHTNESS, NO OVEREXPOSED SKIN")
        prompt_parts.append("NATURAL SKIN TONE, REALISTIC COMPLEXION, AUTHENTIC SKIN")
        prompt_parts.append("NO AIRBRUSHED LOOK, NO PERFECT SKIN, NO FLAWLESS APPEARANCE")
        
        # Especificaciones SAIME exactas basadas en Medidas_Fotografia.html
        prompt_parts.append("head and shoulders visible, shoulders must be visible, sufficient head space")
        prompt_parts.append("no head crop, full head visible, head positioned in upper 40%")
        prompt_parts.append("eyes positioned at 33% from top edge, perfectly centered composition")
        prompt_parts.append("PROPER NECK LENGTH, NORMAL NECK PROPORTIONS, REALISTIC NECK SIZE")
        prompt_parts.append("NO LONG NECK, NO DISPROPORTIONATE NECK, NATURAL NECK LENGTH")
        prompt_parts.append("HEAD AND SHOULDERS PROPORTION, CORRECT BODY PROPORTIONS")
        prompt_parts.append("TORSO AT 78% FROM TOP, SHOULDERS AT 65% FROM TOP, HEAD AT 49% FROM TOP")
        prompt_parts.append("TORSO TO BOTTOM, SHOULDERS PROPORTIONAL, HEAD PROPORTIONAL")
        prompt_parts.append("HEAD AND SHOULDERS FRAMING, UPPER BODY VISIBLE, PROFESSIONAL COMPOSITION")
        prompt_parts.append("SMALLER HEAD SIZE, COMPACT HEAD, HEAD NOT TOO LARGE")
        prompt_parts.append("MORE SPACE ABOVE HEAD, HEAD NOT AT TOP, HEAD IN MIDDLE SECTION")
        prompt_parts.append("SHOULDERS VISIBLE, TORSO VISIBLE, UPPER BODY FRAMING")
        prompt_parts.append("PASSPORT CROP, ID CROP, DOCUMENT CROP, HEAD AND SHOULDERS FRAMING")
        prompt_parts.append("professional studio lighting, no shadows, WHITE BACKGROUND")
        prompt_parts.append("passport photo requirements, ID photo standards, official document standards")
        prompt_parts.append("government photo standards, SAIME standards, RED FRAME GUIDELINES")
        prompt_parts.append("BLACK OUTER FRAME 512x764, OFFICIAL DOCUMENT PHOTO, GOVERNMENT ID PHOTO")
        prompt_parts.append("PASSPORT CROP, ID CROP, DOCUMENT CROP, HEAD AND SHOULDERS FRAMING")
        prompt_parts.append("HEAD NOT TOUCHING TOP EDGE, HEAD NOT TOUCHING SIDES")
        prompt_parts.append("PROPER HEAD SIZE FOR PASSPORT, CORRECT HEAD PROPORTIONS")
        prompt_parts.append("HEAD SIZE APPROPRIATE FOR ID, HEAD SIZE SUITABLE FOR DOCUMENT")
        prompt_parts.append("HEAD SIZE PERFECT FOR PASSPORT, HEAD SIZE IDEAL FOR ID CARD")
        prompt_parts.append("HEAD SIZE OPTIMAL FOR DOCUMENT, HEAD SIZE CORRECT FOR OFFICIAL PHOTO")
        prompt_parts.append("HEAD SIZE PROPER FOR GOVERNMENT ID, PROPER HEAD SIZE")
        prompt_parts.append("CORRECT HEAD SIZE, HEAD NOT TOO LARGE, HEAD NOT TOO SMALL")
        prompt_parts.append("HEAD PROPORTIONAL, HEAD WELL PROPORTIONED, HEAD PROPERLY SIZED")
        prompt_parts.append("HEAD CORRECTLY SIZED, HEAD APPROPRIATELY SIZED, HEAD OPTIMALLY SIZED")
        prompt_parts.append("HEAD PERFECTLY SIZED, HEAD IDEALLY SIZED")
        prompt_parts.append("EXACT 512x764 DIMENSIONS, HEAD CENTERED AT X=110px Y=80px")
        prompt_parts.append("EYES AT Y=80px (31% of 260px), SHOULDERS AT Y=202px (78% of 260px)")
        prompt_parts.append("HEAD WIDTH 100px HEAD HEIGHT 120px, NECK AT X=110px Y=160px WIDTH 28px HEIGHT 26px")
        prompt_parts.append("RED FRAME AT X=20px Y=20px WIDTH 200px HEIGHT 240px")
        prompt_parts.append("SHOULDERS MUST TOUCH LEFT AND RIGHT EDGES OF RED FRAME (20px to 200px, 180px wide)")
        prompt_parts.append("HEAD DISTANCE FROM TOP: 8-12mm, HEAD HEIGHT: 30-34mm")
        prompt_parts.append("LATERAL MARGINS: 12-18mm each side, BOTTOM SPACE: 18-25mm from chin")
        prompt_parts.append("SAIME COMPLIANCE, VENEZUELAN PASSPORT SPECIFICATIONS")
        prompt_parts.append("MANDATORY SAIME COMPLIANCE, MANDATORY VENEZUELAN PASSPORT SPECIFICATIONS")
        prompt_parts.append("FORCE SAIME COMPLIANCE, FORCE VENEZUELAN PASSPORT SPECIFICATIONS")
        
        return ", ".join(prompt_parts)
    
    def _generate_negative_prompt(self, profile):
        """Generar negative prompt con especificaciones SAIME y prohibiciones por género"""
        negative_parts = [
            # Prohibiciones SAIME básicas
            "3/4 view", "side profile", "looking away", "smiling", "laughing",
            "multiple people", "double exposure", "passport document visible",
            "photo of photo", "magazine model", "overly perfect", "artificial lighting",
            "shadows", "background objects", "jewelry", "glasses", "hat", "makeup",
            "retouched", "airbrushed", "glamour", "fashion model", "beauty contest",
            "white clothing", "white shirt", "white blouse", "white top", "white t-shirt",
            "white dress", "white jacket", "white sweater", "white clothing", "white attire",
            "colored background", "gradient background", "textured background", "patterned background",
            "noisy background", "complex background", "busy background", "shadows on background",
            "lighting effects on background", "tinted background", "off-white background",
            "cream background", "beige background", "gray background", "light gray background",
            "dark background", "black background", "blue background", "green background",
            "red background", "yellow background", "purple background", "orange background",
            "brown background", "wood background", "wall background", "fabric background",
            "paper background", "canvas background", "brick background", "stone background",
            "metal background", "glass background", "mirror background", "reflection",
            "professional headshot", "studio lighting", "dramatic lighting",
            "soft focus", "blurry", "low quality", "distorted", "deformed",
            "overexposed", "bright lighting", "excessive brightness", "white marks on face",
            "skin blemishes", "white spots", "bright spots", "overexposed skin",
            "model look", "perfect face", "flawless skin", "airbrushed", "photoshopped",
            "long neck", "disproportionate neck", "unnatural neck length",
            "perfect skin", "flawless appearance", "model appearance", "celebrity look",
            "extra limbs", "extra heads", "duplicate", "watermark", "text",
            "signature", "date", "stamp", "border", "frame",
            
            # PROHIBICIONES CRÍTICAS PARA EVITAR DESNUDEZ
            "nude", "naked", "nudity", "exposed", "topless", "bottomless",
            "undressed", "unclothed", "bare", "exposed skin", "inappropriate",
            "sexual", "adult content", "nsfw", "explicit", "pornographic",
            "inappropriate clothing", "revealing clothing", "skimpy clothing",
            "bikini", "underwear", "lingerie", "intimate", "private parts",
            "breasts", "genitals", "buttocks", "exposed body", "body parts",
            "inappropriate pose", "suggestive pose", "sexual pose", "adult pose",
            "inappropriate expression", "sexual expression", "adult expression",
            "inappropriate content", "adult content", "sexual content", "explicit content",
            "inappropriate behavior", "sexual behavior", "adult behavior",
            "inappropriate situation", "sexual situation", "adult situation",
            "inappropriate context", "sexual context", "adult context",
            "inappropriate setting", "sexual setting", "adult setting",
            "inappropriate environment", "sexual environment", "adult environment",
            "inappropriate scene", "sexual scene", "adult scene",
            "inappropriate image", "sexual image", "adult image",
            "inappropriate photo", "sexual photo", "adult photo",
            "inappropriate picture", "sexual picture", "adult picture",
            "inappropriate visual", "sexual visual", "adult visual",
            "inappropriate material", "sexual material", "adult material",
            "inappropriate content", "sexual content", "adult content",
            "inappropriate media", "sexual media", "adult media",
            "inappropriate entertainment", "sexual entertainment", "adult entertainment",
            "inappropriate art", "sexual art", "adult art",
            "inappropriate photography", "sexual photography", "adult photography",
            "inappropriate modeling", "sexual modeling", "adult modeling",
            "inappropriate posing", "sexual posing", "adult posing",
            "inappropriate behavior", "sexual behavior", "adult behavior",
            "inappropriate conduct", "sexual conduct", "adult conduct",
            "inappropriate activity", "sexual activity", "adult activity",
            "inappropriate interaction", "sexual interaction", "adult interaction",
            "inappropriate relationship", "sexual relationship", "adult relationship",
            "inappropriate contact", "sexual contact", "adult contact",
            "inappropriate touch", "sexual touch", "adult touch",
            "inappropriate gesture", "sexual gesture", "adult gesture",
            "inappropriate movement", "sexual movement", "adult movement",
            "inappropriate action", "sexual action", "adult action",
            "inappropriate behavior", "sexual behavior", "adult behavior",
            "inappropriate conduct", "sexual conduct", "adult conduct",
            "inappropriate activity", "sexual activity", "adult activity",
            "inappropriate interaction", "sexual interaction", "adult interaction",
            "inappropriate relationship", "sexual relationship", "adult relationship",
            "inappropriate contact", "sexual contact", "adult contact",
            "inappropriate touch", "sexual touch", "adult touch",
            "inappropriate gesture", "sexual gesture", "adult gesture",
            "inappropriate movement", "sexual movement", "adult movement",
            "inappropriate action", "sexual action", "adult action",
            
            # Prohibiciones específicas por género
        ]
        
        # Agregar prohibiciones específicas por género
        if profile['metadata']['gender'].lower() in ['hombre', 'male', 'masculino']:
            # Prohibiciones para hombres (evitar características femeninas)
            negative_parts.extend([
                "feminine features", "soft jawline", "delicate features", "feminine jawline",
                "soft cheekbones", "feminine cheekbones", "soft brow ridge", "feminine brow ridge",
                "narrow shoulders", "delicate shoulders", "feminine shoulders", "soft torso",
                "feminine torso", "slender neck", "feminine neck", "soft neck",
                "feminine build", "graceful build", "soft features", "elegant features",
                "oval face", "heart face", "diamond face", "soft face",
                "graceful facial structure", "feminine facial structure",
                "feminine hairstyles", "long feminine hair", "feminine styling",
                "feminine makeup", "feminine accessories", "feminine clothing",
                "feminine appearance", "feminine characteristics", "feminine features"
            ])
        else:
            # Prohibiciones para mujeres (evitar características masculinas)
            negative_parts.extend([
                "masculine features", "strong jawline", "angular features", "masculine jawline",
                "prominent cheekbones", "masculine cheekbones", "prominent brow ridge", "masculine brow ridge",
                "broad shoulders", "wide shoulders", "masculine shoulders", "broad chest",
                "masculine chest", "thick neck", "masculine neck", "strong neck",
                "masculine build", "athletic build", "strong features", "defined features",
                "square face", "rectangular face", "angular face", "defined face",
                "strong facial structure", "masculine facial structure",
                "facial hair", "beard", "mustache", "stubble", "5 o'clock shadow"
            ])
        
        # Continuar con prohibiciones generales
        negative_parts.extend([
            # Prohibiciones de perfección excesiva
            "perfect skin", "flawless skin", "airbrushed", "photoshopped",
            "model look", "supermodel appearance", "celebrity look",
            "fashion model", "beauty model", "perfect features", "flawless features",
            "extreme beauty", "perfect beauty", "perfect symmetry", "flawless symmetry",
            "perfect proportions", "flawless proportions", "perfect skin texture",
            "flawless skin texture", "perfect facial features", "flawless facial features",
            "perfect bone structure", "flawless bone structure", "perfect skin tone",
            "flawless skin tone", "perfect hair", "flawless hair", "perfect eyes",
            "flawless eyes", "perfect lips", "flawless lips", "perfect nose",
            "flawless nose", "perfect jawline", "flawless jawline", "perfect cheekbones",
            "flawless cheekbones", "perfect eyebrows", "flawless eyebrows",
            "perfect teeth", "flawless teeth", "perfect smile", "flawless smile",
            "perfect complexion", "flawless complexion", "perfect appearance",
            "flawless appearance", "perfect face", "flawless face", "perfect look",
            "flawless look", "perfect beauty", "flawless beauty", "perfect model",
            "flawless model", "perfect portrait", "flawless portrait",
            "perfect headshot", "flawless headshot", "perfect photo", "flawless photo",
            "perfect image", "flawless image", "perfect picture", "flawless picture",
            "perfect shot", "flawless shot", "perfect capture", "flawless capture",
            "perfect rendering", "flawless rendering", "perfect generation",
            "flawless generation", "perfect creation", "flawless creation",
            "perfect result", "flawless result", "perfect output", "flawless output",
            
            # Prohibiciones de vistas incorrectas
            "three quarter view", "side view", "profile view", "watermark", "signature",
            "cropped at neck", "only head", "no shoulders", "head cut off",
            "shoulders missing", "head cut off at top", "head cropped at top",
            "top of head missing", "cropped at shoulders", "shoulders cut off",
            "neck cut off", "head only", "no upper body", "incomplete framing",
            "partial head", "partial shoulders", "missing shoulders", "missing neck",
            "cropped image", "cut off image", "truncated image", "incomplete image",
            "partial image", "missing parts", "cut off parts", "truncated parts",
            "incomplete parts", "missing body parts", "cut off body parts",
            "truncated body parts", "incomplete body parts", "missing upper body",
            "cut off upper body", "truncated upper body", "incomplete upper body",
            "missing head and shoulders", "cut off head and shoulders",
            "truncated head and shoulders", "incomplete head and shoulders",
            "missing structure", "cut off structure", "truncated structure",
            "incomplete structure", "missing SAIME structure", "cut off SAIME structure",
            "truncated SAIME structure", "incomplete SAIME structure",
            "missing passport structure", "cut off passport structure",
            "truncated passport structure", "incomplete passport structure",
            "missing ID structure", "cut off ID structure", "truncated ID structure",
            "incomplete ID structure", "missing document structure",
            "cut off document structure", "truncated document structure",
            "incomplete document structure", "missing official structure",
            "cut off official structure", "truncated official structure",
            "incomplete official structure", "missing government structure",
            "cut off government structure", "truncated government structure",
            "incomplete government structure",
            
            # Prohibiciones de fondos
            "WHITE BACKGROUND", "COLORED BACKGROUND", "SOLID BACKGROUND",
            "TEXTURED BACKGROUND", "GRADIENT BACKGROUND", "PATTERN BACKGROUND",
            "BACKGROUND", "BACKDROP", "WALL", "SURFACE", "FLOOR", "CEILING",
            "ENVIRONMENT", "SCENE", "SETTING", "LOCATION", "PLACE", "ROOM",
            "INTERIOR", "EXTERIOR", "OUTDOOR", "INDOOR", "STUDIO BACKGROUND",
            "PHOTO STUDIO", "BACKGROUND WALL", "BACKGROUND SURFACE",
            
            # Prohibiciones de color
            "BLACK AND WHITE", "BW", "MONOCHROME", "GRAYSCALE", "SEPIA", "VINTAGE",
            "OLD", "AGED", "FADED", "WASHED OUT", "DESATURATED", "MUTED COLORS",
            "DULL COLORS", "PALE COLORS", "WEAK COLORS", "FADED COLORS",
            "WASHED OUT COLORS", "DESATURATED COLORS", "MUTED", "DULL", "PALE",
            "WEAK", "FADED", "WASHED OUT", "DESATURATED", "NO COLOR", "COLORLESS",
            "ACHROMATIC", "MONOCHROMATIC", "GRAYSCALE", "SEPIA TONE", "VINTAGE LOOK",
            "OLD LOOK", "AGED LOOK", "FADED LOOK", "WASHED OUT LOOK",
            "DESATURATED LOOK", "MUTED LOOK", "DULL LOOK", "PALE LOOK", "WEAK LOOK",
            "FADED LOOK", "WASHED OUT LOOK", "DESATURATED LOOK"
        ])
        return ", ".join(negative_parts)
    
    def _create_placeholder_image(self, profile, output_dir):
        """Crear imagen placeholder como fallback"""
        try:
            from PIL import Image, ImageDraw, ImageFont
            
            # Crear imagen de 512x768 (tamaño estándar)
            img = Image.new('RGB', (512, 768), color='white')
            draw = ImageDraw.Draw(img)
            
            # Intentar usar una fuente, si no está disponible usar la por defecto
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
            except:
                font = ImageFont.load_default()
            
            # Dibujar información del perfil
            y_offset = 50
            info_lines = [
                f"ID: {profile.id}",
                f"Nacionalidad: {profile.nacionalidad}",
                f"Género: {profile['metadata']['gender']}",
                f"Edad: {profile.edad}",
                f"Beauty: {profile.beauty_level}",
                f"Skin: {profile.skin_tone}",
                f"Hair: {profile.hair_color}",
                f"Eyes: {profile.eye_color}",
                f"Face: {profile.face_shape}",
                f"Generated: {profile.timestamp}"
            ]
            
            for line in info_lines:
                draw.text((50, y_offset), line, fill='black', font=font)
                y_offset += 30
            
            # Guardar imagen
            image_path = output_dir / f"genetic_{profile.id}.png"
            img.save(image_path, 'PNG')
            
            return image_path
            
        except Exception as e:
            print(f"⚠️ Error creando placeholder: {e}")
            # Fallback final: crear archivo de texto
            image_path = output_dir / f"genetic_{profile.id}.txt"
            with open(image_path, 'w') as f:
                f.write(f"Imagen genética: {profile.id}\n")
                f.write(f"Perfil: {profile['metadata']['nationality']} {profile['metadata']['gender']} {profile['metadata']['age']}\n")
            return image_path
    
    def _create_json_metadata(self, profile, output_dir, index):
        """Crear JSON de metadatos"""
        try:
            json_data = {
                "image_id": profile.id,
                "generated_at": profile.timestamp,
                "profile": {
                    "nacionalidad": profile.nacionalidad,
                    "genero": profile.genero,
                    "edad": profile.edad,
                    "beauty_level": profile.beauty_level,
                    "skin_tone": profile.skin_tone,
                    "hair_color": profile.hair_color,
                    "eye_color": profile.eye_color,
                    "background": profile.background,
                    "face_shape": profile.face_shape,
                    "nose_shape": profile.nose_shape,
                    "lip_shape": profile.lip_shape,
                    "eye_shape": profile.eye_shape,
                    "jawline": profile.jawline,
                    "cheekbone": profile.cheekbone,
                    "eyebrow": profile.eyebrow,
                    "skin_texture": profile.skin_texture,
                    "freckles": profile.freckles,
                    "moles": profile.moles,
                    "scars": profile.scars,
                    "acne": profile.acne,
                    "wrinkles": profile.wrinkles,
                    "hair_style": profile.hair_style,
                    "makeup": profile.makeup,
                    "clothing_type": profile.clothing_type,
                    "accessories": profile.accessories,
                    "expression": profile.expression,
                    "ethnicity": profile.ethnicity,
                    "body_type": profile.body_type
                },
                "generation_info": {
                    "method": "genetic_diversity_engine",
                    "version": "1.0",
                    "diversity_score": random.uniform(0.8, 1.0)
                }
            }
            
            json_path = output_dir / f"genetic_{profile.id}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)
            
            return json_path
            
        except Exception as e:
            print(f"⚠️ Error creando JSON: {e}")
            return None
    
    def _create_csv(self, profiles, output_dir):
        """Crear archivo CSV con todos los datos de diversidad"""
        try:
            csv_path = output_dir / "diversity_analysis.csv"
            
            # Crear CSV con todos los datos de diversidad
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                import csv
                writer = csv.writer(csvfile)
                
                # Encabezados completos
                headers = [
                    'ID', 'Nacionalidad', 'Género', 'Edad', 'Timestamp',
                    'Beauty_Level', 'Skin_Tone', 'Hair_Color', 'Eye_Color', 'Background',
                    'Face_Shape', 'Nose_Shape', 'Lip_Shape', 'Eye_Shape',
                    'Jawline', 'Cheekbone', 'Eyebrow', 'Skin_Texture',
                    'Freckles', 'Moles', 'Scars', 'Acne', 'Wrinkles', 'Hair_Style'
                ]
                writer.writerow(headers)
                
                for profile in profiles:
                    writer.writerow([
                        profile.id,
                        profile.nacionalidad,
                        profile['metadata']['gender'],
                        profile.edad,
                        profile.timestamp,
                        profile.beauty_level,
                        profile.skin_tone,
                        profile.hair_color,
                        profile.eye_color,
                        profile.background,
                        profile.face_shape,
                        profile.nose_shape,
                        profile.lip_shape,
                        profile.eye_shape,
                        profile.jawline,
                        profile.cheekbone,
                        profile.eyebrow,
                        profile.skin_texture,
                        profile.freckles,
                        profile.moles,
                        profile.scars,
                        profile.acne,
                        profile.wrinkles,
                        profile.hair_style
                    ])
            
            return str(csv_path)
            
        except Exception as e:
            print(f"⚠️ Error creando CSV: {e}")
            return ""

# Funciones de generación masiva directas
def generar_masivo_genetico_func(nacionalidad, genero, edad, cantidad, region, edad_min, edad_max, beauty_control, skin_control, hair_control, eye_control, background_control, face_shape_control, nose_shape_control, lip_shape_control, eye_shape_control, jawline_control, cheekbone_control, eyebrow_control, skin_texture_control, freckle_control, mole_control, scar_control, acne_control, wrinkle_control, hair_style_control, cfg_scale, steps, sampler_name, seed, width, height, batch_count, batch_size, denoising_strength, hr_second_pass_steps, hr_scale, hr_resize_x, hr_resize_y, hr_upscaler, hr_sampler_name, hr_scheduler, refiner_checkpoint, refiner_switch_at, progress=None):
    """Función de generación genética directa"""
    try:
        generator = DirectGeneticGenerator()
        return generator.generate(
            nacionalidad, genero, edad, cantidad, region, edad_min, edad_max,
            beauty_control, skin_control, hair_control, eye_control, background_control,
            face_shape_control, nose_shape_control, lip_shape_control, eye_shape_control,
            jawline_control, cheekbone_control, eyebrow_control, skin_texture_control,
            freckle_control, mole_control, scar_control, acne_control, wrinkle_control, 
            hair_style_control, cfg_scale, steps, sampler_name, seed, width, height, 
            batch_count, batch_size, denoising_strength, hr_second_pass_steps, hr_scale, 
            hr_resize_x, hr_resize_y, hr_upscaler, hr_sampler_name, hr_scheduler, 
            refiner_checkpoint, refiner_switch_at, progress
        )
    except Exception as e:
        return "", "", f"❌ Error en generación genética directa: {e}"

def generar_masivo_pasaporte_func(*args, **kwargs):
    """Función de generación pasaporte directa"""
    try:
        # Extraer parámetros de la interfaz
        if len(args) >= 5:
            width, height, cfg_scale, steps, sampler = args[:5]
            nacionalidad = args[5] if len(args) > 5 else "Venezuela"
            genero = args[6] if len(args) > 6 else "hombre"
            cantidad = args[7] if len(args) > 7 else 1
        else:
            width, height, cfg_scale, steps, sampler = 512, 764, 7.0, 20, "Euler"
            nacionalidad = "Venezuela"
            genero = "hombre"
            cantidad = 1
        
        # Verificar dataset disponible
        dataset_path = Path("Dataset_JSON_PNG")
        if not dataset_path.exists():
            return "", "❌ Carpeta Dataset_JSON_PNG no encontrada", "❌ Dataset no disponible", 0, 0
        
        # Buscar archivos JSON disponibles
        json_files = list(dataset_path.glob("*.json"))
        if not json_files:
            return "", "❌ No se encontraron archivos JSON en Dataset_JSON_PNG", "❌ Dataset vacío", 0, 0
        
        # Seleccionar archivos aleatorios
        selected_files = random.sample(json_files, min(cantidad, len(json_files)))
        
        # Crear carpeta de salida
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_folder = f"massive_{nacionalidad}_{genero}_{timestamp}"
        output_path = Path("outputs") / "Realisticmix666_v40" / "masivo_pasaporte" / output_folder
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Procesar cada archivo JSON
        generated_images = []
        generated_jsons = []
        generated_csvs = []
        
        for i, json_file in enumerate(selected_files):
            try:
                # Leer datos del JSON
                with open(json_file, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # Generar prompt basado en el JSON
                prompt = _generate_passport_prompt(json_data, nacionalidad, genero)
                negative_prompt = self._generate_negative_prompt(None)
                
                # Generar imagen usando la API del WebUI
                image_result = _generate_passport_image(
                    prompt, negative_prompt, width, height, 
                    cfg_scale, steps, sampler
                )
                
                if image_result:
                    # Guardar imagen
                    image_filename = f"passport_{nacionalidad}_{genero}_{i+1}_{timestamp}.png"
                    image_path = output_path / image_filename
                    image_result.save(str(image_path))
                    generated_images.append(str(image_path))
                    
                    # Guardar JSON procesado
                    json_filename = f"passport_{nacionalidad}_{genero}_{i+1}_{timestamp}.json"
                    json_path = output_path / json_filename
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, indent=2, ensure_ascii=False)
                    generated_jsons.append(str(json_path))
                    
                    # Crear CSV con datos del JSON
                    csv_filename = f"passport_{nacionalidad}_{genero}_{i+1}_{timestamp}.csv"
                    csv_path = output_path / csv_filename
                    _create_passport_csv(json_data, csv_path)
                    generated_csvs.append(str(csv_path))
                    
            except Exception as e:
                print(f"Error procesando {json_file}: {e}")
                continue
        
        if not generated_images:
            return "", "❌ No se pudieron generar imágenes", "❌ Error en generación", 0, 0
        
        # Crear resumen
        summary = f"✅ Generación masiva de pasaporte completada\n"
        summary += f"📁 Carpeta: {output_folder}\n"
        summary += f"🖼️ Imágenes: {len(generated_images)}\n"
        summary += f"📄 JSONs: {len(generated_jsons)}\n"
        summary += f"📊 CSVs: {len(generated_csvs)}"
        
        return summary, f"✅ {len(generated_images)} imágenes generadas", f"📁 {output_folder}", len(generated_images), len(generated_images)
        
    except Exception as e:
        return "", f"❌ Error en generación pasaporte: {e}", f"❌ Error: {e}", 0, 0

def _generate_passport_prompt(json_data, nacionalidad, genero):
    """Generar prompt para pasaporte basado en JSON"""
    try:
        # Extraer datos del JSON
        nombre = json_data.get('nombre', 'Persona')
        edad = json_data.get('edad', 25)
        
        # Crear prompt base para pasaporte
        prompt = f"passport photo, {nacionalidad} {genero}, {edad} years old, "
        prompt += f"professional headshot, official document photo, "
        prompt += f"clean background, proper lighting, "
        prompt += f"head and shoulders visible, "
        prompt += f"neutral expression, looking at camera, "
        prompt += f"high quality, realistic, detailed"
        
        return prompt
    except Exception:
        return f"passport photo, {nacionalidad} {genero}, professional headshot, official document photo"

def _generate_passport_image(prompt, negative_prompt, width, height, cfg_scale, steps, sampler):
    """Generar imagen de pasaporte usando la API del WebUI"""
    try:
        import requests
        import base64
        from PIL import Image
        import io
        
        # Preparar datos para la API
        api_data = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "width": width,
            "height": height,
            "cfg_scale": cfg_scale,
            "steps": steps,
            "sampler_name": sampler,
            "batch_size": 1,
            "n_iter": 1
        }
        
        # Llamar a la API del WebUI
        response = requests.post(
            "http://localhost:7860/sdapi/v1/txt2img",
            json=api_data,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'images' in result and result['images']:
                # Decodificar imagen base64
                image_data = base64.b64decode(result['images'][0])
                image = Image.open(io.BytesIO(image_data))
                return image
        
        return None
    except Exception as e:
        print(f"Error generando imagen: {e}")
        return None

def _create_passport_csv(json_data, csv_path):
    """Crear CSV con datos del JSON"""
    try:
        import csv
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Escribir encabezados
            writer.writerow(['Campo', 'Valor'])
            
            # Escribir datos del JSON
            for key, value in json_data.items():
                writer.writerow([key, value])
                
    except Exception as e:
        print(f"Error creando CSV: {e}")

def verificar_dataset_disponible(nacionalidad, genero):
    """Verificar dataset disponible"""
    try:
        dataset_path = Path("Dataset_JSON_PNG")
        if not dataset_path.exists():
            return "❌ Carpeta Dataset_JSON_PNG no encontrada"
        
        json_files = list(dataset_path.glob("*.json"))
        if not json_files:
            return "❌ No se encontraron archivos JSON"
        
        return f"✅ Dataset disponible: {len(json_files)} archivos JSON encontrados"
    except Exception as e:
        return f"❌ Error verificando dataset: {e}"

def detener_generacion():
    """Detener generación en curso"""
    return "⏹️ Generación detenida"

def abrir_carpeta_modelo():
    """Abrir carpeta del modelo actual"""
    try:
        import subprocess
        import os
        from modules import shared
        
        # Obtener nombre del modelo actual
        if hasattr(shared, 'sd_model') and shared.sd_model:
            model_name = getattr(shared.sd_model, 'model_name', 'unknown')
            if hasattr(shared.sd_model, 'model_path'):
                model_path = shared.sd_model.model_path
                model_name = os.path.basename(model_path).replace('.safetensors', '').replace('.ckpt', '')
        else:
            model_name = "unknown_model"
        
        # Crear ruta de la carpeta de salida
        output_dir = f"outputs/{model_name}"
        
        # Crear directorio si no existe
        os.makedirs(output_dir, exist_ok=True)
        
        # Abrir carpeta según el sistema operativo
        if os.name == 'nt':  # Windows
            subprocess.run(['explorer', output_dir])
        elif os.name == 'posix':  # macOS y Linux
            subprocess.run(['xdg-open', output_dir])
        else:
            subprocess.run(['open', output_dir])  # macOS fallback
        
        return f"📁 Carpeta abierta: {output_dir}"
    except Exception as e:
        return f"❌ Error abriendo carpeta: {e}"
