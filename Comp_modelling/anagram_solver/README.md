# Anagram Frequency Distribution Analysis

## Project
This Python project analyzes how many valid English words can be formed from every 9-letter anagram generated from the English alphabet. It filters words based on dictionary membership, letter inclusion, and word length constraints.

The distribution of solution counts per anagram reveals interesting statistical behavior — including stretched Gaussian and exponential-like tails — patterns that also appear in physical and economic systems.

**Key features:**
- Generates all possible 9-letter letter combinations
- Solves anagrams using binary search
- Filters for central letter and word length (3–9 letters)
- Visualizes the frequency distribution using Matplotlib

---

## Prerequisites
- Python 3.8 or higher
- A text file containing a lowercase dictionary (e.g., `dictionary.txt`)
- Required Python packages:
  - `matplotlib`

---

## Setup
Clone the repo and navigate to the project directory:

```bash
git clone https://github.com/Hades786/Portfolio/Comp_modelling.git
cd Comp_modelling/anagram_solver
````

Ensure `dictionary.txt` is present in the same directory.

---

## Testing

### 1. Generate Anagrams

This step generates all possible 9-letter combinations:

```bash
python combinations.py
```

### 2. Solve Anagrams

This script filters and counts valid dictionary words per anagram:

```bash
python anagram_solver_binary_v3.py
```

### 3. Visualize Results

To generate a histogram of solution frequencies:

```bash
python histogram_function.py
```

---

## Documentation

**Folder Structure:**

```
anagram_solver/
├── combinations.py              # Generates ~3.1 million 9-letter anagram puzzles
├── anagram_solver_binary_v3.py # Solves anagrams using constraints + binary search
├── histogram_function.py       # Plots histogram of valid solution counts
├── dictionary.txt              # Required (user-supplied)
├── solutions.txt               # Optional: stores solution counts per anagram
└── fig1.pdf                    # Visualization of distribution
```

**Example Output:**
![PDF of Solutions](fig1.pdf)

---

## License

MIT License

```
```
