import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root,
    else:
        return "No real roots"

def log_to_file(a, b, c, result):
    with open("quadratic_solutions.txt", "a") as file:
        file.write(f"Equation: {a}x^2 + {b}x + {c} = 0\n")
        file.write(f"Solution: {result}\n")
        file.write("-" * 30 + "\n")

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a == 0:
        print("Not a quadratic equation.")
        return
    
    result = solve_quadratic(a, b, c)
    print("Solution:", result)
    log_to_file(a, b, c, result)

if __name__ == "__main__":
    main()
