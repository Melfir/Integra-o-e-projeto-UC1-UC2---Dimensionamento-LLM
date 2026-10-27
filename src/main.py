"""Interface de linha de comando do AI Edge Estimator."""
from .models import MODELOS
from .hardware import obter_ram_disponivel_gb
from .calculator import calcular_memoria_gb
from .estimator import avaliar_viabilidade


def main():
    print("=== AI Edge Estimator ===")
    ram = obter_ram_disponivel_gb()
    print(f"RAM disponível: {ram:.2f} GiB")
    print("\nModelos disponíveis:")
    for codigo, modelo in MODELOS.items():
        print(f"{codigo} - {modelo['nome']}")

    escolha = input("Selecione o número do modelo: ").strip()
    if escolha not in MODELOS:
        print("Modelo inválido.")
        return
    precisao = input("Precisão (FP16/INT4): ").strip().upper()
    if precisao not in ("FP16", "INT4"):
        print("Precisão inválida.")
        return

    modelo = MODELOS[escolha]
    memoria = calcular_memoria_gb(modelo["parametros_bilhoes"], precisao)
    print(f"\nModelo: {modelo['nome']} ({precisao})")
    print(f"Memória teórica dos pesos: {memoria:.2f} GiB")
    print(avaliar_viabilidade(memoria, ram))
    print("Nota: esta versão não mede VRAM nem o consumo real de inferência.")


if __name__ == "__main__":
    main()
