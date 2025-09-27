import pandas as pd


data = {
    'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
    'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
    'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
    'edad': [28, 35, 42, 31, 29, 38, 45, 33]
}
df = pd.DataFrame(data)

print("Empleados de IT Y salario > 60,000")
print(df[(df["departamento"] == "IT") & (df["salario"] > 60000)], "\n")

print("Empleados de Ventas O mayores de 40 años")
print(df[(df["departamento"] == "Ventas") | (df["edad"] > 40)], "\n")

print("Empleados que NO son de Marketing")
print(df[~(df["departamento"] == "Marketing")])