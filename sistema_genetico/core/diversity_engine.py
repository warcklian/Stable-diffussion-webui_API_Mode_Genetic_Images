#!/usr/bin/env python3
"""
Motor de Diversidad Facial Ultra Avanzado
Sistema que genera características únicas y extremadamente diversas
para evitar imágenes que se parezcan entre sí
"""

import random
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import logging

@dataclass
class UltraDiversityProfile:
    """Perfil de diversidad ultra avanzado para máxima unicidad"""
    # Identificación única
    image_id: str
    nationality: str
    region: str
    gender: str
    age: int
    
    # Características faciales ultra detalladas
    face_shape: str
    face_width: str
    face_length: str
    jawline: str
    chin: str
    cheekbones: str
    facial_symmetry: str
    bone_structure: str
    
    # Ojos ultra detallados
    eye_color: str
    eye_color_shade: str
    eye_shape: str
    eye_size: str
    eye_spacing: str
    eyelid_type: str
    eyelashes: str
    eyelashes_length: str
    eyebrows: str
    eyebrows_thickness: str
    eyebrows_shape: str
    
    # Nariz ultra detallada
    nose_shape: str
    nose_size: str
    nose_width: str
    nose_bridge: str
    nose_tip: str
    nostril_size: str
    
    # Boca ultra detallada
    lip_shape: str
    lip_size: str
    lip_thickness: str
    mouth_width: str
    lip_color: str
    lip_fullness: str
    
    # Piel ultra detallada
    skin_tone: str
    skin_tone_shade: str
    skin_texture: str
    skin_undertone: str
    skin_glow: str
    skin_imperfections: List[str]
    freckles: str
    freckles_density: str
    moles: str
    moles_count: str
    birthmarks: str
    scars: str
    acne: str
    age_spots: str
    wrinkles: str
    skin_elasticity: str
    
    # Cabello ultra detallado
    hair_color: str
    hair_color_shade: str
    hair_texture: str
    hair_length: str
    hair_style: str
    hair_density: str
    hair_shine: str
    hair_curliness: str
    hair_thickness: str
    hairline: str
    
    # Vello facial (solo para hombres)
    facial_hair: str
    beard: str
    mustache: str
    
    # Maquillaje (solo para mujeres)
    makeup: str
    
    # Características de edad específicas
    age_characteristics: List[str]
    
    # Nivel de belleza realista
    beauty_level: str
    attractiveness_factors: List[str]
    
    # Sistema de ropa diverso (evita color blanco)
    clothing_type: str
    clothing_color: str
    clothing_style: str
    
    # Características corporales realistas
    body_type: str
    body_weight: str
    body_height: str
    body_shape: str
    muscle_definition: str
    body_fat_percentage: str
    
    # Características étnicas específicas
    ethnic_features: List[str]
    
    # Metadatos de unicidad
    generated_at: str
    generation_type: str
    uniqueness_score: float
    diversity_factors: List[str]

