import random
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Cargar palabras
with open("palabras.txt", "r", encoding="utf-8") as f:
    palabras = [line.strip() for line in f.readlines()]

# Gráfico del ahorcado
ahorcado = [
    "",
    " O ",
    " O \n | ",
    " O \n/| ",
    " O \n/|\\ ",
    " O \n/|\\ \n/  ",
    " O \n/|\\ \n/ \\ "
]

# Niveles: (longitud máxima de palabra, intentos)
niveles = {"F": (6, 8), "M": (10, 6), "D": (15, 4)}

# Archivo de puntuaciones
score_file = "scores.json"
if not os.path.exists(score_file):
    with open(score_file, "w") as f:
        json.dump([], f)

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "▢" for letra in palabra])

def mostrar_barra_vida(intentos, total):
    return Fore.RED + "❤️" * intentos + Fore.BLACK + "🖤" * (total - intentos)

def guardar_puntuacion(nombre, puntos):
    try:
        with open(score_file, "r") as f:
            scores = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        scores = []

    # Revisa si el usuario ya existe
    usuario_existente = next((s for s in scores if s["nombre"] == nombre), None)
    if usuario_existente:
        # Actualiza solo si la nueva puntuación es mayor
        if puntos > usuario_existente["puntos"]:
            usuario_existente["puntos"] = puntos
    else:
        # Agrega nuevo jugador
        scores.append({"nombre": nombre, "puntos": puntos})

    # Ordena y mantiene top 5
    scores = sorted(scores, key=lambda x: x["puntos"], reverse=True)[:5]

    with open(score_file, "w") as f:
        json.dump(scores, f)

def mostrar_ranking():
    try:
        with open(score_file, "r") as f:
            scores = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        scores = []

    print(Fore.CYAN + "\n🏆 Ranking Top 5:")
    for i, s in enumerate(scores, start=1):
        print(f"{i}. {s['nombre']} - {s['puntos']} pts")

def jugar():
    # Elegir el nivel
    nivel = input("Elige nivel: Fácil (F), Medio (M), Difícil (D): ").upper()
    if nivel not in niveles:
        nivel = "M"
    max_len, total_intentos = niveles[nivel]

    # Limite de pistas según nivel
    max_pistas = {"F": 1, "M": 2, "D": 3}[nivel]
    pistas_usadas = 0

    # Mostrar Nro. de pistas antes del input
    print(Fore.CYAN + f"💡 Pistas disponibles: {max_pistas}\n")

    # Solicita nombre del jugador
    nombre = input("Ingresa tu nombre: ")

    palabras_filtradas = [p for p in palabras if len(p) <= max_len]
    palabra = random.choice(palabras_filtradas).upper()
    intentos = total_intentos
    letras_adivinadas = set()
    puntos = 0

    print(Fore.CYAN + Style.BRIGHT + "\n🎮 ¡Bienvenido al Juego de Adivinanza! 🎮")
    print(Fore.YELLOW + f"Tienes {total_intentos} intentos para adivinar la palabra.\n")

    max_pasos = len(ahorcado) - 1  # gráfico dinámico

    while intentos > 0:
        print(mostrar_palabra(palabra, letras_adivinadas))
        print("Intentos:", mostrar_barra_vida(intentos, total_intentos))

        # calcular indice para el gráfico
        indice = (max_pasos * (total_intentos - intentos)) // total_intentos
        print(Fore.MAGENTA + ahorcado[indice], "\n")

        letra = input("🔤 Ingresa una letra (o '?' para pista): ").upper()

        if letra == "?":
            if pistas_usadas < max_pistas:
                pista = random.choice([l for l in palabra if l not in letras_adivinadas])
                print(Fore.BLUE + f"💡 Pista: una letra de la palabra es '{pista}'")
                pistas_usadas += 1
                print(Fore.BLUE + f"💡 Te quedan {max_pistas - pistas_usadas} pista(s) disponibles.\n")
            else:
                print(Fore.RED + "⚠️ Ya no te quedan pistas disponibles.\n")
            continue

        if letra in letras_adivinadas:
            print(Fore.MAGENTA + "⚠️  Ya intentaste esa letra. Intenta otra.\n")
            continue

        letras_adivinadas.add(letra)

        if letra in palabra:
            print(Fore.GREEN + "🎯 ¡Correcto!\n")
            puntos += 10
        else:
            print(Fore.RED + "❌ Incorrecto\n")
            intentos -= 1
            puntos -= 2

        palabra_actual = mostrar_palabra(palabra, letras_adivinadas)
        if "_" not in palabra_actual and "▢" not in palabra_actual:
            print(Fore.GREEN + Style.BRIGHT + f"🏆 ¡Felicidades! Adivinaste la palabra: {palabra}")
            puntos += intentos * 5
            break
    else:
        print(Fore.RED + Style.BRIGHT + f"👾 Se acabaron los intentos. La palabra era: {palabra}")

    print(Fore.YELLOW + f"\n🎯 Puntos obtenidos: {puntos}")
    guardar_puntuacion(nombre, puntos)
    mostrar_ranking()

if __name__ == "__main__":
    while True:
        jugar()
        respuesta = input("\n¿Quieres jugar otra vez? (S/N): ").upper()
        if respuesta != "S":
            print(Fore.CYAN + "\n👋 ¡Gracias por jugar! Hasta la próxima.")
            break
