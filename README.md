<!--
Readme temporário. Ainda é necessário especificar:
- quais arquivos/pastas foram desenvolvidos por min; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->

## Inventory Report
<br>

### Contexto:

Esse projeto foi proposto pela  [Trybe](https://www.betrybe.com/)  como forma de avaliação após conclusão de uma seção do módulo de Ciência da Computação do curso de Desenvolvimento Web.

Toda a configuração do projeto e alguns arquivos necessários para a avaliação são de autoria da [Trybe](https://github.com/tryber) (arquivos e pastas do "initial commit"). O README original, testes, commits e alguns arquivo de autoria da Trybe foram removidos.
<br><br><br>


### Projeto:

Gerador de relatório que recebe dados de estoque por meio de arquivos CSV, JSON ou XML para emitir relatórios simples ou completos do estoque.
<br>

Esse programa foi desenvolvido usando Python, aplicando conceitos de Programação Orientada a Objetos e alguns Padrões de Projeto como Strategy e Iterator.
<br><br><br>

### Tecnologias usadas:
Python e Pytest
<br><br><br>


### Orientações para executar o projeto:

**Para testar esse programa em sua máquina é preciso ter o Python3, python3-venv e o pip instalados.**
<br><br>

-  Para clonar o repositório por GitHub CLI e entrar na pasta do projeto:
```bash
gh repo clone nayara-vasconcelos/trybe-inventory-report && cd trybe-inventory-report
```
<br>

- Para criar e ativar o ambiente virtual para o projeto:
```bash
python3 -m venv .venv && source .venv/bin/activate
```
<br>

- Para instalar as dependências e o programa no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt && pip install .
```
<br>

- Para executar o programa no terminal:
```bash
inventory_report inventory_report/data/inventory.csv completo
```
**Obs:** É possível testar com outros arquivos com o comando:
`inventory_report [caminho do arquivo] [tipo do relatório]`
<br>
O tipo do arquivo pode ser `simples` ou `completo`, o caminho dos arquivos é `inventory_report/data/`, o arquivo se chama `inventory` e está disponível nas extensões `.csv`, `.json`, `.xml`.

<br>

- Para desativar o ambiente virtual:
```bash
deactivate
```

<br><br>

*#OOP #DesignPatterns #Python*
