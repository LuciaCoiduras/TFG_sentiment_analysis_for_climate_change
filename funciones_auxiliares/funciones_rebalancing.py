import pandas as pd

from imblearn.over_sampling  import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler


def oversample(df, tweets_label, sentiment_label):
    # Conteo de muestras por clase
    class_counts = df[sentiment_label].value_counts()
    print("Recuento de muestras por clase antes de oversampling:")
    print(class_counts)

    # Identificar la clase mayoritaria
    majority_class = class_counts.idxmax()
    max_samples = class_counts.max()
    print(majority_class)

    # Aplicar oversampling solo a las clases minoritarias
    oversample_ratio = {label: max_samples for label in class_counts.index}

    # Inicializar el sampler
    oversampler = RandomOverSampler(sampling_strategy=oversample_ratio, random_state=42)

    # Separar características y etiquetas
    X = df[tweets_label].values.reshape(-1, 1)  # Usamos solo la columna de texto como características
    y = df[sentiment_label].values

    # Aplicar oversampling
    X_resampled, y_resampled = oversampler.fit_resample(X, y)

    # Crear un nuevo DataFrame con las muestras oversampleadas
    df_oversampled = pd.DataFrame({tweets_label: X_resampled.flatten(), sentiment_label: y_resampled})

    # Verificar el recuento de muestras por clase después de oversampling
    new_class_counts = df_oversampled[sentiment_label].value_counts()
    print("\nRecuento de muestras por clase después de oversampling:")
    print(new_class_counts)

    # df_resampled ahora contiene el DataFrame con clases equilibradas
    print("\nDataFrame con oversampling:")
    print(df_oversampled)

def undersample(df, tweets_label, sentiment_label):
    class_counts = df[sentiment_label].value_counts()
    print("Recuento de muestras por clase antes de undersampling:")
    print(class_counts)

    # Determinar el número mínimo de muestras entre todas las clases
    min_samples = class_counts.min()

    # Definir el ratio de undersampling para igualar todas las clases al número mínimo de muestras
    undersample_ratio = {label: min_samples for label in class_counts.index}

    # Inicializar el RandomUnderSampler con la estrategia de sampling
    undersampler = RandomUnderSampler(sampling_strategy=undersample_ratio, random_state=42)

    # Separar características (X) y etiquetas (y)
    X = df[tweets_label].values.reshape(-1, 1)  # Usamos solo la columna de texto como características
    y = df[sentiment_label].values

    # Aplicar undersampling
    X_resampled, y_resampled = undersampler.fit_resample(X, y)

    # Crear un nuevo DataFrame con las muestras undersampleadas
    df_undersampled = pd.DataFrame({tweets_label: X_resampled.flatten(), sentiment_label: y_resampled})

    # Verificar el recuento de muestras por clase después de undersampling
    new_class_counts = df_undersampled[sentiment_label].value_counts()
    print("\nRecuento de muestras por clase después de undersampling:")
    print(new_class_counts)
    
    return df_undersampled