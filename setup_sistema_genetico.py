#!/usr/bin/env python3
"""
Script de configuración para Sistema de Generación Masiva Genética
Instala dependencias y configura el sistema
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def install_requirements():
    """Instalar dependencias de requirements.txt"""
    print("📦 Instalando dependencias...")
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True, check=True)
        
        print("✅ Dependencias instaladas correctamente")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error instalando dependencias: {e}")
        print(f"   Salida: {e.stdout}")
        print(f"   Error: {e.stderr}")
        return False

def create_config_files():
    """Crear archivos de configuración necesarios"""
    print("⚙️ Creando archivos de configuración...")
    
    # Crear archivo de configuración del sistema
    system_config = {
        "webui": {
            "base_url": "http://localhost:7860",
            "timeout": 300,
            "retry_attempts": 3
        },
        "genetic_system": {
            "max_concurrent_generations": 1,
            "output_directory": "outputs",
            "diversity_engine": "ultra_diversity",
            "anti_repetition": {
                "max_recent_choices": 15,
                "gender_specific": True
            }
        },
        "saime": {
            "dimensions": {
                "width": 512,
                "height": 764
            },
            "validation": True,
            "strict_compliance": True
        },
        "api": {
            "host": "0.0.0.0",
            "port": 5000,
            "debug": False
        }
    }
    
    config_path = Path("sistema_genetico/data/system_config.json")
    with open(config_path, 'w') as f:
        json.dump(system_config, f, indent=2)
    
    print(f"✅ Configuración del sistema creada: {config_path}")
    
    # Crear archivo de logging
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "default",
                "filename": "sistema_genetico/outputs/logs/system.log"
            }
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file"]
        }
    }
    
    # Crear directorio de logs
    logs_dir = Path("sistema_genetico/outputs/logs")
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    logging_path = Path("sistema_genetico/data/logging_config.json")
    with open(logging_path, 'w') as f:
        json.dump(logging_config, f, indent=2)
    
    print(f"✅ Configuración de logging creada: {logging_path}")
    
    return True

def verify_structure():
    """Verificar estructura de directorios"""
    print("🔍 Verificando estructura de directorios...")
    
    required_dirs = [
        "webui_standalone",
        "sistema_genetico/core",
        "sistema_genetico/interfaces",
        "sistema_genetico/data",
        "sistema_genetico/outputs/genetic_images",
        "sistema_genetico/outputs/passport_images",
        "sistema_genetico/outputs/analysis",
        "sistema_genetico/outputs/logs"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not Path(dir_path).exists():
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print("❌ Directorios faltantes:")
        for dir_path in missing_dirs:
            print(f"   - {dir_path}")
        return False
    
    print("✅ Estructura de directorios correcta")
    return True

def create_startup_scripts():
    """Crear scripts de inicio"""
    print("🚀 Creando scripts de inicio...")
    
    # Script de inicio del sistema genético
    genetic_start_script = '''#!/usr/bin/env python3
"""
Script de inicio para Sistema Genético
"""

import sys
from pathlib import Path

# Agregar directorio core al path
sys.path.append(str(Path(__file__).parent / "core"))

from interfaces.web_interface import app

if __name__ == "__main__":
    print("🧬 Iniciando Sistema Genético...")
    app.run(host='0.0.0.0', port=5000, debug=False)
'''
    
    start_script_path = Path("sistema_genetico/start_genetic_system.py")
    with open(start_script_path, 'w') as f:
        f.write(genetic_start_script)
    
    # Hacer ejecutable
    os.chmod(start_script_path, 0o755)
    
    print(f"✅ Script de inicio creado: {start_script_path}")
    
    return True

def test_imports():
    """Probar importaciones de módulos"""
    print("🧪 Probando importaciones...")
    
    try:
        # Probar importaciones básicas
        import flask
        import requests
        import json
        import threading
        from pathlib import Path
        
        print("✅ Importaciones básicas funcionando")
        
        # Probar importaciones del sistema genético
        sys.path.append(str(Path("sistema_genetico/core")))
        
        try:
            from api_client import WebUIAPIClient
            print("✅ Cliente API importado correctamente")
        except ImportError as e:
            print(f"⚠️ Advertencia: No se pudo importar cliente API: {e}")
        
        try:
            from diversity_engine import UltraDiversityEngine
            print("✅ Motor de diversidad importado correctamente")
        except ImportError as e:
            print(f"⚠️ Advertencia: No se pudo importar motor de diversidad: {e}")
        
        try:
            from saime_validator import SAIMEValidator
            print("✅ Validador SAIME importado correctamente")
        except ImportError as e:
            print(f"⚠️ Advertencia: No se pudo importar validador SAIME: {e}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error en importaciones: {e}")
        return False

def main():
    """Función principal de configuración"""
    print("🧬 CONFIGURACIÓN DEL SISTEMA DE GENERACIÓN MASIVA GENÉTICA")
    print("=" * 60)
    
    # Verificar estructura
    if not verify_structure():
        print("❌ Error: Estructura de directorios incorrecta")
        return False
    
    # Instalar dependencias
    if not install_requirements():
        print("❌ Error: No se pudieron instalar las dependencias")
        return False
    
    # Crear archivos de configuración
    if not create_config_files():
        print("❌ Error: No se pudieron crear archivos de configuración")
        return False
    
    # Crear scripts de inicio
    if not create_startup_scripts():
        print("❌ Error: No se pudieron crear scripts de inicio")
        return False
    
    # Probar importaciones
    if not test_imports():
        print("⚠️ Advertencia: Algunas importaciones fallaron")
    
    print("=" * 60)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 60)
    print("🚀 Para iniciar el sistema:")
    print("   ./run.sh")
    print("")
    print("🌐 Accesos:")
    print("   - WebUI API: http://localhost:7860")
    print("   - Sistema Genético: http://localhost:5000")
    print("")
    print("📚 Documentación: docs/README.md")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
