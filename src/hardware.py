"""Leitura da memória RAM do computador."""
import psutil


def obter_ram_disponivel_gb():
    """Retorna a RAM disponível no momento, em GiB."""
    return psutil.virtual_memory().available / (1024 ** 3)
