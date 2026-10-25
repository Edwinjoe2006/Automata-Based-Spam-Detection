# FLA Viva Questions & Answers (Top 10)
## Project: Automata-Based Spam Email Detection Using JFLAP

---

### 1. What is an alphabet ($\Sigma$)?
**Answer:**  
An alphabet is a finite, non-empty set of symbols. In our project, $\Sigma = \{F, W, P, O, U, C, K, B\}$, where each symbol represents a specific spam keyword category like FREE, WINNER, PRIZE, etc.

---

### 2. What is a string ($w$)?
**Answer:**  
A string is a finite sequence of symbols chosen from an alphabet $\Sigma$. For example, the email *"You won a free prize"* produces the string $w = \text{"W F P"}$ over our alphabet $\Sigma$.

---

### 3. What is a language ($L$)?
**Answer:**  
A language is a set of strings over an alphabet $\Sigma$ (a subset of $\Sigma^*$). In our project, the language $L$ is the set of all symbolic strings having length 2 or more ($|w| \ge 2$), which represents emails containing multiple spam triggers.

---

### 4. What is an NFA (Non-deterministic Finite Automaton)?
**Answer:**  
An NFA is a finite state machine where, for a given state and input symbol, the transition can lead to zero, one, or multiple possible next states. It can also permit $\epsilon$-transitions (state changes without consuming input).

---

### 5. What is a DFA (Deterministic Finite Automaton)?
**Answer:**  
A DFA is a finite state machine where, for every state and input symbol, there is exactly one unique next state. There are no choices or $\epsilon$-transitions, making execution completely deterministic and predictable.

---

### 6. What is the key difference between NFA and DFA?
**Answer:**  
In a DFA, $\delta: Q \times \Sigma \to Q$ (each input symbol has exactly one unique next state). In an NFA, $\delta: Q \times \Sigma \to 2^Q$ (an input symbol can transition to a set of multiple states). However, both recognize the exact same class of regular languages.

---

### 7. What is an accepting / final state?
**Answer:**  
An accepting state is a state designated in the set $F$. If the automaton processes the entire input string and halts in an accepting state (here, state $S_2$), the string is **Accepted** (classified as **SPAM**); otherwise, it is **Rejected** (classified as **HAM**).

---

### 8. Why did you convert email words into symbols?
**Answer:**  
Finite state automata operate on discrete mathematical symbols over a finite alphabet, not unstructured natural language text. Mapping predefined keyword classes into single letters ($\Sigma = \{F, W, P, O, U, C, K, B\}$) allows the automaton to process the email sequentially.

---

### 9. How does your DFA detect spam?
**Answer:**  
The DFA begins in state $S_0$ (0 triggers). If it reads one spam symbol, it moves to state $S_1$ (HAM). If it reads a second spam symbol, it moves to accepting state $S_2$ and loops there for any further triggers. Reaching $S_2$ accepts the string, classifying the email as SPAM.

---

### 10. Why is this an FLA project instead of a Machine Learning project?
**Answer:**  
Because we do not use statistical models, weights, loss functions, or ML algorithms (like Naive Bayes or Random Forest). Instead, we use formal grammar, regular expressions, NFA, DFA, and subset construction to classify emails deterministically based on automata theory.
