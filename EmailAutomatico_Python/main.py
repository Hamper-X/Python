# IMPORTS ====================================
import os
import smtplib

# FUNCOES ====================================

def getName(email):
    nome, _ = email.strip().split('@')
    return nome

def mensageGenerator(nome):
    mensagem = f"""Bom dia, {nome.capitalaze()}
    Gostaria de lhe dar os parabéns pelo trabalho e dedicação,
    Nos, do curso de ciencia da computação, ficamos felizes em
    ter professores tão capacitados como vocês.  
    """
    return mensagem

def sendEmail(email,mensagem,titulo):
    try:
            msgFrom = email
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            msgTo = 'origem@gmail.com'
            toPass = 'senha'
            smtpObj.login(msgTo, toPass)
            msg = mensagem
            smtpObj.sendmail(msgTo,msgFrom,f"Subject: {titulo}")
            smtpObj.quit()
            print("Email enviado com sucesso!")
    except:
            print("Erro ao enviar e-mail")
# MAIN    ====================================

def main():
    arqWay = os.path.join(os.getcwd(), 'cadastro_professores.txt')
    with open(arqWay) as arq:
        for email in arq:
            nome = getName(email)
            mensagem = mensageGenerator(nome)
            sendEmail(email,mensagem,"Parabenizações")
if __name__ == "__main__":
    main()
