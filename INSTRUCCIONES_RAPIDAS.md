# 🚀 Instrucciones Rápidas - Sistema de Generación Masiva Genética

## ⚡ **INICIO RÁPIDO**

### **Primera Vez (Recomendado)**
```bash
# 1. Configurar sistema
python3 setup_sistema_genetico.py

# 2. Primera instalación (10-15 minutos)
./run_first_time.sh
```

### **Uso Normal**
```bash
# Sistema completo (WebUI + Sistema Genético)
./run.sh
```

### **WebUI ya ejecutándose**
```bash
# Solo sistema genético
./start_genetic_only.sh
```

## 📋 **SCRIPTS DISPONIBLES**

| Script | Descripción | Tiempo | Uso |
|--------|-------------|--------|-----|
| `run_first_time.sh` | Primera instalación | 10-15 min | ✅ **Recomendado primera vez** |
| `run.sh` | Sistema completo | 2-3 min | ✅ Uso normal |
| `start_genetic_only.sh` | Solo sistema genético | 30 seg | ✅ WebUI ya ejecutándose |
| `setup_sistema_genetico.py` | Configuración | 1-2 min | ✅ Primera vez |

## 🎯 **CASOS DE USO**

### **Caso 1: Primera vez usando el sistema**
```bash
# Configurar
python3 setup_sistema_genetico.py

# Primera instalación (paciente)
./run_first_time.sh
```

### **Caso 2: Uso normal**
```bash
# Sistema completo
./run.sh
```

### **Caso 3: WebUI ya ejecutándose**
```bash
# Solo sistema genético
./start_genetic_only.sh
```

### **Caso 4: Desarrollo**
```bash
# Terminal 1: WebUI
cd webui_standalone
./webui.sh --api --listen --no-browser --xformers

# Terminal 2: Sistema genético
./start_genetic_only.sh
```

## 🔧 **SOLUCIÓN DE PROBLEMAS**

### **Error: "WebUI no responde"**
```bash
# Primera instalación puede tardar mucho
./run_first_time.sh
```

### **Error: "Sistema genético no configurado"**
```bash
# Configurar sistema
python3 setup_sistema_genetico.py
```

### **Error: "Puerto 7860 en uso"**
```bash
# Verificar procesos
netstat -tulpn | grep 7860

# Matar proceso si es necesario
sudo kill -9 <PID>
```

### **Error: "Puerto 5000 en uso"**
```bash
# Verificar procesos
netstat -tulpn | grep 5000

# Matar proceso si es necesario
sudo kill -9 <PID>
```

## 📱 **ACCESOS**

- **WebUI API**: http://localhost:7860
- **Sistema Genético**: http://localhost:5000

## 🎉 **RESULTADO ESPERADO**

```
🎉 Sistema iniciado exitosamente!
==================================
📡 WebUI API: http://localhost:7860
🧬 Sistema Genético: http://localhost:5000

📱 Accede a la interfaz web en: http://localhost:5000
```

## 💡 **CONSEJOS**

1. **Primera vez**: Usa `run_first_time.sh` - es más paciente
2. **Uso normal**: Usa `run.sh` - es más rápido
3. **Desarrollo**: WebUI en una terminal, sistema genético en otra
4. **Producción**: `run.sh` con monitoreo automático

## 🚀 **¡LISTO PARA USAR!**

El sistema está completamente funcional y listo para generar imágenes tipo pasaporte con diversidad genética excepcional.
