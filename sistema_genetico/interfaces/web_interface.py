#!/usr/bin/env python3
"""
Interfaz Web Flask para Sistema de Generación Masiva Genética
Interfaz atractiva y funcional con prioridad en funcionalidad
"""

from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import json
import time
import os

# Función para traducir opciones de español a inglés
def translate_to_english(spanish_value):
    """Traduce valores en español a inglés para el JSON"""
    # Manejar valores None o vacíos
    if spanish_value is None or spanish_value == '' or spanish_value == 'aleatorio':
        return 'random'
    
    translations = {
        # Beauty levels
        'aleatorio': 'random',
        'muy_bella': 'stunning',
        'bella': 'beautiful',
        'atractiva': 'attractive',
        'normal': 'average',
        'poco_atractiva': 'unattractive',
        
        # Skin tones
        'muy_clara': 'porcelain',
        'clara': 'fair',
        'media': 'medium',
        'morena': 'dark',
        'muy_morena': 'very_dark',
        
        # Hair colors
        'negro': 'black',
        'marrón_oscuro': 'dark_brown',
        'marrón': 'brown',
        'castaño': 'light_brown',
        'rubio': 'blonde',
        'rojo': 'red',
        'gris': 'gray',
        'blanco': 'white',
        
        # Hair lengths
        'calvo': 'bald',
        'muy_corto': 'very_short',
        'corto': 'short',
        'medio': 'medium',
        'largo': 'long',
        'muy_largo': 'very_long',
        
        # Eye colors
        'marrón': 'brown',
        'marrón_claro': 'light_brown',
        'verde': 'green',
        'azul': 'blue',
        'azul_claro': 'light_blue',
        'gris': 'gray',
        'avellana': 'hazel',
        
        # Face shapes
        'ovalada': 'oval',
        'redonda': 'round',
        'cuadrada': 'square',
        'corazón': 'heart',
        'diamante': 'diamond',
        'triangular': 'triangle',
        
        # Nose shapes
        'recta': 'straight',
        'romana': 'roman',
        'botón': 'button',
        'bulbosa': 'bulbous',
        'aquilina': 'aquiline',
        'chata': 'snub',
        
        # Lip shapes
        'llenos': 'full',
        'finos': 'thin',
        'anchos': 'wide',
        'estrechos': 'narrow',
        'definidos': 'defined',
        'indefinidos': 'undefined',
        
        # Eye shapes
        'almendrados': 'almond',
        'redondos': 'round',
        'ovalados': 'oval',
        'hacia_arriba': 'upturned',
        'hacia_abajo': 'downturned',
        'hundidos': 'deep_set',
        
        # Jawlines
        'definida': 'defined',
        'suave': 'soft',
        'angular': 'angular',
        'redonda': 'round',
        'cuadrada': 'square',
        'puntiaguda': 'pointed',
        
        # Cheekbones
        'altos': 'high',
        'bajos': 'low',
        'prominentes': 'prominent',
        'planos': 'flat',
        'definidos': 'defined',
        'suaves': 'soft',
        
        # Eyebrows
        'gruesas': 'thick',
        'finas': 'thin',
        'arqueadas': 'arched',
        'rectas': 'straight',
        'redondeadas': 'rounded',
        'anguladas': 'angled',
        
        # Skin textures
        'suave': 'smooth',
        'áspera': 'rough',
        'grasa': 'oily',
        'seca': 'dry',
        'mixta': 'combination',
        'madura': 'mature',
        
        # Makeup types
        'natural': 'natural',
        'mínimo': 'minimal',
        'ligero': 'light',
        'medio': 'medium',
        'pesado': 'heavy',
        'dramático': 'dramatic',
        'sin_maquillaje': 'no_makeup',
        
        # Clothing types
        'traje_negocio': 'business_suit',
        'camisa_casual': 'casual_shirt',
        'camiseta': 't_shirt',
        'polo': 'polo_shirt',
        'camisa_formal': 'dress_shirt',
        'blazer': 'blazer',
        'suéter': 'sweater',
        
        # Clothing colors
        'blanco': 'white',
        'negro': 'black',
        'gris': 'gray',
        'azul_marino': 'navy',
        'azul': 'blue',
        'rojo': 'red',
        'verde': 'green',
        'marrón': 'brown',
        'beige': 'beige',
        
        # Backgrounds
        'blanco_solido': 'white_solid',
        'gris_claro': 'light_gray',
        'neutral': 'neutral',
        'profesional': 'professional',
        
        # Freckles
        'ninguna': 'none',
        'ligeras': 'light',
        'medias': 'medium',
        'pesadas': 'heavy',
        'esparcidas': 'scattered',
        'concentradas': 'concentrated',
        
        # Moles
        'ninguno': 'none',
        'uno': 'one',
        'pocos': 'few',
        'varios': 'several',
        'muchos': 'many',
        'faciales': 'facial',
        
        # Scars
        'ninguna': 'none',
        'pequeña': 'small',
        'mediana': 'medium',
        'grande': 'large',
        'facial': 'facial',
        'corporal': 'body',
        
        # Acne
        'ninguno': 'none',
        'leve': 'mild',
        'moderado': 'moderate',
        'severo': 'severe',
        'ocasional': 'occasional',
        'crónico': 'chronic',
        
        # Wrinkles
        'ninguna': 'none',
        'líneas_finas': 'fine_lines',
        'moderadas': 'moderate',
        'profundas': 'deep',
        'patas_gallo': 'crow_feet',
        'líneas_frente': 'forehead_lines',
        
        # Hair styles
        'liso': 'straight',
        'ondulado': 'wavy',
        'rizado': 'curly',
        'muy_rizado': 'very_curly',
        'corte_pixie': 'pixie_cut',
        'bob': 'bob',
        'capas': 'layered',
        
        # Facial hair
        'ninguno': 'none',
        'ligero': 'light',
        'moderado': 'moderate',
        'pesado': 'heavy',
        
        # Beard types
        'ninguna': 'none',
        'barba_incipiente': 'stubble',
        'corta': 'short',
        'media': 'medium',
        'larga': 'long',
        'completa': 'full',
        
        # Mustache types
        'ninguno': 'none',
        'ligero': 'light',
        'medio': 'medium',
        'grueso': 'thick',
        'manillar': 'handlebar',
        
        # Physical complexion
        'muy_delgado': 'very_thin',
        'delgado': 'thin',
        'ligeramente_delgado': 'slightly_thin',
        'normal': 'normal',
        'ligeramente_sobrepeso': 'slightly_overweight',
        'sobrepeso': 'overweight',
        'obeso': 'obese',
        'muy_obeso': 'very_obese',
        'atlético': 'athletic',
        'musculoso': 'muscular',
        'delgado_atlético': 'lean_athletic',
        'robusto': 'stocky'
    }
    
    # Convertir a string y manejar errores
    try:
        spanish_str = str(spanish_value).lower().strip()
        return translations.get(spanish_str, spanish_str)
    except Exception as e:
        print(f"Error en translate_to_english: {e}, valor: {spanish_value}")
        return 'random'
