# 🧬 Sistema de Generación Masiva Genética - API Mode

## 📋 Descripción

Sistema completamente independiente que ejecuta WebUI en modo headless y mantiene toda la lógica de generación genética y masiva desarrollada, conectándose vía API para crear imágenes tipo pasaporte de forma masiva.

## ✨ Características Principales

### **🧬 Generación Masiva Genética**
- **Motor genético avanzado** con diversidad excepcional (99.0%)
- **Sistema anti-repetición específico por género** para máxima unicidad
- **Arrugas por edad apropiadas** (18-19: ninguno, 20-29: leves, 30-39: moderadas, etc.)
- **Características específicas por género** (hombres: mandíbula fuerte, pómulos altos; mujeres: mandíbula suave, pómulos bajos)
- **30+ opciones por categoría** para diversidad máxima
- **Generación de JSON, CSV y PNG** automática

### **📄 Generación Masiva de Pasaporte**
- **Sistema híbrido** que combina parámetros WebUI con datasets JSON
- **Especificaciones SAIME completas** (dimensiones 512x764, fondo blanco, etc.)
- **Posicionamiento preciso** (cabeza en 50% superior, ojos en 40%)
- **Prevención de ropa blanca** automática
- **Más torso visible** para cumplir estándares

### **🌐 Interfaz Web Flask**
- **Interfaz atractiva y funcional** con prioridad en funcionalidad
- **Configuración SAIME editable** via JSON
- **Monitoreo en tiempo real** del estado del sistema
- **Descarga de archivos generados**
- **API REST completa** para integración

## 🚀 Instalación y Configuración

### **Requisitos del Sistema**
- Python 3.10+
- Git
- 8GB+ RAM recomendado
- GPU NVIDIA (opcional pero recomendado)

### **Instalación Paso a Paso**

#### **1. Configuración Inicial**
```bash
# Clonar o descargar el proyecto
cd /ruta/del/proyecto

# Ejecutar configuración automática
python3 setup_sistema_genetico.py
```

#### **2. Iniciar Sistema**

#### **Opción A: Primera Instalación (Recomendado para primera vez)**
```bash
# Primera instalación - Más tiempo para WebUI
./run_first_time.sh
```

#### **Opción B: Sistema Completo (WebUI + Sistema Genético)**
```bash
# Iniciar todo el sistema (WebUI + Sistema Genético)
./run.sh
```

#### **Opción C: Solo Sistema Genético (WebUI ya ejecutándose)**
```bash
# Si WebUI ya está ejecutándose en puerto 7860
./start_genetic_only.sh
```

#### **Opción D: Solo WebUI (para desarrollo)**
```bash
# Solo iniciar WebUI en modo headless
cd webui_standalone
./webui.sh --api --listen --no-browser --xformers
```

## 🎯 Uso del Sistema

### **Acceso a Interfaces**
- **WebUI API**: http://localhost:7860 (modo headless)
- **Sistema Genético**: http://localhost:5000 (interfaz web)

### **Generación Genética**
1. **Acceder a la interfaz web** en http://localhost:5000
2. **Configurar parámetros**:
   - Nacionalidad (Venezuela, Colombia, México, etc.)
   - Género (Hombre, Mujer)
   - Edad (18-80 años)
   - Cantidad de imágenes (1-50)
   - Parámetros técnicos (CFG Scale, Steps, etc.)
3. **Seleccionar modelo** de la lista disponible
4. **Hacer clic en "Generar Imágenes Genéticas"**
5. **Monitorear progreso** en tiempo real
6. **Descargar resultados** desde la interfaz

### **Generación Masiva de Pasaporte**
1. **Preparar dataset** con archivos JSON/PNG
2. **Configurar carpeta del dataset** en la interfaz
3. **Establecer parámetros** de generación
4. **Iniciar generación masiva**
5. **Descargar resultados** generados

