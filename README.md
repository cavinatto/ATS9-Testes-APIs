# ATS9 - Testes APIs

Projeto de testes de APIs utilizando Tavern, um framework declarativo para testes de API baseado em YAML.

## 📋 Descrição

Este projeto implementa testes automatizados para validar fluxos de tarefas através de APIs REST. Os testes utilizam a API JSONPlaceholder como referência para demonstrar:

- Requisições HTTP (GET, POST, etc.)
- Captura e reutilização de variáveis entre stages
- Parametrização de testes
- Validação de respostas

## 🛠️ Stack Tecnológico

- **Python 3.14.2**
- **Tavern 3.3.3** - Framework para testes de API
- **Pytest 9.0.2** - Test runner
- **Requests** - Cliente HTTP (usado internamente pelo Tavern)

## 📁 Estrutura do Projeto

```
ATS9 - Testes APIs/
├── README.md                          # Este arquivo
├── test_fluxo_todos.tavern.yaml      # Teste principal em Tavern
├── test_performance.py                # Testes de performance
├── api_pagamentos.py                  # Módulo de API de pagamentos
├── utils.py                           # Utilitários e validações customizadas
└── __pycache__/                       # Cache Python
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. Instale as dependências:
```bash
pip install tavern pytest requests
```

2. Navegue até o diretório do projeto:
```bash
cd "c:\Users\2400911\Downloads\ATS9 - Testes APIs"
```

### Executar os Testes

**Executar o teste Tavern:**
```bash
python -m pytest test_fluxo_todos.tavern.yaml -v
```

**Executar com saída detalhada:**
```bash
python -m pytest test_fluxo_todos.tavern.yaml -v -s
```

**Executar todos os testes:**
```bash
python -m pytest
```

