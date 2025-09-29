#!/bin/bash

# 🚀 WebUI Headless - Solo WebUI
# Script que inicia únicamente WebUI en modo headless

echo "🚀 WebUI Headless - Modo API"
echo "============================"

# Verificar que estamos en el directorio correcto
if [ ! -d "webui_standalone" ]; then
    echo "❌ Error: No se encuentra el directorio webui_standalone"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar si WebUI ya está ejecutándose
echo "🔍 Verificando estado de WebUI..."

if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
    echo "✅ WebUI ya está ejecutándose en http://localhost:7860"
    echo "   Para usar el sistema genético, ejecuta: ./genetic.sh"
    echo "   Para detener WebUI: pkill -f webui"
    exit 0
fi

echo "🚀 Iniciando WebUI en modo headless..."

cd webui_standalone

if [ ! -f "webui.sh" ]; then
    echo "❌ Error: webui.sh no encontrado en webui_standalone/"
    exit 1
fi

chmod +x webui.sh

echo "   Iniciando WebUI con parámetros: --api --listen"
echo "   ⏳ Primera instalación puede tardar varios minutos..."
echo ""

# Iniciar WebUI en background
./webui.sh --api --listen --port 7860 --xformers &
WEBUI_PID=$!

echo "   WebUI iniciado con PID: $WEBUI_PID"
echo "   Esperando que WebUI esté disponible..."

# Esperar a que WebUI esté disponible
for i in {1..120}; do
    if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
        echo "✅ WebUI disponible en http://localhost:7860"
        echo ""
        echo "🎉 WebUI ejecutándose en modo headless"
        echo "📱 Para usar el sistema genético: ./genetic.sh"
        echo "🛑 Para detener WebUI: pkill -f webui"
        echo ""
        echo "💡 WebUI seguirá ejecutándose en esta terminal"
        echo "   Usa Ctrl+C para detener WebUI"
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

# Función de limpieza
cleanup() {
    echo ""
    echo "🛑 Deteniendo WebUI..."
    kill $WEBUI_PID 2>/dev/null
    sleep 2
    pkill -f "webui" 2>/dev/null
    echo "✅ WebUI detenido"
    exit 0
}

# Capturar señales para limpieza
trap cleanup SIGINT SIGTERM

# Mantener el script ejecutándose para que WebUI siga funcionando
echo "🔄 WebUI ejecutándose... (Ctrl+C para detener)"
wait $WEBUI_PID