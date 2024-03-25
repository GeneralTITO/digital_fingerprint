# Sistema modelo de Registro de Ponto de Funcionários

## Visão Geral

Este é um sistema modelo de registro de ponto de funcionários, desenvolvido para facilitar o acompanhamento preciso do horário de entrada e saída dos colaboradores.

## Funcionalidades Principais

- Registro de ponto de entrada e saída.
- Relatórios de presença diários

## Como usar :

 ### 1- Entre na área admin e cadastre  funcionarios
 ![entrando na área admin](./img//admin.png)
 ![cadastrando funcionario](./img/cadastrando.png)
 ### 1.1- Cadastre a digital
 ![cadastrando funcionario](./img/digital.png)
 ![aperte em 'next'](./img/digital1.png)
 ![escolha o dedo que quer cadastrar](./img/digital2.png)
 ![siga as instruções](./img/digital3.png)

 ## 2- Agora você pode voltar e verificar sua digital.
 ![verifica](./img/verifica.png)
 ![verifica](./img/verifica1.png)

 Ao fazer a verificação, a confirmação pode vir de inumeras formas, como é um programa modelo, e de baixo custo, o funcionario receberá um email para a confirmação
 ![verifica](./img/verifica2.png)

 Para o controle de horários, também foi feita uma forma de baixo custo:
  Junto com o programa é iniciado um bot do telegram, que pode enviar as informações que for solicitado remotamente.
 ![verifica](./img/telegram.png)



## To Do:
- [X] cadastrar salvando em um arquivo
- [X] limpar os campos das entry após o cadastro
- [X] por os dados do arquivo na treeview
- [X] fazer a verificação
- [X] fazer um arquivo mostrando quem foi verificado e o horario
- [X] poder editar esses dados
- [X] cadastrar salvando em um arquivo
- [X] enviar os dados no telegram por dia escolhido
- [X] aumentar a tela do admin e trocar o telefone por email
- [X] verificação na hora de cadastrar para n ir vazio
- [X] enviar email de confirmação do ponto pro funcionario
- [X] poder excluir um funcionario
- [ ] salvar o arquivo de dados na nuvem
- [ ] poder abrir um arquivo 

## Como Executar o Sistema de Registro de Ponto de Funcionários

### Requisitos:
1. Ter um Leitor Biométrico Nitgen Hamster III/DX
2. Ter o compilador C/C++ MSVC para compilar a biblioteca modificada `nbsp_fingerprint`.
3. Ter Python instalado.
4. Instalar todas as bibliotecas listadas no arquivo `requirements.txt`.

### Passos para Execução:

1. Compile a biblioteca modificada `nbsp_fingerprint`.
entre na pasta dela e rode o comando:
 ```python
pip install .
``` 
3. Instale as bibliotecas Python necessárias usando o arquivo `requirements.txt`.
saia da pasta da biblioteca e rode:
```python
pip install -r requirements.txt
``` 
3. Execute o comando:
```python
python main.py
``` 

