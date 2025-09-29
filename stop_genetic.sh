#!/bin/bash

# 🛑 Detener Sistema Genético
# Script para detener solo el sistema genético sin afectar WebUI

echo "🛑 Deteniendo Sistema Genético..."

# Detener procesos de web_interface
pkill -f "python.*web_interface"

# Verificar que se detuvo
sleep 2
if pgrep -f "python.*web_interface" > /dev/null; then
    echo "⚠️  Algunos procesos pueden seguir ejecutándose"
    echo "   Usa: pkill -f 'python.*web_interface' para forzar"
else
    echo "✅ Sistema Genético detenido"
fi

# Verificar que WebUI sigue funcionando
if curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
    echo "✅ WebUI sigue funcionando en http://localhost:7860"
else
    echo "❌ WebUI no está disponible"
fi

echo ""
echo "💡 Para reiniciar el sistema genético: ./genetic.sh"
