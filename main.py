import curses
from functions import *
import sys

users_data()

def opcion1():
    # Acciones para la opción 1
    economics_data()
    percentage()

def opcion2():
    # Acciones para la opción 2
    montly_budget()

def opcion3():
    # Acciones para la opción 3
    sys.exit()

def main(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    
    while True:#Bucle que engloba todo el menú
        # Configuración inicial
        opcion_actual = 0
        opciones = ["Gastos mensuales", "Presupuesto mensual", "Salir"]
        funciones = {0: opcion1, 1: opcion2, 2: opcion3}
        stdscr.clear()

        while True:
            stdscr.clear()

            # Imprime las opciones
            for i, opcion in enumerate(opciones):
                if i == opcion_actual:
                    stdscr.addstr(i, 0, f"> {opcion}", curses.A_REVERSE)
                else:
                    stdscr.addstr(i, 0, f"  {opcion}")

            # Captura la entrada del teclado
            key = stdscr.getch()

            # Maneja la navegación
            if key == curses.KEY_UP:
                opcion_actual = (opcion_actual - 1) % len(opciones)
            elif key == curses.KEY_DOWN:
                opcion_actual = (opcion_actual + 1) % len(opciones)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                curses.endwin()
                funciones[opcion_actual]()  # Llama a la función asociada a la opción seleccionada
                stdscr.getch()
                break
            

curses.wrapper(main)


