# Criptografía 

## Créditos

* **Materia:** Criptografía
* **Profesor:** Dr. Alfonso Francisco De Abiega L Eglisse
* **Institución:** Facultad de Ingeniería UNAM.
* **Semestre:** 2026-1

**Integrantes del equipo:**

* Roja Mares Luis Iván
* Lee Obando Ileana Verónica

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

### 2.1 Cifrado César

### 2.2 Cifrado Vigenère

### 2.3 Cifrado Hill

### 2.4 Cifrado Playfair

### 2.5 Cifrado Vernam

### 2.6 Máquina Enigma

Además de los algoritmos anteriores, se incluye un **reporte explicativo** sobre la **Máquina Enigma**, dispositivo mecánico de cifrado utilizado por Alemania durante la Segunda Guerra Mundial.


## Estructura del repositorio

```
📂 Criptografia/
├── cesar/
│   └── cesar.py
├── vigenere/
│   └── vigenere.py
├── hill/
│   └── hill.py
├── playfair/
│   └── playfair.py
├── vernam/
│   └── vernam.py
└── reportes/
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
