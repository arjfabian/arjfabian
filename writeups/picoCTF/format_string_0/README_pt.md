# format string 0

**Tags**: [CTF, Exploração Binária, picoCTF]  
**Dificuldade**: [Iniciante]  
**Idiomas**: [English, Español, Português]  
**Data**: 2024-11-23  

**Idiomas Disponíveis**

[![English](../../../assets/icons/flags/gb.png)](README.md)
[![Español](../../../assets/icons/flags/es.png)](README_es.md)
[![Português](../../../assets/icons/flags/pt.png)](README_pt.md)  

---

## **Introdução**

Este desafio gira em torno de **vulnerabilidades de formato de string** (**format string vulnerabilities**), uma falha de segurança em que entradas do usuário passadas para funções de saída formatada (como `printf`) são manipuladas incorretamente, potencialmente expondo dados sensíveis ou alterando o fluxo do programa. O objetivo é explorar essas vulnerabilidades para obter a flag.

### Arquivos fornecidos  

- **Binário**: [format-string-0](https://artifacts.picoctf.net/c_mimas/76/format-string-0)  
- **Código fonte**: [format-string-0.c](https://artifacts.picoctf.net/c_mimas/76/format-string-0.c)  

---

## **Detalhamento do Problema**

O programa possui duas etapas:  

1. Ajudar **Patrick** (ativar `serve_patrick()` para passar para `serve_bob()`).  
2. Ajudar **Bob** (explorar uma vulnerabilidade em `serve_bob()` para extrair a flag).  

Pontos-chave no código fonte fornecido:  

1. **Tarefa de Patrick** (`serve_patrick()`):  
   - A entrada é limitada a itens de menu predefinidos.  
   - A saída é impressa usando `printf`, criando uma potencial vulnerabilidade de formato de string.  
   - Se o comprimento da saída exceder `64` caracteres (`2 * BUFSIZE`), `serve_bob()` é chamado.  

2. **Tarefa de Bob** (`serve_bob()`):  
   - Aqui aparece outra vulnerabilidade de formato de string.  
   - Explorar corretamente permite revelar a flag armazenada na memória.  

---

## **Destaques do Código Fonte**

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

* O programa imprime a entrada do usuário diretamente com `printf`, interpretando `%` como um especificador de formato.

* Para `Gr%114d_Cheese`, `%114d` faz com que `printf` gere 114 espaços, aumentando o comprimento da saída.

### serve_bob()
```c
Copy code
char choice2[BUFSIZE];
scanf("%s", choice2);
char *menu2[3] = {"Pe%to_Portobello", "$outhwest_Burger", "Cla%sic_Che%s%steak"};

printf(choice2);
```

* De forma semelhante, a entrada do usuário com especificadores de formato (`%s`, `%d`) pode manipular o `printf`.

* O item do menu `Cla%sic_Che%s%steak` explora `%s` para imprimir memória além de `choice2`, eventualmente revelando a flag.

## Como Resolvi

### Passo 1: Passando para serve_bob()

O objetivo aqui é ativar a condição count > 64. Escolher Gr%114d_Cheese funciona porque %114d expande significativamente a string:

* Entrada: `Gr%114d_Cheese`
* Saída (aproximada): `Gr<114 espaços>Cheese`
* Comprimento: > 64 caracteres.

Isso faz com que o programa passe para `serve_bob()`.

### Passo 2: Extraindo a Flag

Agora, o objetivo é explorar `printf` em `serve_bob()` para filtrar a flag. Testando os itens do menu fornecidos:

* Pe%to_Portobello: Não afeta suficientemente o comprimento da saída.
* $outhwest_Burger: Nenhuma vulnerabilidade observável.
* Cla%sic_Che%s%steak: Explora %s para interpretar a memória da stack como strings.

Ao inserir Cla%sic_Che%s%steak, o programa gera:

```perl
Copy code
Cla%sic_Che%s%steak
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}
```

## Análise do Exploit

O especificador `%s` lê a memória apontada pelos argumentos após `choice2`.
Isso faz com que `printf` percorra locais aleatórios de memória, filtrando dados sensíveis até encontrar um byte nulo.

O manipulador de `SIGSEGV` garante que a flag seja impressa em caso de falha de segmentação.

## Lições Aprendidas

* **Tratamento Seguro de Entradas:** As vulnerabilidades de formato de string surgem quando entradas do usuário são passadas diretamente para funções como printf. Sempre valide e sanitize as entradas!

* **Entendendo os Especificadores `%`:** Exploits frequentemente dependem de aproveitar especificadores de formato (`%s`, `%d`, `%x`) para manipular o fluxo do programa ou acessar a memória.

** **Exploração Prática:** Desafios como este ilustram a importância de práticas de codificação seguras em C/C++.

## Conclusão

Este desafio foi uma introdução simples à exploração de vulnerabilidades de formato de string. Ele destaca a necessidade crítica de validar entradas e demonstra as graves consequências de vulnerabilidades aparentemente menores.

Se tiver dúvidas ou comentários, sinta-se à vontade para entrar em contato. Boa sorte e bom hacking!