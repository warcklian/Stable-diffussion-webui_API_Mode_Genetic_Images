#!/bin/bash

# 🧬 Script para iniciar solo el Sistema Genético
# Usar cuando WebUI ya está ejecutándose

echo "🧬 Iniciando Solo Sistema Genético"
echo "=================================="

# Verificar que estamos en el directorio correcto
if [ ! -d "sistema_genetico" ]; then
    echo "❌ Error: Directorio sistema_genetico no encontrado"
    echo "   Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar que WebUI esté ejecutándose
echo "🔍 Verificando que WebUI esté ejecutándose..."
if ! curl -s http://localhost:7860/sdapi/v1/options > /dev/null 2>&1; then
    echo "❌ Error: WebUI no está ejecutándose en http://localhost:7860"
    echo "   Inicia WebUI primero con:"
    echo "   cd webui_standalone && ./webui.sh --api --listen"
    exit 1
fi

echo "✅ WebUI está ejecutándose correctamente"

# Función para limpiar al salir
cleanup() {
    echo ""
    echo "🛑 Deteniendo Sistema Genético..."
    if [ ! -z "$GENETIC_PID" ]; then
        echo "   Deteniendo Sistema Genético (PID: $GENETIC_PID)"
        kill $GENETIC_PID 2>/dev/null
    fi
    echo "✅ Sistema Genético detenido"
    exit 0
}

# Capturar señales para limpieza
trap cleanup SIGINT SIGTERM

# Iniciar Sistema Genético
echo "🧬 Iniciando Sistema Genético..."
cd sistema_genetico

# Verificar que el sistema genético esté configurado
if [ ! -f "interfaces/web_interface.py" ]; then
    echo "❌ Error: Sistema genético no configurado"
    echo "   Ejecuta setup_sistema_genetico.py primero"
    exit 1
fi

# Iniciar sistema genético
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
        kill $GENETIC_PID 2>/dev/null
        exit 1
    fi
    echo "   Esperando Sistema Genético... ($i/30)"
    sleep 2
done

cd ..

# Mostrar información del sistema
echo ""
echo "🎉 Sistema Genético iniciado exitosamente!"
echo "=========================================="
echo "📡 WebUI API: http://localhost:7860 (ya ejecutándose)"
echo "🧬 Sistema Genético: http://localhost:5000"
echo ""
echo "🔧 Controles:"
echo "   - Ctrl+C para detener el Sistema Genético"
echo "   - WebUI seguirá ejecutándose"
echo ""
echo "📱 Accede a la interfaz web en: http://localhost:5000"
echo ""

# Mantener el script corriendo y monitorear el proceso
while true; do
    # Verificar que Sistema Genético siga corriendo
    if ! kill -0 $GENETIC_PID 2>/dev/null; then
        echo "❌ Sistema Genético se detuvo inesperadamente"
        cleanup
    fi
    
    sleep 5
done
