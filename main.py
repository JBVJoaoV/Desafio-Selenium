# Importa as bibliotecas utilizaddas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cria uma função para aguardar o elemento estar na tela
def aguardar(navegador, By, value, timeout=10):
    """
    Aguarda até que um elemento esteja presente no DOM, dentro do tempo limite especificado.

    Parâmetros:
        navegador (webdriver): Instância atual do navegador Selenium.
        by (By): Tipo de seletor a ser usado (ex: By.ID, By.CLASS_NAME).
        value (str): Valor correspondente ao seletor (ex: "login-button").
        timeout (int, opcional): Tempo máximo de espera em segundos. Padrão é 10.

    Retorna:
        WebElement: O elemento encontrado assim que estiver presente no DOM.

    Exceções:
        Lança TimeoutException se o elemento não for encontrado dentro do tempo limite.
    """
    return WebDriverWait(navegador, timeout).until(EC.presence_of_element_located((By, value)))

# Cria uma função para esperar 3 segundos
def esperar():
    """Uma função sem parametros, criada para um delay de 3 segundos para a melhor visualização das etapas"""
    time.sleep(2)

# Define configurações do navegador e coloca em modo anonimo 
options = Options()
options.add_argument("--incognito")
options.add_argument("--start-maximized")

# Abre o navegador com as configurações definidas
navegador = webdriver.Chrome(options=options)

# Acessas o link do desafio e maximiza a tela 
navegador.get("https://www.saucedemo.com/")

# Obtem e divide os elementos contidos nas divs de creddenciais, e senha
login_div = aguardar(navegador, By.ID, "login_credentials")
usernames = login_div.text.split("\n")[1:]
username = usernames[0]

password_div = aguardar(navegador, By.CLASS_NAME, "login_password")
password = password_div.text.split("\n")[1]

# Preenche os campos com as informações obtidas, e passa para a proxima pagina
aguardar(navegador, By.ID, "user-name").send_keys(username)
aguardar(navegador, By.ID, "password").send_keys(password)
esperar()

login_button = aguardar(navegador, By.ID, "login-button").click()
esperar()

# Gera uma lista com todos os botões de compra com base no css, e clica neles
botoes = WebDriverWait(navegador, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory"))
)
for botao in botoes:
    botao.click()
esperar()

# Encontra e clica no carrinho
carrinho = aguardar(navegador, By.CLASS_NAME, "shopping_cart_link").click()
esperar()

# Gera uma lista com os botões do elemetos dentro do carrinho e tira todos, menos os 2 primeiros
remover = WebDriverWait(navegador, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.cart_button"))
)
for i, item in enumerate(remover):
    if i >= 2:
        item.click()
esperar()

# Encontra e clica no botão de checkout
checkout = aguardar(navegador, By.ID, "checkout").click()
esperar()

# Preenche as informações de Checkout e clica no botão de continuar
nome = aguardar(navegador, By.ID, "first-name").send_keys("João")
sobrenome = aguardar(navegador, By.ID, "last-name").send_keys("Vieira")
cep = aguardar(navegador, By.ID, "postal-code").send_keys("00000")
esperar()

continue_button = aguardar(navegador, By.ID, "continue").click()
esperar()

# Encontra e clica no botão para finalizar a tareda
finish_button = aguardar(navegador, By.ID, "finish").click()
esperar()

# Aguarda a mensagem de confirmação e valida
try:
    mensagem_elemento = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    mensagem = mensagem_elemento.text

    if "THANK YOU FOR YOUR ORDER" in mensagem.upper():
        print("✅ Compra finalizada com sucesso!")
    else:
        print("❌ Mensagem de sucesso não corresponde ao esperado.")
except:
    print("❌ Confirmação de compra não encontrada a tempo.")

# Fecha o navegador 
navegador.quit()