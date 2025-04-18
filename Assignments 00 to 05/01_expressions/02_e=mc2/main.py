import time

# Constants
C = 299_792_458  # Speed of light in m/s

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def main():
    print(f"""{CYAN}
***************************************************
*        {BOLD}E = m × c² — Energy Calculator{RESET}{CYAN}        *
***************************************************{RESET}
""")
    time.sleep(0.5)

    # Input
    mass_in_kg = float(input(f"{YELLOW}Enter mass in kilograms: {RESET}"))

    # Calculation
    energy_in_joules = mass_in_kg * (C ** 2)

    # Output
    print(f"\n{MAGENTA}Using Einstein’s Famous Equation:{RESET}")
    print(f"{CYAN}e = m * c²{RESET}")
    print(f"{GREEN}m = {mass_in_kg} kg{RESET}")
    print(f"{GREEN}c = {C:,} m/s{RESET}")

    time.sleep(0.5)
    print(f"\n{BOLD}{RED}You get ≈ {energy_in_joules:.6e} joules of energy! ⚡{RESET}")

    print(f"\n{CYAN}Thank you for using the energy calculator! 🚀{RESET}\n")

if __name__ == '__main__':
    main()
