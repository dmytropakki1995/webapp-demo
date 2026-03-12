from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>

<h2>Простий калькулятор</h2>

<form method="post">
    <input type="number" step="any" name="a" required>
    
    <select name="op">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>

    <input type="number" step="any" name="b" required>

    <button type="submit">Обчислити</button>
</form>

{% if result is not none %}
<h3>Результат: {{result}}</h3>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]

        print("Test logs")

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                result = "Ділення на нуль!"
            else:
                result = a / b

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)