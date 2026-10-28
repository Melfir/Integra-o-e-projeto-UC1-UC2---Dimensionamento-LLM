"""Estimativas da memória ocupada pelos pesos do modelo."""

BITS_POR_PRECISAO = {
    "FP16": 16,
    "INT8": 8,
    "INT4": 4,
}


def estimate_memory_gb(parameters_billions: float, bits_per_parameter: int) -> float:
    """Estima a memória dos pesos de um modelo em GB decimais."""
    if parameters_billions <= 0:
        raise ValueError("A quantidade de parâmetros deve ser positiva.")

    if bits_per_parameter not in (4, 8, 16):
        raise ValueError("Precisão aceita: 4, 8 ou 16 bits.")

    # Parâmetros em bilhões × bits por parâmetro ÷ bits por byte.
    return parameters_billions * bits_per_parameter / 8


def check_memory_requirements(
    required_gb: float,
    available_gb: float,
    safety_margin: float = 1.2,
) -> dict:
    """Verifica se há memória disponível com uma margem de segurança."""
    if required_gb < 0:
        raise ValueError("A memória necessária não pode ser negativa.")

    if available_gb < 0:
        raise ValueError("A memória disponível não pode ser negativa.")

    if safety_margin < 1:
        raise ValueError("A margem de segurança deve ser pelo menos 1.")

    estimated_total_gb = required_gb * safety_margin

    return {
        "required_gb": required_gb,
        "estimated_total_gb": estimated_total_gb,
        "available_gb": available_gb,
        "feasible": estimated_total_gb <= available_gb,
    }


def calcular_memoria_gb(parametros_bilhoes: float, precisao: str) -> float:
    """Calcula os GiB teóricos de pesos, sem overhead nem cache KV (compatibilidade com Aluno A)."""
    if parametros_bilhoes <= 0:
        raise ValueError("A quantidade de parâmetros deve ser positiva.")
    if precisao not in BITS_POR_PRECISAO:
        raise ValueError("Precisão inválida. Use FP16 ou INT4.")
    bytes_estimados = parametros_bilhoes * 1_000_000_000 * BITS_POR_PRECISAO[precisao] / 8
    return bytes_estimados / (1024 ** 3)
