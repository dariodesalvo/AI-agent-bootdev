# 🤖 Build an AI Agent (en construcción)

Este proyecto forma parte del curso **Build an AI Agent** de [Boot.dev](https://www.boot.dev).  
El objetivo es construir una versión simplificada de un editor con capacidades de IA, similar a **Claude Code** o **Cursor**, utilizando la **API gratuita de Google Gemini**.

## 🚧 Estado del proyecto
> **En desarrollo** – actualmente configurando la estructura base del CLI y las funciones del agente.

## 🧠 ¿Qué hará el agente?
El programa será una herramienta de línea de comandos (CLI) que:
- Acepta una tarea de programación (por ejemplo: _"las cadenas no se dividen en mi app, por favor ayúdame 🥺👉🏽👈🏽"_).
- Selecciona entre un conjunto de funciones predefinidas, como:
  - Escanear archivos de un directorio.
  - Leer el contenido de un archivo.
  - Sobrescribir el contenido de un archivo.
  - Ejecutar un archivo Python.
- Repite el proceso hasta completar la tarea (o fallar  😅).
