
from flask import Flask, render_template, request

app = Flask(__name__)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Ejercicio 1: cálculo de notas
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":

        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        if not all(10 <= nota <= 70 for nota in [nota1, nota2, nota3]):
            return "Error: las notas deben estar entre 10 y 70", 400

        if not 0 <= asistencia <= 100:
            return "Error: la asistencia debe estar entre 0 y 100", 400

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            "resultado.html",
            promedio=round(promedio, 1),
            estado=estado
        )

    return render_template("ejercicio1.html")


# Ejercicio 2: comparación de nombres
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    if request.method == "POST":

        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombres = [nombre1, nombre2, nombre3]

        if not all(nombre for nombre in nombres):
            return "Error: debes ingresar los tres nombres", 400

        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            return "Error: debes ingresar tres nombres diferentes", 400

        nombre_mayor = max(nombres, key=len)
        cantidad = len(nombre_mayor)

        return render_template(
            "resultado.html",
            nombre=nombre_mayor,
            cantidad=cantidad
        )

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
