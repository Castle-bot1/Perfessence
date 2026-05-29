# PERFESSENCE

## Descripción

Perfessence es un sistema de recomendación de perfumes que utiliza una base de datos de grafos en Neo4j para generar recomendaciones personalizadas para los usuarios.

El sistema implementa dos enfoques principales:

- **Filtrado colaborativo:** recomienda perfumes basándose en las valoraciones realizadas por usuarios con gustos similares.
- **Recomendación basada en preferencias:** utiliza un cuestionario para sugerir perfumes según características seleccionadas por el usuario, como familia olfativa, ocasión de uso, intensidad y género.

La aplicación cuenta con una interfaz web desarrollada en Flask que permite interactuar fácilmente con el sistema de recomendaciones.

---

## Tecnologías Utilizadas

- Python 3.10+
- Flask
- Neo4j
- Neo4j Python Driver
- Python Dotenv
- HTML5
- CSS3
- JavaScript

---

## Arquitectura del Sistema

```text
Usuario
   │
   ▼
Interfaz Web (Flask)
   │
   ▼
Motor de Recomendación
   │
   ├── Filtrado colaborativo
   └── Recomendación basada en cuestionario
   │
   ▼
Neo4j Graph Database
```

---

## Requisitos de Software

### Requisitos mínimos

- Python 3.10 o superior
- Neo4j 5.x
- Git

### Dependencias

- Flask
- neo4j
- python-dotenv

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Castle-bot1/Perfessence.git
cd Perfessence
```

### 2. Crear un entorno virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install flask neo4j python-dotenv
```

O si existe un archivo requirements.txt:

```bash
pip install -r requirements.txt
```

---

## Configuración de Neo4j

El sistema requiere una instancia de Neo4j en ejecución.

Crear un archivo `.env` en la raíz del proyecto con la siguiente configuración:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=tu_contraseña
```

---

## Estructura del Proyecto

```text
Perfessence/
│
├── app.py
├── database.py
├── recommender.py
│
├── templates/
│   ├── index.html
│   └── test.html
│
├── static/
│   ├── app.js
│   └── test.js
│
└── Documentacion_fases/
```

### Archivos principales

| Archivo | Descripción |
|----------|-------------|
| app.py | Punto de entrada de la aplicación Flask |
| database.py | Manejo de la conexión con Neo4j |
| recommender.py | Implementación de la lógica de recomendación |
| templates/ | Plantillas HTML de la aplicación |
| static/ | Recursos estáticos y scripts JavaScript |

---

## Ejecución del Sistema

Para iniciar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en:

```text
http://localhost:5000
```

---

## Funcionamiento del Sistema de Recomendación

### Filtrado Colaborativo

Este método identifica usuarios con preferencias similares y recomienda perfumes altamente valorados por dichos usuarios.

Factores considerados:

- Valoraciones realizadas por los usuarios.
- Similitud entre perfiles.
- Popularidad de los perfumes recomendados.

### Recomendación Basada en Preferencias

Cuando un usuario no cuenta con suficiente historial de valoraciones, el sistema utiliza un cuestionario para generar recomendaciones.

Los criterios utilizados incluyen:

- Familia olfativa.
- Ocasión de uso.
- Intensidad deseada.
- Género.

A partir de estas preferencias se seleccionan los perfumes más adecuados.

---

## Integración con Otras Aplicaciones

Perfessence puede utilizarse como un motor de recomendaciones independiente mediante los endpoints expuestos por la aplicación Flask.

### Flujo de Integración

```text
Aplicación Externa
        │
        ▼
 API REST (Flask)
        │
        ▼
 Motor de Recomendación
        │
        ▼
      Neo4j
```

### Ejemplo de Consumo desde JavaScript

```javascript
fetch("http://localhost:5000/recommend", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        username: "usuario"
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Solución de Problemas

### Error de conexión con Neo4j

Verifique que:

- El servicio Neo4j esté en ejecución.
- Las credenciales configuradas en el archivo `.env` sean correctas.
- El puerto 7687 esté habilitado.

### Error por dependencias faltantes

Ejecute:

```bash
pip install flask neo4j python-dotenv
```

---

## Posibles Mejoras Futuras

- Incorporar técnicas de aprendizaje automático para mejorar la precisión de las recomendaciones.
- Implementar autenticación y gestión de usuarios.
- Exponer una API documentada con Swagger/OpenAPI.
- Desplegar el sistema mediante Docker.

---

## Autores

Proyecto desarrollado por el equipo **Perfessence** como sistema de recomendación de perfumes utilizando bases de datos de grafos y técnicas de recomendación personalizadas.

Diego Castillo - 25779
Edgar Guevara - 251154
Héctor Duarte - 25939