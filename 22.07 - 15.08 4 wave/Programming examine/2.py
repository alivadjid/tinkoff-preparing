import sys

total = 0

def calculate():
    try:
        line = sys.stdin.readline().strip()
        a, b, c = map(float, line.split())
        d = b**2 - 4*a*c

        if d < 0:
            return
        elif d == 0:
            print(-b / (2*a))
        else:
            print((d**0.5 - b) / (2*a))
            print((-d**0.5 - b) / (2*a))
    except ValueError:
        pass

calculate()

try:
    sys.stdin.readline()  # Keep reading input
except EOFError:
    print(total)
    sys.exit(0)