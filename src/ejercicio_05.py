import pandas as pd


data = {
    'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
    'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
    'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
    'edad': [28, 35, 42, 31, 29, 38, 45, 33]
}
df = pd.DataFrame(data)

print("Empleados de IT con más de 30 años Y salario > 60,000")
print(df[(df["departamento"] == "IT") & (df["edad"] > 30) & (df["salario"] > 60000)])

print("Empleados cuyo nombre empieza con 'L' O son de RRHH")
print(df[(df["nombre"].str.startswith("L")) | (df["departamento"] == "RRHH")])