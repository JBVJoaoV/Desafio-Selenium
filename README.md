# 🧪 Desafio Selenium - Evo Systems

Este projeto tem como objetivo automatizar o fluxo completo de compra no site de testes [SauceDemo](https://www.saucedemo.com/) utilizando **Python** e **Selenium WebDriver**.

## ✅ Como instalar as dependências

1. Verifique se você possui o **Python 3.10+** instalado na sua máquina, com o comando:

```bash
python -V

```

2. Instale o Selenium executando o seguinte comando no terminal:

```bash
pip install selenium
```

> 💡 **Observação:** Certifique-se de executar este comando **dentro da pasta onde o projeto está localizado**, para garantir que o ambiente correto seja utilizado (especialmente se estiver usando um ambiente virtual).


## ▶️ Como executar o script

1. Clone este [repositório](https://github.com/JBVJoaoV/Desafio-Selenium) ou extraia os arquivos main.py e README.md.
2. No terminal, execute o script com:

```bash
python main.py
```

## 🧪 Cenários de Teste Cobertos

### ✅ 1. Login com credenciais visíveis na interface do SauceDemo
O script acessa o site e extrai automaticamente o nome de usuário e a senha exibidos na interface.
Essas credenciais são usadas para realizar o login sem necessidade de digitação manual.

### ✅ 2. Adição de todos os produtos ao carrinho
Após o login, o script localiza todos os botões "Add to cart" e clica neles, adicionando todos os produtos disponíveis ao carrinho.

### ✅ 3. Remoção de todos os produtos, exceto dois
No carrinho, o script localiza todos os botões "Remove" e clica neles, mantendo apenas os dois primeiros itens na lista.

### ✅ 4. Preenchimento do formulário de checkout
O script preenche automaticamente os campos obrigatórios do checkout: primeiro nome, sobrenome e código postal.

### ✅ 5. Finalização do pedido
Após preencher os dados, o script clica em "Continue" e depois em "Finish" para concluir a compra.

### ✅ 6. Validação da mensagem de confirmação de compra
O script aguarda a exibição da mensagem "THANK YOU FOR YOUR ORDER" e valida se ela realmente apareceu, confirmando o sucesso da operação.

## 🔁 O que o código faz

O script automatiza, com o Selenium WebDriver, o processo completo de compra no site de testes [SauceDemo](https://www.saucedemo.com/), simulando o comportamento de um usuário real. Abaixo está o detalhamento completo de cada etapa:

1. **Inicializa o navegador em modo anônimo:**
   - Utiliza a biblioteca `webdriver` do Selenium com opções de privacidade ativadas (para configurar o navegador em modo anônimo, evitando assim pop-ups indesejados).
   - O navegador é aberto e a janela é maximizada para garantir que todos os elementos fiquem visíveis durante a execução.

2. **Acessa o site SauceDemo:**
   - O script acessa diretamente a URL `https://www.saucedemo.com`, onde está localizada a interface de login do desafio.

3. **Extrai dinamicamente as credenciais da tela de login:**
   - O nome de usuário e a senha são obtidos diretamente da interface da página, extraindo o texto presente nas tags:
    `<div id="login_credentials">`
    `<div class="login_password">`.
   
      Isso elimina a necessidade de credenciais fixas no código e garante maior robustez em testes.

4. **Preenche os campos de login e realiza o login:**
   - Os campos `user-name` e `password` são preenchidos usando os dados extraídos.
   - Em seguida, o botão de login é clicado para acessar a área autenticada do site.

5. **Adiciona todos os produtos ao carrinho:**
   - O script localiza todos os botões "Add to cart" usando o seletor CSS correspondente e clica em cada um deles.
   - Isso simula um usuário adicionando todos os itens disponíveis à sua cesta.

6. **Acessa o carrinho de compras:**
   - Após adicionar os produtos, o script clica no ícone do carrinho (`.shopping_cart_link`) para acessar a lista de itens adicionados.

7. **Remove todos os produtos, exceto dois:**
   - Dentro do carrinho, o script coleta os botões "Remove" e clica neles para remover os produtos **a partir do terceiro**.
   - Com isso, apenas dois produtos permanecem no carrinho.

8. **Inicia o processo de checkout:**
   - O botão `checkout` é clicado para avançar para o formulário de dados do cliente.
   - O script então preenche os campos obrigatórios:
     - Primeiro nome (`first-name`)
     - Sobrenome (`last-name`)
     - Código postal (`postal-code`)
   - Após preencher, o botão `continue` é clicado para prosseguir.

9. **Finaliza a compra:**
   - O script localiza e clica no botão `finish`, finalizando a simulação de compra.

10. **Valida a mensagem de confirmação de pedido:**
    - A automação aguarda a aparição do texto `"THANK YOU FOR YOUR ORDER"` na tela, que indica sucesso no processo de compra.
    - Se a mensagem for encontrada, o script imprime um log de sucesso no terminal.

11. **Encerra o navegador:**
    - Ao final do processo, o navegador é fechado automaticamente.

Esse fluxo cobre todos os requisitos do desafio proposto pela Evo Systems, simulando uma jornada de compra real com login, navegação, ações no carrinho, checkout e validação final.


## 📁 Estrutura do Repositório

Desafio-Selenium/

├── main.py # Script principal que executa o fluxo de automação com Selenium

└── README.md # Documentação explicando instalação, execução e cenários de teste

## 🚀 Requisitos

- Python 3.10 ou superior
- Google Chrome instalado
- Driver do Chrome compatível com sua versão (disponível no PATH)
