import sys

def even_odd(n):
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

if __name__ == "__main__":
    num = int(sys.argv[1])
    print("Number:", num)
    print("Result:", even_odd(num))