import sys
from pathlib import Path
import threading
import logging

# Agregar el directorio core al path
sys.path.append(str(Path(__file__).parent.parent / "core"))

from api_client import WebUIAPIClient, GeneticAPIGenerator
from diversity_engine import UltraDiversityEngine
from saime_validator import SAIMEValidator
from file_manager import FileManager
from massive_engine import MassiveGenerationEngine

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Variables globales
api_client = None
genetic_generator = None
diversity_engine = None
saime_validator = None
file_manager = None
massive_engine = None
generation_status = {"running": False, "progress": 0, "current": 0, "total": 0}

def init_system():
    """Inicializar sistema genético"""
    global api_client, genetic_generator, diversity_engine, saime_validator, file_manager, massive_engine
    
    try:
        # Inicializar cliente API
        api_client = WebUIAPIClient()
        
        # Esperar que WebUI esté disponible
        if not api_client.wait_for_webui():
            logger.error("No se pudo conectar con WebUI")
            return False
        
        # Inicializar motor de diversidad
        diversity_engine = UltraDiversityEngine()
        
        # Inicializar validador SAIME
        saime_validator = SAIMEValidator()
        
        # Inicializar gestor de archivos
        file_manager = FileManager()
        
        # Inicializar generador genético
        genetic_generator = GeneticAPIGenerator(api_client)
        
        # Inicializar motor de generación masiva
        massive_engine = MassiveGenerationEngine()
        
        logger.info("✅ Sistema genético inicializado correctamente")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error inicializando sistema: {e}")
        return False

