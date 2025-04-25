# Anagram Frequency Distribution Analysis

This project explores statistical behaviors that emerge from solving anagram puzzles generated from all 9-letter combinations of the English alphabet. The frequency of valid solutions is analyzed and visualized, revealing stretched Gaussian and exponential-tail behavior — a phenomenon common in both physical and economic systems.

## Repository Structure

```
Comp_modelling/
└── anagram_solver/
    ├── combinations.py              # Generates ~3.1 million 9-letter anagram puzzles
    ├── anagram_solver_binary_v3.py # Solves each anagram under dictionary constraints
    ├── histogram_function.py       # Plots frequency distribution of solutions
    ├── dictionary.txt              # (not uploaded; user-supplied)
    ├── solutions.txt               # Output of anagram vs solution count (optional)
    ├── anagram_report.pdf          # Formal LaTeX report
    └── fig1.pdf                    # Distribution graph
```

## Features

- Generates all 9-letter combinations from the English alphabet  
- Solves anagrams with constraints:  
  - Must contain a central letter  
  - Length between 3 to 9 letters  
  - Must appear in dictionary  
- Set filtering and binary search used for fast lookups  
- Multiprocessing for improved speed  
- Visualizes distribution using Matplotlib  

## Methodology

1. Generate all 9-letter anagram puzzles using combinations  
2. Solve based on inclusion and dictionary validation  
3. Count valid solutions per puzzle  
4. Plot the resulting distribution of solution frequencies  

## Requirements

- Python 3.8+  
- matplotlib  

## Usage

**Generate Anagrams:**
```bash
python combinations.py
```

**Solve Anagrams:**
```bash
python anagram_solver_binary_v3.py
```

**Visualize Results:**
```bash
python histogram_function.py
```

> Make sure `dictionary.txt` is available in the same directory.

## Visualization

![PDF of Solutions](fig1.pdf)

## Author

Ahmed Raza Patel  
Formal report available in `anagram_report.pdf`

## License

MIT (OS)
```
