🐍 Gestor de Contactos en Python

Este proyecto, desarrollado como entrega final para el curso de Python de **Rocket Girls Costa Rica**, es una aplicación de consola que permite gestionar una agenda de contactos de forma local.

El programa aplica conceptos fundamentales como el manejo de archivos para guardar los datos de forma permanente, la modularización con funciones para un código limpio, y la gestión de errores para ofrecer una experiencia de usuario robusta y funcional.


📋1. Características y Funcionalidades

Este proyecto implementa todos los requisitos solicitados y añade mejoras de validación para asegurar la calidad de los datos y la usabilidad del programa.

💾 1.1 Gestión de Contactos

*   **Agregar Contacto:** Permite registrar nuevos contactos con validaciones clave para garantizar la integridad de los datos:
    *   ✔️ **Nombre Obligatorio:** Se valida que el campo del nombre no puede estar vacío.
    *   ✔️ **Medio de Contacto Requerido:** Se asegura que cada contacto tenga al menos un **teléfono** o un **correo electrónico**.
    *   ✔️ **Validación "Justo a Tiempo":** Las validaciones se realizan inmediatamente, cancelando la operación si un campo obligatorio es incorrecto para no hacer perder tiempo al usuario.

*   **Listar Contactos:** Muestra una lista completa de todos los contactos guardados.
    *   ⭐ **Mejora de Usabilidad:** La lista se presenta siempre **ordenada alfabéticamente** para una fácil visualización y con un formato claro.

*   **Buscar Contacto:** Permite encontrar contactos específicos.
    *   ⭐ **Mejora de Usabilidad:** La búsqueda se puede realizar por **nombre completo o parcial** y no distingue entre mayúsculas y minúsculas.

💾 1.2. Gestión de Agenda

*   **Fecha de Reunión Opcional:** Al agregar un contacto, el programa pregunta explícitamente al usuario (`si/no`) si desea añadir una fecha de reunión, ofreciendo mayor flexibilidad.
*   **Actualizar Fecha:** Permite modificar la fecha de un contacto existente.
    *   Se busca el contacto por su **nombre exacto**.
    *   **Si el contacto no se encuentra, se informa al usuario con un mensaje de error.** (Esta es la corrección al error lógico).
*   ✔️ **Formato de Fecha Estricto:** Tanto al crear como al actualizar, se valida que el formato de la fecha sea `DD MM AAAA`, garantizando la consistencia de los datos.

💾 1.3 Experiencia de Usuario y Robustez

*   **Menú Interactivo:** La navegación se realiza a través de un menú de opciones claro y persistente.
*   **Interfaz Limpia:** La pantalla de la consola se limpia (`os.system`) en cada ciclo del menú para una presentación ordenada.
*   **Manejo de Errores de Archivo:** Si el archivo `contactos.txt` no existe al iniciar, el programa lo crea automáticamente (`try/except`), evitando que la aplicación se detenga.


✔️ 2. Ejemplo del menú principal

===== Gestor de Contactos =====
1. Agregar contacto
2. Listar contactos
3. Buscar contacto por nombre
4. Actualizar fecha de reunión
5. Salir
===============================
Elige una opción:


💾 3. Persistencia de datos

Toda la información se almacena en el archivo:

contactos.txt

Si el archivo no existe, se crea automáticamente al iniciar el programa.

Cada contacto ocupa una línea.

Los campos están separados por punto y coma ;.

📌 Ejemplo real del archivo:

Floricienta;+56 8963578210;Flo;5 freidoras en alquiler para stand;14 12 2025
Manuela Fernandez;+89 563957129;;Interesado en 45 freidoras;19 11 2025
Maria Gomez;+56 2262 3665812;maria56@outlook.com;;
Tai Comportena;+56 35987110;Comportena11@gmail.com;45 freidoras;10 12 2025
Tai Rodea;+96 2369542;RodeaT@gmail.com;;14 12 2025


🏗️ 4. Arquitectura del programa

El programa está dividido en funciones para mantener claridad y reutilización.

Principales módulos internos:

cargar_contactos() → Lee archivo y convierte cada línea en diccionario

guardar_contactos() → Sobrescribe el archivo con la lista actual

agregar_contacto() → Validaciones + creación de contacto

listar_contactos() → Muestra contactos ordenados

buscar_contacto() → Busca coincidencias de texto

actualizar_contacto() → Modifica solo la fecha de un contacto específico

pedir_fecha_valida() → Valida formato DD MM AAAA

main() → Control del programa y del menú


📁 5. Estructura del proyecto

Proyecto_agenda_contactos_inicial.py/ 
│
├── agenda_contactos_inicial.py     ← Archivo principal del programa
├── contactos.txt                   ← Archivo de datos persistentes
├── README.md                       ← Documentación del proyecto
├── Proyecto Planteamiento.pdf      ← Enunciado del proyecto (Original)
├── Guion Tecnico.pdf               ← Planif. demo técnica
└── Guion Funcional.pdf             ← Planif. demo funcionalpráctica


▶️ 6. Cómo ejecutar el programa

Requisitos

Python 3.8 o superior

No requiere librerías adicionales

Ejecución

En la terminal, dentro de la carpeta del proyecto:

python agenda_contactos_inicial.py

Si el archivo contactos.txt no existe, el programa lo crea automáticamente.


🚀 7. Mejoras futuras (Opcional, no obligatorio)

Implementar versión POO con clases (Contacto, Agenda)

Agregar opción para eliminar contactos

Exportar contactos en formato CSV o JSON

Filtrar por fecha próxima de reunión

Integrar colores en consola para mejor interfaz

Agregar sistema de backup automático

🎥 8. Video de demostración

El proyecto incluye un video donde se muestra:

Revisión del código

Ejecución del programa

Agregar un contacto

Listar contactos

Buscar por nombre

Actualizar la fecha

Este video cumple con los requisitos del planteamiento del proyecto.

🎉 9. Conclusión

Este proyecto implementa un gestor de contactos completo, profesional y totalmente funcional utilizando únicamente Python estándar.

Incluye manejo de archivos, validaciones avanzadas, menú interactivo y una estructura clara basada en funciones.
