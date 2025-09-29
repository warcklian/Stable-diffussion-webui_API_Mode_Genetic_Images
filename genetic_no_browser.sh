#!/bin/bash

# 🧬 Sistema de Generación Masiva Genética (Sin Auto-abrir Navegador)
# Script de inicio rápido para el sistema genético independiente

echo "🧬 Sistema de Generación Masiva Genética"
echo "========================================"

# Verificar que estamos en el directorio correcto
if [ ! -d "sistema_genetico" ]; then
    echo "❌ Error: No se encuentra el directorio sistema_genetico"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar que WebUI esté ejecutándose
echo "🔍 Verificando que WebUI esté ejecutándose..."
if ! curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
    echo "❌ Error: WebUI no está ejecutándose en http://localhost:7860"
    echo "   Inicia WebUI primero con:"
    echo "   cd webui_standalone && ./webui.sh --api --listen"
    echo "   O ejecuta: ./run.sh"
    exit 1
fi

echo "✅ WebUI disponible en http://localhost:7860"

# Cambiar al directorio del sistema genético
cd sistema_genetico

# Verificar que el archivo de interfaz web existe
if [ ! -f "interfaces/web_interface.py" ]; then
    echo "❌ Error: interfaces/web_interface.py no encontrado"
    exit 1
fi

# Iniciar el sistema genético
echo "🚀 Iniciando Sistema Genético..."
echo "📱 Accede a: http://localhost:5000"
echo ""
echo "💡 Para detener el sistema: Ctrl+C"
echo ""

python3 interfaces/web_interface.py
