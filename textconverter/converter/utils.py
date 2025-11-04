import re

def convert_to_latex_math(text):
    # 1. Remove unwanted symbols
    text = text.replace('*', '').replace('#', '')

    # 2. Remove square brackets [ ] but keep inside content
    text = re.sub(r'\[([^\]]+)\]', r'\1', text)

    # 3. Detect and wrap math-like expressions
    def wrap_math(match):
        expr = match.group(0)
        expr = re.sub(r'(\d+)\s*/\s*(\d+)', r'\\frac{\1}{\2}', expr)
        expr = expr.replace('*', r'\times')
        return f"${expr.strip()}$"

    # 4. Wrap equations/numbers in math mode
    latex_text = re.sub(r'([A-Za-z0-9\+\-\=\/\^\.\(\) ]+)', wrap_math, text)

    return latex_text
