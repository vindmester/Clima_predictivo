## 🌬️ Proyecto de Clasificación de Dirección del Viento en Chile

Este es un proyecto que utiliza datos meteorológicos históricos para predecir la dirección del viento a partir de variables como humedad, condiciones climáticas, velocidad del viento y nubosidad.

## 📄 Descripción
-Se extrajo una base de datos que contenia información sobre distintos apartados del clima. Esos datos se exportaron a un CSV llamado 'chile_weather_filtrado'.
-De ese CSV se confeccionaron graficos de Caja con el obejetivo de quitar los datos atipicos que pudieran entorpecer las predicciones. Estos datos se exportaron a un CSV llamdo 'chile_weather_filtrado.csv'.

-A partir de lo anterior se entrenó un modelo de clasificación supervisada utilizando datos extraídos del archivo CSV llamado 'chile_weather_filtrado.csv'.  
El objetivo es predecir hacia qué dirección cardinal (N, NE, E, etc.) se moverá el viento, según las condiciones atmosféricas registradas.

## 🧠 Tecnologías

- Python 3.12.5  
- pandas: Para el procesamiento y análisis de datos tabulares.  
- scikit-learn: Para el entrenamiento de modelos de clasificación.  
- matplotlib y seaborn: Para la visualización de resultados (matriz de confusión, gráficos de evaluación).  
- pickle: Para guardar y cargar el modelo entrenado.  

## 📓 Notebooks

En la carpeta `notebooks/`, encontrarás archivos Jupyter (`.ipynb`) que:

- Cargan y limpian el dataset.
- Entrenan un modelo con 8 clases cardinales.
- Evalúan el rendimiento del modelo.
- Permiten hacer predicciones a partir de nuevos datos introducidos manualmente.

## 📈 Variables utilizadas

- humidity_%: Humedad relativa del aire.  
- condition_text: Descripción textual del clima (ej. "Despejado", "Lluvia ligera", "Neblina", etc.)  
- wind_kph: Velocidad del viento en km/h.  
- cloud_%: Porcentaje de nubosidad.  
- wind_dir: Dirección del viento original (agrupada en 8 direcciones cardinales).

## 🔍 Resultado

El modelo permite predecir direcciones del viento agrupadas en 8 clases: N, NE, E, SE, S, SW, W, NW.  
Además, se proporciona una interfaz para ingresar valores nuevos y obtener predicciones usando el modelo entrenado.

## 🤝 Contribuciones

Si deseas contribuir a este proyecto, por favor abre un pull request o un issue con tus sugerencias o mejoras.
