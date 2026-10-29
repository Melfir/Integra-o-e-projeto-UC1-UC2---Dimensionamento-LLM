# AI Edge Estimator

Projeto integrador UC1 + UC2: estimativa inicial de memória para executar LLMs localmente. 

## Requisitos

- Python 3.10+
- Biblioteca `psutil`

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows, a ativação é `.venv\\Scripts\\activate`.

## Execução

```bash
python -m src.main
```

## Testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

- `src/models.py`: catálogo de modelos
- `src/hardware.py`: memória RAM disponível
- `src/calculator.py`: memória teórica dos pesos
- `src/estimator.py`: comparação com RAM
- `src/main.py`: interface do terminal
- `tests/`: testes automatizados

## Limitações

O cálculo considera apenas o armazenamento dos pesos e assume 4 bits exatos para INT4. Não inclui metadados de quantização, cache KV, ativações, overhead do runtime ou VRAM. Portanto, o resultado é uma triagem inicial, não garantia de execução.
