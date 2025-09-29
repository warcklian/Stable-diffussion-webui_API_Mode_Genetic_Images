#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Gestión de Archivos para Generación Genética
Basado en la estructura del proyecto anterior
"""

import os
import json
import csv
import time
import subprocess
import platform
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import logging

class FileManager:
    """Gestor de archivos para el sistema genético independiente"""
    
    def __init__(self, base_dir: str = None):
        """
        Inicializar gestor de archivos
        
        Args:
            base_dir: Directorio base del proyecto (por defecto: directorio actual)
        """
        self.logger = logging.getLogger(__name__)
        
        # Directorio base del proyecto
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent
        self.base_dir = Path(base_dir)
        
        # Directorio de salida del sistema genético
        self.outputs_dir = self.base_dir / "outputs"
        self.outputs_dir.mkdir(exist_ok=True)
        
        self.logger.info(f"FileManager inicializado en: {self.base_dir}")
        self.logger.info(f"Directorio de salida: {self.outputs_dir}")
    
    def create_output_structure(self, model_name: str, generation_type: str, 
                              nacionalidad: str = None, genero: str = None) -> Path:
        """
        Crear estructura de directorios de salida
        
        Args:
            model_name: Nombre del modelo
            generation_type: Tipo de generación (genetico_premium, masivo_premium, etc.)
            nacionalidad: Nacionalidad (opcional)
            genero: Género (opcional)
            
        Returns:
            Path: Directorio de salida creado
        """
        try:
            # Limpiar nombre del modelo
            model_name_clean = self._clean_filename(model_name)
            
            # Crear directorio del modelo
            model_dir = self.outputs_dir / model_name_clean
            model_dir.mkdir(exist_ok=True)
            
            # Crear directorio con timestamp y parámetros (todos los archivos juntos)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if nacionalidad and genero:
                batch_name = f"{generation_type}_{nacionalidad}_{genero}_{timestamp}"
            else:
                batch_name = f"{generation_type}_{timestamp}"
            
            batch_dir = model_dir / batch_name
            batch_dir.mkdir(exist_ok=True)
            
            # No crear subdirectorios innecesarios
            
            self.logger.info(f"Estructura creada: {batch_dir}")
            return batch_dir
            
        except Exception as e:
            self.logger.error(f"Error creando estructura: {e}")
            raise
    
    def save_image(self, image_data: bytes, output_dir: Path, filename: str, 
                  metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Guardar imagen generada
        
        Args:
            image_data: Datos de la imagen (bytes)
            output_dir: Directorio de salida
            filename: Nombre del archivo
            metadata: Metadatos adicionales
            
        Returns:
            Dict: Resultado de la operación
        """
        try:
            # Limpiar nombre del archivo
            clean_filename = self._clean_filename(filename)
            if not clean_filename.endswith(('.png', '.jpg', '.jpeg')):
                clean_filename += '.png'
            
            # Crear ruta completa del archivo (directamente en la carpeta principal)
            file_path = output_dir / clean_filename
            
            # Guardar imagen
            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            # Guardar metadatos JSON en la misma carpeta si se proporcionan
            if metadata:
                json_filename = clean_filename.replace('.png', '.json')
                json_path = output_dir / json_filename
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            return {
                'success': True,
                'file_path': str(file_path),
                'file_size': file_path.stat().st_size
            }
            
        except Exception as e:
            self.logger.error(f"Error guardando imagen: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def save_json_metadata(self, output_dir: Path, filename: str, 
                         metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Guardar metadatos en formato JSON
        
        Args:
            output_dir: Directorio de salida
            filename: Nombre del archivo
            metadata: Metadatos a guardar
            
        Returns:
            Dict: Resultado de la operación
        """
        try:
            # Crear directorio de metadatos si no existe
            metadata_dir = output_dir / "metadata"
            metadata_dir.mkdir(exist_ok=True)
            
            # Limpiar nombre del archivo
            clean_filename = self._clean_filename(filename)
            if not clean_filename.endswith('.json'):
                clean_filename += '.json'
            
            # Crear ruta completa del archivo
            file_path = metadata_dir / clean_filename
            
            # Guardar JSON
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            
            return {
                'success': True,
                'file_path': str(file_path)
            }
            
        except Exception as e:
            self.logger.error(f"Error guardando JSON: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def save_csv_analysis(self, output_dir: Path, filename: str, 
                         data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Guardar análisis en formato CSV
        
        Args:
            output_dir: Directorio de salida
            filename: Nombre del archivo
            data: Datos a guardar
            
        Returns:
            Dict: Resultado de la operación
        """
        try:
            # Crear directorio de metadatos si no existe
            metadata_dir = output_dir / "metadata"
            metadata_dir.mkdir(exist_ok=True)
            
            # Limpiar nombre del archivo
            clean_filename = self._clean_filename(filename)
            if not clean_filename.endswith('.csv'):
                clean_filename += '.csv'
            
            # Crear ruta completa del archivo
            file_path = metadata_dir / clean_filename
            
            # Guardar CSV
            if data:
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
            
            return {
                'success': True,
                'file_path': str(file_path)
            }
            
        except Exception as e:
            self.logger.error(f"Error guardando CSV: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def save_csv_analysis(self, output_dir: Path, filename: str, data: List[Dict[str, Any]]) -> dict:
        """Guarda análisis de diversidad en un archivo CSV en la carpeta principal."""
        try:
            import csv
            csv_path = output_dir / filename
            
            if not data:
                return {'success': False, 'error': 'No hay datos para guardar en CSV'}
            
            # Obtener las claves del primer elemento para las columnas
            fieldnames = list(data[0].keys())
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            self.logger.info(f"Análisis CSV guardado: {csv_path}")
            return {'success': True, 'file_path': str(csv_path)}
            
        except Exception as e:
            self.logger.error(f"Error guardando análisis CSV {filename}: {e}")
            return {'success': False, 'error': str(e)}
    
    def get_output_folder_path(self) -> str:
        """
        Obtener ruta del directorio de salida
        
        Returns:
            str: Ruta absoluta del directorio de salida
        """
        return str(self.outputs_dir.absolute())
    
    def open_output_folder(self) -> Dict[str, Any]:
        """
        Abrir carpeta de salida en el explorador del sistema
        
        Returns:
            Dict: Resultado de la operación
        """
        try:
            # Asegurar que la carpeta outputs existe
            self.outputs_dir.mkdir(parents=True, exist_ok=True)
            folder_path = str(self.outputs_dir.absolute())
            
            # Determinar comando según el sistema operativo
            system = platform.system()
            if system == "Windows":
                os.startfile(folder_path)
            elif system == "Darwin":  # macOS
                subprocess.run(["open", folder_path])
            else:  # Linux y otros
                subprocess.run(["xdg-open", folder_path])
            
            self.logger.info(f"Carpeta abierta: {folder_path}")
            return {
                'success': True,
                'folder_path': folder_path
            }
            
        except Exception as e:
            self.logger.error(f"Error abriendo carpeta: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def list_generated_files(self) -> List[Dict[str, Any]]:
        """
        Listar archivos generados
        
        Returns:
            List[Dict]: Lista de archivos generados
        """
        try:
            files = []
            
            # Recorrer estructura de directorios
            for model_dir in self.outputs_dir.iterdir():
                if model_dir.is_dir():
                    for generation_dir in model_dir.iterdir():
                        if generation_dir.is_dir():
                            for batch_dir in generation_dir.iterdir():
                                if batch_dir.is_dir():
                                    # Buscar archivos en subdirectorios
                                    for subdir in ["images", "metadata"]:
                                        subdir_path = batch_dir / subdir
                                        if subdir_path.exists():
                                            for file_path in subdir_path.iterdir():
                                                if file_path.is_file():
                                                    files.append({
                                                        'name': file_path.name,
                                                        'path': str(file_path),
                                                        'size': file_path.stat().st_size,
                                                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
                                                        'type': subdir,
                                                        'model': model_dir.name,
                                                        'generation': generation_dir.name,
                                                        'batch': batch_dir.name
                                                    })
            
            # Ordenar por fecha de modificación (más recientes primero)
            files.sort(key=lambda x: x['modified'], reverse=True)
            
            return files
            
        except Exception as e:
            self.logger.error(f"Error listando archivos: {e}")
            return []
    
    def _clean_filename(self, filename: str) -> str:
        """
        Limpiar nombre de archivo para que sea seguro
        
        Args:
            filename: Nombre original
            
        Returns:
            str: Nombre limpio
        """
        # Caracteres no permitidos
        invalid_chars = '<>:"/\\|?*'
        
        # Reemplazar caracteres no válidos
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        
        # Limitar longitud
        if len(filename) > 200:
            filename = filename[:200]
        
        return filename.strip()