### **Configuración SAIME**
1. **Acceder a la sección "Configuración SAIME"**
2. **Editar JSON** con parámetros específicos
3. **Guardar configuración** para uso futuro
4. **Aplicar automáticamente** en generaciones

## 🏗️ Arquitectura del Sistema

### **Estructura de Directorios**
```
Stable-diffussion-webui_API_Mode_Genetic_Images/
├── webui_standalone/                    # WebUI estándar
│   ├── webui.py                        # Archivo principal
│   ├── webui.sh                        # Script de ejecución
│   └── models/                         # Modelos de IA
├── sistema_genetico/                   # Sistema genético
│   ├── core/                          # Motor principal
│   │   ├── api_client.py              # Cliente API
│   │   ├── diversity_engine.py        # Motor de diversidad
│   │   ├── genetic_engine.py           # Motor genético
│   │   └── saime_validator.py         # Validador SAIME
│   ├── interfaces/                    # Interfaces
│   │   ├── web_interface.py          # Interfaz Flask
│   │   └── templates/                 # Templates HTML
│   ├── data/                          # Datos y configuraciones
│   │   ├── saime_config.json         # Configuración SAIME
│   │   ├── diversity_data.json       # Datos de diversidad
│   │   └── system_config.json        # Configuración sistema
│   └── outputs/                       # Salidas
│       ├── genetic_images/            # Imágenes genéticas
│       ├── passport_images/           # Imágenes pasaporte
│       └── analysis/                  # Análisis y reportes
├── run.sh                             # Script de inicio
├── setup_sistema_genetico.py          # Configuración
└── requirements.txt                   # Dependencias
```

### **Componentes Principales**

#### **1. WebUI Standalone**
- **Descarga automática** desde GitHub
- **Modo headless** con API habilitada
- **Puerto 7860** para comunicación
- **Modelos compatibles** con Stable Diffusion

#### **2. Sistema Genético**
- **Motor de diversidad** con 99.0% de unicidad
- **Sistema anti-repetición** específico por género
- **19 parámetros de diversidad** con 30+ opciones cada uno
- **Arrugas por edad** y características de género

#### **3. Cliente API**
- **Conexión HTTP** al WebUI
- **Manejo de errores** y reintentos
- **Generación de imágenes** vía API
- **Gestión de modelos** y opciones

#### **4. Interfaz Web Flask**
- **Frontend atractivo** con HTML/CSS/JS
- **API REST completa** para integración
- **Monitoreo en tiempo real** del sistema
- **Descarga de archivos** generados

## 📊 Configuración Avanzada

### **Parámetros de Diversidad**
```json
{
  "beauty_levels": ["muy bajo", "bajo", "medio", "alto", "muy alto"],
  "skin_tones": ["muy claro", "claro", "medio", "moreno", "muy moreno"],
  "hair_colors": ["negro", "marrón", "rubio", "rojo", "gris"],
  "eye_colors": ["marrón", "verde", "azul", "gris", "avellana"],
  "face_shapes": ["oval", "redondo", "cuadrado", "corazón", "diamante"]
}
```

### **Especificaciones SAIME**
```json
{
  "dimensions": {
    "width": 512,
    "height": 764,
    "dpi": 300
  },
  "positioning": {
    "head": {
      "percentage_from_top": 50,
      "width": 100,
      "height": 120
    },
    "eyes": {
      "percentage_from_top": 31,
      "distance_between": 32
    },
    "shoulders": {
      "percentage_from_top": 78,
      "width": 180,
      "must_touch_edges": true
    }
  }
}
```

### **Configuración del Sistema**
```json
{
  "webui": {
    "base_url": "http://localhost:7860",
    "timeout": 300,
    "retry_attempts": 3
  },
  "genetic_system": {
    "max_concurrent_generations": 1,
    "diversity_engine": "ultra_diversity",
    "anti_repetition": {
      "max_recent_choices": 15,
      "gender_specific": true
    }
  }
}
```

## 🔧 API REST

