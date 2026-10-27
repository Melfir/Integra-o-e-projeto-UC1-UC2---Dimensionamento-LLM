"""Comparação simplificada entre memória estimada e RAM disponível."""


def avaliar_viabilidade(memoria_necessaria_gb, ram_disponivel_gb):
    if memoria_necessaria_gb > ram_disponivel_gb:
        return "Risco elevado de OOM: pesos excedem a RAM disponível."
    return "Pesos cabem na RAM disponível; execução não garantida (overhead, KV cache e VRAM)."
