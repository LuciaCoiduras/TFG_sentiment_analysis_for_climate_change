import pandas as pd

def read_data_from_excel(file_path, exclude_sheets = ['informacion']):
    # Lee el archivo Excel
    xl = pd.ExcelFile(file_path)

    # Obtén una lista de nombres de todas las hojas en el archivo
    all_sheet_names = xl.sheet_names

    # Filtra las hojas para excluir la hoja especificada
    sheets_to_read = [sheet_name for sheet_name in all_sheet_names if sheet_name not in exclude_sheets]

    df = pd.DataFrame()
    for hoja in sheets_to_read:
        df = pd.concat([df,pd.read_excel(file_path, sheet_name=hoja)], ignore_index= True)
    return df

def format_sentiment_column(df):
    df['Sentiment'] = df['Sentiment'].replace({
        -2: int(0),
        -1: int(0),
         0: int(1),
         1: int(2)
    })

    df.dropna(subset='Sentiment', inplace=True)
    df['Sentiment'] = df['Sentiment'].astype(int)
    return df