@app.route('/')
def index():
    """Página principal con interfaz atractiva"""
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """Estado del sistema"""
    try:
        if api_client:
            options = api_client.get_options()
            models = api_client.get_models()
            
            return jsonify({
                'webui_connected': True,
                'models_count': len(models),
                'models': [model.get('title', model.get('model_name', 'Unknown')) for model in models],
                'current_model': options.get('sd_model_checkpoint', 'Unknown'),
                'generation_status': generation_status
            })
        else:
            return jsonify({'webui_connected': False})
    except Exception as e:
        logger.error(f"Error obteniendo estado: {e}")
        return jsonify({'webui_connected': False, 'error': str(e)})

@app.route('/api/models')
def api_models():
    """Obtener modelos disponibles"""
    try:
        if api_client:
            models = api_client.get_models()
            return jsonify({
                'success': True,
                'models': models
            })
        return jsonify({'success': False, 'error': 'API client not initialized'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/set_model', methods=['POST'])
def api_set_model():
    """Cambiar modelo activo"""
    try:
        data = request.json
        model_name = data.get('model_name')
        
        if api_client and model_name:
            success = api_client.set_model(model_name)
            return jsonify({'success': success})
        return jsonify({'success': False, 'error': 'Invalid parameters'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/generate/genetic', methods=['POST'])
def api_generate_genetic():
    """API para generación genética"""
    try:
        if generation_status["running"]:
            return jsonify({'success': False, 'error': 'Generación en progreso'})
        
        # Manejar tanto JSON como FormData
        if request.is_json:
            data = request.json
        else:
            data = request.form.to_dict()
        
        # Validar parámetros
        required_params = ['nacionalidad', 'genero', 'edad_min', 'edad_max', 'cantidad']
        for param in required_params:
            if param not in data:
                return jsonify({'success': False, 'error': f'Parámetro requerido: {param}'})
        
        # Validar rango de edad
        if int(data['edad_min']) > int(data['edad_max']):
            return jsonify({'success': False, 'error': 'La edad mínima no puede ser mayor que la máxima'})
        
        # Obtener modelo activo
        current_model = "unknown_model"
        if api_client:
            try:
                current_model = api_client.get_current_model()
            except Exception as e:
                print(f"⚠️ Error obteniendo modelo activo: {e}")
        
        # Convertir tipos y agregar controles de diversidad
        params = {
            'nacionalidad': data['nacionalidad'],
            'genero': data['genero'],
            'region': data.get('region', 'random'),
            'edad_min': int(data['edad_min']),
            'edad_max': int(data['edad_max']),
            'cantidad': int(data['cantidad']),
            'model': current_model,  # Agregar modelo activo
            'width': int(data.get('width', 512)),
            'height': int(data.get('height', 764)),
            'cfg_scale': float(data.get('cfg_scale', 7.0)),
            'steps': int(data.get('steps', 20)),
            'sampler_name': data.get('sampler_name', 'DPM++ 2M'),
            'seed': int(data.get('seed', -1)),
            # Controles de diversidad genética (español a inglés)
            'beauty_control': translate_to_english(data.get('beauty_control', 'aleatorio')),
            'skin_control': translate_to_english(data.get('skin_control', 'aleatorio')),
            'hair_control': translate_to_english(data.get('hair_control', 'aleatorio')),
            'hair_length_control': translate_to_english(data.get('hair_length_control', 'aleatorio')),
            'hair_style_control': translate_to_english(data.get('hair_style_control', 'aleatorio')),
            'eye_control': translate_to_english(data.get('eye_control', 'aleatorio')),
            'eye_shape_control': translate_to_english(data.get('eye_shape_control', 'aleatorio')),
            'face_shape_control': translate_to_english(data.get('face_shape_control', 'aleatorio')),
            'nose_shape_control': translate_to_english(data.get('nose_shape_control', 'aleatorio')),
            'lip_shape_control': translate_to_english(data.get('lip_shape_control', 'aleatorio')),
            'jawline_control': translate_to_english(data.get('jawline_control', 'aleatorio')),
            'cheekbone_control': translate_to_english(data.get('cheekbone_control', 'aleatorio')),
            'eyebrow_control': translate_to_english(data.get('eyebrow_control', 'aleatorio')),
            'skin_texture_control': translate_to_english(data.get('skin_texture_control', 'aleatorio')),
            'makeup_control': translate_to_english(data.get('makeup_control', 'aleatorio')),
            'clothing_type_control': translate_to_english(data.get('clothing_type_control', 'aleatorio')),
            'clothing_color_control': translate_to_english(data.get('clothing_color_control', 'aleatorio')),
            'background_control': translate_to_english(data.get('background_control', 'blanco_solido')),
            'freckle_control': translate_to_english(data.get('freckle_control', 'aleatorio')),
            'mole_control': translate_to_english(data.get('mole_control', 'aleatorio')),
            'scar_control': translate_to_english(data.get('scar_control', 'aleatorio')),
            'acne_control': translate_to_english(data.get('acne_control', 'aleatorio')),
            'wrinkle_control': translate_to_english(data.get('wrinkle_control', 'aleatorio')),
            # Nuevos controles de diversidad
            'facial_hair_control': translate_to_english(data.get('facial_hair_control', 'aleatorio')),
            'beard_control': translate_to_english(data.get('beard_control', 'aleatorio')),
            'mustache_control': translate_to_english(data.get('mustache_control', 'aleatorio')),
            'physical_complexion_control': translate_to_english(data.get('physical_complexion_control', 'aleatorio'))
        }
        
        # Iniciar generación en hilo separado
        def generate_worker():
            global generation_status
            generation_status["running"] = True
            generation_status["progress"] = 0
            generation_status["current"] = 0
            generation_status["total"] = params['cantidad']
            
            try:
                # Importar función de generación genética
                from genetic_engine import generate_genetic_batch
                result = generate_genetic_batch(params)
                generation_status["running"] = False
                generation_status["progress"] = 100
                logger.info(f"Generación completada: {result}")
            except Exception as e:
                generation_status["running"] = False
                logger.error(f"Error en generación: {e}")
        
        thread = threading.Thread(target=generate_worker)
        thread.daemon = True
        thread.start()
        
        return jsonify({'success': True, 'message': 'Generación iniciada'})
        
    except Exception as e:
        logger.error(f"Error en API genética: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/generate/massive', methods=['POST'])
def api_generate_massive():
    """API para generación masiva con diversidad genética"""
    try:
        if generation_status["running"]:
            return jsonify({'success': False, 'error': 'Generación en progreso'})
        
        data = request.json
        
        # Validar parámetros requeridos
        dataset_path = data.get('dataset_path')
        if not dataset_path:
            return jsonify({'success': False, 'error': 'Ruta del dataset requerida'})
        
        # Parámetros de generación
        params = {
            'model': data.get('model'),
            'cantidad': int(data.get('cantidad', 10)),
            'width': int(data.get('width', 512)),
            'height': int(data.get('height', 764)),
            'cfg_scale': float(data.get('cfg_scale', 7.5)),
            'steps': int(data.get('steps', 20)),
            'seed': int(data.get('seed', -1)),
            # Controles de diversidad genética
            'skin_control': data.get('skin_control', 'aleatorio'),
            'hair_control': data.get('hair_control', 'aleatorio'),
            'hair_style_control': data.get('hair_style_control', 'aleatorio'),
            'beauty_control': data.get('beauty_control', 'aleatorio')
        }
        
        # Iniciar generación en hilo separado
        def generate_worker():
            global generation_status
            generation_status["running"] = True
            generation_status["progress"] = 0
            generation_status["current"] = 0
            generation_status["total"] = params['cantidad']
            
            try:
                result = massive_engine.generate_massive_batch(dataset_path, params)
                generation_status["running"] = False
                generation_status["progress"] = 100
                logger.info(f"Generación masiva completada: {result}")
            except Exception as e:
                generation_status["running"] = False
                logger.error(f"Error en generación masiva: {e}")
        
        thread = threading.Thread(target=generate_worker)
        thread.daemon = True
        thread.start()
        
        return jsonify({'success': True, 'message': 'Generación masiva iniciada'})
        
    except Exception as e:
        logger.error(f"Error en API masiva: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/stop_generation', methods=['POST'])
def api_stop_generation():
    """Detener generación en curso"""
    try:
        generation_status["running"] = False
        return jsonify({'success': True, 'message': 'Generación detenida'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/saime_config')
def api_saime_config():
    """Obtener configuración SAIME"""
    try:
        config_path = Path("data/saime_config.json")
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = json.load(f)
            return jsonify({'success': True, 'config': config})
        return jsonify({'success': False, 'error': 'Configuración SAIME no encontrada'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/diversity_options', methods=['GET'])
def api_diversity_options():
    """Obtener opciones de diversidad"""
    try:
        options_path = Path("data/diversity_options.json")
        if options_path.exists():
            with open(options_path, 'r') as f:
                options = json.load(f)
            return jsonify({'success': True, 'options': options})
        return jsonify({'success': False, 'error': 'Opciones de diversidad no encontradas'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/saime_config', methods=['POST'])
def api_update_saime_config():
    """Actualizar configuración SAIME"""
    try:
        data = request.json
        config_path = Path("data/saime_config.json")
        
        with open(config_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        return jsonify({'success': True, 'message': 'Configuración SAIME actualizada'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/outputs')
def api_outputs():
    """Obtener lista de archivos generados"""
    try:
        outputs_dir = Path("outputs")
        if not outputs_dir.exists():
            return jsonify({'success': True, 'files': []})
        
        files = []
        for file_path in outputs_dir.rglob("*"):
            if file_path.is_file():
                files.append({
                    'name': file_path.name,
                    'path': str(file_path.relative_to(outputs_dir)),
                    'size': file_path.stat().st_size,
                    'modified': file_path.stat().st_mtime
                })
        
        return jsonify({'success': True, 'files': files})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/open_output_folder', methods=['POST'])
def api_open_output_folder():
    """API para abrir carpeta de salida"""
    try:
        if file_manager is None:
            return jsonify({'success': False, 'error': 'FileManager no inicializado'})
        
        result = file_manager.open_output_folder()
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error abriendo carpeta: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download/<path:filename>')
def download_file(filename):
    """Descargar archivo generado"""
    try:
        file_path = Path("outputs") / filename
        if file_path.exists():
            return send_file(file_path, as_attachment=True)
        return jsonify({'error': 'Archivo no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🧬 Iniciando Sistema de Generación Masiva Genética")
    print("=" * 50)
    
    # Inicializar sistema
    if init_system():
        print("✅ Sistema inicializado correctamente")
        print("🌐 Iniciando interfaz web en puerto 5000...")
        print("📱 Accede a: http://localhost:5000")
        
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print("❌ Error inicializando sistema")
        print("   Verifica que WebUI esté ejecutándose en http://localhost:7860")
        sys.exit(1)
