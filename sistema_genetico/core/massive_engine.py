#!/usr/bin/env python3
"""
Motor de Generación Masiva con Diversidad Genética
Procesa dataset JSON/PNG existente y genera nuevas variaciones con diversidad genética
"""

import json
import random
import time
import logging
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

# Importar módulos del sistema genético
from diversity_engine import UltraDiversityEngine
from api_client import WebUIAPIClient
from file_manager import FileManager

# Configurar logger
logger = logging.getLogger(__name__)

class MassiveGenerationEngine:
    """Motor de generación masiva con diversidad genética"""
    
    def __init__(self):
        self.diversity_engine = UltraDiversityEngine()
        self.api_client = WebUIAPIClient()
        self.file_manager = FileManager()
        self.logger = logger
        
    def load_dataset(self, dataset_path: str) -> List[Dict[str, Any]]:
        """
        Cargar dataset de JSON/PNG existente
        
        Args:
            dataset_path: Ruta al directorio del dataset
            
        Returns:
            Lista de entradas del dataset con metadatos
        """
        try:
            dataset_dir = Path(dataset_path)
            if not dataset_dir.exists():
                raise FileNotFoundError(f"Dataset no encontrado: {dataset_path}")
            
            dataset_entries = []
            
            # Buscar archivos JSON
            json_files = list(dataset_dir.glob("*.json"))
            self.logger.info(f"Encontrados {len(json_files)} archivos JSON en el dataset")
            
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Buscar imagen PNG correspondiente
                    png_file = json_file.with_suffix('.png')
                    if png_file.exists():
                        dataset_entries.append({
                            'json_file': str(json_file),
                            'png_file': str(png_file),
                            'metadata': data,
                            'image_id': data.get('image_id', 'unknown'),
                            'nationality': data.get('metadata', {}).get('nationality', 'venezuelan'),
                            'gender': data.get('metadata', {}).get('gender', 'hombre'),
                            'age': data.get('metadata', {}).get('age', 25)
                        })
                    else:
                        self.logger.warning(f"Imagen PNG no encontrada para {json_file}")
                        
                except Exception as e:
                    self.logger.error(f"Error cargando {json_file}: {e}")
                    continue
            
            self.logger.info(f"Dataset cargado: {len(dataset_entries)} entradas válidas")
            return dataset_entries
            
        except Exception as e:
            self.logger.error(f"Error cargando dataset: {e}")
            raise
    
    def apply_genetic_diversity(self, base_metadata: Dict[str, Any], 
                               diversity_controls: Dict[str, str]) -> Dict[str, Any]:
        """
        Aplicar diversidad genética a metadatos base
        
        Args:
            base_metadata: Metadatos originales del dataset
            diversity_controls: Controles de diversidad genética
            
        Returns:
            Metadatos modificados con diversidad genética
        """
        try:
            # Extraer información base
            nationality = base_metadata.get('metadata', {}).get('nationality', 'venezuelan')
            gender = base_metadata.get('metadata', {}).get('gender', 'hombre')
            base_age = base_metadata.get('metadata', {}).get('age', 25)
            
            # Generar nueva edad con variación
            age_variation = random.randint(-5, 5)
            new_age = max(18, min(80, base_age + age_variation))
            
            # Crear perfil genético diverso
            genetic_profile = {
                'nationality': nationality,
                'gender': gender,
                'age': new_age,
                'diversity_applied': True,
                'original_age': base_age,
                'genetic_timestamp': datetime.now().isoformat()
            }
            
            # Aplicar controles de diversidad si están disponibles
            if 'ethnic_characteristics' in base_metadata:
                ethnic = base_metadata['ethnic_characteristics'].copy()
                
                # Modificar características según controles de diversidad
                if diversity_controls.get('skin_control') != 'aleatorio':
                    ethnic['skin_tone'] = self._apply_skin_diversity(
                        ethnic.get('skin_tone', 'fair'), 
                        diversity_controls['skin_control']
                    )
                
                if diversity_controls.get('hair_control') != 'aleatorio':
                    ethnic['hair_color'] = self._apply_hair_diversity(
                        ethnic.get('hair_color', 'dark brown'),
                        diversity_controls['hair_control']
                    )
                
                if diversity_controls.get('hair_style_control') != 'aleatorio':
                    ethnic['hair_style'] = self._apply_hair_style_diversity(
                        ethnic.get('hair_style', 'messy'),
                        diversity_controls['hair_style_control']
                    )
                
                genetic_profile['ethnic_characteristics'] = ethnic
            
            return genetic_profile
            
        except Exception as e:
            self.logger.error(f"Error aplicando diversidad genética: {e}")
            return base_metadata
    
    def _apply_skin_diversity(self, original_skin: str, control: str) -> str:
        """Aplicar diversidad al tono de piel"""
        skin_variations = {
            'muy_claro': ['very fair', 'pale', 'light'],
            'claro': ['fair', 'light', 'medium-light'],
            'medio': ['medium', 'olive', 'tan'],
            'oscuro': ['dark', 'brown', 'deep'],
            'muy_oscuro': ['very dark', 'deep brown', 'ebony']
        }
        return random.choice(skin_variations.get(control, [original_skin]))
    
    def _apply_hair_diversity(self, original_hair: str, control: str) -> str:
        """Aplicar diversidad al color de cabello"""
        hair_variations = {
            'negro': ['black', 'dark black', 'jet black'],
            'castano': ['brown', 'dark brown', 'chestnut'],
            'rubio': ['blonde', 'golden blonde', 'light blonde'],
            'pelirrojo': ['red', 'auburn', 'ginger'],
            'gris': ['gray', 'silver', 'salt and pepper']
        }
        return random.choice(hair_variations.get(control, [original_hair]))
    
    def _apply_hair_style_diversity(self, original_style: str, control: str) -> str:
        """Aplicar diversidad al estilo de cabello"""
        style_variations = {
            'corto': ['short', 'buzz cut', 'pixie'],
            'medio': ['medium length', 'shoulder length'],
            'largo': ['long', 'long hair', 'flowing'],
            'rizado': ['curly', 'wavy', 'curled'],
            'liso': ['straight', 'sleek', 'smooth']
        }
        return random.choice(style_variations.get(control, [original_style]))
    
    def generate_massive_batch(self, dataset_path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generar lote masivo con diversidad genética
        
        Args:
            dataset_path: Ruta al dataset JSON/PNG
            params: Parámetros de generación
            
        Returns:
            Resultado de la generación masiva
        """
        try:
            # Cargar dataset
            dataset_entries = self.load_dataset(dataset_path)
            if not dataset_entries:
                return {'success': False, 'error': 'Dataset vacío o no encontrado'}
            
            # Parámetros de generación
            cantidad = params.get('cantidad', 10)
            model = params.get('model', 'unknown_model')
            
            # Controles de diversidad
            diversity_controls = {
                'skin_control': params.get('skin_control', 'aleatorio'),
                'hair_control': params.get('hair_control', 'aleatorio'),
                'hair_style_control': params.get('hair_style_control', 'aleatorio'),
                'beauty_control': params.get('beauty_control', 'aleatorio')
            }
            
            # Crear estructura de salida
            output_dir = self.file_manager.create_output_structure(
                model_name=model,
                generation_type="masivo_premium",
                nacionalidad="Venezuela",
                genero="mixto"
            )
            
            generated_images = []
            
            # Procesar entradas del dataset
            for i in range(min(cantidad, len(dataset_entries))):
                try:
                    entry = dataset_entries[i]
                    
                    # Aplicar diversidad genética
                    genetic_profile = self.apply_genetic_diversity(
                        entry['metadata'], 
                        diversity_controls
                    )
                    
                    # Crear prompt genético
                    prompt = self._create_genetic_prompt(genetic_profile, entry['metadata'])
                    negative_prompt = self._create_negative_prompt()
                    
                    # Generar imagen
                    image_params = {
                        'width': params.get('width', 512),
                        'height': params.get('height', 764),
                        'cfg_scale': params.get('cfg_scale', 7.5),
                        'steps': params.get('steps', 20),
                        'seed': params.get('seed', -1)
                    }
                    
                    image_result = self.api_client.generate_image(
                        prompt=prompt,
                        negative_prompt=negative_prompt,
                        params=image_params
                    )
                    
                    if image_result:
                        # Guardar imagen
                        filename = f"massive_{i+1:03d}"
                        save_result = self.file_manager.save_image(
                            image_data=image_result,
                            output_dir=output_dir,
                            filename=filename,
                            metadata={
                                'genetic_profile': genetic_profile,
                                'original_entry': entry,
                                'generation_params': params,
                                'timestamp': time.time()
                            }
                        )
                        
                        if save_result['success']:
                            generated_images.append({
                                'genetic_profile': genetic_profile,
                                'image_path': save_result['file_path'],
                                'original_id': entry['image_id']
                            })
                    
                except Exception as e:
                    self.logger.error(f"Error procesando entrada {i+1}: {e}")
                    continue
            
            return {
                'success': True,
                'generated_count': len(generated_images),
                'images': generated_images,
                'dataset_entries_processed': len(dataset_entries)
            }
            
        except Exception as e:
            self.logger.error(f"Error en generación masiva: {e}")
            return {'success': False, 'error': str(e)}
    
    def _create_genetic_prompt(self, genetic_profile: Dict[str, Any], 
                              original_metadata: Dict[str, Any]) -> str:
        """Crear prompt genético basado en el perfil"""
        nationality = genetic_profile.get('nationality', 'venezuelan')
        gender = genetic_profile.get('gender', 'hombre')
        age = genetic_profile.get('age', 25)
        
        # Características étnicas
        ethnic = genetic_profile.get('ethnic_characteristics', {})
        skin_tone = ethnic.get('skin_tone', 'fair')
        hair_color = ethnic.get('hair_color', 'dark brown')
        hair_style = ethnic.get('hair_style', 'messy')
        
        prompt = f"venezuelan passport photo, {gender} from {nationality}, {age} years old, {skin_tone} skin, {hair_color} hair, {hair_style} hair style, professional headshot, official document photo, clean white background, proper lighting, head and shoulders visible, neutral expression, looking at camera, high quality, realistic"
        
        return prompt
    
    def _create_negative_prompt(self) -> str:
        """Crear negative prompt estándar"""
        return "blurry, low quality, distorted, deformed, ugly, bad anatomy, bad proportions, extra limbs, missing limbs, multiple people, smiling, laughing, 3/4 view, side profile, looking away, white clothing, colored background, shadows, jewelry, glasses, hat, makeup"