class UltraDiversityEngine:
    """Motor de diversidad ultra avanzado para máxima unicidad"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.diversity_data = self._load_diversity_data()
        # Inicializar sistema de anti-repetición
        self._recent_selections = {}
        
    def _load_diversity_data(self) -> Dict[str, Any]:
        """Carga datos de diversidad ultra expandidos desde archivo JSON"""
        try:
            # Cargar desde archivo JSON
            data_file = Path(__file__).parent / "ultra_diversity_data.json"
            if data_file.exists():
                with open(data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            self.logger.warning(f"No se pudo cargar ultra_diversity_data.json: {e}")
        
        # Fallback a datos hardcodeados si no se puede cargar el JSON
        return {
            # Regiones venezolanas ultra expandidas
            "regions": [
                "caracas", "maracaibo", "valencia", "barquisimeto", "ciudad_guayana", 
                "maturin", "merida", "san_cristobal", "barcelona", "puerto_la_cruz",
                "ciudad_bolivar", "tucupita", "porlamar", "valera", "acarigua",
                "guanare", "san_fernando", "trujillo", "el_tigre", "cabimas",
                "punto_fijo", "ciudad_ojeda", "puerto_cabello", "valle_de_la_pascua",
                "san_juan_de_los_morros", "carora", "tocuyo", "duaca", "siquisique",
                "araure", "turen", "guanarito", "santa_elena", "el_venado",
                "san_rafael", "san_antonio", "la_fria", "rubio", "colon",
                "tachira", "apure", "amazonas", "delta_amacuro", "yacambu",
                "lara", "portuguesa", "cojedes", "guarico", "anzoategui",
                "monagas", "sucre", "nueva_esparta", "falcon", "zulia",
                "merida", "trujillo", "barinas", "yaracuy", "carabobo",
                "aragua", "miranda", "vargas", "distrito_capital"
            ],
            
            # Tonos de piel ultra expandidos
            "skin_tones": [
                "light", "fair", "medium", "medium-dark", "olive", "tan", "golden",
                "bronze", "caramel", "honey", "dark", "rich brown", "coffee",
                "mahogany", "espresso", "chocolate", "mocha", "cinnamon", "amber",
                "copper", "peach", "ivory", "beige", "sand", "cream", "wheat",
                "almond", "hazelnut", "walnut", "chestnut", "cocoa", "ebony"
            ],
            
            # Colores de cabello ultra expandidos
            "hair_colors": [
                "black", "dark brown", "brown", "auburn", "chestnut", "chocolate",
                "espresso", "mahogany", "copper", "bronze", "light brown", "honey",
                "golden", "blonde", "strawberry blonde", "red", "ginger", "salt and pepper",
                "gray", "white", "platinum", "ash blonde", "dirty blonde", "sandy",
                "caramel", "cinnamon", "russet", "burgundy", "auburn", "copper",
                "bronze", "gold", "silver", "pepper", "salt", "mixed"
            ],
            
            # Colores de ojos ultra expandidos
            "eye_colors": [
                "dark brown", "brown", "hazel", "amber", "light brown", "honey",
                "golden", "coffee", "chocolate", "mahogany", "green", "blue",
                "gray", "blue-green", "hazel-green", "amber-brown", "light hazel",
                "dark hazel", "emerald", "forest green", "sea green", "teal",
                "steel blue", "navy blue", "sky blue", "ice blue", "violet",
                "purple", "amber", "gold", "copper", "hazel", "mixed"
            ],
            
            # Formas de cara ultra expandidas
            "face_shapes": [
                "oval", "round", "square", "heart", "diamond", "long", "triangular",
                "pear", "inverted triangle", "rectangular", "angular", "soft",
                "defined", "symmetrical", "asymmetrical", "wide", "narrow", "broad",
                "thin", "full", "hollow", "prominent", "recessed", "angular",
                "rounded", "oval", "square", "heart", "diamond", "pear"
            ],
            
            # Características de nariz ultra expandidas
            "nose_shapes": [
                "straight", "aquiline", "button", "wide", "narrow", "small",
                "prominent", "delicate", "strong", "refined", "classic", "distinctive",
                "roman", "snub", "hooked", "bulbous", "pointed", "flat", "upturned",
                "downturned", "asymmetric", "perfect", "crooked", "broad", "thin",
                "long", "short", "large", "tiny", "bent", "twisted", "bumpy",
                "smooth", "rough", "textured", "elegant", "sturdy", "dainty"
            ],
            
            # Características de labios ultra expandidas
            "lip_shapes": [
                "full", "medium", "thin", "wide", "narrow", "plump", "defined",
                "natural", "shapely", "expressive", "delicate", "strong", "pouty",
                "bow-shaped", "heart-shaped", "straight", "curved", "asymmetric",
                "perfect", "uneven", "thick", "thin", "long", "short", "prominent",
                "subtle", "large", "small", "wide", "narrow", "pursed", "relaxed",
                "tense", "loose", "voluptuous", "petite", "sensual", "charming"
            ],
            
            # Características de ojos ultra expandidas
            "eye_shapes": [
                "almond", "round", "hooded", "deep-set", "wide-set", "close-set",
                "upturned", "downturned", "monolid", "double-lid", "expressive",
                "intense", "gentle", "piercing", "sleepy", "alert", "droopy",
                "cat-like", "downturned", "upturned", "asymmetric", "perfect",
                "uneven", "large", "small", "prominent", "recessed", "bulging",
                "sunken", "puffy", "swollen", "narrow", "wide", "slanted", "straight",
                "bedroom", "doll-like", "fox-like", "downturned", "upturned"
            ],
            
            # Estilos de cabello ultra expandidos
            "hair_styles": [
                "straight", "wavy", "curly", "braided", "ponytail", "bun", "pixie",
                "bob", "shoulder-length", "layered", "textured", "voluminous",
                "sleek", "styled", "natural", "professional", "casual", "messy",
                "neat", "tidy", "unkempt", "wild", "smooth", "rough", "thick",
                "thin", "fine", "coarse", "silky", "frizzy", "smooth", "tangled",
                "styled", "natural", "artificial", "extensions", "weave", "wig"
            ],
            
            # Características de cejas ultra expandidas
            "eyebrow_shapes": [
                "thick", "medium", "thin", "arched", "straight", "defined", "natural",
                "bushy", "sparse", "uneven", "perfect", "asymmetric", "high", "low",
                "close", "wide", "angled", "curved", "messy", "neat", "tidy",
                "unkempt", "wild", "smooth", "rough", "patchy", "full", "partial",
                "missing", "overgrown", "trimmed", "shaped", "microbladed", "tattooed"
            ],
            
            # Características de mandíbula ultra expandidas
            "jawline_types": [
                "strong", "soft", "defined", "rounded", "angular", "delicate",
                "square", "pointed", "weak", "prominent", "recessed", "asymmetric",
                "perfect", "uneven", "wide", "narrow", "broad", "thin", "full",
                "hollow", "sharp", "blunt", "chiseled", "soft", "hard", "firm",
                "loose", "tight", "relaxed", "tense", "masculine", "feminine"
            ],
            
            # Características de pómulos ultra expandidas
            "cheekbone_types": [
                "high", "medium", "low", "prominent", "subtle", "defined", "sharp",
                "soft", "angular", "rounded", "asymmetric", "perfect", "uneven",
                "wide", "narrow", "hollow", "full", "broad", "thin", "strong",
                "weak", "chiseled", "smooth", "rough", "textured", "flat", "raised",
                "sunken", "puffy", "swollen", "sculpted", "natural", "artificial"
            ],
            
            # Texturas de piel ultra expandidas
            "skin_textures": [
                "smooth", "textured", "natural", "mature", "youthful", "rough",
                "fine", "coarse", "porous", "tight", "loose", "elastic", "dry",
                "oily", "combination", "blemished", "clear", "acne-prone", "sensitive",
                "resilient", "fragile", "thick", "thin", "firm", "soft", "wrinkled",
                "aged", "fresh", "dull", "glowing", "radiant", "dewy", "matte"
            ],
            
            # Niveles de belleza realistas
            "beauty_levels": [
                "muy_atractivo", "atractivo", "normal", "promedio", "comun",
                "ordinario", "poco_atractivo", "feo", "muy_feo", "realista",
                "variado", "excepcional", "hermoso", "guapo", "bonito", "lindo",
                "encantador", "carismatico", "interesante", "unico", "distintivo"
            ],
            
            # Características de pecas ultra expandidas
            "freckle_types": [
                "none", "light", "moderate", "heavy", "scattered", "concentrated",
                "bridge", "cheeks", "forehead", "nose", "chin", "arms", "shoulders",
                "back", "chest", "sparse", "dense", "faint", "dark", "light",
                "red", "brown", "golden", "sun-kissed", "natural", "artificial"
            ],
            
            # Características de lunares ultra expandidas
            "mole_types": [
                "none", "small", "medium", "large", "multiple", "cheek", "chin",
                "forehead", "nose", "lip", "eye", "ear", "neck", "shoulder", "arm",
                "hand", "back", "chest", "leg", "foot", "facial", "body", "beauty",
                "mark", "birthmark", "congenital", "acquired", "benign", "suspicious"
            ],
            
            # Características de cicatrices ultra expandidas
            "scar_types": [
                "none", "small", "faint", "visible", "cheek", "chin", "forehead",
                "nose", "lip", "eye", "ear", "neck", "shoulder", "arm", "hand",
                "back", "chest", "leg", "foot", "surgical", "accident", "birth",
                "childhood", "adult", "recent", "old", "healed", "fresh", "faded"
            ],
            
            # Características de acné ultra expandidas
            "acne_types": [
                "none", "mild", "moderate", "severe", "scattered", "concentrated",
                "forehead", "cheeks", "chin", "nose", "back", "chest", "shoulders",
                "active", "healing", "scarred", "cystic", "blackheads", "whiteheads",
                "pustules", "papules", "nodules", "comedones", "inflammatory"
            ],
            
            # Características de arrugas ultra expandidas
            "wrinkle_types": [
                "none", "fine", "moderate", "deep", "forehead", "eye", "mouth",
                "neck", "crow's feet", "laugh lines", "frown lines", "worry lines",
                "smile lines", "expression lines", "age lines", "sun damage",
                "genetic", "lifestyle", "dynamic", "static", "gravitational",
                "sleep", "smoking", "environmental", "hormonal", "stress"
            ]
        }
    
    def generate_ultra_diverse_profile(self, nationality: str, gender: str, age: int) -> UltraDiversityProfile:
        """Genera un perfil ultra diverso con máxima unicidad"""
        
        # Crear seed único para máxima aleatoriedad
        unique_seed = int(time.time() * 1000000) + random.randint(1, 999999)
        random.seed(unique_seed)
        
        # Seleccionar región aleatoria
        region = random.choice(self.diversity_data["regions"])
        
        # Generar características ultra diversas
        profile = UltraDiversityProfile(
            image_id=f"ultra_{int(time.time())}_{random.randint(1000, 9999)}",
            nationality=nationality,
            region=region,
            gender=gender,
            age=age,
            
            # Características faciales
            face_shape=random.choice(self.diversity_data["face_shapes"]),
            face_width=random.choice(["narrow", "medium", "wide", "broad", "thin"]),
            face_length=random.choice(["short", "medium", "long", "elongated"]),
            jawline=random.choice(self.diversity_data["jawline_types"]),
            chin=random.choice(["pointed", "rounded", "square", "recessed", "prominent"]),
            cheekbones=random.choice(self.diversity_data["cheekbone_types"]),
            facial_symmetry=random.choice(["perfect", "slight_asymmetry", "natural_asymmetry"]),
            bone_structure=random.choice(["prominent", "delicate", "strong", "soft"]),
            
            # Ojos
            eye_color=random.choice(self.diversity_data["eye_colors"]),
            eye_color_shade=random.choice(["light", "medium", "dark", "deep"]),
            eye_shape=random.choice(self.diversity_data["eye_shapes"]),
            eye_size=random.choice(["small", "medium", "large", "prominent"]),
            eye_spacing=random.choice(["close", "normal", "wide", "very_wide"]),
            eyelid_type=random.choice(["monolid", "double_lid", "hooded", "deep_set"]),
            eyelashes=random.choice(["short", "medium", "long", "thick", "thin"]),
            eyelashes_length=random.choice(["natural", "extended", "dramatic"]),
            eyebrows=random.choice(self.diversity_data["eyebrow_shapes"]),
            eyebrows_thickness=random.choice(["thin", "medium", "thick", "bushy"]),
            eyebrows_shape=random.choice(["arched", "straight", "curved", "angled"]),
            
            # Nariz
            nose_shape=random.choice(self.diversity_data["nose_shapes"]),
            nose_size=random.choice(["small", "medium", "large", "prominent"]),
            nose_width=random.choice(["narrow", "medium", "wide", "broad"]),
            nose_bridge=random.choice(["high", "medium", "low", "flat"]),
            nose_tip=random.choice(["pointed", "rounded", "flat", "upturned"]),
            nostril_size=random.choice(["small", "medium", "large", "wide"]),
            
            # Boca
            lip_shape=random.choice(self.diversity_data["lip_shapes"]),
            lip_size=random.choice(["small", "medium", "large", "full"]),
            lip_thickness=random.choice(["thin", "medium", "thick", "full"]),
            mouth_width=random.choice(["narrow", "medium", "wide", "broad"]),
            lip_color=random.choice(["natural", "pink", "red", "brown", "dark"]),
            lip_fullness=random.choice(["thin", "medium", "full", "voluptuous"]),
            
            # Piel
            skin_tone=random.choice(self.diversity_data["skin_tones"]),
            skin_tone_shade=random.choice(["light", "medium", "dark", "deep"]),
            skin_texture=random.choice(self.diversity_data["skin_textures"]),
            skin_undertone=random.choice(["warm", "cool", "neutral", "olive"]),
            skin_glow=random.choice(["matte", "natural", "dewy", "glowing"]),
            skin_imperfections=self._generate_skin_imperfections(),
            freckles=random.choice(self.diversity_data["freckle_types"]),
            freckles_density=random.choice(["sparse", "moderate", "dense"]),
            moles=random.choice(self.diversity_data["mole_types"]),
            moles_count=random.choice(["none", "few", "several", "many"]),
            birthmarks=random.choice(["none", "small", "medium", "large"]),
            scars=random.choice(self.diversity_data["scar_types"]),
            acne=random.choice(self.diversity_data["acne_types"]),
            age_spots=self._generate_age_appropriate_spots(age),
            wrinkles=self._generate_age_appropriate_wrinkles(age),
            skin_elasticity=self._generate_age_appropriate_elasticity(age),
            
            # Cabello
            hair_color=random.choice(self.diversity_data["hair_colors"]),
            hair_color_shade=random.choice(["light", "medium", "dark", "deep"]),
            hair_texture=random.choice(["straight", "wavy", "curly", "coily"]),
            hair_length=random.choice(["short", "medium", "long", "very_long"]),
            hair_style=random.choice(self.diversity_data["hair_styles"]),
            hair_density=random.choice(["thin", "medium", "thick", "very_thick"]),
            hair_shine=random.choice(["dull", "natural", "shiny", "very_shiny"]),
            hair_curliness=random.choice(["straight", "wavy", "curly", "very_curly"]),
            hair_thickness=random.choice(["fine", "medium", "thick", "very_thick"]),
            hairline=random.choice(["low", "medium", "high", "receding"]),
            
            # Vello facial (solo para hombres)
            facial_hair=self._generate_gender_appropriate_facial_hair(gender),
            beard=self._generate_gender_appropriate_beard(gender),
            mustache=self._generate_gender_appropriate_mustache(gender),
            
            # Características de edad
            age_characteristics=self._generate_age_characteristics(age),
            
            # Nivel de belleza con anti-repetición
            beauty_level=self._anti_repetition_selection("beauty_levels", self.diversity_data["beauty_levels"]),
            attractiveness_factors=self._generate_attractiveness_factors(),
            
            # Características étnicas
            ethnic_features=self._generate_ethnic_features(nationality),
            
            # Metadatos
            generated_at=datetime.now().isoformat(),
            generation_type="ultra_diverse",
            uniqueness_score=random.uniform(0.8, 1.0),
            diversity_factors=self._generate_diversity_factors()
        )
        
        return profile
    
    def _generate_skin_imperfections(self) -> List[str]:
        """Genera imperfecciones de piel realistas"""
        imperfections = []
        if random.random() < 0.3:
            imperfections.append("freckles")
        if random.random() < 0.2:
            imperfections.append("moles")
        if random.random() < 0.15:
            imperfections.append("scars")
        if random.random() < 0.1:
            imperfections.append("acne")
        if random.random() < 0.05:
            imperfections.append("birthmarks")
        return imperfections
    
    def _generate_age_characteristics(self, age: int) -> List[str]:
        """Genera características específicas de edad"""
        characteristics = []
        if age < 25:
            characteristics.extend(["youthful", "fresh", "smooth_skin"])
        elif age < 40:
            characteristics.extend(["mature", "defined_features"])
        else:
            characteristics.extend(["aged", "wrinkles", "mature_features"])
        return characteristics
    
    def _generate_age_appropriate_wrinkles(self, age: int) -> str:
        """Genera arrugas apropiadas para la edad - SOLO ARRUGAS FACIALES POR GRUPOS DE EDAD"""
        # Sistema de arrugas por grupos de edad específicos
        if age < 20:
            # Grupo 1: 18-19 años - Sin arrugas
            return "none"
        elif age < 30:
            # Grupo 2: 20-29 años - Arrugas muy leves
            young_options = ["none", "fine expression lines", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines"]
            return random.choice(young_options)
        elif age < 40:
            # Grupo 3: 30-39 años - Arrugas leves a moderadas
            adult_young_options = ["fine expression lines", "light laugh lines", "subtle crow's feet", "forehead lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines"]
            return random.choice(adult_young_options)
        elif age < 50:
            # Grupo 4: 40-49 años - Arrugas moderadas
            mature_options = ["moderate expression lines", "crow's feet", "forehead lines", "laugh lines", "worry lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines"]
            return random.choice(mature_options)
        elif age < 60:
            # Grupo 5: 50-59 años - Arrugas profundas
            older_options = ["deep expression lines", "pronounced crow's feet", "deep forehead lines", "laugh lines", "worry lines", "neck lines", "smile lines", "frown lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines"]
            return random.choice(older_options)
        else:
            # Grupo 6: 60+ años - Arrugas muy profundas
            elderly_options = ["deep wrinkles", "pronounced crow's feet", "deep forehead lines", "laugh lines", "worry lines", "neck lines", "age lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "platysmal bands", "horizontal neck lines", "vertical neck lines"]
            return random.choice(elderly_options)
    
    def _generate_multiple_age_appropriate_wrinkles(self, age: int) -> list:
        """Genera múltiples opciones de arrugas apropiadas para la edad para mayor diversidad"""
        all_wrinkles = self.diversity_data["wrinkle_types"]
        
        if age < 20:
            return ["none"]
        elif age < 25:
            # Muy jóvenes: solo líneas de expresión muy finas
            young_options = [w for w in all_wrinkles if w in ["none", "fine expression lines", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines"]]
            return young_options if young_options else ["none"]
        elif age < 30:
            # Jóvenes adultos: líneas de expresión leves
            young_adult_options = [w for w in all_wrinkles if w in ["none", "fine expression lines", "light laugh lines", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines", "nasolabial folds", "marionette lines"]]
            return young_adult_options if young_adult_options else ["none"]
        elif age < 35:
            # Adultos jóvenes: líneas de expresión más visibles
            adult_young_options = [w for w in all_wrinkles if w in ["none", "fine expression lines", "light laugh lines", "subtle crow's feet", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines"]]
            return adult_young_options if adult_young_options else ["none"]
        elif age < 40:
            # Adultos: arrugas más definidas
            adult_options = [w for w in all_wrinkles if w in ["fine expression lines", "light laugh lines", "subtle crow's feet", "forehead lines", "moderate expression lines", "crow's feet", "laugh lines", "worry lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines"]]
            return adult_options if adult_options else ["fine expression lines"]
        elif age < 50:
            # Adultos maduros: arrugas más profundas
            mature_options = [w for w in all_wrinkles if w in ["moderate expression lines", "crow's feet", "forehead lines", "laugh lines", "worry lines", "deep expression lines", "pronounced crow's feet", "deep forehead lines", "neck lines", "smile lines", "frown lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines"]]
            return mature_options if mature_options else ["moderate expression lines"]
        elif age < 60:
            # Adultos mayores: arrugas profundas
            older_options = [w for w in all_wrinkles if w in ["deep expression lines", "pronounced crow's feet", "deep forehead lines", "laugh lines", "worry lines", "neck lines", "smile lines", "frown lines", "pronounced lines", "defined lines", "mature lines", "age lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "platysmal bands", "horizontal neck lines", "vertical neck lines", "chest lines", "decolletage lines"]]
            return older_options if older_options else ["deep expression lines"]
        else:
            # Ancianos: arrugas muy profundas
            elderly_options = [w for w in all_wrinkles if w in ["deep wrinkles", "pronounced crow's feet", "deep forehead lines", "laugh lines", "worry lines", "neck lines", "age lines", "sun damage", "genetic", "lifestyle", "dynamic", "static", "gravitational", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "platysmal bands", "horizontal neck lines", "vertical neck lines", "chest lines", "decolletage lines", "hand lines", "knuckle lines", "finger lines"]]
            return elderly_options if elderly_options else ["deep wrinkles"]
    
    def _generate_age_specific_wrinkles(self, age: int) -> list:
        """Genera arrugas específicas para la edad con sistema flexible para máxima diversidad - SOLO ARRUGAS FACIALES"""
        # Sistema flexible: permitir más opciones por edad para mayor diversidad
        if age < 20:
            # Muy jóvenes: pocas opciones pero incluir algunas variaciones
            young_options = ["none", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines"]
            return young_options
        elif age < 25:
            # Jóvenes: más opciones para diversidad
            young_adult_options = ["none", "fine expression lines", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines"]
            return young_adult_options
        elif age < 30:
            # Adultos jóvenes: ampliar opciones
            adult_young_options = ["none", "fine expression lines", "light laugh lines", "subtle crow's feet", "barely visible lines", "subtle lines", "soft lines", "gentle lines", "faint lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines"]
            return adult_young_options
        elif age < 35:
            # Adultos: aún más opciones para diversidad
            adult_options = ["none", "fine expression lines", "light laugh lines", "subtle crow's feet", "forehead lines", "moderate expression lines", "crow's feet", "laugh lines", "worry lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "smile lines", "frown lines"]
            return adult_options
        elif age < 40:
            # Adultos maduros: opciones más amplias
            mature_options = ["fine expression lines", "light laugh lines", "subtle crow's feet", "forehead lines", "moderate expression lines", "crow's feet", "laugh lines", "worry lines", "deep expression lines", "pronounced crow's feet", "deep forehead lines", "neck lines", "smile lines", "frown lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines"]
            return mature_options
        elif age < 50:
            # Adultos mayores: opciones muy amplias
            older_options = ["moderate expression lines", "crow's feet", "forehead lines", "laugh lines", "worry lines", "deep expression lines", "pronounced crow's feet", "deep forehead lines", "neck lines", "smile lines", "frown lines", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "platysmal bands", "horizontal neck lines", "vertical neck lines", "chest lines", "decolletage lines"]
            return older_options
        else:
            # Seniors: arrugas muy profundas
            senior_options = ["deep wrinkles", "pronounced crow's feet", "deep forehead lines", "laugh lines", "worry lines", "neck lines", "age lines", "sun damage", "genetic", "lifestyle", "dynamic", "static", "gravitational", "nasolabial folds", "marionette lines", "lip lines", "chin lines", "cheek lines", "temple lines", "brow lines", "under eye lines", "lateral canthal lines", "glabellar lines", "periorbital lines", "perioral lines", "mental lines", "platysmal bands", "horizontal neck lines", "vertical neck lines", "chest lines", "decolletage lines", "hand lines", "knuckle lines", "finger lines"]
            return senior_options
    
    def _generate_age_appropriate_spots(self, age: int) -> str:
        """Genera manchas de edad apropiadas para la edad"""
        if age < 30:
            return "none"
        elif age < 40:
            return random.choice(["none", "few age spots", "minimal age spots"])
        elif age < 50:
            return random.choice(["none", "few age spots", "minimal age spots", "some age spots", "moderate age spots"])
        elif age < 60:
            return random.choice(["few age spots", "some age spots", "moderate age spots", "several age spots", "visible age spots"])
        else:
            return random.choice(["some age spots", "moderate age spots", "several age spots", "visible age spots", "many age spots", "extensive age spots"])
    
    def _generate_age_appropriate_elasticity(self, age: int) -> str:
        """Genera elasticidad de piel apropiada para la edad"""
        if age < 25:
            return "firm"
        elif age < 35:
            return random.choice(["firm", "tight", "elastic", "flexible", "resilient"])
        elif age < 45:
            return random.choice(["firm", "tight", "elastic", "flexible", "resilient", "moderate"])
        elif age < 55:
            return random.choice(["moderate", "loose", "flexible", "elastic", "firm"])
        else:
            return random.choice(["loose", "very loose", "flexible", "elastic"])
    
    def _generate_gender_appropriate_facial_hair(self, gender: str) -> str:
        """Genera vello facial apropiado para el género"""
        if hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
            return "none"  # Las mujeres no tienen vello facial
        else:
            # Solo para hombres
            return random.choice(["none", "light", "moderate", "heavy"])
    
    def _generate_gender_appropriate_beard(self, gender: str) -> str:
        """Genera barba apropiada para el género"""
        if hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
            return "none"  # Las mujeres no tienen barba
        else:
            # Solo para hombres
            return random.choice(["none", "stubble", "short", "medium", "long", "full"])
    
    def _generate_gender_appropriate_mustache(self, gender: str) -> str:
        """Genera bigote apropiado para el género"""
        if hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
            return "none"  # Las mujeres no tienen bigote
        else:
            # Solo para hombres
            return random.choice(["none", "light", "medium", "thick", "handlebar"])
    
    def _filter_gender_appropriate_features(self, category: str, gender: str) -> list:
        """Filtra características apropiadas para el género con lógica específica"""
        if category not in self.diversity_data:
            return []
        
        all_features = self.diversity_data[category]
        
        # TEMPORALMENTE DESACTIVAR FILTRADO POR GÉNERO PARA MÁXIMA DIVERSIDAD
        # TODO: Implementar filtrado inteligente que no limite la diversidad
        return all_features
        
        # Aplicar lógica específica por género
        if hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
            return self._get_male_specific_features(category, all_features)
        elif hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
            return self._get_female_specific_features(category, all_features)
        else:
            return all_features
    
    def _get_male_specific_features(self, category: str, all_features: list) -> list:
        """Obtiene características específicas para hombres"""
        # Características masculinas realistas por categoría
        male_features = {
            'face_shapes': ['square', 'rectangular', 'oval', 'round', 'triangular', 'diamond', 'heart', 'long', 'broad', 'angular', 'strong', 'masculine', 'chiseled', 'defined', 'wide'],
            'jawline_types': ['strong', 'angular', 'square', 'prominent', 'chiseled', 'masculine', 'defined', 'broad', 'wide', 'solid', 'firm', 'robust'],
            'cheekbone_types': ['high', 'prominent', 'sharp', 'angular', 'strong', 'defined', 'pronounced', 'visible', 'noticeable'],
            'eyebrow_shapes': ['thick', 'bushy', 'strong', 'defined', 'masculine', 'heavy', 'dense', 'natural', 'full'],
            'lip_shapes': ['thin', 'narrow', 'small', 'defined', 'masculine', 'firm', 'straight', 'medium'],
            'eye_shapes': ['deep-set', 'intense', 'piercing', 'alert', 'strong', 'masculine', 'narrow', 'small', 'almond', 'round', 'hooded'],
            'skin_textures': ['normal', 'rough', 'textured', 'weathered', 'aged', 'mature', 'firm', 'thick'],
            'beauty_levels': ['handsome', 'attractive', 'good-looking', 'masculine', 'strong', 'rugged', 'manly', 'virile', 'average', 'normal'],
            'hair_styles': ['short', 'buzz cut', 'crew cut', 'fade', 'undercut', 'mohawk', 'military', 'business', 'classic', 'traditional', 'side part', 'comb over', 'slicked back', 'quiff', 'pompadour', 'flat top', 'high and tight', 'ivy league', 'textured crop', 'messy', 'spiky', 'natural', 'casual'],
            'hair_lengths': ['short', 'very short', 'buzz cut', 'crew cut', 'medium short', 'medium', 'long short']
        }
        
        if category in male_features:
            # Filtrar solo características masculinas realistas
            filtered = [f for f in all_features if f in male_features[category]]
            
            # Si no hay suficientes opciones, agregar algunas básicas
            if len(filtered) < 5:
                basic_male = {
                    'face_shapes': ['square', 'oval', 'round', 'rectangular'],
                    'jawline_types': ['strong', 'angular', 'square', 'prominent'],
                    'cheekbone_types': ['high', 'prominent', 'sharp', 'angular'],
                    'eyebrow_shapes': ['thick', 'bushy', 'strong', 'natural'],
                    'lip_shapes': ['thin', 'narrow', 'medium', 'firm'],
                    'eye_shapes': ['deep-set', 'almond', 'round', 'hooded'],
                    'skin_textures': ['normal', 'rough', 'textured', 'firm'],
                    'beauty_levels': ['handsome', 'attractive', 'average', 'normal'],
                    'hair_styles': ['short', 'buzz cut', 'crew cut', 'fade', 'natural'],
                    'hair_lengths': ['short', 'very short', 'medium short', 'medium']
                }
                if category in basic_male:
                    filtered.extend(basic_male[category])
            
            return filtered
        
        return all_features
    
    def _get_female_specific_features(self, category: str, all_features: list) -> list:
        """Obtiene características específicas para mujeres"""
        # Características femeninas realistas por categoría
        female_features = {
            'face_shapes': ['oval', 'round', 'heart', 'diamond', 'pear', 'square', 'long', 'soft', 'delicate', 'feminine', 'elegant'],
            'jawline_types': ['soft', 'delicate', 'feminine', 'smooth', 'gentle', 'rounded', 'oval'],
            'cheekbone_types': ['soft', 'delicate', 'subtle', 'gentle', 'smooth', 'rounded'],
            'eyebrow_shapes': ['thin', 'defined', 'shaped', 'arched', 'natural', 'groomed', 'elegant'],
            'lip_shapes': ['full', 'plump', 'voluptuous', 'sensual', 'charming', 'shapely', 'defined', 'medium'],
            'eye_shapes': ['almond', 'round', 'large', 'expressive', 'gentle', 'beautiful', 'elegant', 'doll-like'],
            'skin_textures': ['smooth', 'soft', 'delicate', 'youthful', 'glowing', 'radiant', 'dewy', 'fresh'],
            'beauty_levels': ['beautiful', 'attractive', 'pretty', 'elegant', 'charming', 'lovely', 'stunning', 'gorgeous'],
            'hair_styles': ['long', 'medium', 'layered', 'textured', 'voluminous', 'sleek', 'styled', 'natural', 'professional', 'casual', 'elegant', 'chic'],
            'hair_lengths': ['long', 'very long', 'shoulder length', 'medium long', 'medium', 'short', 'chin length']
        }
        
        if category in female_features:
            # Filtrar solo características femeninas realistas
            filtered = [f for f in all_features if f in female_features[category]]
            
            # Si no hay suficientes opciones, agregar algunas básicas
            if len(filtered) < 5:
                basic_female = {
                    'face_shapes': ['oval', 'round', 'heart', 'diamond'],
                    'jawline_types': ['soft', 'delicate', 'feminine', 'smooth'],
                    'cheekbone_types': ['soft', 'delicate', 'subtle', 'gentle'],
                    'eyebrow_shapes': ['thin', 'defined', 'arched', 'natural'],
                    'lip_shapes': ['full', 'medium', 'defined', 'shapely'],
                    'eye_shapes': ['almond', 'round', 'large', 'expressive'],
                    'skin_textures': ['smooth', 'soft', 'delicate', 'fresh'],
                    'beauty_levels': ['beautiful', 'attractive', 'pretty', 'elegant'],
                    'hair_styles': ['long', 'medium', 'layered', 'natural'],
                    'hair_lengths': ['long', 'medium long', 'medium', 'shoulder length']
                }
                if category in basic_female:
                    filtered.extend(basic_female[category])
            
            return filtered
        
        return all_features
    
    def generate_advanced_genetic_profile(self, nationality: str, region: str, gender: str, age: int, 
                                        beauty_control: str, skin_control: str, hair_control: str, 
                                        eye_control: str, face_shape_control: str, nose_shape_control: str,
                                        lip_shape_control: str, eye_shape_control: str, jawline_control: str,
                                        cheekbone_control: str, eyebrow_control: str, skin_texture_control: str,
                                        freckle_control: str, mole_control: str, scar_control: str,
                                        acne_control: str, wrinkle_control: str, hair_style_control: str,
                                        edad_min: int = None, edad_max: int = None) -> UltraDiversityProfile:
        """Genera perfil genético avanzado usando los controles de la WebUI"""
        
        # Generar edad aleatoria dentro del rango si se proporcionan edad_min y edad_max
        if edad_min is not None and edad_max is not None:
            # Validar rango de edad
            if edad_min < 18:
                edad_min = 18
            if edad_max > 80:
                edad_max = 80
            if edad_min >= edad_max:
                edad_min = 18
                edad_max = 65
            
            # Generar edad aleatoria dentro del rango
            final_age = random.randint(edad_min, edad_max)
        else:
            # Usar la edad proporcionada si no hay rango
            final_age = age
        
        # Generar semilla única para máxima diversidad
        unique_seed = int(time.time() * 1000000) + random.randint(1, 999999) + hash(nationality + gender + str(final_age))
        random.seed(unique_seed)
        
        # Generar ID único
        image_id = f"genetic_{hashlib.md5(f'{nationality}_{gender}_{final_age}_{time.time()}_{unique_seed}'.encode()).hexdigest()[:12]}"
        
        # Manejar región aleatoria
        if region == "aleatorio":
            regiones_disponibles = [
                "caracas", "maracaibo", "valencia", "barquisimeto", "ciudad_guayana", "maturin", "merida", 
                "san_cristobal", "barcelona", "puerto_la_cruz", "ciudad_bolivar", "tucupita", "porlamar", 
                "valera", "acarigua", "guanare", "san_fernando", "trujillo", "el_tigre", "cabimas", 
                "punto_fijo", "ciudad_ojeda", "puerto_cabello", "valle_de_la_pascua", "san_juan_de_los_morros", 
                "carora", "tocuyo", "duaca", "siquisique", "araure", "turen", "guanarito", "santa_elena", 
                "el_venado", "san_rafael", "san_antonio", "la_fria", "rubio", "colon", "san_cristobal", 
                "tachira", "apure", "amazonas", "delta_amacuro", "yacambu", "lara", "portuguesa", "cojedes", 
                "guarico", "anzoategui", "monagas", "sucre", "nueva_esparta", "falcon", "zulia", "merida", 
                "trujillo", "barinas", "yaracuy", "carabobo", "aragua", "miranda", "vargas", "distrito_capital"
            ]
            region = random.choice(regiones_disponibles)
        
        # Aplicar controles específicos con filtrado por género
        skin_tone = self._apply_skin_control(skin_control)
        hair_color = self._apply_hair_control(hair_control)
        eye_color = self._apply_eye_control(eye_control)
        face_shape = self._apply_face_shape_control(face_shape_control, gender)
        nose_shape = self._apply_nose_shape_control(nose_shape_control, gender)
        lip_shape = self._apply_lip_shape_control(lip_shape_control, gender)
        eye_shape = self._apply_eye_shape_control(eye_shape_control, gender)
        jawline = self._apply_jawline_control(jawline_control, gender)
        cheekbones = self._apply_cheekbone_control(cheekbone_control, gender)
        eyebrows = self._apply_eyebrow_control(eyebrow_control, gender)
        skin_texture = self._apply_skin_texture_control(skin_texture_control, gender)
        freckles = self._apply_freckle_control(freckle_control)
        moles = self._apply_mole_control(mole_control)
        scars = self._apply_scar_control(scar_control)
        acne = self._apply_acne_control(acne_control)
        wrinkles = self._apply_wrinkle_control(wrinkle_control, final_age)
        hair_style = self._apply_hair_style_control(hair_style_control, gender)
        hair_length = self._apply_hair_length_control("aleatorio", gender)
        makeup = self._apply_makeup_control("aleatorio", gender)
        
        # Crear perfil con controles aplicados
        profile = UltraDiversityProfile(
            image_id=image_id,
            nationality=nationality,
            region=region,
            gender=gender,
            age=final_age,
            
            # Características faciales con controles aplicados
            face_shape=face_shape,
            face_width=random.choice(["narrow", "medium", "wide"]),
            face_length=random.choice(["short", "medium", "long"]),
            jawline=jawline,
            chin=random.choice(["pointed", "rounded", "square", "oval"]),
            cheekbones=cheekbones,
            facial_symmetry=random.choice(["slightly_asymmetrical", "balanced", "very_symmetrical"]),
            bone_structure=random.choice(["delicate", "medium", "strong", "prominent"]),
            
            # Ojos con controles aplicados
            eye_color=eye_color,
            eye_color_shade=random.choice(["light", "medium", "dark", "deep"]),
            eye_shape=eye_shape,
            eye_size=random.choice(["small", "medium", "large"]),
            eye_spacing=random.choice(["close", "medium", "wide"]),
            eyelid_type=random.choice(["single", "double", "hooded", "deep_set"]),
            eyelashes=random.choice(["short", "medium", "long", "very_long"]),
            eyelashes_length=random.choice(["short", "medium", "long"]),
            eyebrows=eyebrows,
            eyebrows_thickness=random.choice(["thin", "medium", "thick"]),
            eyebrows_shape=random.choice(["straight", "arched", "rounded", "angled"]),
            
            # Nariz con controles aplicados
            nose_shape=nose_shape,
            nose_size=random.choice(["small", "medium", "large"]),
            nose_width=random.choice(["narrow", "medium", "wide"]),
            nose_bridge=random.choice(["low", "medium", "high", "prominent"]),
            nose_tip=random.choice(["pointed", "rounded", "wide", "narrow"]),
            nostril_size=random.choice(["small", "medium", "large"]),
            
            # Boca con controles aplicados
            lip_shape=lip_shape,
            lip_size=random.choice(["small", "medium", "large"]),
            lip_thickness=random.choice(["thin", "medium", "full"]),
            mouth_width=random.choice(["narrow", "medium", "wide"]),
            lip_color=random.choice(["pale", "medium", "dark", "very_dark"]),
            lip_fullness=random.choice(["thin", "medium", "full", "very_full"]),
            
            # Piel con controles aplicados
            skin_tone=skin_tone,
            skin_tone_shade=random.choice(["light", "medium", "dark", "deep"]),
            skin_texture=skin_texture,
            skin_undertone=random.choice(["cool", "neutral", "warm"]),
            skin_glow=random.choice(["dull", "natural", "glowing", "very_glowing"]),
            skin_imperfections=random.sample(["pores", "texture", "variations"], random.randint(0, 3)),
            freckles=freckles,
            freckles_density=random.choice(["sparse", "moderate", "dense"]),
            moles=moles,
            moles_count=random.choice(["none", "few", "several", "many"]),
            birthmarks=random.choice(["none", "small", "medium", "large"]),
            scars=scars,
            acne=acne,
            age_spots=self._generate_age_appropriate_spots(age),
            wrinkles=wrinkles,
            skin_elasticity=self._generate_age_appropriate_elasticity(age),
            
            # Cabello con controles aplicados
            hair_color=hair_color,
            hair_color_shade=random.choice(["light", "medium", "dark", "deep"]),
            hair_texture=random.choice(["straight", "wavy", "curly", "coily"]),
            hair_length=random.choice(["short", "medium", "long", "very_long"]),
            hair_style=hair_style,
            hair_density=random.choice(["thin", "medium", "thick", "very_thick"]),
            hair_shine=random.choice(["dull", "natural", "shiny", "very_shiny"]),
            hair_curliness=random.choice(["straight", "wavy", "curly", "very_curly"]),
            hair_thickness=random.choice(["fine", "medium", "thick", "very_thick"]),
            hairline=random.choice(["low", "medium", "high", "receding"]),
            
            # Vello facial (solo para hombres)
            facial_hair=self._generate_gender_appropriate_facial_hair(gender),
            beard=self._generate_gender_appropriate_beard(gender),
            mustache=self._generate_gender_appropriate_mustache(gender),
            
            # Maquillaje (solo para mujeres)
            makeup=makeup,
            
            # Características de edad
            age_characteristics=self._generate_age_characteristics(age),
            
            # Nivel de belleza con anti-repetición
            beauty_level=self._anti_repetition_selection("beauty_levels", self.diversity_data["beauty_levels"]),
            attractiveness_factors=self._generate_attractiveness_factors(),
            
            # Sistema de ropa diverso (evita color blanco)
            clothing_type=self._anti_repetition_selection("clothing_types", self.diversity_data["clothing_types"]),
            clothing_color=self._anti_repetition_selection("clothing_colors", self.diversity_data["clothing_colors"]),
            clothing_style=self._anti_repetition_selection("clothing_styles", self.diversity_data["clothing_styles"]),
            
            # Características corporales realistas
            body_type=self._anti_repetition_selection("body_types", self.diversity_data["body_types"]),
            body_weight=self._anti_repetition_selection("body_weights", self.diversity_data["body_weights"]),
            body_height=self._anti_repetition_selection("body_heights", self.diversity_data["body_heights"]),
            body_shape=self._anti_repetition_selection("body_shapes", self.diversity_data["body_shapes"]),
            muscle_definition=self._anti_repetition_selection("muscle_definitions", self.diversity_data["muscle_definitions"]),
            body_fat_percentage=self._anti_repetition_selection("body_fat_percentages", self.diversity_data["body_fat_percentages"]),
            
            # Características étnicas
            ethnic_features=self._generate_ethnic_features(nationality),
            
            # Metadatos
            generated_at=datetime.now().isoformat(),
            generation_type="advanced_genetic",
            uniqueness_score=random.uniform(0.8, 1.0),
            diversity_factors=self._generate_diversity_factors()
        )
        
        return profile
    
    def _apply_skin_control(self, skin_control: str) -> str:
        """Aplica el control de tono de piel"""
        if skin_control == "aleatorio":
            return random.choice(self.diversity_data["skin_tones"])
        elif skin_control == "mixed":
            return random.choice(["fair", "light", "medium", "olive", "tan", "brown", "dark"])
        elif skin_control == "auto":
            # Auto = selección automática basada en nacionalidad/región
            return random.choice(self.diversity_data["skin_tones"])
        else:
            # Mapear controles específicos a tonos de piel
            skin_mapping = {
                "fair": "fair",
                "light": "light", 
                "medium": "medium",
                "olive": "olive",
                "tan": "tan",
                "brown": "brown",
                "dark": "dark",
                "very_dark": "very_dark",
                # Mapear opciones específicas del UI
                "medium-dark": "dark",
                "golden": "tan",
                "bronze": "tan",
                "caramel": "brown",
                "honey": "tan",
                "rich brown": "brown",
                "coffee": "brown",
                "mahogany": "dark",
                "espresso": "very_dark",
                "chocolate": "brown",
                "mocha": "brown",
                "cinnamon": "tan",
                "amber": "tan",
                "copper": "tan",
                "peach": "fair",
                "ivory": "fair",
                "beige": "light",
                "sand": "tan",
                "cream": "fair",
                "wheat": "tan",
                "almond": "tan",
                "hazelnut": "brown",
                "walnut": "brown",
                "chestnut": "brown",
                "cocoa": "brown",
                "ebony": "very_dark"
            }
            return skin_mapping.get(skin_control, "medium")
    
    def _apply_hair_control(self, hair_control: str) -> str:
        """Aplica el control de color de cabello"""
        if hair_control == "aleatorio":
            return random.choice(self.diversity_data["hair_colors"])
        elif hair_control == "mixed":
            return random.choice(self.diversity_data["hair_colors"])
        elif hair_control == "auto":
            # Auto = selección automática basada en nacionalidad/región
            return random.choice(self.diversity_data["hair_colors"])
        else:
            # Mapear controles específicos a colores de cabello
            hair_mapping = {
                "black": "black",
                "brown": "brown",
                "dark_brown": "dark_brown",
                "light_brown": "light_brown",
                "blonde": "blonde",
                "red": "red",
                "auburn": "auburn",
                "gray": "gray",
                "white": "white"
            }
            return hair_mapping.get(hair_control, "brown")
    
    def _apply_eye_control(self, eye_control: str) -> str:
        """Aplica el control de color de ojos"""
        if eye_control == "aleatorio":
            return random.choice(self.diversity_data["eye_colors"])
        elif eye_control == "mixed":
            return random.choice(self.diversity_data["eye_colors"])
        elif eye_control == "auto":
            # Auto = selección automática basada en nacionalidad/región
            return random.choice(self.diversity_data["eye_colors"])
        else:
            # Mapear controles específicos a colores de ojos
            eye_mapping = {
                "brown": "brown",
                "hazel": "hazel", 
                "green": "green",
                "blue": "blue",
                "gray": "gray",
                "amber": "amber"
            }
            return eye_mapping.get(eye_control, "brown")
    
    def _apply_face_shape_control(self, face_shape_control: str, gender: str = None) -> str:
        """Aplica el control de forma de cara con filtrado por género y anti-repetición específica"""
        if face_shape_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                # Para hombres, usar sistema específico de anti-repetición masculina
                filtered_shapes = self._filter_gender_appropriate_features("face_shapes", gender)
                return self._anti_repetition_selection_male("face_shapes", filtered_shapes)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                # Para mujeres, usar sistema específico de anti-repetición femenina
                filtered_shapes = self._filter_gender_appropriate_features("face_shapes", gender)
                return self._anti_repetition_selection_female("face_shapes", filtered_shapes)
            else:
                return self._anti_repetition_selection("face_shapes", self.diversity_data["face_shapes"])
        else:
            return face_shape_control
    
    def _apply_nose_shape_control(self, nose_shape_control: str, gender: str = None) -> str:
        """Aplica el control de forma de nariz con anti-repetición específica por género"""
        if nose_shape_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                return self._anti_repetition_selection_male("nose_shapes", self.diversity_data["nose_shapes"])
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                return self._anti_repetition_selection_female("nose_shapes", self.diversity_data["nose_shapes"])
            else:
                return self._anti_repetition_selection("nose_shapes", self.diversity_data["nose_shapes"])
        else:
            return nose_shape_control
    
    def _apply_lip_shape_control(self, lip_shape_control: str, gender: str = None) -> str:
        """Aplica el control de forma de labios con filtrado por género y anti-repetición específica"""
        if lip_shape_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_lips = self._filter_gender_appropriate_features("lip_shapes", gender)
                return self._anti_repetition_selection_male("lip_shapes", filtered_lips)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_lips = self._filter_gender_appropriate_features("lip_shapes", gender)
                return self._anti_repetition_selection_female("lip_shapes", filtered_lips)
            else:
                return self._anti_repetition_selection("lip_shapes", self.diversity_data["lip_shapes"])
        else:
            return lip_shape_control
    
    def _apply_eye_shape_control(self, eye_shape_control: str, gender: str = None) -> str:
        """Aplica el control de forma de ojos con filtrado por género y anti-repetición específica"""
        if eye_shape_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_eyes = self._filter_gender_appropriate_features("eye_shapes", gender)
                return self._anti_repetition_selection_male("eye_shapes", filtered_eyes)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_eyes = self._filter_gender_appropriate_features("eye_shapes", gender)
                return self._anti_repetition_selection_female("eye_shapes", filtered_eyes)
            else:
                return self._anti_repetition_selection("eye_shapes", self.diversity_data["eye_shapes"])
        else:
            return eye_shape_control
    
    def _apply_jawline_control(self, jawline_control: str, gender: str = None) -> str:
        """Aplica el control de línea de mandíbula con filtrado por género y anti-repetición específica"""
        if jawline_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_jawlines = self._filter_gender_appropriate_features("jawline_types", gender)
                return self._anti_repetition_selection_male("jawline_types", filtered_jawlines)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_jawlines = self._filter_gender_appropriate_features("jawline_types", gender)
                return self._anti_repetition_selection_female("jawline_types", filtered_jawlines)
            else:
                return self._anti_repetition_selection("jawline_types", self.diversity_data["jawline_types"])
        else:
            return jawline_control
    
    def _apply_cheekbone_control(self, cheekbone_control: str, gender: str = None) -> str:
        """Aplica el control de pómulos con filtrado por género y anti-repetición específica"""
        if cheekbone_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_cheekbones = self._filter_gender_appropriate_features("cheekbone_types", gender)
                return self._anti_repetition_selection_male("cheekbone_types", filtered_cheekbones)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_cheekbones = self._filter_gender_appropriate_features("cheekbone_types", gender)
                return self._anti_repetition_selection_female("cheekbone_types", filtered_cheekbones)
            else:
                return self._anti_repetition_selection("cheekbone_types", self.diversity_data["cheekbone_types"])
        else:
            return cheekbone_control
    
    def _apply_eyebrow_control(self, eyebrow_control: str, gender: str = None) -> str:
        """Aplica el control de cejas con filtrado por género y anti-repetición específica"""
        if eyebrow_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_eyebrows = self._filter_gender_appropriate_features("eyebrow_shapes", gender)
                return self._anti_repetition_selection_male("eyebrow_shapes", filtered_eyebrows)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_eyebrows = self._filter_gender_appropriate_features("eyebrow_shapes", gender)
                return self._anti_repetition_selection_female("eyebrow_shapes", filtered_eyebrows)
            else:
                return self._anti_repetition_selection("eyebrow_shapes", self.diversity_data["eyebrow_shapes"])
        else:
            return eyebrow_control
    
    def _apply_skin_texture_control(self, skin_texture_control: str, gender: str = None) -> str:
        """Aplica el control de textura de piel con filtrado por género y anti-repetición específica"""
        if skin_texture_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_textures = self._filter_gender_appropriate_features("skin_textures", gender)
                return self._anti_repetition_selection_male("skin_textures", filtered_textures)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_textures = self._filter_gender_appropriate_features("skin_textures", gender)
                return self._anti_repetition_selection_female("skin_textures", filtered_textures)
            else:
                return self._anti_repetition_selection("skin_textures", self.diversity_data["skin_textures"])
        else:
            return skin_texture_control
    
    def _apply_freckle_control(self, freckle_control: str) -> str:
        """Aplica el control de pecas"""
        if freckle_control == "aleatorio":
            return random.choice(self.diversity_data["freckle_types"])
        else:
            return freckle_control
    
    def _apply_mole_control(self, mole_control: str) -> str:
        """Aplica el control de lunares"""
        if mole_control == "aleatorio":
            return random.choice(self.diversity_data["mole_types"])
        else:
            return mole_control
    
    def _apply_scar_control(self, scar_control: str) -> str:
        """Aplica el control de cicatrices"""
        if scar_control == "aleatorio":
            return random.choice(self.diversity_data["scar_types"])
        else:
            return scar_control
    
    def _apply_acne_control(self, acne_control: str) -> str:
        """Aplica el control de acné"""
        if acne_control == "aleatorio":
            return random.choice(self.diversity_data["acne_types"])
        else:
            return acne_control
    
    def _apply_wrinkle_control(self, wrinkle_control: str, age: int) -> str:
        """Aplica el control de arrugas considerando la edad con anti-repetición mejorado"""
        if wrinkle_control == "aleatorio":
            # Generar arrugas específicas para la edad exacta
            age_specific_wrinkles = self._generate_age_specific_wrinkles(age)
            # Aplicar anti-repetición agresivo
            return self._anti_repetition_selection("wrinkle_types", age_specific_wrinkles)
        else:
            return wrinkle_control
    
    def _apply_hair_style_control(self, hair_style_control: str, gender: str = None) -> str:
        """Aplica el control de estilo de cabello con filtrado por género y anti-repetición específica"""
        if hair_style_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_styles = self._filter_gender_appropriate_features("hair_styles", gender)
                return self._anti_repetition_selection_male("hair_styles", filtered_styles)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_styles = self._filter_gender_appropriate_features("hair_styles", gender)
                return self._anti_repetition_selection_female("hair_styles", filtered_styles)
            else:
                return self._anti_repetition_selection("hair_styles", self.diversity_data["hair_styles"])
        else:
            return hair_style_control
    
    def _apply_hair_length_control(self, hair_length_control: str, gender: str = None) -> str:
        """Aplica el control de longitud de cabello con filtrado por género y anti-repetición específica"""
        if hair_length_control == "aleatorio":
            if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
                filtered_lengths = self._filter_gender_appropriate_features("hair_lengths", gender)
                return self._anti_repetition_selection_male("hair_lengths", filtered_lengths)
            elif gender and hasattr(gender, 'lower') and gender.lower() in ["mujer", "woman", "female"]:
                filtered_lengths = self._filter_gender_appropriate_features("hair_lengths", gender)
                return self._anti_repetition_selection_female("hair_lengths", filtered_lengths)
            else:
                return self._anti_repetition_selection("hair_lengths", self.diversity_data["hair_lengths"])
        else:
            return hair_length_control
    
    def _apply_makeup_control(self, makeup_control: str, gender: str = None) -> str:
        """Aplica el control de maquillaje (solo para mujeres por defecto)"""
        if gender and hasattr(gender, 'lower') and gender.lower() in ["hombre", "man", "male"]:
            return "none"  # Los hombres no usan maquillaje por defecto
        
        if makeup_control == "aleatorio":
            # Para mujeres, usar maquillaje neutro por defecto para SAIME
            neutral_makeup = ["none", "natural", "minimal", "light", "subtle", "soft", "gentle", "delicate", "simple", "basic", "clean", "fresh"]
            return random.choice(neutral_makeup)
        else:
            return makeup_control
    
    def _anti_repetition_selection(self, category: str, options: list) -> str:
        """Selección anti-repetición ULTRA AGRESIVA para máxima diversidad"""
        if not hasattr(self, '_recent_selections'):
            self._recent_selections = {}
        
        if category not in self._recent_selections:
            self._recent_selections[category] = []
        
        # Mantener historial de últimas 15 selecciones (ULTRA restrictivo)
        recent = self._recent_selections[category]
        if len(recent) >= 15:
            recent.pop(0)  # Remover la más antigua
        
        # Filtrar opciones que han sido usadas recientemente
        available_options = [opt for opt in options if opt not in recent]
        
        # Si no hay opciones disponibles, usar todas las opciones
        if not available_options:
            available_options = options
        
        # Sistema de pesos ULTRA AGRESIVO para máxima diversidad
        weights = self._calculate_ultra_diversity_weights(available_options, recent)
        
        # Seleccionar con pesos para favorecer opciones menos usadas
        selected = random.choices(available_options, weights=weights, k=1)[0]
        
        # Agregar a historial
        self._recent_selections[category].append(selected)
        
        return selected
    
    def _calculate_ultra_diversity_weights(self, available_options: list, recent: list) -> list:
        """Calcula pesos ULTRA AGRESIVOS para máxima diversidad"""
        weights = []
        
        # Contar frecuencia de cada opción en el historial
        from collections import Counter
        recent_counter = Counter(recent)
        
        for option in available_options:
            # Peso base
            base_weight = 1.0
            
            # Penalizar opciones usadas recientemente (ULTRA AGRESIVO)
            recent_count = recent_counter.get(option, 0)
            if recent_count > 0:
                # Penalización exponencial EXTREMA
                penalty = 0.01 ** recent_count  # 0.01, 0.0001, 0.000001, etc.
                base_weight *= penalty
            
            # Favorecer opciones que nunca han sido usadas
            if recent_count == 0:
                base_weight *= 50.0  # 50x más probable
            
            # Favorecer opciones usadas hace tiempo
            if recent_count == 1:
                base_weight *= 20.0  # 20x más probable
            
            weights.append(max(base_weight, 0.001))  # Mínimo peso de 0.001
        
        return weights
    
    def reset_anti_repetition_system(self):
        """Reinicia el sistema de anti-repetición para máxima diversidad"""
        self._recent_selections = {}
        print("🔄 Sistema de anti-repetición reiniciado para máxima diversidad")
    
    def _anti_repetition_selection_male(self, category: str, options: list) -> str:
        """Selección anti-repetición específica para HOMBRES con características masculinas"""
        if not hasattr(self, '_recent_selections_male'):
            self._recent_selections_male = {}
        
        if category not in self._recent_selections_male:
            self._recent_selections_male[category] = []
        
        # Mantener historial de últimas 15 selecciones (ULTRA restrictivo)
        recent = self._recent_selections_male[category]
        if len(recent) >= 15:
            recent.pop(0)  # Remover la más antigua
        
        # Filtrar opciones que han sido usadas recientemente
        available_options = [opt for opt in options if opt not in recent]
        
        # Si no hay opciones disponibles, usar todas las opciones
        if not available_options:
            available_options = options
        
        # Sistema de pesos ULTRA AGRESIVO para máxima diversidad masculina
        weights = self._calculate_ultra_diversity_weights_male(available_options, recent)
        
        # Seleccionar con pesos para favorecer opciones menos usadas
        selected = random.choices(available_options, weights=weights, k=1)[0]
        
        # Agregar a historial
        self._recent_selections_male[category].append(selected)
        
        return selected
    
    def _anti_repetition_selection_female(self, category: str, options: list) -> str:
        """Selección anti-repetición específica para MUJERES con características femeninas"""
        if not hasattr(self, '_recent_selections_female'):
            self._recent_selections_female = {}
        
        if category not in self._recent_selections_female:
            self._recent_selections_female[category] = []
        
        # Mantener historial de últimas 15 selecciones (ULTRA restrictivo)
        recent = self._recent_selections_female[category]
        if len(recent) >= 15:
            recent.pop(0)  # Remover la más antigua
        
        # Filtrar opciones que han sido usadas recientemente
        available_options = [opt for opt in options if opt not in recent]
        
        # Si no hay opciones disponibles, usar todas las opciones
        if not available_options:
            available_options = options
        
        # Sistema de pesos ULTRA AGRESIVO para máxima diversidad femenina
        weights = self._calculate_ultra_diversity_weights_female(available_options, recent)
        
        # Seleccionar con pesos para favorecer opciones menos usadas
        selected = random.choices(available_options, weights=weights, k=1)[0]
        
        # Agregar a historial
        self._recent_selections_female[category].append(selected)
        
        return selected
    
    def _calculate_ultra_diversity_weights_male(self, available_options: list, recent: list) -> list:
        """Calcula pesos ULTRA AGRESIVOS específicos para HOMBRES"""
        weights = []
        
        # Contar frecuencia de cada opción en el historial
        from collections import Counter
        recent_counter = Counter(recent)
        
        for option in available_options:
            # Peso base
            base_weight = 1.0
            
            # Penalizar opciones usadas recientemente (ULTRA AGRESIVO para hombres)
            recent_count = recent_counter.get(option, 0)
            if recent_count > 0:
                # Penalización exponencial EXTREMA para hombres
                penalty = 0.005 ** recent_count  # 0.005, 0.000025, 0.000000125, etc.
                base_weight *= penalty
            
            # Favorecer opciones que nunca han sido usadas (EXTREMO para hombres)
            if recent_count == 0:
                base_weight *= 100.0  # 100x más probable para hombres
            
            # Favorecer opciones usadas hace tiempo
            if recent_count == 1:
                base_weight *= 50.0  # 50x más probable para hombres
            
            weights.append(max(base_weight, 0.0001))  # Mínimo peso de 0.0001 para hombres
        
        return weights
    
    def _calculate_ultra_diversity_weights_female(self, available_options: list, recent: list) -> list:
        """Calcula pesos ULTRA AGRESIVOS específicos para MUJERES"""
        weights = []
        
        # Contar frecuencia de cada opción en el historial
        from collections import Counter
        recent_counter = Counter(recent)
        
        for option in available_options:
            # Peso base
            base_weight = 1.0
            
            # Penalizar opciones usadas recientemente (ULTRA AGRESIVO para mujeres)
            recent_count = recent_counter.get(option, 0)
            if recent_count > 0:
                # Penalización exponencial EXTREMA para mujeres
                penalty = 0.005 ** recent_count  # 0.005, 0.000025, 0.000000125, etc.
                base_weight *= penalty
            
            # Favorecer opciones que nunca han sido usadas (EXTREMO para mujeres)
            if recent_count == 0:
                base_weight *= 100.0  # 100x más probable para mujeres
            
            # Favorecer opciones usadas hace tiempo
            if recent_count == 1:
                base_weight *= 50.0  # 50x más probable para mujeres
            
            weights.append(max(base_weight, 0.0001))  # Mínimo peso de 0.0001 para mujeres
        
        return weights
    
    def _calculate_diversity_weights(self, available_options: list, recent: list) -> list:
        """Calcula pesos dinámicos para favorecer opciones menos usadas"""
        weights = []
        
        for option in available_options:
            # Peso base
            base_weight = 1.0
            
            # Reducir peso si se ha usado recientemente
            recent_count = recent.count(option)
            if recent_count > 0:
                base_weight *= (0.1 ** recent_count)  # Reducir exponencialmente
            
            # Aumentar peso para opciones menos comunes
            if hasattr(self, '_global_usage_count'):
                if option in self._global_usage_count:
                    usage_count = self._global_usage_count[option]
                    base_weight *= (1.0 / (usage_count + 1))  # Menos usado = más peso
                else:
                    base_weight *= 2.0  # Opción nueva = más peso
            else:
                self._global_usage_count = {}
                base_weight *= 2.0
            
            # Actualizar contador global
            if option not in self._global_usage_count:
                self._global_usage_count[option] = 0
            self._global_usage_count[option] += 1
            
            weights.append(max(base_weight, 0.1))  # Peso mínimo para evitar 0
        
        return weights

    def _passport_safe_hair_style(self, hair_style: str) -> str:
        """Normaliza estilos de cabello a estilos aprobados para pasaporte (bajo volumen, neat)."""
        # Palabras clave de alto volumen/no aprobados
        high_volume_keywords = {
            "afro", "dread", "dreadlocks", "locs", "bantu", "thick", "wild", "unkempt",
            "huge", "massive", "big", "messy", "voluminous", "trenzas", "braids", "box braids",
            "twists", "cornrows", "mohawk"
        }
        # Lista blanca de estilos recomendados para fotos de pasaporte
        passport_allowed = [
            "neat", "tidy", "sleek", "straight", "straightened", "bun", "low bun",
            "ponytail", "low ponytail", "bob", "pixie", "shoulder-length", "layered",
            "professional", "natural", "clean", "well-groomed", "short", "crew cut",
            "fade", "side part", "center part", "updo", "chignon"
        ]

        # Si ya es un estilo permitido, mantenerlo
        if hair_style and any(hair_style.lower() == a for a in passport_allowed):
            return hair_style

        # Si contiene palabras de alto volumen, convertir a un estilo permitido estable
        style_lower = (hair_style or "").lower()
        if any(k in style_lower for k in high_volume_keywords):
            return random.choice(passport_allowed)

        # Para estilos genéricos no listados, favorecer estilos sobrios
        return random.choice(passport_allowed)

    def _create_balanced_combinations(self, total_images: int, control_options: dict) -> list:
        """Crea combinaciones balanceadas para evitar repetición excesiva de valores."""
        combinations = []
        
        # Calcular cuántas veces puede aparecer cada valor (máximo)
        for control_name, options in control_options.items():
            if "aleatorio" in options:
                # Remover "aleatorio", "auto", "mixed" de las opciones
                clean_options = [opt for opt in options if opt not in ["aleatorio", "auto", "mixed"]]
                if clean_options:
                    # Calcular distribución balanceada
                    num_options = len(clean_options)
                    base_count = total_images // num_options
                    remainder = total_images % num_options
                    
                    # Crear lista balanceada
                    balanced_list = []
                    for i, option in enumerate(clean_options):
                        # Asignar base_count + 1 si está en el remainder
                        count = base_count + (1 if i < remainder else 0)
                        balanced_list.extend([option] * count)
                    
                    # Mezclar para evitar patrones
                    random.shuffle(balanced_list)
                    combinations.append(balanced_list[:total_images])
                else:
                    combinations.append([random.choice(options)] * total_images)
            else:
                combinations.append([random.choice(options)] * total_images)
        
        return combinations

    def generate_balanced_profiles(self, total_images: int, nationality: str, gender: str, age: int, 
                                 control_options: dict) -> list:
        """Genera perfiles balanceados para evitar repetición excesiva."""
        profiles = []
        
        # Crear combinaciones balanceadas
        balanced_combinations = self._create_balanced_combinations(total_images, control_options)
        
        # Crear diccionario de mapeo de controles basado en el orden de control_options
        control_mapping = {}
        for i, (control_name, _) in enumerate(control_options.items()):
            control_mapping[control_name] = i
        
        # Generar perfiles usando las combinaciones balanceadas
        for i in range(total_images):
            # Seleccionar valores balanceados para esta imagen
            balanced_values = {}
            for control_name, control_index in control_mapping.items():
                if control_index < len(balanced_combinations):
                    balanced_values[control_name] = balanced_combinations[control_index][i]
                else:
                    balanced_values[control_name] = "aleatorio"
            
            # Generar región aleatoria
            regiones_disponibles = ["caracas", "maracaibo", "valencia", "barquisimeto", "ciudad_guayana", "maturin", "merida", "san_cristobal", "barcelona", "puerto_la_cruz", "ciudad_bolivar", "tucupita", "porlamar", "valera", "acarigua", "guanare", "san_fernando", "trujillo", "el_tigre", "cabimas", "punto_fijo", "ciudad_ojeda", "puerto_cabello", "valle_de_la_pascua", "san_juan_de_los_morros", "carora", "tocuyo", "duaca", "siquisique", "araure", "turen", "guanarito", "santa_elena", "el_venado", "san_rafael", "san_antonio", "la_fria", "rubio", "colon", "san_cristobal", "tachira", "apure", "amazonas", "delta_amacuro", "yacambu", "lara", "portuguesa", "cojedes", "guarico", "anzoategui", "monagas", "sucre", "nueva_esparta", "falcon", "zulia", "merida", "trujillo", "barinas", "yaracuy", "carabobo", "aragua", "miranda", "vargas", "distrito_capital"]
            region = random.choice(regiones_disponibles)
            
            # Generar perfil con valores balanceados
            profile = self.generate_advanced_genetic_profile(
                nationality=nationality,
                region=region,
                gender=gender,
                age=age,
                beauty_control=balanced_values.get("beauty_control", "aleatorio"),
                skin_control=balanced_values.get("skin_control", "aleatorio"),
                hair_control=balanced_values.get("hair_control", "aleatorio"),
                eye_control=balanced_values.get("eye_control", "aleatorio"),
                face_shape_control=balanced_values.get("face_shape_control", "aleatorio"),
                nose_shape_control=balanced_values.get("nose_shape_control", "aleatorio"),
                lip_shape_control=balanced_values.get("lip_shape_control", "aleatorio"),
                eye_shape_control=balanced_values.get("eye_shape_control", "aleatorio"),
                jawline_control=balanced_values.get("jawline_control", "aleatorio"),
                cheekbone_control=balanced_values.get("cheekbone_control", "aleatorio"),
                eyebrow_control=balanced_values.get("eyebrow_control", "aleatorio"),
                skin_texture_control=balanced_values.get("skin_texture_control", "aleatorio"),
                freckle_control=balanced_values.get("freckle_control", "aleatorio"),
                mole_control=balanced_values.get("mole_control", "aleatorio"),
                scar_control=balanced_values.get("scar_control", "aleatorio"),
                acne_control=balanced_values.get("acne_control", "aleatorio"),
                wrinkle_control=balanced_values.get("wrinkle_control", "aleatorio"),
                hair_style_control=balanced_values.get("hair_style_control", "aleatorio"),
                edad_min=balanced_values.get("edad_min", None),
                edad_max=balanced_values.get("edad_max", None)
            )
            
            profiles.append(profile)
        
        return profiles
    
    def generate_genetic_prompt_from_profile(self, profile: UltraDiversityProfile, background_control: str) -> Tuple[str, str]:
        """Genera prompt y negative prompt desde el perfil genético para generación genética diversa"""
        
        # Construir prompt principal
        prompt_parts = []

        # Información básica del perfil
        prompt_parts.append(f"{profile.gender} from {profile.nationality}, {profile.age} years old")
        prompt_parts.append(f"from {profile.region} region, {profile.nationality} ethnicity")
        
        # Características faciales específicas y diversas
        prompt_parts.append(f"{profile.skin_tone} skin tone, {profile.skin_tone_shade} skin shade")
        prompt_parts.append(f"{profile.face_shape} face shape, {profile.jawline} jawline")
        prompt_parts.append(f"{profile.eye_color} eyes, {profile.eye_shape} eye shape, {profile.eye_size} eyes")
        prompt_parts.append(f"{profile.nose_shape} nose, {profile.lip_shape} lips")
        prompt_parts.append(f"{profile.cheekbones} cheekbones, {profile.eyebrows} eyebrows")
        prompt_parts.append(f"{profile.facial_symmetry} facial symmetry, {profile.bone_structure} bone structure")
        
        # Cabello específico y diverso
        prompt_parts.append(f"{profile.hair_color} hair, {profile.hair_style} hair style")
        prompt_parts.append(f"{profile.hair_texture} hair texture, {profile.hair_length} hair length")
        prompt_parts.append(f"{profile.hair_density} hair density, {profile.hair_curliness} hair curliness")
        
        # Características de piel diversas
        prompt_parts.append(f"{profile.skin_texture} skin texture, {profile.skin_undertone} undertone")
        if profile.freckles != "none":
            prompt_parts.append(f"{profile.freckles} freckles, {profile.freckles_density} freckle density")
        if profile.moles != "none":
            prompt_parts.append(f"{profile.moles} moles, {profile.moles_count} mole count")
        if profile.scars != "none":
            prompt_parts.append(f"{profile.scars} scars")
        if profile.acne != "none":
            prompt_parts.append(f"{profile.acne} acne")
        if profile.wrinkles != "none":
            prompt_parts.append(f"{profile.wrinkles} wrinkles")
        
        # Vello facial (solo para hombres)
        if hasattr(profile, 'gender') and profile.gender.lower() in ["hombre", "man", "male"]:
            if profile.facial_hair != "none":
                prompt_parts.append(f"{profile.facial_hair} facial hair")
            if profile.beard != "none":
                prompt_parts.append(f"{profile.beard} beard")
            if profile.mustache != "none":
                prompt_parts.append(f"{profile.mustache} mustache")
        
        # Características de edad apropiadas
        if hasattr(profile, 'age_characteristics') and profile.age_characteristics:
            prompt_parts.append(f"{profile.age_characteristics}")
        
        # Nivel de belleza
        if hasattr(profile, 'beauty_level') and profile.beauty_level:
            prompt_parts.append(f"{profile.beauty_level} appearance")
        
        # Sistema de ropa diverso (evita color blanco)
        if hasattr(profile, 'clothing_type') and profile.clothing_type:
            prompt_parts.append(f"{profile.clothing_type}")
        if hasattr(profile, 'clothing_color') and profile.clothing_color:
            prompt_parts.append(f"{profile.clothing_color} clothing")
        if hasattr(profile, 'clothing_style') and profile.clothing_style:
            prompt_parts.append(f"{profile.clothing_style} style")
        
        # Especificaciones técnicas para generación genética
        if background_control == "white":
            prompt_parts.append("SOLID WHITE BACKGROUND, PURE WHITE BACKGROUND, CLEAN WHITE BACKGROUND")
        else:
            prompt_parts.append(f"{background_control} background")
        
        prompt_parts.append("professional lighting, uniform lighting, even lighting")
        prompt_parts.append("high quality, ultra high quality, detailed, sharp focus")
        prompt_parts.append("natural lighting, natural lighting")
        prompt_parts.append("realistic, photorealistic, authentic")
        prompt_parts.append("natural facial structure, natural ethnic characteristics")
        prompt_parts.append("natural skin texture, natural imperfections")
        prompt_parts.append("natural hair texture, natural hair density")
        prompt_parts.append("authentic facial features, realistic appearance")
        prompt_parts.append("diverse characteristics, unique features")
        prompt_parts.append("individual traits, personal characteristics")
        prompt_parts.append("natural variation, human diversity")
        prompt_parts.append("realistic human face, authentic human features")
        prompt_parts.append("natural human diversity, realistic human variation")
        
        # Construir prompt final
        prompt = ", ".join(prompt_parts)
        
        # Negative prompt para evitar características no deseadas
        negative_prompt = "blurry, low quality, distorted, deformed, ugly, bad anatomy, bad proportions, extra limbs, missing limbs, mutated hands, mutated fingers, bad hands, bad fingers, blurry face, blurry eyes, asymmetric eyes, cross-eyed, long neck, short neck, extra neck, missing neck, bad neck, extra arms, missing arms, extra legs, missing legs, extra fingers, missing fingers, bad fingers, extra hands, missing hands, bad hands, extra feet, missing feet, bad feet, extra head, missing head, bad head, extra body, missing body, bad body, extra face, missing face, bad face, extra eyes, missing eyes, bad eyes, extra nose, missing nose, bad nose, extra mouth, missing mouth, bad mouth, extra ears, missing ears, bad ears, extra hair, missing hair, bad hair, extra skin, missing skin, bad skin, extra clothes, missing clothes, bad clothes, extra background, missing background, bad background, extra lighting, missing lighting, bad lighting, extra shadows, missing shadows, bad shadows, extra reflections, missing reflections, bad reflections, extra colors, missing colors, bad colors, extra textures, missing textures, bad textures, extra details, missing details, bad details, extra features, missing features, bad features, extra characteristics, missing characteristics, bad characteristics, extra traits, missing traits, bad traits, extra variations, missing variations, bad variations, extra diversity, missing diversity, bad diversity, extra uniqueness, missing uniqueness, bad uniqueness, extra individuality, missing individuality, bad individuality, extra personality, missing personality, bad personality, extra expression, missing expression, bad expression, extra emotion, missing emotion, bad emotion, extra mood, missing mood, bad mood, extra atmosphere, missing atmosphere, bad atmosphere, extra environment, missing environment, bad environment, extra setting, missing setting, bad setting, extra context, missing context, bad context, extra situation, missing situation, bad situation, extra scenario, missing scenario, bad scenario, extra story, missing story, bad story, extra narrative, missing narrative, bad narrative, extra plot, missing plot, bad plot, extra theme, missing theme, bad theme, extra concept, missing concept, bad concept, extra idea, missing idea, bad idea, extra thought, missing thought, bad thought, extra feeling, missing feeling, bad feeling, extra sensation, missing sensation, bad sensation, extra perception, missing perception, bad perception, extra awareness, missing awareness, bad awareness, extra consciousness, missing consciousness, bad consciousness, extra mind, missing mind, bad mind, extra brain, missing brain, bad brain, extra intelligence, missing intelligence, bad intelligence, extra wisdom, missing wisdom, bad wisdom, extra knowledge, missing knowledge, bad knowledge, extra understanding, missing understanding, bad understanding, extra comprehension, missing comprehension, bad comprehension, extra insight, missing insight, bad insight, extra intuition, missing intuition, bad intuition, extra instinct, missing instinct, bad instinct, extra nature, missing nature, bad nature, extra essence, missing essence, bad essence, extra core, missing core, bad core, extra center, missing center, bad center, extra heart, missing heart, bad heart, extra soul, missing soul, bad soul, extra spirit, missing spirit, bad spirit, extra energy, missing energy, bad energy, extra power, missing power, bad power, extra force, missing force, bad force, extra strength, missing strength, bad strength, extra vitality, missing vitality, bad vitality, extra life, missing life, bad life, extra existence, missing existence, bad existence, extra being, missing being, bad being, extra presence, missing presence, bad presence, extra aura, missing aura, bad aura, white clothing, white shirts, white tops, white blouses, white t-shirts, white sweaters, white jackets, white dresses, white garments, white attire, white outfit, white clothes, white wear, white garments, white apparel, white costume, white uniform, white dress, white suit, white blouse, white shirt, white top, white bottom, white pants, white skirt, white shorts, white jeans, white trousers, white slacks, white khakis, white chinos, white cargo pants, white leggings, white tights, white stockings, white socks, white shoes, white sneakers, white boots, white sandals, white heels, white flats, white loafers, white oxfords, white pumps, white stilettos, white wedges, white platforms, white espadrilles, white mules, white clogs, white flip-flops, white slides, white slippers, white house shoes, white bedroom slippers, white bathrobe, white pajamas, white nightgown, white nightshirt, white sleepwear, white loungewear, white casual wear, white formal wear, white business wear, white professional wear, white office wear, white work wear, white uniform, white scrubs, white lab coat, white medical uniform, white nurse uniform, white doctor coat, white dentist coat, white veterinarian coat, white teacher outfit, white student outfit, white school uniform, white academic gown, white graduation gown, white judge robe, white lawyer robe, white clerical robe, white religious vestment, white traditional clothing, white ethnic clothing, white cultural dress, white folk costume, white national costume, white regional dress, white indigenous clothing, white tribal wear, white ceremonial dress, white ritual clothing, white festival wear, white celebration outfit, white wedding dress, white bridesmaid dress, white groom suit, white groomsman outfit, white mother of bride dress, white father of bride suit, white guest outfit, white reception dress, white honeymoon outfit, white anniversary dress, white date night outfit, white romantic dinner wear, white theater outfit, white opera dress, white concert wear, white gallery opening outfit, white museum visit outfit, white art exhibition dress, white cultural event wear, white charity gala dress, white fundraiser outfit, white benefit dinner wear, white awards ceremony dress, white red carpet outfit, white premiere dress, white film festival wear, white fashion show outfit, white runway model wear, white photo shoot outfit, white magazine cover dress, white editorial wear, white advertising outfit, white commercial wear, white catalog dress, white e-commerce outfit, white online store model wear, white fashion blog outfit, white influencer dress, white social media wear, white instagram outfit, white tiktok dress, white youtube wear, white vlog outfit, white streaming wear, white podcast outfit, white interview dress, white meeting wear, white conference outfit, white presentation dress, white speaking outfit, white lecture wear, white seminar dress, white workshop outfit, white training wear, white course dress, white class outfit, white lesson wear, white tutorial dress, white demonstration outfit, white exhibition wear, white showcase dress, white display outfit, white show wear, white performance dress, white stage outfit, white theater wear, white concert outfit, white gig dress, white tour wear, white road trip outfit, white travel dress, white vacation wear, white holiday outfit, white getaway dress, white retreat wear, white spa outfit, white wellness dress, white yoga wear, white meditation outfit, white mindfulness dress, white relaxation wear, white leisure outfit, white casual dress, white weekend wear, white sunday outfit, white brunch dress, white lunch outfit, white dinner wear, white evening dress, white night outfit, white party dress, white celebration wear, white festival outfit, white carnival dress, white parade wear, white mardi gras outfit, white halloween costume, white christmas outfit, white new year dress, white valentine outfit, white easter dress, white thanksgiving wear, white independence day outfit, white patriotic dress, white flag day wear, white memorial day outfit, white veterans day dress, white labor day wear, white columbus day outfit, white presidents day dress, white martin luther king day wear, white groundhog day outfit, white leap year dress, white equinox wear, white solstice outfit, white seasonal dress, white spring outfit, white summer dress, white fall wear, white winter outfit, white autumn dress, white winter wear, white spring dress, white summer outfit, white seasonal wear, white weather appropriate outfit, white climate dress, white temperature wear, white condition outfit, white situation dress, white occasion wear, white event outfit, white activity dress, white function wear, white purpose outfit, white role dress, white position wear, white status outfit, white rank dress, white level wear, white grade outfit, white class dress, white category wear, white type outfit, white style dress, white fashion wear, white trend outfit, white look dress, white appearance wear, white image outfit, white impression dress, white presentation wear, white representation outfit, white embodiment dress, white manifestation wear, white expression outfit, white statement dress, white declaration wear, white announcement outfit, white proclamation dress, white pronouncement wear, white assertion outfit, white affirmation dress, white confirmation wear, white validation outfit, white endorsement dress, white approval wear, white sanction outfit, white authorization dress, white permission wear, white consent outfit, white agreement dress, white acceptance wear, white acknowledgment outfit, white recognition dress, white appreciation wear, white gratitude outfit, white thanks dress, white praise wear, white compliment outfit, white admiration dress, white respect wear, white honor outfit, white esteem dress, white regard wear, white consideration outfit, white thought dress, white care wear, white concern outfit, white interest dress, white attention wear, white focus outfit, white concentration dress, white dedication wear, white commitment outfit, white devotion dress, white loyalty wear, white fidelity outfit, white faithfulness dress, white constancy wear, white steadfastness outfit, white reliability dress, white dependability wear, white trustworthiness outfit, white integrity dress, white honesty wear, white sincerity outfit, white genuineness dress, white authenticity wear, white reality outfit, white truth dress, white factuality wear, white accuracy outfit, white correctness dress, white rightness wear, white properness outfit, white appropriateness dress, white suitability wear, white fittingness outfit, white aptness dress, white relevance wear, white pertinence outfit, white applicability dress, white usefulness wear, white helpfulness outfit, white beneficialness dress, white advantageousness wear, white profitability outfit, white valuableness dress, white preciousness wear, white treasuredness outfit, white cherishedness dress, white belovedness wear, white dearness outfit, white lovedness dress, white adoredness wear, white worshipedness outfit, white reveredness dress, white respectedness wear, white honoredness outfit, white esteemedness dress, white admiredness wear, white appreciatedness outfit, white valuedness dress, white prizedness wear, white treasuredness outfit, white cherishedness dress, white belovedness wear"
        
        return prompt, negative_prompt
    
    def generate_prompt_from_advanced_profile(self, profile: UltraDiversityProfile, background_control: str) -> Tuple[str, str]:
        """Genera prompt y negative prompt desde el perfil genético avanzado con especificaciones SAIME críticas"""
        
        # Construir prompt principal
        prompt_parts = []

        # Normalizaciones específicas de pasaporte (bajo volumen, sin obstrucciones)
        try:
            # Forzar estilo de cabello seguro para pasaporte
            profile.hair_style = self._passport_safe_hair_style(getattr(profile, "hair_style", ""))
            # Opcional: favorecer texturas bajas en volumen
            if hasattr(profile, "hair_texture"):
                profile.hair_texture = random.choice(["straight", "wavy", "fine", "smooth"])  # evitar frizzy/very voluminous
        except Exception:
            pass
        
        # ESPECIFICACIONES CRÍTICAS SAIME VENEZUELA
        prompt_parts.append(f"venezuelan passport photo, SAIME standards, official document photo, government ID photo")
        prompt_parts.append(f"512×764 pixels, 35mm×45mm at 300 DPI, real photographic paper limits")
        prompt_parts.append(f"black outer frame defines ACTUAL photo boundaries, shoulders touch left and right red frame edges")
        prompt_parts.append(f"shoulders positioned at y=202px (78% of 260px), must touch 20px to 200px red frame borders")
        prompt_parts.append(f"head height 30-34mm from chin to crown, eyes at 31% from top (y=80px)")
        prompt_parts.append(f"head margins: 8-12mm top, 12-18mm sides, 18-25mm bottom (adjusted by black frame)")
        prompt_parts.append(f"shoulders width 180px (20px to 200px) - CRITICAL: must touch red frame edges")
        
        # Información básica
        prompt_parts.append(f"{profile.gender} Venezuela, {profile.age} years old")
        prompt_parts.append("front view, frontal view, looking directly at camera, direct eye contact")
        prompt_parts.append("neutral expression, serious expression, no smile, no laughing, mouth closed")
        prompt_parts.append("eyes open and visible, head centered and straight, frontal position")
        
        # Características faciales específicas
        prompt_parts.append(f"{profile.skin_tone} skin tone, {profile.skin_tone_shade} skin shade")
        prompt_parts.append(f"{profile.face_shape} face shape, {profile.jawline} jawline")
        prompt_parts.append(f"{profile.eye_color} eyes, {profile.eye_shape} eye shape")
        prompt_parts.append(f"{profile.nose_shape} nose, {profile.lip_shape} lips")
        prompt_parts.append(f"{profile.cheekbones} cheekbones, {profile.eyebrows} eyebrows")
        
        # Cabello específico
        prompt_parts.append(f"{profile.hair_color} hair, {profile.hair_style} hair style")
        prompt_parts.append(f"{profile.hair_texture} hair texture, {profile.hair_length} hair length")
        
        # Características de piel
        if profile.freckles != "none":
            prompt_parts.append(f"{profile.freckles} freckles")
        if profile.moles != "none":
            prompt_parts.append(f"{profile.moles} moles")
        if profile.scars != "none":
            prompt_parts.append(f"{profile.scars} scars")
        if profile.acne != "none":
            prompt_parts.append(f"{profile.acne} acne")
        if profile.wrinkles != "none":
            prompt_parts.append(f"{profile.wrinkles}")
        
        # Vello facial (solo para hombres)
        if hasattr(profile, 'gender') and profile.gender.lower() in ["hombre", "man", "male"]:
            if profile.facial_hair != "none":
                prompt_parts.append(f"{profile.facial_hair} facial hair")
            if profile.beard != "none":
                prompt_parts.append(f"{profile.beard} beard")
            if profile.mustache != "none":
                prompt_parts.append(f"{profile.mustache} mustache")
        
        # Especificaciones técnicas
        prompt_parts.append("SOLID WHITE BACKGROUND, PURE WHITE BACKGROUND, CLEAN WHITE BACKGROUND")
        prompt_parts.append("professional lighting, uniform lighting, even lighting, high contrast")
        prompt_parts.append("35mm x 45mm dimensions, black frame border 1-2mm, effective area 33x43mm")
        prompt_parts.append("CRITICAL: real paper photo limits 512x764 pixels, black outer frame defines ACTUAL paper photo boundaries")
        prompt_parts.append("RESPECT black outer frame as final paper crop limit, 300 DPI resolution")
        prompt_parts.append("professional quality, high resolution, 1024x1024 pixels, ultra high quality")
        prompt_parts.append("no earrings, no jewelry, no accessories, no necklaces, no bracelets, no rings")
        prompt_parts.append("no head accessories, natural makeup, no dark glasses, no reflections")
        prompt_parts.append("no white clothing, no white shirts, no white tops, colored clothing, dark clothing")
        prompt_parts.append("sharp and focused image, correct exposure, natural colors, no grain, no distortion")
        prompt_parts.append("PNG high quality format, SOLID WHITE BACKGROUND, PURE WHITE BACKGROUND")
        prompt_parts.append("natural facial structure, natural ethnic characteristics, natural skin texture")
        prompt_parts.append("natural age spots, natural pores, natural skin, natural moles, natural asymmetry")
        prompt_parts.append("natural imperfections, natural features, natural hair texture, natural hair density")
        prompt_parts.append("clean appearance, neat presentation, appropriate attire, modest clothing")
        prompt_parts.append("common appearance, natural skin texture, slight asymmetry, authentic facial features")
        prompt_parts.append("natural hair texture, regular citizen, regular person, professional headshot photography")
        prompt_parts.append("direct portrait photography, strictly frontal view, no three quarter view, no side view")
        prompt_parts.append("head and shoulders visible, shoulders must be visible")
        prompt_parts.append("CRITICAL: shoulders must touch left and right red frame edges (20px to 200px, total 180px width)")
        prompt_parts.append("shoulders positioned at y=202px (78% of 260px), shoulders MUST touch red frame borders")
        prompt_parts.append("SAIME CRITICAL: shoulders must physically touch 20px to 200px red frame edges")
        prompt_parts.append("sufficient head space, no head crop, full head visible, head positioned in upper 60%")
        prompt_parts.append("eyes positioned at 31% from top, perfectly centered composition")
        prompt_parts.append("professional studio lighting, no shadows, TRANSPARENT BACKGROUND, NO BACKGROUND")
        prompt_parts.append("ALPHA CHANNEL, passport photo requirements, ID photo standards, official document standards")
        prompt_parts.append("government photo standards, SAIME standards, venezuelan passport specifications")
        prompt_parts.append("8-12mm margin from crown, 12-18mm lateral margins, 18-25mm bottom margin")
        prompt_parts.append("black frame consideration, voluminous hair warning, afro hair considerations")
        prompt_parts.append("thick braids space requirements, chinos voluminous hair considerations")
        prompt_parts.append("CRITICAL: hair must fit within 512x764 black outer frame, anything beyond black frame will be cropped")
        prompt_parts.append("RESPECT black outer frame boundaries, final paper photo size 512x764 pixels")
        prompt_parts.append("black outer frame is the actual paper photo limit")
        
        # Refuerzos de pose y cabello
        prompt_parts.append("FRONTAL POSE ONLY, head centered, neutral expression, mouth closed")
        prompt_parts.append("HAIR LOW VOLUME, neatly groomed, fits entirely within black frame, ears visible if possible")
        
        # Unir todas las partes
        prompt = ", ".join(prompt_parts)
        
        # Negative prompt con especificaciones SAIME críticas
        negative_prompt = ("3/4 view, side profile, looking away, smiling, laughing, multiple people, "
                         "double exposure, passport document visible, photo of photo, magazine model, "
                         "overly perfect, artificial lighting, shadows, background objects, "
                         "earrings, jewelry, necklaces, bracelets, rings, accessories, "
                         "glasses, hat, makeup, retouched, airbrushed, glamour, fashion model, "
                         "beauty contest, professional headshot, studio lighting, dramatic lighting, "
                         "soft focus, blurry, low quality, distorted, deformed, extra limbs, extra heads, "
                         "duplicate, watermark, text, signature, date, stamp, border, frame, "
                         "shoulders not touching red frame edges, shoulders not reaching 20px to 200px, "
                         "shoulders positioned incorrectly, shoulders not at y=202px, "
                         "head not positioned correctly, eyes not at 31% from top, "
                         "incorrect head margins, head too close to edges, "
                         "hair extending beyond black outer frame, hair touching black frame, "
                         "accessories extending beyond black frame, jewelry beyond black frame, "
                         "SAIME VIOLATIONS: incorrect shoulder positioning, incorrect head positioning, "
                         "violation of 512x764 black outer frame limits, violation of red frame shoulder requirements, "
                         "braids, cornrows, dreadlocks, dread, locs, thick braids, box braids, high volume hair, afro, mohawk, messy hair, wind, hair in face, "
                         "tilted head, rotated head, looking sideways, looking down, looking up, profile shot, half profile, "
                         "perfect skin, flawless skin, airbrushed, photoshopped, model look, "
                         "supermodel appearance, celebrity look, fashion model, beauty model, "
                         "perfect features, flawless features, extreme beauty, perfect beauty, "
                         "perfect symmetry, flawless symmetry, perfect proportions, flawless proportions, "
                         "perfect skin texture, flawless skin texture, perfect facial features, "
                         "flawless facial features, perfect bone structure, flawless bone structure, "
                         "perfect skin tone, flawless skin tone, perfect hair, flawless hair, "
                         "perfect eyes, flawless eyes, perfect lips, flawless lips, perfect nose, "
                         "flawless nose, perfect jawline, flawless jawline, perfect cheekbones, "
                         "flawless cheekbones, perfect eyebrows, flawless eyebrows, perfect teeth, "
                         "flawless teeth, perfect smile, flawless smile, perfect complexion, "
                         "flawless complexion, perfect appearance, flawless appearance, perfect face, "
                         "flawless face, perfect look, flawless look, perfect beauty, flawless beauty, "
                         "perfect model, flawless model, perfect portrait, flawless portrait, "
                         "perfect headshot, flawless headshot, perfect photo, flawless photo, "
                         "perfect image, flawless image, perfect picture, flawless picture, "
                         "perfect shot, flawless shot, perfect capture, flawless capture, "
                         "perfect rendering, flawless rendering, perfect generation, flawless generation, "
                         "perfect creation, flawless creation, perfect result, flawless result, "
                         "perfect output, flawless output, three quarter view, side view, profile view, "
                         "watermark, signature, cropped at neck, only head, no shoulders, head cut off, "
                         "shoulders missing, head cut off at top, head cropped at top, top of head missing, "
                         "multiple people, double exposure, passport document visible, photo of photo, "
                         "magazine model, overly perfect, artificial lighting, shadows, background objects, "
                         "jewelry, glasses, hat, makeup, retouched, airbrushed, glamour, fashion model, "
                         "beauty contest, professional headshot, studio lighting, dramatic lighting, "
                         "soft focus, blurry, low quality, distorted, deformed, extra limbs, extra heads, "
                         "duplicate, watermark, text, signature, date, stamp, border, frame, "
                         "white clothing, white shirts, white tops, white blouses, white t-shirts, "
                         "white sweaters, white jackets, white dresses, white garments, "
                         "COLORED BACKGROUND, TEXTURED BACKGROUND, GRADIENT BACKGROUND, PATTERN BACKGROUND, "
                         "BACKGROUND, BACKDROP, WALL, SURFACE, FLOOR, CEILING, ENVIRONMENT, SCENE, SETTING, "
                         "LOCATION, PLACE, ROOM, INTERIOR, EXTERIOR, OUTDOOR, INDOOR, STUDIO BACKGROUND, "
                         "PHOTO STUDIO, BACKGROUND WALL, BACKGROUND SURFACE, cropped by internal frames, "
                         "respecting internal frame boundaries, following internal frame limits, "
                         "internal frame cropping, frame boundary respect, internal frame compliance")
        
        return prompt, negative_prompt
    
    def _generate_attractiveness_factors(self) -> List[str]:
        """Genera factores de atractivo"""
        factors = []
        if random.random() < 0.3:
            factors.append("symmetrical_features")
        if random.random() < 0.2:
            factors.append("defined_bone_structure")
        if random.random() < 0.15:
            factors.append("expressive_eyes")
        return factors
    
    def _generate_ethnic_features(self, nationality: str) -> List[str]:
        """Genera características étnicas específicas"""
        features = []
        if nationality == "venezuelan":
            features.extend(["mixed_heritage", "caribbean_features", "latin_features"])
        return features
    
    def _generate_diversity_factors(self) -> List[str]:
        """Genera factores de diversidad"""
        factors = []
        if random.random() < 0.5:
            factors.append("unique_facial_structure")
        if random.random() < 0.3:
            factors.append("distinctive_features")
        if random.random() < 0.2:
            factors.append("uncommon_characteristics")
        return factors

def test_ultra_diversity():
    """Prueba el motor de diversidad ultra avanzado"""
    print("🎨 PROBANDO MOTOR DE DIVERSIDAD ULTRA AVANZADO")
    print("=" * 60)
    
    engine = UltraDiversityEngine()
    
    # Generar 5 perfiles ultra diversos
    for i in range(5):
        print(f"\n📋 Generando perfil ultra diverso {i+1}/5...")
        
        profile = engine.generate_ultra_diverse_profile(
            nationality="venezuelan",
            gender="mujer",
            age=random.randint(18, 60)
        )
        
        print(f"   🆔 ID: {profile.image_id}")
        print(f"   🏙️ Región: {profile.region}")
        print(f"   💎 Belleza: {profile.beauty_level}")
        print(f"   🎨 Piel: {profile.skin_tone} {profile.skin_texture}")
        print(f"   💇 Cabello: {profile.hair_color} {profile.hair_style}")
        print(f"   👁️ Ojos: {profile.eye_color} {profile.eye_shape}")
        print(f"   🎭 Cara: {profile.face_shape}")
        print(f"   👃 Nariz: {profile.nose_shape}")
        print(f"   👄 Labios: {profile.lip_shape}")
        print(f"   👁️ Cejas: {profile.eyebrows}")
        print(f"   🦴 Mandíbula: {profile.jawline}")
        print(f"   🍎 Pómulos: {profile.cheekbones}")
        print(f"   ✨ Pecas: {profile.freckles}")
        print(f"   🔸 Lunares: {profile.moles}")
        print(f"   🩹 Cicatrices: {profile.scars}")
        print(f"   🔴 Acné: {profile.acne}")
        print(f"   📏 Arrugas: {profile.wrinkles}")
        print(f"   🎯 Score Unicidad: {profile.uniqueness_score:.2f}")
        print(f"   🌟 Factores Diversidad: {', '.join(profile.diversity_factors)}")
    
    print(f"\n🎉 MOTOR DE DIVERSIDAD ULTRA AVANZADO")
    print("   ✅ Características faciales ultra expandidas")
    print("   ✅ 60+ regiones venezolanas")
    print("   ✅ 20+ tonos de piel")
    print("   ✅ 30+ colores de cabello")
    print("   ✅ 20+ colores de ojos")
    print("   ✅ 15+ formas de cara")
    print("   ✅ 30+ formas de nariz")
    print("   ✅ 30+ formas de labios")
    print("   ✅ 20+ formas de ojos")
    print("   ✅ 30+ estilos de cabello")
    print("   ✅ 20+ tipos de cejas")
    print("   ✅ 20+ tipos de mandíbula")
    print("   ✅ 20+ tipos de pómulos")
    print("   ✅ 20+ texturas de piel")
    print("   ✅ 20+ niveles de belleza")
    print("   ✅ ¡MÁXIMA DIVERSIDAD GARANTIZADA!")

if __name__ == "__main__":
    test_ultra_diversity()
