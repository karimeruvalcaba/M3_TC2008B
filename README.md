# 🚦 M3_TC2008B

Este proyecto simula un sistema inteligente de gestión del tráfico donde los semáforos responden dinámicamente a los vehículos cercanos. La simulación utiliza modelos basados en agentes para replicar el comportamiento del tráfico en el mundo real y explora cómo la comunicación descentralizada entre vehículos puede mejorar el flujo vehicular.

## ✨ Características

- **🚥 Semáforos Dinámicos**: Los semáforos se adaptan al comportamiento de los vehículos ajustando sus horarios en función del tiempo estimado de llegada.
- **🚗🛵 Comportamiento de Agentes**:
  - Autos con estados personalizables (por ejemplo, color rojo para estados 'enojados').
  - Motocicletas, Camiones y Autos como agentes adicionales con comportamientos únicos.
- **🎮 Integración de Teoría de Juegos**:
  - Implementa una estrategia de negociación basada en la Teoría de Juegos.
  - Incluye una matriz de recompensas y análisis de equilibrio de Nash.
- **📡 Comunicación Descentralizada**:
  - Los vehículos se comunican utilizando esquemas simples de intercambio de información.
  - Promueve comportamientos no cooperativos para probar estrategias de negociación.
- **🗺️ Búsqueda de Rutas**:
  - Utiliza el algoritmo A* para planificar rutas óptimas en escenarios de tráfico complejos.

## 📂 Estructura de Archivos

- **`server.py`**: 🖥️ Administra el backend de la simulación, procesando las interacciones entre agentes y los horarios de los semáforos.
- **`model.py`**: 🛠️ Define el modelo central de la simulación, incluida la configuración del entorno y la lógica del tráfico.
- **`agent.py`**: 🤖 Contiene las clases de agentes, como `CarAgent` y `MotorcycleAgent`, junto con sus comportamientos.
- **`map.py`**: 🗺️ Administra la red vial y el mapeo de intersecciones, asegurando una correcta gestión de rutas y carriles.
- **`aStar.py`**: ⭐ Implementa el algoritmo A* para la optimización de rutas.

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/simulacion-trafico.git
   cd simulacion-trafico
  ``
## ⚙️ Instalación

1. **Instala las dependencias necesarias**:
   ```bash
   pip install mesa
   ``
   ``
  ## 🚗 Resumen de la Simulación

1. **🏙️ Diseño de Intersecciones**:
   - Simula intersecciones con múltiples carriles y semáforos inteligentes.
   - Aplica reglas sobre cuándo los vehículos pueden moverse en función del estado del semáforo.

2. **📜 Reglas de Tráfico**:
   - Ejemplos de reglas incluyen:
     - Los autos que parten de posiciones específicas solo pueden moverse cuando su semáforo asignado está en verde.
     - Los semáforos en ciertas intersecciones pueden no cambiar nunca a verde para direcciones específicas.

3. **🤝 Interacción entre Agentes**:
   - Incluye comportamientos no cooperativos y basados en razonamiento para analizar la eficiencia de diferentes estrategias.

4. **🎥 Animación**:
   - Visualización en tiempo real del movimiento de vehículos a través de las intersecciones.

## 🛠️ Cómo Usar

1. **🔧 Personalizar Agentes**:
   - Modifica los parámetros de los agentes en `agent.py` para ajustar sus comportamientos o añadir nuevos tipos.

2. **🗺️ Ajustar Configuración del Mapa**:
   - Actualiza las redes viales y las intersecciones en `map.py`.

3. **▶️ Ejecutar la Simulación**:
   - Ejecuta el script del servidor para iniciar la "server.py" y ver los resultados.


