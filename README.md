# Juego de Adivinanza de Palabras

Juego de consola en Python donde debes **adivinar una palabra letra por letra** antes de quedarte sin intentos.
Cuenta con gráficos ASCII, puntaje, ranking Top 5 y pistas limitadas según la dificultad.

------------------------------------------------

## 🚀 Cómo jugar

1. Clona el repositorio:

git clone https://github.com/tu-usuario/juego-adivinanza.git
cd juego-adivinanza

2. Crea un entorno virtual e instala dependencias:

3. Ejecuta el juego:

python juego.py

------------------------------------------------

## 🎯 Mecánica del juego

- Elige un nivel de dificultad:

Nivel      | Intentos | Pistas
-----------|----------|-------
Fácil (F)  | 8        | 1
Medio (M)  | 6        | 2
Difícil (D)| 4        | 3

- Ingresa tu nombre y comienza a adivinar letra por letra.
- Usa una pista escribiendo `?` (solo disponible según el nivel).
- Cada letra correcta suma puntos, cada error resta puntos.
- Los intentos restantes al adivinar la palabra dan puntos extra.

------------------------------------------------

## 🏆 Ranking y puntuación

- Se guarda automáticamente un **ranking Top 5** en `scores.json`.
- Si un jugador repite, se **actualiza su puntuación solo si es mayor**.

Ejemplo de ranking:

🏆 Ranking Top 5:
1. Frank  - 120 pts
2. Ana    - 95 pts
3. Luis   - 88 pts
4. Juan   - 75 pts
5. Carla  - 60 pts

------------------------------------------------

## 🖥 Características

- Gráficos ASCII para mostrar los intentos restantes.
- Barra de vida con corazones coloridos: ❤️🖤
- Mensajes y pistas con colores usando `colorama`.
- Opción de jugar varias partidas consecutivas sin reiniciar el juego.
- Pistas limitadas y visualización de cuántas quedan.
- Mantiene el Top 5 actualizado.

------------------------------------------------

```bash
📂 Estructura del proyecto
juego-adivinanza/
├─ juego.py         # Código principal
├─ palabras.txt     # Lista de palabras para el juego
├─ scores.json      # Archivo de ranking
├─ LICENSE
└─ README.md

------------------------------------------------

## 🤝 Contribuciones

Si quieres mejorar el juego, agregar palabras o nuevas funcionalidades, ¡las contribuciones son bienvenidas!

1. Haz un fork del repositorio.
2. Crea tu rama:

git checkout -b feature/nueva-funcion

3. Haz commit de tus cambios:

git commit -m 'Agrega nueva función'

4. Envía un pull request.

------------------------------------------------

## 📜 Licencia

Este proyecto está bajo la **licencia MIT**.
Puedes ver el archivo completo [aquí](LICENSE)
