import telebot

CHAVE_API = "1977253598:AAHL5gFCUwtWLswd5L55nWdTbZjPdwE9Xdg"

bot = telebot.TeleBot(CHAVE_API)

#Processos da Área de Teste
@bot.message_handler(commands=["Massa_de_Teste"])
def Massa_de_Teste(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/display/TES/Massa+de+Teste")

@bot.message_handler(commands=["Processo_por_Fabrica"])
def Processo_por_Fabrica(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/display/TES/Processo+por+Fabrica")

#Controle de Versão e Repositórios
@bot.message_handler(commands=["Git"])
def Git(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/display/TES/Git")

@bot.message_handler(commands=["Git_Hub"])
def Git_Hub(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/display/TES/GitHub")

#Máquinas Automação
@bot.message_handler(commands=["Maquinas"])
def Maquinas(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=102109300")

@bot.message_handler(commands=["Liberacao_Path"])
def Liberacao_Path(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=118688219")

#Controle de Licenças
@bot.message_handler(commands=["Licencas"])
def Licencas(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=118688234")

#Trilha de Conhecimento QA
@bot.message_handler(commands=["Trilha_Estudos"])
def Trilha_Estudos(mensagem):
    bot.send_message(mensagem.chat.id, "APIs - Testes: https://confluence.prosoft.com.br:8061/display/TES/APIs+-+Testes")
    bot.send_message(mensagem.chat.id, "On-Premises > Automação: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=139003685")
    bot.send_message(mensagem.chat.id, "Qualidade do Produto - Conhecimento Fundamental: https://confluence.prosoft.com.br:8061/display/TES/Qualidade+do+Produto+-+Conhecimento+Fundamental")
    bot.send_message(mensagem.chat.id, "TDD - Testes Unitários: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=139003689")
    bot.send_message(mensagem.chat.id, "Web > Automação: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=139003690")
    bot.send_message(mensagem.chat.id, "Web > HTML + CSS: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=139003691")

@bot.message_handler(commands=["Automacao"])
def Automacao(mensagem):
    bot.send_message(mensagem.chat.id, "Estudos e Dicas - Testes: https://confluence.prosoft.com.br:8061/display/TES/Estudos+e+Dicas")
    bot.send_message(mensagem.chat.id, "Conceitos utilizados pela Automação: https://confluence.prosoft.com.br:8061/pages/viewpage.action?pageId=35390848")


@bot.message_handler(commands=["Tecnicas"])
def Tecnicas(mensagem):
    bot.send_message(mensagem.chat.id, "Planejar: https://confluence.prosoft.com.br:8061/display/TES/1+-+Planejar")
    bot.send_message(mensagem.chat.id, "Projetar: https://confluence.prosoft.com.br:8061/display/TES/2+-+Projetar")

#Papel do QA
@bot.message_handler(commands=["Papel_do_QA"])
def Papel_do_QA(mensagem):
    bot.send_message(mensagem.chat.id, "Clique no link: https://confluence.prosoft.com.br:8061/display/TES/Papel+analista+de+qualidade+detalhado")



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Massa_de_Teste Mapa de Processo criado para ajudar o qa a montar um fluxo para sua fabrica.
    /Processo_por_Fabrica Saiba como é criado o mapa de processo por funcionalidade.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Git Passo a passo orientando como funciona o versionamento pelo Git.
    /Git_Hub Entenda um pouco mais sobre esse repositório.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Maquinas Aqui você encontrará todas as maquinas reservadas para as automações Desktop das fábricas.
    /Liberacao_Path Vm´s exclusivas para os testes automatizados de liberação.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Licencas Saiba quais e quantas licenças temos disponiveis.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Trilha_Estudos Aprofunde seu conhecimento.
    /Automacao Dicas e Conceitos sobre Automação.
    /Tecnicas Conheça Técnicas de teste.
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao6"])
def opcao6(mensagem):
    texto = """
    Selecione a opção desejada: (Clique em uma opção)
    /Papel_do_QA O que é,faz ou não faz um qa.
    """
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Bem Vindos ao nosso Ambiente de QA. Aqui você poderá aprofundar seus conhecimentos nesse universo incrivel da qualidade (Clique no item):
     /opcao1 Processos da Área de Teste
     /opcao2 Controle de Versão e Repositórios
     /opcao3 Máquinas Automação
     /opcao4 Controle de Licencas
     /opcao5 Trilha de Conhecimento QA
     /opcao6 Papel do QA
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()