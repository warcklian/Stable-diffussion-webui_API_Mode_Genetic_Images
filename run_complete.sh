#!/bin/bash

# 🧬 Sistema Completo - WebUI + Sistema Genético
# Script que inicia WebUI headless + Sistema Genético en una sola terminal

echo "🧬 Sistema Completo - WebUI + Sistema Genético"
echo "=============================================="

# Verificar que estamos en el directorio correcto
if [ ! -d "webui_standalone" ]; then
    echo "❌ Error: No se encuentra el directorio webui_standalone"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

if [ ! -d "sistema_genetico" ]; then
    echo "❌ Error: No se encuentra el directorio sistema_genetico"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar si WebUI ya está ejecutándose
echo "🔍 Verificando estado de WebUI..."

if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
    echo "✅ WebUI ya está ejecutándose en http://localhost:7860"
    echo "   Continuando con sistema genético..."
    WEBUI_PID=""
    WEBUI_ALREADY_RUNNING=true
else
    echo "🚀 WebUI no está ejecutándose, iniciando..."
    cd webui_standalone

    if [ ! -f "webui.sh" ]; then
        echo "❌ Error: webui.sh no encontrado en webui_standalone/"
        exit 1
    fi

    chmod +x webui.sh

    echo "   Iniciando WebUI con parámetros: --api --listen"
    ./webui.sh --api --listen --port 7860 --xformers &
    WEBUI_PID=$!
    WEBUI_ALREADY_RUNNING=false

    echo "   WebUI iniciado con PID: $WEBUI_PID"
    echo "   Esperando que WebUI esté disponible..."
    echo "   ⏳ Primera instalación puede tardar varios minutos..."
    cd ..
    for i in {1..120}; do
        if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
            echo "✅ WebUI disponible en http://localhost:7860"
            break
        fi
        if [ $i -eq 120 ]; then
            echo "❌ Error: WebUI no responde después de 4 minutos"
            echo "   Primera instalación puede tardar más tiempo"
            echo "   Verifica que no haya otro proceso usando el puerto 7860"
            kill $WEBUI_PID 2>/dev/null
            exit 1
        fi
        if [ $i -le 60 ]; then
            echo "   Esperando WebUI... ($i/120) - Instalando dependencias..."
        else
            echo "   Esperando WebUI... ($i/120) - Iniciando servicios..."
        fi
        sleep 2
    done
fi

# Iniciar Sistema Genético
echo ""
echo "🧬 Iniciando Sistema Genético..."

cd sistema_genetico

if [ ! -f "interfaces/web_interface.py" ]; then
    echo "❌ Error: interfaces/web_interface.py no encontrado"
    exit 1
fi

echo "🌐 Iniciando interfaz web en puerto 5000..."
echo "📱 Accede a: http://localhost:5000"
echo ""

# Función de limpieza
cleanup() {
    echo ""
    echo "🛑 Deteniendo sistema..."
    
    # Detener sistema genético
    pkill -f "python.*web_interface" 2>/dev/null
    
    # Solo detener WebUI si lo iniciamos nosotros
    if [ "$WEBUI_ALREADY_RUNNING" = "false" ] && [ ! -z "$WEBUI_PID" ]; then
        echo "🛑 Deteniendo WebUI..."
        kill $WEBUI_PID 2>/dev/null
        sleep 2
        pkill -f "webui" 2>/dev/null
    else
        echo "ℹ️  WebUI seguirá ejecutándose (no fue iniciado por este script)"
    fi
    
    echo "✅ Sistema detenido"
    exit 0
}

# Capturar señales para limpieza
trap cleanup SIGINT SIGTERM

# Iniciar sistema genético
python3 interfaces/web_interface.py
