# coding: utf-8
import numpy as np
import pandas as pd
from babs_visualizations import usage_stats

def question_3(data):
    """
    This function will check that the sample data has been wrangled properly.
    """

    n_correct = 0

    # Check that there are a correct number of lines in the dataset.
    if data.shape[0] != 27345:
        print("Eram esperados 27,345 pontos de dados, Encontrados apenas {:d}.".format(data.shape[0]))
    else:
        n_correct += 1

    # Check that the durations have been converted into terms of minutes.
    data_duration_stats = usage_stats(data, verbose = False)
    expected_duration_stats = np.array([6.816667, 10.716667, 17.28333])
    if not np.allclose(data_duration_stats, expected_duration_stats):
        print("Os dados de duração não batem com o esperado (em minutos).")
        if np.allclose(data_duration_stats, np.array([409, 643, 1037])):
            print("  Parece que as unidades ainda se encontram em segundos.")
        elif np.allclose(data_duration_stats, np.array([24520, 38580, 62220])):
            print("  Parece que você usou o operador matemático errado para a sua conversão.")
        print("  Lembre-se que existem 60 segundos em um minuto.")
    else:
        n_correct += 1

    # Check that the timestamps have been wrangled properly.
    expected_time_vals = {'start_month': [25243, 2102],
                          'start_hour': [2851, 2291, 2219, 2171, 2131, 1976,
                                      1833, 1799, 1791, 1644, 1359, 1269,
                                      1071,  797,  644,  440,  394,  276,
                                       153,   65,   55,   45,   42,   29],
                          'weekday': [4712, 4493, 4370, 3860, 3637, 3138, 3135]}

    for column in expected_time_vals.keys():
        col_data = data[column].value_counts().values
        n_values = len(col_data)
        n_values_expected = len(expected_time_vals[column])
        if not n_values == n_values_expected:
            print("Número errado de valores únicos encontrados para a coluna : {}".format(column))
            print("  {:d} valores únicos esperados; {:d} valores encontrados.".format(n_values_expected, n_values))
        elif not np.array_equal(col_data, expected_time_vals[column]):
            expected_max = expected_time_vals[column][0]
            expected_min = expected_time_vals[column][-1]
            print("Contagem de valores erradas para a coluna: {}".format(column))
            print("  Valor mais comum esperado {:d} pontos de dados; {:d} viagens encontradas.".format(expected_max, col_data[0]))
            print("  Valor menos esperado {:d} pontos de dados; {:d} viagens enconrtadas.".format(expected_min, col_data[-1]))
        else:
            n_correct += 1

    if n_correct == len(expected_time_vals.keys()) + 2:
        print("Todas as contagens estão como esperadas.")