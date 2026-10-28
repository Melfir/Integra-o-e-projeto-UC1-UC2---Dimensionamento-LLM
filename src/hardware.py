"""Leitura da memória RAM do computador."""
import psutil


def get_ram_info() -> dict:
    """Retorna informações de RAM em GB decimais."""
    memory = psutil.virtual_memory()

    return {
        "total_gb": memory.total / 1_000_000_000,
        "available_gb": memory.available / 1_000_000_000,
        "used_percent": memory.percent,
    }


def obter_ram_disponivel_gb() -> float:
    """Retorna a RAM disponível no momento, em GiB (compatibilidade com Aluno A)."""
    return psutil.virtual_memory().available / (1024 ** 3)


if __name__ == "__main__":
    ram = get_ram_info()

    print(f"RAM total: {ram['total_gb']:.2f} GB")
    print(f"RAM disponível: {ram['available_gb']:.2f} GB")
    print(f"RAM em uso: {ram['used_percent']:.1f}%")
