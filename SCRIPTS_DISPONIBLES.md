# 🚀 Scripts Disponibles - Sistema de Generación Masiva Genética

## 📋 **RESUMEN DE SCRIPTS**

### **1. `run.sh` - Sistema Completo** 🎯
**Descripción**: Inicia WebUI (si no está ejecutándose) + Sistema Genético
**Uso**: Cuando quieres iniciar todo el sistema desde cero

```bash
./run.sh
```

**Comportamiento**:
- ✅ **Verifica si WebUI ya está ejecutándose** en puerto 7860
- ✅ **Si WebUI NO está ejecutándose**: Lo inicia automáticamente
- ✅ **Si WebUI YA está ejecutándose**: Solo inicia el Sistema Genético
- ✅ **Inicia Sistema Genético** en puerto 5000
- ✅ **Monitorea ambos procesos** y los detiene al salir (solo WebUI si lo inició)

### **2. `start_genetic_only.sh` - Solo Sistema Genético** 🧬
**Descripción**: Inicia solo el Sistema Genético (requiere WebUI ejecutándose)
**Uso**: Cuando WebUI ya está ejecutándose y solo quieres el sistema genético

```bash
./start_genetic_only.sh
```

**Comportamiento**:
- ✅ **Verifica que WebUI esté ejecutándose** en puerto 7860
- ✅ **Si WebUI NO está ejecutándose**: Muestra error y sale
- ✅ **Si WebUI está ejecutándose**: Inicia Sistema Genético
- ✅ **Solo monitorea Sistema Genético** (no toca WebUI)

### **3. `setup_sistema_genetico.py` - Configuración** ⚙️
**Descripción**: Configura dependencias y archivos del sistema
**Uso**: Primera vez o después de cambios en dependencias

```bash
python3 setup_sistema_genetico.py
```

**Comportamiento**:
- ✅ **Instala dependencias** de requirements.txt
- ✅ **Crea archivos de configuración** necesarios
- ✅ **Verifica estructura** de directorios
- ✅ **Prueba importaciones** de módulos

## 🎯 **CASOS DE USO**

### **Caso 1: Primera vez usando el sistema**
```bash
# 1. Configurar sistema
python3 setup_sistema_genetico.py

# 2. Iniciar todo el sistema
./run.sh
```

### **Caso 2: WebUI ya está ejecutándose**
```bash
# Solo iniciar sistema genético
./start_genetic_only.sh
```

### **Caso 3: Desarrollo - Solo WebUI**
```bash
# Solo WebUI para desarrollo
cd webui_standalone
./webui.sh --api --listen --no-browser --xformers
```

### **Caso 4: Reiniciar solo Sistema Genético**
```bash
# Si el sistema genético se detiene pero WebUI sigue ejecutándose
./start_genetic_only.sh
```

## 🔧 **COMPORTAMIENTO INTELIGENTE**

### **`run.sh` - Detección Automática**
```
🔍 Verificando estado de WebUI...
✅ WebUI ya está ejecutándose en http://localhost:7860
   Continuando con sistema genético...
```

**O**
```
🔍 Verificando estado de WebUI...
🚀 WebUI no está ejecutándose, iniciando...
   Iniciando WebUI con parámetros: --api --listen --no-browser
   WebUI iniciado con PID: 12345
   Esperando que WebUI esté disponible...
```

### **`start_genetic_only.sh` - Verificación Estricta**
```
🔍 Verificando que WebUI esté ejecutándose...
✅ WebUI está ejecutándose correctamente
🧬 Iniciando Sistema Genético...
```

**O**
```
🔍 Verificando que WebUI esté ejecutándose...
❌ Error: WebUI no está ejecutándose en http://localhost:7860
   Inicia WebUI primero con:
   cd webui_standalone && ./webui.sh --api --listen --no-browser
```

## 🛑 **LIMPIEZA AUTOMÁTICA**

### **`run.sh` - Limpieza Inteligente**
- **Si inició WebUI**: Lo detiene al salir
- **Si WebUI ya estaba ejecutándose**: NO lo detiene
- **Sistema Genético**: Siempre lo detiene

### **`start_genetic_only.sh` - Limpieza Simple**
- **WebUI**: No lo toca (no lo inició)
- **Sistema Genético**: Lo detiene al salir

## 📊 **MONITOREO DE PROCESOS**

### **`run.sh`**
- Monitorea WebUI (solo si lo inició)
- Monitorea Sistema Genético
- Detiene todo al salir

### **`start_genetic_only.sh`**
- Solo monitorea Sistema Genético
- No toca WebUI

## 🎯 **RECOMENDACIONES DE USO**

### **Para Uso Normal**
```bash
# Usar run.sh - es inteligente y maneja todo
./run.sh
```

### **Para Desarrollo**
```bash
# Terminal 1: WebUI
cd webui_standalone
./webui.sh --api --listen --no-browser --xformers

# Terminal 2: Sistema Genético
./start_genetic_only.sh
```

### **Para Producción**
```bash
# Sistema completo con monitoreo
./run.sh
```

## 🚀 **VENTAJAS DEL SISTEMA**

### **✅ Inteligente**
- Detecta automáticamente si WebUI está ejecutándose
- No duplica procesos
- Limpieza automática apropiada

### **✅ Flexible**
- Múltiples opciones de inicio
- Desarrollo independiente
- Producción integrada

### **✅ Robusto**
- Verificaciones de estado
- Manejo de errores
- Monitoreo continuo

### **✅ Modular**
- Scripts independientes
- Fácil mantenimiento
- Configuración clara

## 🎉 **RESULTADO FINAL**

El sistema ahora es **completamente inteligente**:

1. **`run.sh`** - Detecta si WebUI está ejecutándose y actúa apropiadamente
2. **`start_genetic_only.sh`** - Solo para cuando WebUI ya está ejecutándose
3. **Limpieza automática** - Solo detiene procesos que inició
4. **Monitoreo inteligente** - Solo monitorea procesos relevantes

**¡El sistema está listo para usar en cualquier escenario!**
