
import random
import string
import time
import sys
import os

# Colores ANSI para Windows 10/11 y terminales modernas
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def ejecutar():
    limpiar()
    

    # 1. ESCANEO
    for i in range(101):
        barra = "█" * (i // 5) + "░" * (20 - i // 5)
        print(
            f"\r{VERDE}INICIANDO ESCANEO: "
            f"[{barra}] {i}%{RESET}",
            end="",
            flush=True
        )
        time.sleep(0.2)

    print(f"\n\n{VERDE}Escaneo terminado.{RESET}\n")
    time.sleep(2)

    # 2. MENSAJES CON SENTIDO
    mensajes = [
        "[SISTEMA] Iniciando conexión segura...",
        "[RED] Analizando paquetes de datos...",
        "[ESCANEO] Buscando dispositivos conectados...",
        "[SEGURIDAD] Comprobando protocolos...",
        "[DATOS] Analizando archivos del sistema...",
        "[RED] Verificando dirección IP...",
        "[SISTEMA] Proceso ejecutado correctamente.",
        "[SEGURIDAD] No se detectaron amenazas.",
        "[ANALISIS] Recopilando información...",
        "[ESTADO] Conexión establecida."
    ]

    for mensaje in mensajes:
        hora = time.strftime("%H:%M:%S")
        print(f"{VERDE}[{hora}] {mensaje}{RESET}")
        time.sleep(0.7)

    print(f"\n{VERDE}Iniciando flujo de datos...{RESET}\n")
    time.sleep(1)

    # 3. LETRAS ALEATORIAS INFINITAS
    try:
        while True:
            linea = "".join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=150
                )
            )
            print(f"{VERDE}{linea}{RESET}")
            time.sleep(0.000001)

    except KeyboardInterrupt:
        print(f"\n{RESET}Proceso detenido correctamente.")

if __name__ == "__main__":
    try:
        ejecutar()
    except Exception as error:
        print(f"\n{ROJO}Error: {error}{RESET}")
        input("Pulsa Enter para salir...")
