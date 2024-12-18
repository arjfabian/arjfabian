# format string 0

**Etiquetas**: [CTF, Explotación Binaria, picoCTF]  
**Dificultad**: [Principiante]  
**Idiomas**: [English, Español, Português]  
**Fecha**: 2024-11-23  

**Idiomas Disponibles**

[![English](../../../assets/icons/flags/gb.png)](README.md)
[![Español](../../../assets/icons/flags/es.png)](README_es.md)
[![Português](../../../assets/icons/flags/pt.png)](README_pt.md)  

---

## **Introducción**

Este desafío se centra en las **vulnerabilidades de cadenas de formato** (**format string vulnerabilities**), una falla de seguridad en la que la entrada del usuario pasada a funciones de salida formateada (como `printf`) se maneja incorrectamente, lo que puede exponer datos sensibles o alterar el flujo del programa. El objetivo es explotar estas vulnerabilidades para obtener la bandera.

### Archivos proporcionados  

- **Binario**: [format-string-0](https://artifacts.picoctf.net/c_mimas/76/format-string-0)  
- **Código fuente**: [format-string-0.c](https://artifacts.picoctf.net/c_mimas/76/format-string-0.c)  

---

## **Desglose del problema**

El programa tiene dos etapas:  

1. Ayudar a **Patrick** (activar `serve_patrick()` para pasar a `serve_bob()`).  
2. Ayudar a **Bob** (explotar una vulnerabilidad en `serve_bob()` para extraer la bandera).  

Puntos clave del código fuente proporcionado:  

1. **Tarea de Patrick** (`serve_patrick()`):  
   - La entrada está limitada a elementos de menú predefinidos.  
   - La salida se imprime usando `printf`, lo que crea una posible vulnerabilidad de cadena de formato.  
   - Si la longitud de la salida supera los `64` caracteres (`2 * BUFSIZE`), se llama a `serve_bob()`.  

2. **Tarea de Bob** (`serve_bob()`):  
   - Aquí aparece otra vulnerabilidad de cadena de formato.  
   - Explorarla correctamente permite revelar la bandera almacenada en memoria.  

---

## **Puntos clave del código fuente**

### serve_patrick()

```c
char choice1[BUFSIZE];
scanf("%s", choice1);
char *menu1[3] = {"Breakf@st_Burger", "Gr%114d_Cheese", "Bac0n_D3luxe"};

int count = printf(choice1);
if (count > 2 * BUFSIZE) {
    serve_bob();
}
```

* El programa imprime la entrada del usuario directamente con `printf`, interpretando `%` como un especificador de formato.

* Para `Gr%114d_Cheese`, `%114d` hace que `printf` genere 114 espacios, aumentando la longitud de la salida.

### serve_bob()

```c
Copy code
char choice2[BUFSIZE];
scanf("%s", choice2);
char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};

printf(choice2);
```

* De manera similar, la entrada del usuario con especificadores de formato (`%s`, `%d`) puede manipular `printf`.
* El elemento del menú `Cla%sic_Che%s%steak` explota `%s` para imprimir memoria más allá de choice2, revelando eventualmente la bandera.

## Cómo lo resolví

### Paso 1: Pasar a `serve_bob()`

El objetivo aquí es activar la condición `count > 64`. Elegir `Gr%114d_Cheese` funciona porque `%114d` expande significativamente la cadena:

* Entrada: `Gr%114d_Cheese`
* Salida (aproximada): `Gr<114 espacios>Cheese`
* Longitud: > 64 caracteres.

Esto hace que el programa pase a `serve_bob()`.

### Paso 2: Extraer la bandera

Ahora, el objetivo es explotar `printf` en `serve_bob()` para filtrar la bandera. Probando los elementos del menú proporcionados:

* `Pe%to_Portobello`: No afecta suficientemente la longitud de la salida.
* `$outhwest_Burger`: No muestra ninguna vulnerabilidad observable.
* `Cla%sic_Che%s%steak`: Explota %s para interpretar la memoria del stack como cadenas.
Ingresando `Cla%sic_Che%s%steak`, el programa genera:

```perl
Cla%sic_Che%s%steak
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}
```

## Análisis del exploit

* El especificador `%s` lee la memoria apuntada por argumentos posteriores a choice2.
* Esto hace que `printf` recorra ubicaciones de memoria aleatorias, filtrando datos sensibles hasta encontrar un byte nulo.

El handler `SIGSEGV` asegura que la bandera se imprima en caso de una falla de segmentación.

## Lecciones aprendidas

* **Manejo seguro de entradas:** Las vulnerabilidades de cadenas de formato surgen cuando se pasa directamente la entrada del usuario a funciones como `printf`. ¡Siempre valida y sanitiza la entrada!

* **Entendiendo los especificadores `%`:** Los exploits a menudo se basan en aprovechar especificadores de formato (`%s`, `%d`, `%x`) para manipular el flujo del programa o acceder a la memoria.

* **Explotación práctica:** Desafíos como este ilustran la importancia de prácticas de codificación seguras en C/C++.

## Conclusión

Este desafío fue una introducción sencilla a la explotación de cadenas de formato. Enfatiza la necesidad crítica de validar la entrada y demuestra las graves consecuencias de vulnerabilidades aparentemente menores.

Si tienes preguntas o comentarios, no dudes en escribirme. ¡Feliz hacking!