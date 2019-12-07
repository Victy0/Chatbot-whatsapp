import re
from bot import wppbot

bot = wppbot('Robozin')
bot.treina('treino')
bot.inicia('Redes - policia do zap')
bot.saudacao(['BOT: Oi, sou o Zac Zapson!','BOT: Use :: no início para falar comigo'])
ultimo_texto = ''



while True:

    texto = bot.escuta()

    if texto != ultimo_texto and re.match(r'^::', texto):

        ultimo_texto = texto
        texto = texto.replace('::', '')
        texto = texto.lower()

        if (te xto == 'aprender' or texto == ' aprender' or texto == 'ensinar' or texto == ' ensinar'):
            bot.aprender(texto,'BOT: Escreva a pergunta e após o ? a resposta.','BOT: Obrigado por ensinar! Agora já sei!','BOT: Você escreveu algo errado! Comece novamente..')
        elif (texto == 'noticias' or texto == ' noticias' or texto == 'noticia' or texto == ' noticia' or texto == 'notícias' or texto == ' notícias' or texto == 'notícia' or texto == ' notícia'):
            bot.noticias()
        else:
            bot.responde(texto)