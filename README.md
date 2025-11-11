# Criptografía 

## Créditos

* **Materia:** Criptografía
* **Profesor:** Dr. Alfonso Francisco De Abiega L Eglisse
* **Grupo:** 02
* **Institución:** Facultad de Ingeniería UNAM.
* **Semestre:** 2026-1

**Integrantes del equipo:**

* Roja Mares Luis Iván
* Lee Obando Ileana Verónica

## Evaluación
* Examen: 40%
* Prácticas: 60%

---

## Descripción general de implementación de algoritmos clásicos de cifrado

El presente repositorio contiene la implementación y análisis de diversos **algoritmos clásicos de cifrado**, desarrollados como parte de la asignatura **Criptografía**.
El objetivo principal es comprender el funcionamiento de los métodos tradicionales de encriptación simétrica y su relevancia histórica en el desarrollo de los sistemas modernos de seguridad de la información.

Cada algoritmo fue implementado en el lenguaje **Python**, priorizando la claridad en la lógica de cifrado y descifrado, así como la facilidad para realizar pruebas con diferentes entradas y claves.

## Objetivos de aprendizaje

* Comprender los principios fundamentales de los cifrados clásicos.
* Aplicar conocimientos de matemáticas (álgebra lineal y modular) en el ámbito criptográfico.
* Identificar las debilidades de los sistemas de cifrado histórico.
* Reconocer la evolución de los métodos de encriptación hasta los modelos modernos.

## Algoritmos

### 1. Cifrado César

### 2. Cifrado Vigenère

### 3. Cifrado Hill

### 4. Cifrado Playfair

### 5. Cifrado Vernam

### 6. Cifrado de Wheatstone

### 7. Algoritmo de euclides extendido

### 8. Reporte de Máquina Enigma

### 9. Reporte Proyecto Final

Además de los algoritmos anteriores, se incluye un **reporte explicativo** sobre la **Máquina Enigma**, dispositivo mecánico de cifrado utilizado por Alemania durante la Segunda Guerra Mundial.

---

## Estructura del repositorio

```
📂 Criptografia/
├── Cifrado de Cesar/
│   ├── cesar.py
│   └── README.md
│
├── Cifrado de Vigenere/
│   ├── vigenere.py
│   └── README.md
│
├── Cifrado de Playfair/
│   ├── playfair.py
│   └── README.md
│
├── Cifrado de Vernam/
│   ├── vernam.py
│   └── README.md
│
├── Cifrado de Hill/
│   ├── hill.py
│   └── README.md
│
├── Cifrado de Wheatstone/
│   ├── wheatstone.py
│   └── README.md
│
├── Algoritmo de euclides extendido/
│   ├── euclides_extendido.py
│   └── README.md
│
└── Reportes/
    └── Maquina_Enigma.pdf
    
```

Cada subcarpeta contiene el código fuente correspondiente a un algoritmo, junto con comentarios descriptivos y ejemplos de uso.

##  Requisitos y entorno de ejecución

* **Lenguaje:** Python 3.x
* **Librerías necesarias:**

  * `numpy` (para operaciones matriciales en el cifrado Hill)
  * `string`
  * `random`

Instalación de dependencias:

```bash
pip install numpy
```

Ejecución de un ejemplo:

```bash
python hill.py
```
