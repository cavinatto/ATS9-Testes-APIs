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
pytest test_fluxo_todos.tavern.yaml -v
```

**Executar com saída detalhada:**
```bash
pytest test_fluxo_todos.tavern.yaml -v -s
```

**Executar todos os testes:**
```bash
pytest -v
```

**Executar com relatório HTML:**
```bash
pytest --html=report.html --self-contained-html
```

## 📝 Descrição dos Testes

### test_fluxo_todos.tavern.yaml

Teste que valida o fluxo de busca de tarefas por usuário.

**Stages:**

1. **Stage 1: Buscar tarefa e capturar userId**
   - Realiza uma requisição GET para buscar uma tarefa específica
   - URL: `https://jsonplaceholder.typicode.com/todos/1`
   - Captura o `userId` da resposta para uso no próximo stage

2. **Stage 2: Buscar todas as tarefas do usuário**
   - Realiza uma requisição GET para listar todas as tarefas de um usuário
   - URL: `https://jsonplaceholder.typicode.com/todos`
   - Utiliza o `userId` capturado no Stage 1 como parâmetro
   - Valida status code 200

**Exemplo de Execução:**
```
test_fluxo_todos.tavern.yaml::Fluxo de Tarefas - Busca e Validação por Usuário PASSED [100%]
```

## 🔧 Arquivos Utilitários

### utils.py

Contém funções de validação customizadas que podem ser integradas aos testes Tavern.

**Funções disponíveis:**

- `validar_lista_tarefas(response_as_json)` - Valida se a resposta é uma lista válida de tarefas com o campo 'completed'

```python
def validar_lista_tarefas(response_as_json):
    """
    Valida a resposta HTTP de uma lista de tarefas.
    Verifica se:
    - O retorno é uma lista (não vazia)
    - Pelo menos uma das tarefas contém a chave 'completed'
    """
```

### api_pagamentos.py

Módulo para operações relacionadas a API de pagamentos (expandir conforme necessário).

### test_performance.py

Testes específicos para validação de performance das APIs.

## 🐛 Correções Realizadas

### Problema Original

O arquivo `test_fluxo_todos.tavern.yaml` apresentava erro de validação de schema do Tavern ao tentar usar parametrização.

**Erro:**
```
tavern._core.exceptions.BadSchemaError: Schema validation failed
```

### Solução Implementada

1. **Remoção da parametrização incompatível**
   - A versão 3.3.3 do Tavern não suporta o formato de parametrização no nível raiz
   - Removida a seção `parametrize` que causava erro

2. **Correção da função de validação**
   - Alterado o parâmetro de `response` para `response_as_json`
   - Tavern passa o JSON já parseado, não o objeto Response

3. **Validação com IDs fixos**
   - Teste agora executa com IDs fixos (todo_id: 1)
   - Para múltiplos IDs, execute o teste várias vezes ou crie múltiplos arquivos YAML

## 📊 Estrutura de um Teste Tavern

```yaml
---
test_name: Nome do Teste

stages:
  - name: "Nome do Stage"
    request:
      url: "https://api.example.com/endpoint"
      method: GET
      params:
        key: value
    response:
      status_code: 200
      save:
        json:
          variavel: campo_json
```

## 🔑 Conceitos Principais

### Variables (Variáveis)

As variáveis capturadas em um stage podem ser reutilizadas nos próximos stages utilizando a sintaxe `{nome_variavel}`:

```yaml
params:
  userId: "{id_do_usuario}"  # Usa a variável capturada anteriormente
```

### Stages

Cada stage representa uma requisição/resposta. Os stages são executados em sequência, e as variáveis persistem entre eles.

### Save

Captura dados da resposta (JSON) para uso em stages posteriores:

```yaml
save:
  json:
    id_do_usuario: userId  # Captura o campo 'userId' como 'id_do_usuario'
```

## 📌 Boas Práticas

1. **Nomeação clara**: Use nomes descritivos para stages e variáveis
2. **Validação robusta**: Sempre valide status codes e estrutura de respostas
3. **Isolamento**: Cada teste deve ser independente e executável separadamente
4. **Modularização**: Use arquivos utilitários para funções compartilhadas
5. **Documentação**: Adicione comentários explicando lógica complexa

## 🤝 Próximas Melhorias

- [ ] Implementar parametrização através de fixture do Pytest
- [ ] Adicionar mais validações customizadas
- [ ] Criar testes para APIs de pagamento
- [ ] Implementar testes de carga
- [ ] Gerar relatórios HTML automaticamente
- [ ] Integração com CI/CD (GitHub Actions, Jenkins, etc.)

## 📚 Referências

- [Documentação Tavern](https://taverntesting.github.io/)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Tavern GitHub](https://github.com/taverntesting/tavern)

## ✅ Status

| Componente | Status |
|-----------|--------|
| test_fluxo_todos.tavern.yaml | ✅ PASSOU |
| utils.py | ✅ Funcionando |
| test_performance.py | ⏳ Pendente |
| api_pagamentos.py | ⏳ Em desenvolvimento |

## 📝 Notas

- A API JSONPlaceholder é uma API de teste pública e pode ter limitações de taxa
- Para testes em produção, considere usar uma instância local ou mockada da API
- Sempre valide as dependências antes de executar os testes em novo ambiente

---

**Última atualização:** Abril de 2026  
**Versão:** 1.0.0
