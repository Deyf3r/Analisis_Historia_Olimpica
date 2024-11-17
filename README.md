# 🏅 Análisis de Datos de Atletas Olímpicos

## 📊 Objetivo

Este proyecto analiza un conjunto de datos de atletas olímpicos, enfocándose en:

1. Evaluación de la calidad de los datos
2. Análisis estadístico básico
3. Visualización de distribuciones clave
4. Análisis de medallas
5. Análisis de correlación entre variables numéricas

## 🔍 Resultados

### 1. Evaluación de la Calidad de los Datos

- Proporciona una visión general de los valores nulos en cada columna.
- Identifica posibles problemas de calidad o información faltante.

### 2. Análisis Estadístico Básico

Para cada columna numérica, se calculan:

- Media
- Mediana
- Desviación Estándar
- Mínimo
- Máximo
- Primer Cuartil (percentil 25)
- Tercer Cuartil (percentil 75)

### 3. Visualización de Datos

Se visualizan dos distribuciones clave:

#### 3.1 Distribución de Participaciones en Juegos

- Muestra en cuántos Juegos Olímpicos suelen participar los atletas.
- Utiliza histograma con superposición de Estimación de Densidad del Kernel (KDE).

#### 3.2 Distribución de Años de Nacimiento de los Atletas

- Ilustra la distribución de edad de los atletas olímpicos a lo largo del tiempo.
- También utiliza histograma con superposición KDE.

### 4. Análisis de Medallas

- Calcula el número total de atletas en el conjunto de datos.
- Determina cuántos atletas han ganado medallas.
- Calcula el porcentaje de atletas que han ganado medallas.

### 5. Análisis de Correlación

- Calcula una matriz de correlación para todas las variables numéricas.
- Ayuda a identificar posibles relaciones entre atributos numéricos de los atletas.

## 🚨 Consideraciones Importantes

1. **Carga de Datos**: 
   - Opción 1: Ruta relativa
   - Opción 2: Ruta absoluta con `os.path.join`

2. **Calidad de los Datos**: 
   - Atención a altos porcentajes de valores nulos.
   - Puede requerir limpieza o imputación de datos.

3. **Visualizaciones**: 
   - Parámetro de ancho de banda en KDE ajustable (0.5 para participaciones, 3 para años de nacimiento).

4. **Análisis de Medallas**: 
   - Visión general de alto nivel.
   - Considerar análisis más detallados por deporte, país o período.

5. **Análisis de Correlación**: 
   - Las correlaciones no implican causalidad.
   - Investigar correlaciones fuertes para insights significativos.

6. **Rendimiento**: 
   - Para grandes conjuntos de datos, considerar técnicas de muestreo.

7. **Interpretabilidad**: 
   - Interpretar resultados en el contexto del atletismo olímpico.
   - El conocimiento del dominio es crucial.

