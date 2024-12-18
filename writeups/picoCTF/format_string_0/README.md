# format string 0

**Tags**: [CTF, Binary Exploitation, picoCTF]  
**Difficulty**: [Beginner]  
**Languages**: [English, Español, Português]  
**Date**: 2024-11-23  

**Available Languages**

[![English](../../../assets/icons/flags/gb.png)](README.md)
[![Español](../../../assets/icons/flags/es.png)](README_es.md)
[![Português](../../../assets/icons/flags/pt.png)](README_pt.md)  

---

## **Introduction**

This challenge revolves around **format string vulnerabilities**, a security flaw where user input passed to formatted output functions (e.g., `printf`) is mishandled, potentially exposing sensitive data or altering program flow. The goal is to exploit these vulnerabilities to get the flag.

### Provided Files

- **Binary**: [format-string-0](https://artifacts.picoctf.net/c_mimas/76/format-string-0)  
- **Source**: [format-string-0.c](https://artifacts.picoctf.net/c_mimas/76/format-string-0.c)  

---

## **Problem Breakdown**

The program has two stages:

1. Help **Patrick** (trigger `serve_patrick()` to transition into `serve_bob()`).
2. Help **Bob** (exploit a vulnerability in `serve_bob()` to extract the flag).

Key points in the provided source code:

1. **Patrick's Task** (`serve_patrick()`):
   - Input is limited to predefined menu items.
   - Output is printed using `printf`, creating a potential format string vulnerability.
   - If the output length exceeds `64` characters (`2 * BUFSIZE`), `serve_bob()` is called.

2. **Bob's Task** (`serve_bob()`):
   - Another format string vulnerability appears here.
   - Exploiting it correctly reveals the flag stored in memory.

---

## **Source Code Highlights**

Here's the critical part of the source code for each stage:

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

* The program prints user input directly with `printf`, interpreting `%` as a format specifier.

* For `Gr%114d_Cheese`, `%114d` causes `printf` to output 114 spaces, increasing the output length.

### serve_bob()

```c
char choice2[BUFSIZE];
scanf("%s", choice2);
char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};

printf(choice2);
```

* Similarly, user input with format specifiers (`%s`, `%d`) can manipulate `printf`.

* The menu item `Cla%sic_Che%s%steak` exploits `%s` to print memory beyond `choice2`, eventually leaking the flag.

## How I Solved It

### Step 1: Transitioning to `serve_bob()`

The goal here is to trigger the condition `count > 64`. Choosing `Gr%114d_Cheese` works because `%114d` expands the string significantly:

* Input: `Gr%114d_Cheese`
* Output (approx.): `Gr<114 spaces>Cheese`
* Length: > 64 characters.

This transitions the program into `serve_bob()`.

### Step 2: Extracting the Flag

Now, the objective is to exploit `printf` in `serve_bob()` to leak the flag. Testing the provided menu items:

* `Pe%to_Portobello`: Does not affect the output length sufficiently.
* `$outhwest_Burger`: No observable vulnerability.
* `Cla%sic_Che%s%steak`: Exploits `%s` to interpret stack memory as strings.

By entering `Cla%sic_Che%s%steak`, the program outputs:

```perl
Cla%sic_Che%s%steak
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}
```

## Analysis of the Exploit

The `%s` specifier reads memory pointed to by arguments after `choice2`.

This causes `printf` to traverse random memory locations, leaking sensitive data until it hits a null byte.

The `SIGSEGV` handler ensures the flag is printed in case of a segmentation fault.

## Lessons Learned

* **Secure Input Handling:** Format string vulnerabilities arise when user input is directly passed to functions like `printf`. Always validate and sanitize input!

* **Understanding `%` Specifiers:** Exploits often rely on leveraging format specifiers (`%s`, `%d`, `%x`) to manipulate program flow or access memory.

* **Practical Exploitation:** Challenges like these help illustrate the importance of secure coding practices in C/C++.

## Final Thoughts

This challenge was a straightforward introduction to format string exploitation. It emphasizes the critical need for input validation and demonstrates the severe consequences of even seemingly minor vulnerabilities.

Feel free to reach out with questions or feedback. Happy hacking!