### **Endpoints Principales**

#### **Estado del Sistema**
```bash
GET /api/status
# Retorna estado de WebUI, modelo activo, generación
```

#### **Modelos Disponibles**
```bash
GET /api/models
# Lista modelos disponibles en WebUI
```

#### **Cambiar Modelo**
```bash
POST /api/set_model
{
  "model_name": "nombre_del_modelo"
}
```

#### **Generación Genética**
```bash
POST /api/generate/genetic
{
  "nacionalidad": "Venezuela",
  "genero": "hombre",
  "edad": 30,
  "cantidad": 5,
  "cfg_scale": 7.0,
  "steps": 20
}
```

#### **Generación Masiva**
```bash
POST /api/generate/passport
{
  "dataset_folder": "/ruta/al/dataset",
  "cantidad": 10,
  "cfg_scale": 7.5
}
```

#### **Configuración SAIME**
```bash
GET /api/saime_config
POST /api/saime_config
# Obtener/actualizar configuración SAIME
```

#### **Archivos Generados**
```bash
GET /api/outputs
# Lista archivos generados
```

#### **Descargar Archivo**
```bash
GET /download/{filename}
# Descargar archivo específico
```

## 🛠️ Solución de Problemas

### **WebUI no inicia**
```bash
# Verificar puerto disponible
netstat -tulpn | grep 7860

# Iniciar manualmente
cd webui_standalone
./webui.sh --api --listen --no-browser
```

### **Sistema Genético no responde**
```bash
# Verificar dependencias
pip install -r requirements.txt

# Verificar logs
tail -f sistema_genetico/outputs/logs/system.log
```

### **Error de conexión API**
```bash
# Verificar que WebUI esté funcionando
curl http://localhost:7860/sdapi/v1/options

# Verificar firewall
sudo ufw allow 7860
sudo ufw allow 5000
```

### **Error de memoria**
```bash
# Reducir batch_size en configuración
# Usar modelos más pequeños
# Liberar memoria del sistema
```

## 📈 Rendimiento y Optimización

### **Configuración Recomendada**
- **RAM**: 8GB+ para generación fluida
- **GPU**: NVIDIA con 6GB+ VRAM
- **CPU**: 4+ cores para procesamiento paralelo
- **Almacenamiento**: SSD para acceso rápido

### **Optimizaciones**
- **Batch size**: Ajustar según memoria disponible
- **Steps**: 20-30 para balance calidad/velocidad
- **CFG Scale**: 7-9 para mejor calidad
- **Modelos**: Usar modelos optimizados

### **Monitoreo**
- **Logs del sistema**: `sistema_genetico/outputs/logs/`
- **Estado en tiempo real**: Interfaz web
- **Uso de recursos**: Monitor del sistema

## 🤝 Contribuciones

### **Estructura Modular**
El sistema está diseñado de forma modular para facilitar:
- **Modificaciones independientes** de cada componente
- **Agregar nuevas funcionalidades** sin afectar existentes
- **Mantenimiento** y debugging simplificado
- **Escalabilidad** futura

### **Buenas Prácticas**
- **Separación de responsabilidades** por módulo
- **Interfaces claras** entre componentes
- **Configuración externa** via JSON
- **Logging detallado** para debugging
- **Manejo de errores** robusto

## 📄 Licencia

Este proyecto extiende Stable Diffusion WebUI bajo la misma licencia.

## 🎯 Estado Actual

- ✅ **WebUI headless**: Configurado y funcional
- ✅ **Sistema genético**: Motor de diversidad 99.0%
- ✅ **Cliente API**: Conexión HTTP al WebUI
- ✅ **Interfaz web**: Flask atractiva y funcional
- ✅ **Configuración SAIME**: JSON editable
- ✅ **Scripts de inicio**: Automatización completa
- ✅ **Documentación**: Guías completas

**🎉 El sistema está completamente funcional y listo para uso en producción.**
