import matplotlib.pyplot as plt

def extract_solution_counts(solutions_file):
    """Extracts the number of valid words for each anagram from the solutions.txt file"""
    counts = []
    
    with open(solutions_file, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.isdigit():  # Check if the line consists only of digits
                counts.append(int(line))
    
    return counts

def plot_distribution(counts):
    """Plots a distribution of the number of valid words per anagram."""
    plt.figure(figsize=(13, 10))
    plt.hist(counts, bins=5000, edgecolor='black', alpha=0.7)
    plt.xlabel(r"$\rho$", size=34)
    plt.ylabel('PDF', size=34)
    #plt.yscale('log')  # Set y-axis to log scale
    #plt.xscale('log') #set x-axis to log scale
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig('fig1.pdf',dpi=600)
    plt.show()

if __name__ == "__main__":
    solutions_file = 'solutions.txt'
    
    counts = extract_solution_counts(solutions_file)
    plot_distribution(counts)
