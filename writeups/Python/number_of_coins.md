# Find Out the Number of Gold Coins!

## Problem Description

```
                           ,@@@@@@@@@@@@@@@,                          
                      @@@&                   @@@@                     
                  *@@     (@@@@@*     /@@@@@/     @@,                 
                @@    @@@                     @@@    @@               
              @@   (@@                           @@/   @@             
            %@   #@#               @@              %@(   @%           
           @@   @@            &@@@@@@@@@@@           @@   @@          
          @@   @@            @@@   @@   @@@           @@   @@         
          @,  @@             @@@   @@                  @@  ,@         
         @@   @               @@@@@@@                   @   @@        
         @@  /@                    @@@@@@@              @,  @@        
         @@   @                    @@   @@@             @   @@        
          @.  @@             @@@   @@   *@@            @@  ,@         
          @@   @&            #@@@  @@  %@@@           @@   @@         
           @@   @@             .@@@@@@@@,            @@   @@          
            @@   &@*               @@              *@&   @@           
              @@   @@@                           @@&   @@             
                @@    @@@                     @@@    @@               
                  %@@     @@@@@%       %@@@@@     @@%                 
                      @@@/                   /@@@                     
                           %@@@@@@@@@@@@@@@%                                                                                                                
```

This Kata is the first in the [Do a Smart Guess](https://www.codewars.com/collections/640a8a62431f2d14217eef5f) collection series.

After a long RPG campaign with your friends, you come across a guardian of a great treasure, a chest full of gold coins! As nothing in life is easy, the guardian says that he will only deliver the treasure if you guess the number of gold coins present in the chest. For this, he gives the following tips:

* $1$. If the number of coins were divided between $m_1$ people, $a_1$ coins would be left.

* $2$. If the number of coins were divided between $m_2$ people, $a_2$ coins would be left.

* $3$. If the number of coins were divided between $m_3$ people, $a_3$ coins would be left.

* ⋮

* $N$. If the number of coins were divided between $m_N$ people, $a_N$ coins would be left.

Of course $m_i$ is always a positive integer and $0 \le a_i \le m_i$.

To ensure that a solution for the number of coins always exists, the guardian always chooses values of $m$ that are pairwise relatively prime, that is:

$\text{gcd}(m_i, m_j) = 1 \qquad \forall i \neq j, 1 \le i, j \le N$

($\text{gcd}$ is the Greatest Common Divisor function).

### Your Task

Given the guardian information, write the function ```number_of_coins``` that returns the minimum number of gold coins in the chest.

This function receives information in the form of a list of tuples:

```
[(a1, m1), (a2, m2), ... , (aN, mN)]
```

**Example:**

Suppose that the tips from the guardian are:

1. If the number of coins were divided between $2$ people, $1$ coin would be left.

2. If the number of coins were divided between $5$ people, $2$ coins would be left.

So, the minimum number of gold coins is $7$, because $7$ is the smallest number that when divided by $2$ has remainder $1$ and when divided by $5$ has remainder $2$. Thus:

```
number_of_coins([(1, 2), (2, 5)]) = 7
```

### Performance Requirements

Consider that the input will be always valid, and the maximum input length will be 15 (that is, the guardian will give at most 15 tips, $1 \le N \le 15$).

The $m_i$ values will be always less than $10^{20}$, so the minimum number of gold coins can be quite large. However, that shouldn't be a problem for your algorithm.

If you liked this Kata, try the next one in this series: [Find Out the Number of Grains of Sand!](https://www.codewars.com/kata/640ab019431f2d0be07ef67a).

Have fun coding and please don't forget to vote and rank this kata! :-)

## Solution

The "Find Out the Number of Gold Coins!" kata is essentially a problem involving the **Chinese Remainder Theorem (CRT)** or simply finding the **least common multiple (LCM)** when constraints allow.

**Breaking it Down**

We have pairs $(a_i, m_i)$, meaning "the number of coins is congruent to $a_i$​ modulo $m_i$". We need to find the smallest positive integer satisfying all given congruences.

* An edge case to note is that if there is only one pair $(a,m)$, then the answer is just $a$.

* We need to find a number $x$ that satisfies multiple modular conditions, which leads to LCM-based calculations:

  * If moduli are coprime, we will use an LCM-based method.

  * For a more general case, we will use the CRT.

**Step 1: Handle the Simple Case**

If there’s only one pair $(a,m)$, the answer is trivially $a$.

```PY
def number_of_coins(info):
    if len(info) == 1:
        return info[0][0]
```

**Step 2: Solve for More Pairs using a Loop**

Given two pairs $(a_1,m_1)$ and $(a_2,m_2)$, we need to find the smallest $x$ such that:

$x \equiv a_1 \qquad (\text{mod }m_1)$

$x \equiv a_2 \qquad (\text{mod }m_2)$

For an initial value of $a$, we need to increment it by $m_0$ until it satisfies $a \equiv a_i \ (\text{mod }m_i)$:

```py
for ai, mi in info[1:]:
    while (a % mi) != ai:
        a += m0
    m0 = lcm(m0, mi)
```

The **LCM** of two numbers $a$ and $b$ can be calculated using the **GCD (Greatest Common Divisor)**:

$\displaystyle
\text{lcm}(a,b) = \frac{\left| a \times b \right|}{\text{gcd}(a,b)}$

```py
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
```

And, despite the **GCD** being included in the math library, we can implement it manually using the Euclidean algorithm:

```py
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
```

**Step 3: Optimization**

The approach so far works through multiples of $m_0$, which works, but **can be slow for large numbers**.

Instead, we can solve for $a$ **directly** using the **Extended Euclidean Algorithm**, avoiding unnecessary iterations.

The idea is to solve for $x$ in the equation:

$m_0 \cdot x \equiv (a_i - a) \quad (\text{mod } m_i)$

1. Compute $g = \text{gcd}(m_0, m_1)$.

2. If $(a_i - a)$ is not divisible by $g$, **no solution exists**.

3. Otherwise, solve for $x$ using the modular inverse from the Extended Euclidean Algorithm.

4. Compute the new $a$ in one step.

5. Update $m_0=\text{lcm}(m_0,m_i)$ as before.

The optimized code is as follows:

```py
def number_of_coins(info):
    if len(info) == 1:
        return info[0][0]
    
    a, m0 = info[0]
    
    for ai, mi in info[1:]:
        g = gcd(m0, mi)
        
        if (ai - a) % g != 0:
            return None  # No solution exists
        
        # Solve m0 * x ≡ (ai - a) (mod mi) using Extended Euclidean Algorithm
        _, x, _ = extended_gcd(m0, mi)
        
        # Scale x to get the correct shift
        x *= (ai - a) // g
        mi_g = mi // g  # Reduce modulus
        
        # Update `a`
        a += x * m0
        a %= mi_g * m0  # Keep `a` in the correct range
        
        # Update `m0` to LCM
        m0 = lcm(m0, mi)
    
    return a


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def extended_gcd(a, b):
    """Returns (gcd, x, y) where a*x + b*y = gcd(a, b)."""
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)
```