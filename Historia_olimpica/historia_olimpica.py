import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def load_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse {file_path}. Please check if it's a valid CSV file.")
        return None

# Opción 1: Ruta relativa desde el directorio actual
file_path = './data/olympic_athletes.csv'

# Opción 2: Ruta absoluta usando os.path
file_path = os.path.join(os.path.dirname(__file__), 'data', 'olympic_athletes.csv')

# Carga del archivo CSV
data = load_csv_file(file_path)

if data is None:
    print("Unable to proceed due to file loading error.")
    exit()

# Análisis de calidad de datos 
print("\n" + "="*70)
print("ANÁLISIS DE CALIDAD DE DATOS".center(70))
print("="*70)
null_counts = np.sum(pd.isnull(data), axis=0)
total_registros = len(data)
for columna in data.columns:
    nulos = null_counts[columna]
    porcentaje = (nulos/total_registros) * 100
    print(f"{columna:<30} Nulos: {nulos:>8,} ({porcentaje:>6.2f}%)")

# Estadísticas básicas 
print("\n" + "="*70)
print("ESTADÍSTICAS BÁSICAS".center(70))
print("="*70)
numeric_columns = data.select_dtypes(include=[np.number]).columns
for col in numeric_columns:
    print(f"\nEstadísticas para: {col}")
    print("-" * 50)
    datos = data[col].dropna()
    print(f"Media:          {np.mean(datos):>15.2f}")
    print(f"Mediana:        {np.median(datos):>15.2f}")
    print(f"Desv. Estándar: {np.std(datos):>15.2f}")
    print(f"Mínimo:         {np.min(datos):>15.2f}")
    print(f"Máximo:         {np.max(datos):>15.2f}")
    print(f"Q1 (25%):       {np.percentile(datos, 25):>15.2f}")
    print(f"Q3 (75%):       {np.percentile(datos, 75):>15.2f}")

# Visualizaciones 
plt.style.use('default')
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Distribución de participaciones
datos_participaciones = data['games_participations'].dropna().values
hist, bins = np.histogram(datos_participaciones, bins=20, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

# Calcular KDE manualmente 
kde_participaciones = np.zeros_like(bin_centers)
bandwidth = 0.5  
for x in datos_participaciones:
    kde_participaciones += np.exp(-0.5 * ((bin_centers - x) / bandwidth) ** 2)
kde_participaciones = kde_participaciones / (len(datos_participaciones) * bandwidth * np.sqrt(2 * np.pi))

axs[0].hist(datos_participaciones, bins=20, density=True, alpha=0.7, color='skyblue')
axs[0].plot(bin_centers, kde_participaciones, 'r-', lw=2)
axs[0].set_title('Distribución de Participaciones en Juegos')
axs[0].set_xlabel('Número de Participaciones')
axs[0].set_ylabel('Densidad')
axs[0].grid(True, alpha=0.3)

# Distribución de años de nacimiento
datos_nacimiento = data['athlete_year_birth'].dropna().values
hist, bins = np.histogram(datos_nacimiento, bins=30, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

# Calcular KDE para años de nacimiento
kde_nacimiento = np.zeros_like(bin_centers)
bandwidth = 3  
for x in datos_nacimiento:
    kde_nacimiento += np.exp(-0.5 * ((bin_centers - x) / bandwidth) ** 2)
kde_nacimiento = kde_nacimiento / (len(datos_nacimiento) * bandwidth * np.sqrt(2 * np.pi))

axs[1].hist(datos_nacimiento, bins=30, density=True, alpha=0.7, color='skyblue')
axs[1].plot(bin_centers, kde_nacimiento, 'r-', lw=2)
axs[1].set_title('Distribución del Año de Nacimiento')
axs[1].set_xlabel('Año de Nacimiento')
axs[1].set_ylabel('Densidad')
axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Análisis de medallas 
print("\n" + "="*70)
print("ANÁLISIS DE MEDALLAS".center(70))
print("="*70)
medallas = ~pd.isnull(data['athlete_medals'])
total_atletas = len(data)
atletas_con_medallas = np.sum(medallas)
porcentaje_medallas = (atletas_con_medallas/total_atletas) * 100

print(f"Total de atletas:        {total_atletas:>10,}")
print(f"Atletas con medallas:    {atletas_con_medallas:>10,}")
print(f"Atletas sin medallas:    {total_atletas - atletas_con_medallas:>10,}")
print(f"Porcentaje con medallas: {porcentaje_medallas:>10.2f}%")

# Matriz de correlación 
print("\n" + "="*70)
print("ANÁLISIS DE CORRELACIÓN".center(70))
print("="*70)

# Calcular correlación 
numeric_data = data.select_dtypes(include=[np.number]).values
# Eliminar filas con NaN
valid_rows = ~np.isnan(numeric_data).any(axis=1)
clean_data = numeric_data[valid_rows]
correlation_matrix = np.corrcoef(clean_data.T)

# Crear un DataFrame 
numeric_columns = data.select_dtypes(include=[np.number]).columns
correlation_df = pd.DataFrame(
    correlation_matrix,
    columns=numeric_columns,
    index=numeric_columns
)

# Mostrar matriz de correlación
print("\nMatriz de correlación:")
print("-" * 70)
for i, col in enumerate(correlation_df.columns):
    print(f"{col:>20}", end="")
    for j in range(i + 1):
        value = correlation_matrix[i, j]
        print(f"{value:>12.3f}", end="")
    print()