from django.shortcuts import render
from django import forms
import re

# Form for user input
class TextForm(forms.Form):
    input_text = forms.CharField(
        label="Enter your text",
        widget=forms.Textarea(attrs={
            "rows": 10,
            "class": "form-control",
            "placeholder": "Paste your content here..."
        })
    )

# Function to detect equations or numbers and format them into LaTeX display mode
def convert_to_latex_format(text):
    """
    Converts numerical or equation-like expressions into LaTeX math mode
    while keeping formatting identical to original (like your example format).
    """

    # 1️⃣ Remove $, [, ] but keep * and #
    cleaned_text = re.sub(r'[\$\[\]]', '', text)

    # 2️⃣ Detect mathematical expressions or calculations
    # We'll wrap anything that looks like a formula or expression in $$...$$
    # Example patterns: 1+1=2, E=mc^2, x^2+y^2=z^2, 3/4, etc.
    equation_pattern = re.compile(r'([A-Za-z0-9\\\+\-\*\^\/\=\(\)]+(?:\s*[A-Za-z0-9\\\+\-\*\^\/\=\(\)]+)*)')

    def format_equation(match):
        expr = match.group(1)
        # Avoid converting short plain words (like 'and', 'the')
        if re.fullmatch(r'[A-Za-z]+', expr):
            return expr
        # Wrap equations/numbers in $$ ... $$ for display math mode
        return f"$${expr}$$"

    converted_text = equation_pattern.sub(format_equation, cleaned_text)

    # 3️⃣ Preserve line breaks and indentation
    converted_text = converted_text.replace("\r", "")

    return converted_text


def home(request):
    output_text = ""
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data["input_text"]
            output_text = convert_to_latex_format(input_text)
    else:
        form = TextForm()
    return render(request, "converter/home.html", {"form": form, "output_text": output_text})
