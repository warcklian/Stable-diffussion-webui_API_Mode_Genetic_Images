#!/usr/bin/env python3
"""
Cliente API para conectar con WebUI en modo headless
"""

import requests
import json
import time
import base64
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

class WebUIAPIClient:
    """Cliente para conectar con WebUI vía API"""
    
    def __init__(self, base_url="http://localhost:7860"):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        
    def wait_for_webui(self, timeout=300):
        """Esperar que WebUI esté disponible"""
        print("🔍 Esperando que WebUI esté disponible...")
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = self.session.get(f"{self.base_url}/sdapi/v1/options", timeout=5)
                if response.status_code == 200:
                    print("✅ WebUI disponible")
                    return True
            except:
                pass
            
            print("⏳ Esperando WebUI...")
            time.sleep(5)
        
        print("❌ WebUI no disponible después del timeout")
        return False
    
    def generate_image(self, prompt, negative_prompt, params):
        """Generar imagen vía API"""
        try:
            # Preparar datos para la API
            api_data = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "width": params.get("width", 512),
                "height": params.get("height", 764),
                "cfg_scale": params.get("cfg_scale", 7.0),
                "steps": params.get("steps", 20),
                "sampler_name": params.get("sampler_name", "DPM++ 2M"),
                "batch_size": params.get("batch_size", 1),
                "n_iter": params.get("n_iter", 1),
                "seed": params.get("seed", -1)
            }
            
            # Llamar a la API
            response = self.session.post(
                f"{self.base_url}/sdapi/v1/txt2img",
                json=api_data,
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'images' in result and result['images']:
                    # Decodificar imagen base64
                    image_data = base64.b64decode(result['images'][0])
                    return image_data
                else:
                    self.logger.error("No se generó ninguna imagen")
                    return None
            else:
                self.logger.error(f"Error API: {response.status_code}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error generando imagen: {e}")
            return None
    
    def get_models(self):
        """Obtener modelos disponibles"""
        try:
            response = self.session.get(f"{self.base_url}/sdapi/v1/sd-models")
            if response.status_code == 200:
                return response.json()
            return []
        except:
            return []
    
    def get_options(self):
        """Obtener opciones del WebUI"""
        try:
            response = self.session.get(f"{self.base_url}/sdapi/v1/options")
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}
    
    def set_model(self, model_name):
        """Cambiar modelo activo"""
        try:
            options = {"sd_model_checkpoint": model_name}
            response = self.session.post(
                f"{self.base_url}/sdapi/v1/options",
                json=options
            )
            return response.status_code == 200
        except:
            return False
    
    def get_current_model(self):
        """Obtener modelo activo actual"""
        try:
            response = self.session.get(f"{self.base_url}/sdapi/v1/options")
            if response.status_code == 200:
                options = response.json()
                model_name = options.get('sd_model_checkpoint', 'unknown_model')
                # Limpiar nombre del modelo para usar como nombre de carpeta
                model_name_clean = "".join(c for c in model_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
                return model_name_clean
            else:
                return "unknown_model"
        except Exception as e:
            print(f"⚠️ Error obteniendo modelo activo: {e}")
            return "unknown_model"

class GeneticAPIGenerator:
    """Generador genético usando API"""
    
    def __init__(self, api_client):
        self.api_client = api_client
        self.diversity_engine = None
        self.saime_validator = None
        
        # Cargar módulos del sistema genético
        self._load_genetic_modules()
    
    def _load_genetic_modules(self):
        """Cargar módulos del sistema genético"""
        try:
            # Importar motor de diversidad
            from .diversity_engine import UltraDiversityEngine
            from .saime_validator import SAIMEValidator
            
            self.diversity_engine = UltraDiversityEngine()
            self.saime_validator = SAIMEValidator()
            
            print("✅ Módulos genéticos cargados")
            
        except Exception as e:
            print(f"⚠️ Error cargando módulos genéticos: {e}")
    
    def generate_genetic_batch(self, params):
        """Generar lote genético completo"""
        try:
            print(f"🧬 Generando lote genético: {params['cantidad']} imágenes")
            
            # Crear directorio de salida
            output_dir = Path("sistema_genetico/outputs/genetic_images")
            output_dir.mkdir(parents=True, exist_ok=True)
            
            generated_images = []
            generated_jsons = []
            
            for i in range(params['cantidad']):
                print(f"📸 Generando imagen {i+1}/{params['cantidad']}")
                
                # Generar perfil genético
                if self.diversity_engine:
                    profile = self.diversity_engine.generate_profile(
                        params['nacionalidad'],
                        params['genero'], 
                        params['edad'],
                        params
                    )
                else:
                    # Fallback básico
                    profile = self._create_basic_profile(params, i)
                
                # Generar prompts
                prompt = self._generate_genetic_prompt(profile)
                negative_prompt = self._generate_negative_prompt()
                
                # Generar imagen vía API
                image_data = self.api_client.generate_image(
                    prompt, negative_prompt, params
                )
                
                if image_data:
                    # Guardar imagen
                    image_path = output_dir / f"genetic_{profile['id']}.png"
                    with open(image_path, 'wb') as f:
                        f.write(image_data)
                    generated_images.append(str(image_path))
                    
                    # Guardar JSON
                    json_path = output_dir / f"genetic_{profile['id']}.json"
                    with open(json_path, 'w') as f:
                        json.dump(profile, f, indent=2)
                    generated_jsons.append(str(json_path))
                    
                    print(f"✅ Imagen {i+1} generada: {image_path.name}")
                else:
                    print(f"❌ Error generando imagen {i+1}")
            
            return {
                'success': True,
                'images': generated_images,
                'jsons': generated_jsons,
                'count': len(generated_images)
            }
            
        except Exception as e:
            print(f"❌ Error en generación genética: {e}")
            return {'success': False, 'error': str(e)}
    
    def _create_basic_profile(self, params, index):
        """Crear perfil básico como fallback"""
        return {
            'id': f"genetic_{params['nacionalidad']}_{params['genero']}_{index+1}",
            'nacionalidad': params['nacionalidad'],
            'genero': params['genero'],
            'edad': params['edad'],
            'timestamp': time.strftime("%Y%m%d_%H%M%S")
        }
    
    def _generate_genetic_prompt(self, profile):
        """Generar prompt genético"""
        prompt_parts = [
            f"venezuelan passport photo, {profile['genero']} from venezuela",
            f"{profile['edad']} years old",
            "professional headshot, official document photo",
            "clean white background, proper lighting",
            "head and shoulders visible, neutral expression",
            "looking at camera, high quality, realistic"
        ]
        return ", ".join(prompt_parts)
    
    def _generate_negative_prompt(self):
        """Generar negative prompt"""
        return "blurry, low quality, distorted, deformed, ugly, bad anatomy, bad proportions, extra limbs, missing limbs, multiple people, smiling, laughing, 3/4 view, side profile, looking away, white clothing, colored background, shadows, jewelry, glasses, hat, makeup"

if __name__ == "__main__":
    # Ejemplo de uso
    client = WebUIAPIClient()
    if client.wait_for_webui():
        generator = GeneticAPIGenerator(client)
        
        params = {
            'nacionalidad': 'Venezuela',
            'genero': 'hombre',
            'edad': 30,
            'cantidad': 5,
            'width': 512,
            'height': 764,
            'cfg_scale': 7.0,
            'steps': 20,
            'sampler_name': 'DPM++ 2M'
        }
        
        result = generator.generate_genetic_batch(params)
        print(f"Resultado: {result}")
