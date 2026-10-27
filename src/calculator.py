"""Estimativas simplificadas da memória ocupada pelos pesos do modelo."""
BITS_POR_PRECISAO = {"FP16": 16, "INT4": 4}


def calcular_memoria_gb(parametros_bilhoes, precisao):
    """Calcula os GiB teóricos de pesos, sem overhead nem cache KV."""
    if parametros_bilhoes <= 0:
        raise ValueError("A quantidade de parâmetros deve ser positiva.")
    if precisao not in BITS_POR_PRECISAO:
        raise ValueError("Precisão inválida. Use FP16 ou INT4.")
    bytes_estimados = parametros_bilhoes * 1_000_000_000 * BITS_POR_PRECISAO[precisao] / 8
    return bytes_estimados / (1024 ** 3)
