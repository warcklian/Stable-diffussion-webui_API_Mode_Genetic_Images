#!/bin/bash

# 🛑 Detener WebUI
# Script para detener solo WebUI sin afectar el sistema genético

echo "🛑 Deteniendo WebUI..."

# Detener procesos de WebUI
pkill -f "webui"

# Verificar que se detuvo
sleep 2
if pgrep -f "webui" > /dev/null; then
    echo "⚠️  Algunos procesos de WebUI pueden seguir ejecutándose"
    echo "   Usa: pkill -f webui para forzar"
else
    echo "✅ WebUI detenido"
fi

# Verificar que el sistema genético sigue funcionando
if curl -s http://localhost:5000/api/status > /dev/null 2>&1; then
    echo "✅ Sistema Genético sigue funcionando en http://localhost:5000"
else
    echo "❌ Sistema Genético no está disponible"
fi

echo ""
echo "💡 Para reiniciar WebUI: ./run.sh"
echo "💡 Para detener sistema genético: ./stop_genetic.sh"
