#!/bin/bash

# 🚀 Script para primera instalación - Más tiempo para WebUI
# Usar solo la primera vez que se ejecuta el sistema

echo "🧬 Primera Instalación - Sistema de Generación Masiva Genética"
echo "=============================================================="
echo "⚠️  ADVERTENCIA: Primera instalación puede tardar 10-15 minutos"
echo "   WebUI instalará todas las dependencias necesarias"
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -d "webui_standalone" ]; then
    echo "❌ Error: Directorio webui_standalone no encontrado"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

if [ ! -d "sistema_genetico" ]; then
    echo "❌ Error: Directorio sistema_genetico no encontrado"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Función para limpiar procesos al salir
cleanup() {
    echo ""
    echo "🛑 Deteniendo sistema..."
    
    if [ ! -z "$WEBUI_PID" ]; then
        echo "   Deteniendo WebUI (PID: $WEBUI_PID)"
        kill $WEBUI_PID 2>/dev/null
    fi
    
    if [ ! -z "$GENETIC_PID" ]; then
        echo "   Deteniendo Sistema Genético (PID: $GENETIC_PID)"
        kill $GENETIC_PID 2>/dev/null
    fi
    echo "✅ Sistema detenido"
    exit 0
}

# Capturar señales para limpieza
trap cleanup SIGINT SIGTERM

# PASO 1: Iniciar WebUI (primera instalación)
echo "🚀 Paso 1: Iniciando WebUI (primera instalación)..."
cd webui_standalone

# Verificar que webui.sh existe
if [ ! -f "webui.sh" ]; then
    echo "❌ Error: webui.sh no encontrado en webui_standalone/"
    exit 1
fi

# Hacer webui.sh ejecutable
chmod +x webui.sh

# Iniciar WebUI en background con parámetros headless
echo "   Iniciando WebUI con parámetros: --api --listen"
echo "   ⏳ Esto puede tardar 10-15 minutos en la primera instalación..."
./webui.sh --api --listen --port 7860 --xformers &
WEBUI_PID=$!

echo "   WebUI iniciado con PID: $WEBUI_PID"
echo "   Esperando que WebUI esté disponible..."

# Esperar que WebUI esté disponible (mucho más tiempo para primera instalación)
cd ..
echo "   ⏳ Primera instalación en progreso..."
echo "   📦 Instalando PyTorch, dependencias y modelos..."
echo "   ⏰ Tiempo estimado: 10-15 minutos"

for i in {1..300}; do  # 10 minutos máximo
    if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
        echo "✅ WebUI disponible en http://localhost:7860"
        break
    fi
    if [ $i -eq 300 ]; then
        echo "❌ Error: WebUI no responde después de 10 minutos"
        echo "   Primera instalación puede tardar más tiempo"
        echo "   Puedes intentar ejecutar manualmente:"
        echo "   cd webui_standalone && ./webui.sh --api --listen --no-browser"
        kill $WEBUI_PID 2>/dev/null
        exit 1
    fi
    
    # Mostrar progreso cada 30 segundos
    if [ $((i % 15)) -eq 0 ]; then
        minutes=$((i / 30))
        echo "   ⏳ Instalación en progreso... ${minutes} minutos transcurridos"
    fi
    sleep 2
done

# PASO 2: Configurar sistema genético
echo ""
echo "⚙️ Paso 2: Configurando sistema genético..."

# Verificar si ya está configurado
if [ ! -f "sistema_genetico/interfaces/web_interface.py" ]; then
    echo "   Configurando sistema genético por primera vez..."
    python3 setup_sistema_genetico.py
    if [ $? -ne 0 ]; then
        echo "❌ Error configurando sistema genético"
        kill $WEBUI_PID 2>/dev/null
        exit 1
    fi
    echo "✅ Sistema genético configurado"
else
    echo "✅ Sistema genético ya está configurado"
fi

# PASO 3: Iniciar Sistema Genético
echo ""
echo "🧬 Paso 3: Iniciando Sistema Genético..."

# Iniciar sistema genético
cd sistema_genetico
python3 interfaces/web_interface.py &
GENETIC_PID=$!

echo "   Sistema Genético iniciado con PID: $GENETIC_PID"
echo "   Esperando que esté disponible..."

# Esperar que el sistema genético esté disponible
for i in {1..30}; do
    if curl -s http://localhost:5000/api/status > /dev/null 2>&1; then
        echo "✅ Sistema Genético disponible en http://localhost:5000"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "❌ Error: Sistema Genético no responde después de 1 minuto"
        kill $WEBUI_PID 2>/dev/null
        kill $GENETIC_PID 2>/dev/null
        exit 1
    fi
    echo "   Esperando Sistema Genético... ($i/30)"
    sleep 2
done

cd ..

# PASO 4: Mostrar información del sistema
echo ""
echo "🎉 Sistema iniciado exitosamente!"
echo "=================================="
echo "📡 WebUI API: http://localhost:7860"
echo "🧬 Sistema Genético: http://localhost:5000"
echo ""
echo "🔧 Controles:"
echo "   - Ctrl+C para detener todo el sistema"
echo "   - El sistema se detendrá automáticamente al cerrar esta terminal"
echo ""
echo "📱 Accede a la interfaz web en: http://localhost:5000"
echo ""
echo "💡 Para futuras ejecuciones, usa: ./run.sh"
echo ""

# Mantener el script corriendo y monitorear los procesos
while true; do
    # Verificar que WebUI siga corriendo
    if ! kill -0 $WEBUI_PID 2>/dev/null; then
        echo "❌ WebUI se detuvo inesperadamente"
        cleanup
    fi
    
    # Verificar que Sistema Genético siga corriendo
    if ! kill -0 $GENETIC_PID 2>/dev/null; then
        echo "❌ Sistema Genético se detuvo inesperadamente"
        cleanup
    fi
    
    sleep 5
done
