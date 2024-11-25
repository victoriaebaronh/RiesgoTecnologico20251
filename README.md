
# Oficios24

## Descripción del Proyecto
El proyecto **Oficios24** consiste en desarrollar una página web, escalable a dispositivos móviles, que conecte a personas que ofrecen servicios de oficios (albañiles, carpinteros, plomeros, herreros, entre otros) con usuarios que necesitan de estos servicios. 

### Funcionalidades Principales
- **Registro de trabajadores**: Los trabajadores pueden crear un perfil en el que podrán subir un anuncio detallado de sus servicios.
- **Anuncios**: Cada anuncio incluirá:
  - Descripción detallada del servicio ofrecido.
  - Fotografías del trabajo realizado.
  - Zona geográfica de atención.
  - Métodos de pago aceptados (efectivo o tarjeta).
  - Información de contacto (número de teléfono).
  - Vigencia del anuncio en la plataforma.
  - Calificación obtenida por parte de los clientes.
- **Contratación directa**: Los clientes pueden contratar fácilmente al proveedor del servicio mediante un botón de "Contratar".
- **Panel de administración**: Herramientas de gestión para supervisar y mantener la calidad del contenido.

## Instalación
Sigue los pasos para ejecutar el proyecto en tu máquina local:

1. **Clonar el repositorio**:
   ```bash
   git clone <URL del repositorio>
   cd <directorio del proyecto>
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # En Windows: myenv\Scripts\activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos**:
   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

6. Accede al proyecto desde el navegador:
   ```
   http://127.0.0.1:8000/home/
   ```

## Documentación Completa
La documentación completa del proyecto está disponible en el siguiente enlace:  
[Documentación del Proyecto](https://drive.google.com/drive/folders/1VVyAmIR5wZhjmK_LcMOSLZq4gyjHkf3g?usp=sharing)

## Tecnologías Utilizadas
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Base de datos**: SQLite

## Elaborado por:
**BitBrain**  
- Victoria Elena Barón Herrera  
- Neri Figueroa Pérez  
- Jonatan Jesús Fuentes Hernández  
- Cristian Alonso Tovar González


