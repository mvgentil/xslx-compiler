# XLSX Compiler

![Fluxo](docs/static/fluxo.png)

Este projeto é um script compilador de arquivos XLSX. Ele transforma diversos arquivos XLSX que contenham a mesma estrutura em um único arquivo XLSX.

## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python 3.12.1**
- **[uv](https://github.com/astral-sh/uv)**: Para gerenciamento do ambiente virtual.
- Outras bibliotecas podem ser encontradas no arquivo `requirements.txt`.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas antes de rodar o projeto:

- Python 3.x
- Git
- `uv` para gerenciamento do ambiente virtual

## Instalação e Configuração Local

Siga os passos abaixo para configurar o projeto localmente em sua máquina.

### 1. Clone o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

### 2. Crie um Ambiente Virtual com `uv`

Crie um ambiente virtual utilizando o `uv`:

```bash
uv venv --python 3.12.1
```

### 3. Ative o Ambiente Virtual

Para sistema Windows:
```bash
source .venv/scripts/activate
```

### 4. Instale as bibliotecas com `uv`

```bash
uv sync
```

### 5. Execute o script
Ao executar o script, um novo arquivo no diretório data/output será gerado com o compilado de arquivos xlsx
```bash
uv run app/main.py
```