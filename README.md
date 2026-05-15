# POO_Encapsulamiento

## Proyecto Animales 🐾

## Descripción

Este proyecto es una práctica de Programación Orientada a Objetos (POO) en Python, enfocada en el concepto de encapsulamiento y herencia.
Se implementa una clase base Animal y clases derivadas (Gato, Perro, Loro) que heredan sus propiedades y métodos, agregando comportamientos propios.

## 📂 Organización del proyecto

Proyecto_animales/
│
├── animal.py          # Clase base Animal
├── gato.py            # Clase Gato (hereda de Animal)
├── perro.py           # Clase Perro (hereda de Animal)
├── loro.py            # Clase Loro (hereda de Animal)
├── utils.py           # Funciones auxiliares (mostrar, buscar, etc.)
├── config.py          # Constantes y configuraciones globales
├── main.py            # Punto de entrada del programa
│
├── tests/             # Carpeta para pruebas unitarias
│   └── test_animales.py
│
└── README.md          # Documentación del proyecto

## 🚀 Ejecución
Para correr el programa principal:

python main.py

## 🧪 Pruebas
Ejemplo de prueba con pytest:

pytest tests/

