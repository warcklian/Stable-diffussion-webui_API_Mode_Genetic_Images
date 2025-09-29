# 🚀 COMANDOS RÁPIDOS - Sistema Genético

## 📋 **COMANDOS PRINCIPALES**

### **🚀 Iniciar WebUI Headless**
```bash
./run.sh
```
- **Función**: Inicia solo WebUI en modo headless (API)
- **Verifica**: Que no esté ya ejecutándose
- **Acceso**: http://localhost:7860 (API)
- **Mantiene**: WebUI ejecutándose en la terminal

### **🧬 Iniciar Sistema Genético**
```bash
./genetic.sh
```
- **Función**: Inicia solo el sistema genético (requiere WebUI ejecutándose)
- **Verifica**: Que WebUI esté disponible en puerto 7860
- **Acceso**: http://localhost:5000
- **🌐 Auto-abre**: Navegador automáticamente después de 3 segundos

### **🧬 Iniciar Sin Auto-abrir Navegador**
```bash
./genetic_no_browser.sh
```
- **Función**: Inicia sistema genético sin abrir navegador automáticamente
- **Verifica**: Que WebUI esté disponible en puerto 7860
- **Acceso**: http://localhost:5000 (manual)

### **🛑 Detener Sistema Genético**
```bash
./stop_genetic.sh
```
- **Función**: Detiene solo el sistema genético (WebUI sigue funcionando)
- **Verifica**: Que WebUI siga disponible
- **No afecta**: El WebUI headless

### **🛑 Detener WebUI**
```bash
./stop_webui.sh
```
- **Función**: Detiene solo WebUI (sistema genético sigue funcionando)
- **Verifica**: Que sistema genético siga disponible
- **No afecta**: El sistema genético

### **🚀 Iniciar Todo el Sistema**
```bash
./run.sh
```
- **Función**: Inicia WebUI + Sistema Genético
- **Primera vez**: Usar `./run_first_time.sh`
- **Acceso**: WebUI en 7860, Sistema en 5000

## 📊 **COMANDOS DE VERIFICACIÓN**

### **🔍 Verificar WebUI**
```bash
curl -s http://localhost:7860/sdapi/v1/options
```

### **🔍 Verificar Sistema Genético**
```bash
curl -s http://localhost:5000/api/status
```

### **🔍 Verificar Procesos**
```bash
ps aux | grep -E "(webui|genetic)"
```

## 🎯 **FLUJO DE TRABAJO RECOMENDADO**

### **1. Primera Instalación**
```bash
# Instalar y configurar todo
./run_first_time.sh
```

### **2. Uso Diario - Desarrollo Rápido**
```bash
# Terminal 1: Iniciar WebUI (una sola vez)
./run.sh

# Terminal 2: Iniciar sistema genético
./genetic.sh
```

### **3. Desarrollo/Pruebas**
```bash
# Detener solo sistema genético
./stop_genetic.sh

# Reiniciar solo sistema genético
./genetic.sh
```

### **4. Uso Completo**
```bash
# Todo en una terminal (menos eficiente para desarrollo)
./run_complete.sh
```

## 📱 **ACCESOS**

- **WebUI API**: http://localhost:7860
- **Sistema Genético**: http://localhost:5000

## 🔧 **COMANDOS DE EMERGENCIA**

### **🛑 Detener Todo**
```bash
pkill -f "webui"
pkill -f "genetic"
```

### **🔄 Reiniciar Todo**
```bash
./run.sh
```

### **🧹 Limpiar Procesos**
```bash
pkill -f "python.*web_interface"
pkill -f "webui"
```

## 💡 **CONSEJOS**

1. **WebUI independiente**: Puede ejecutarse por separado
2. **Sistema genético**: Requiere WebUI funcionando
3. **Puertos**: 7860 (WebUI), 5000 (Genético)
4. **Logs**: Revisar terminal para mensajes de estado
5. **Primera vez**: Usar `run_first_time.sh` para instalación completa

## 🎉 **RESULTADO**

**Comandos simples y rápidos para manejar el sistema genético de forma independiente, similar a `webui.sh`!**
