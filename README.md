# FirstReflexPage

**Enmanuel Molina Abreu**  
Análisis y Diseño de Reportes — 5to B de Informática  
Colegio Apec Fernando Arturo de Meriño  

---

## Descripción del Proyecto

Primera página web desarrollada con **[Reflex](https://reflex.dev)**, un framework moderno que permite construir aplicaciones web completas usando únicamente Python, sin necesidad de escribir JavaScript.

La app incluye:
- Título principal personalizado
- Texto de bienvenida
- Botón interactivo que cambia el estado al hacer clic

---

## Requisitos Previos

Antes de comenzar asegúrate de tener instalado:

- [Python 3.10 o superior](https://www.python.org/downloads/) (Reflex no es compatible con Python 3.14+)
- [Poetry](https://python-poetry.org/) — gestor de entornos y dependencias
- [Git](https://git-scm.com/)
- [Node.js 20.19.0 o superior](https://nodejs.org/) — requerido por Reflex

---

## Instrucciones de Instalación

### Paso 1 — Clonar el repositorio

Abre CMD o PowerShell y ejecuta:

```bash
git clone https://github.com/molinaenmanuel32/FirstReflexPage.git
cd FirstReflexPage
```

### Paso 2 — Verificar que tienes Poetry

```bash
poetry --version
```

Si no lo tienes, instálalo con:

```bash
pip install poetry
```

### Paso 3 — Revisar el archivo `pyproject.toml`

Antes de continuar, asegúrate de que el archivo `pyproject.toml` tenga:

- Un **email válido** (no el servidor de la computadora)
- La versión de Python correcta

Debe verse así:

```toml
[project]
name = "firstreflexpage"
version = "0.1.0"
authors = [
    {name = "Enmanuel", email = "tucorreo@gmail.com"}
]
requires-python = ">=3.10,<4.0"
```

> Advertencia: Si el email tiene el nombre del servidor de tu máquina (ejemplo: `usuario@LAPTOP-XXXXX`) o la versión de Python es `>=3.14`, corrígelo antes de continuar o te saldrá un error.

### Paso 4 — Instalar las dependencias con Poetry

```bash
poetry install
```

### Paso 5 — Activar el entorno virtual de Poetry

```bash
poetry env activate
```

Copia el comando que te genere y pégalo en la terminal. Se verá algo así:

```bash
& "C:\...\FirstReflexPage\.venv\Scripts\activate.ps1"
```

> Advertencia: Si Windows bloquea la ejecución del script, ejecuta primero:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Escribe `S` cuando te pregunte y presiona Enter. Luego vuelve a pegar el comando.

Sabrás que el entorno está activo cuando veas esto al inicio de la línea:

```
(firstreflexpage) PS C:\...>
```

### Paso 6 — Inicializar Reflex

```bash
reflex init
```

Cuando aparezca el menú, selecciona la opción **0** para empezar desde cero con una app en blanco.

---

## Cómo Ejecutar la Aplicación

```bash
reflex run
```

Abre tu navegador y ve a:

```
http://localhost:3000
```

Reflex recarga automáticamente cualquier cambio de código en tiempo real, no hace falta reiniciar el servidor cada vez que edites.

---

## Estructura del Proyecto

```
FirstReflexPage/
├── firstreflexpage/
│   ├── __init__.py
│   └── firstreflexpage.py   # Código principal de la app
├── rxconfig.py              # Configuración de Reflex
├── pyproject.toml           # Configuración de Poetry
├── .gitignore
└── README.md
```

---

## Guardar cambios en GitHub

Cada vez que hagas cambios importantes, guarda tu progreso con:

```bash
git add .
git commit -m "descripción de los cambios"
git push origin main
```

---

## Recursos Oficiales

- [Documentación de Reflex](https://reflex.dev/docs/getting-started/introduction/)
- [Instalación de Reflex](https://reflex.dev/docs/getting-started/installation/)
- [Librería de componentes](https://reflex.dev/docs/library/)

---

*Proyecto académico — Santo Domingo, D.N. — Mayo 2026*
