# Integra-o-e-projeto-UC1-UC2---Dimensionamento-LLM[README.md](https://github.com/user-attachments/files/34050925/README.md)
# AI Edge Estimator

Calculadora de viabilidade para execução local de modelos de linguagem (LLMs), desenvolvida em Python como projeto integrador das unidades curriculares **UC1 + UC2**.

> **Status:** em desenvolvimento. Este README descreve o escopo planejado; as funcionalidades serão implementadas ao longo do projeto.

## Objetivo

Estimar se uma máquina possui memória suficiente para carregar os pesos de um modelo de IA localmente, considerando a quantidade de parâmetros e a precisão numérica utilizada.

O projeto integra conceitos de **arquitetura de computadores** (RAM, VRAM, representação numérica e processamento) com **programação em Python** e **colaboração via Git/GitHub**.

## Funcionalidades planejadas

- Catálogo de modelos, inicialmente **Llama 3 8B** e **Mistral 7B**.
- Seleção do modelo e da precisão (**FP16** ou **INT4**).
- Estimativa da memória necessária para armazenar os pesos do modelo.
- Identificação da RAM total e disponível da máquina com a biblioteca `psutil`.
- Comparação entre memória estimada e RAM disponível, com aviso de possível falta de memória (*Out of Memory*, OOM).
- Saída de resultados no terminal.

**Limitação importante:** a estimativa inicial considera principalmente a memória dos pesos. A execução real também consome memória para contexto (KV cache), buffers e runtime. Além disso, `psutil` não informa diretamente a VRAM da GPU. Portanto, um resultado favorável **não garante** que o modelo será executado com sucesso.

## Fórmula de estimativa

A estimativa teórica dos pesos, em gigabytes decimais (GB), é:

```text
memoria_GB = (parametros * bits_por_parametro) / (8 * 1_000_000_000)
```

Exemplo para um modelo de **8 bilhões de parâmetros**:

| Precisão | Bits por parâmetro | Memória teórica dos pesos |
|---|---:|---:|
| FP16 | 16 | 16 GB |
| INT4 | 4 | 4 GB |

Valores aproximados, sem overhead de quantização ou execução. Os formatos reais de quantização podem exigir memória adicional.

## Estrutura planejada

```text
ai-edge-estimator/
├── main.py                # Entrada do programa e interação no terminal
├── models.py              # Catálogo de modelos e parâmetros
├── calculator.py          # Cálculo de memória e verificação de viabilidade
├── hardware.py            # Leitura de RAM usando psutil
├── requirements.txt       # Dependências Python
├── tests/
│   └── test_calculator.py # Testes dos cálculos
└── README.md
```

> Os arquivos acima representam a estrutura prevista e podem ainda não existir no repositório.

## Requisitos e execução (após implementação)

- Python 3.10 ou superior (recomendado).
- Git, para colaboração e controle de versão.
- Biblioteca `psutil`.

Após clonar o repositório, na pasta do projeto:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências (quando o arquivo estiver disponível):

```bash
python -m pip install -r requirements.txt
```

Execute o programa (quando implementado):

```bash
python main.py
```

## Exemplo de resultado esperado

```text
=== AI EDGE ESTIMATOR ===
Modelo: Llama 3 8B
Precisão: INT4
Memória estimada dos pesos: 4.00 GB
RAM disponível: 12.00 GB

Resultado: memória suficiente para os pesos.
Atenção: a execução real requer memória adicional.
```

*Saída ilustrativa; não representa uma execução já validada.*

## Divisão de responsabilidades

### Aluno A — Tech Lead

1. Criar e administrar o repositório original.
2. Definir a estrutura inicial do projeto.
3. Implementar o catálogo de modelos em `models.py`.
4. Preparar a entrada principal em `main.py`.
5. Revisar, aprovar e integrar o Pull Request do contribuidor.
6. Validar o funcionamento do projeto integrado.

### Aluno B — Contribuidor

1. Fazer um **Fork** do repositório e cloná-lo.
2. Criar uma branch de funcionalidade.
3. Implementar o cálculo de memória em `calculator.py`.
4. Implementar a leitura da RAM em `hardware.py`, usando `psutil`.
5. Adicionar testes e verificar cenários de memória suficiente e insuficiente.
6. Fazer commit, push e abrir um **Pull Request** para o repositório original.

## Fluxo colaborativo com GitHub

O contribuidor executa, adaptando a URL ao próprio Fork:

```bash
git clone https://github.com/SEU-USUARIO/ai-edge-estimator.git
cd ai-edge-estimator
git switch -c feature/memory-estimator
```

Após implementar e testar:

```bash
git add .
git commit -m "feat: adiciona estimativa de memoria e leitura de RAM"
git push -u origin feature/memory-estimator
```

Em seguida, abre um **Pull Request** no GitHub, direcionado à branch principal do repositório original. O Tech Lead revisa o código, solicita ajustes se necessário e realiza o **Merge** após a aprovação.

## Critérios de validação

- [ ] Catálogo de modelos implementado.
- [ ] Cálculo de memória para FP16 e INT4 funcionando.
- [ ] Leitura de RAM com `psutil` funcionando.
- [ ] Verificação de viabilidade e aviso de OOM implementados.
- [ ] Testes cobrindo cenários de memória suficiente e insuficiente.
- [ ] Pull Request aberto, revisado e integrado.
- [ ] Programa final executado e documentado.

## Possíveis melhorias futuras

- Detecção de VRAM para GPUs compatíveis.
- Suporte a outras precisões, como INT8.
- Margem configurável para memória adicional de execução.
- Catálogo ampliado de modelos.
- Interface gráfica ou web.

## Contexto acadêmico

**Projeto Integrador UC1 + UC2**

- **UC1:** fundamentos de hardware, memória e arquitetura de sistemas.
- **UC2:** programação Python, implementação de funções e colaboração no desenvolvimento.

---

Desenvolvido para fins educacionais.
