import random
import re

def roll_dice(form):
    formulas = form.split(" ")
    rolls = []
    for formular in formulas:
        match = re.fullmatch(r'(\d+)d(\d+)', formular.strip())
        if not match:
            raise ValueError("Invalid formula. Use format \"NdM\", e.g., \"2d6\".\nFormultiple rolls at once, use \"NdM NdM\" eg. \"2d2 1d10\"")
        n, m = map(int, match.groups())
        rolls.extend([random.randint(1, m) for _ in range(n)])
    return rolls, sum(rolls)

if __name__ == "__main__":
    formula = input("Enter dice formula (e.g., 2d6): ")
    try:
        rolls, total = roll_dice(formula)
        print(f"Rolls: {rolls}")
        print(f"Total: {total}")
    except ValueError as e:
        print(e)