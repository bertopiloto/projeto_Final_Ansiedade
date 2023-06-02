from flask import Flask, render_template, request

app = Flask(__name__)

perguntas = [
    {
        'pergunta': 'Você tem dificuldade em respirar?',
        'sintomas': ['sindrome_panico', 'ansiedade']
    },
    {
        'pergunta': 'Você ouve vozes que outras pessoas não ouvem?',
        'sintomas': ['esquizofrenia']
    },
    {
        'pergunta': 'Você se sente triste na maior parte do tempo?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você experimenta mudanças extremas de humor?',
        'sintomas': ['bipolaridade']
    },
    # Adicione mais perguntas aqui
    {
        'pergunta': 'Você já experimentou ataques súbitos de medo intenso ou desconforto?',
        'sintomas': ['sindrome_panico']
    },
    {
        'pergunta': 'você sente sintomas físicos como palpitações, sudorese, tremores, falta de ar ou sensação de asfixia?',
        'sintomas': ['sindrome_panico']
    },
    # Continue adicionando mais perguntas até completar 60
    {
        'pergunta': 'Você evita lugares ou situações específicas devido ao medo de ter um ataque de pânico??',
        'sintomas': ['sindrome_panico']
    },
    {
        'pergunta': 'Você sente medo intenso de perder o controle ou enlouquecer durante um ataque de pânico?',
        'sintomas': ['sindrome_panico']
    },
    {
        'pergunta': 'Você tem medo de ter novos ataques de pânico e isso interfere em sua vida diária?',
        'sintomas': ['sindrome_panico']
    },
    {
        'pergunta': 'Você sente que seus pensamentos estão sendo controlados ou influenciados por forças externas?',
        'sintomas': ['esquizofrenia']
    },
    {
        'pergunta': 'Você experimenta delírios, como crenças irracionais e infundadas sobre si mesmo ou o mundo ao seu redor?',
        'sintomas': ['esquizofrenia']
    },
    {
        'pergunta': 'Você tem dificuldade em distinguir entre o que é real e o que não é real?',
        'sintomas': ['esquizofrenia']
    },
    {
        'pergunta': 'Você experimenta uma falta de motivação ou interesse em atividades que antes considerava prazerosas?',
        'sintomas': ['esquizofrenia']
    },
    {
        'pergunta': 'Você se sente triste ou deprimido na maior parte do tempo, quase todos os dias?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você perdeu o interesse ou prazer em atividades que antes achava agradáveis?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você tem alterações significativas no apetite ou no peso (perda ou ganho)?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você sente fadiga ou falta de energia frequentemente?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você chora sem motivo aparente?',
        'sintomas': ['depressao']
    },
    {
        'pergunta': 'Você experimenta períodos de humor elevado, conhecidos como episódios de mania, em que se sente excessivamente feliz, excitado ou irritado?',
        'sintomas': ['bipolaridade']
    },
    {
        'pergunta': 'Durante esses períodos de mania, você apresenta um aumento na energia, fala mais rapidamente do que o habitual e tem dificuldade em se concentrar?',
        'sintomas': ['bipolaridade']
    },
    {
        'pergunta': 'Você já teve períodos de depressão, nos quais se sentiu triste, sem esperança e com perda de interesse em atividades que antes eram agradáveis?',
        'sintomas': ['bipolaridade']
    },
    {
        'pergunta': 'Você tem oscilações frequentes entre períodos de mania e depressão?',
        'sintomas': ['bipolaridade']
    },
    {
        'pergunta': 'Você tem problemas com insônia ou dificuldade em dormir durante os episódios de mania?',
        'sintomas': ['bipolaridade']
    },
    {
        'pergunta': 'Você já tomou medidas impulsivas ou arriscadas durante os episódios de mania, como gastos excessivos, comportamento sexual imprudente ou uso de drogas?',
        'sintomas': ['bipolaridade']
    },
]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', perguntas=perguntas)


@app.route('/resultado', methods=['POST'])
def resultado():
    respostas = request.form

    sintomas_selecionados = []
    for pergunta in perguntas:
        if pergunta['pergunta'] in respostas:
            sintomas_selecionados.extend(pergunta['sintomas'])

    total_perguntas = len(perguntas)
    total_sintomas = len(sintomas_selecionados)
    porcentagem = (total_sintomas / total_perguntas) * 100

    resultado = 'Você apresenta os seguintes sintomas: ' + ', '.join(sintomas_selecionados)
    resultado += f'<br><br>A porcentagem de sintomas identificados é: {porcentagem:.2f}%'

    if porcentagem >= 50:
        resultado += '<br><br>Você pode estar com alguma doença. É altamente recomendável que você procure um profissional de saúde para uma avaliação adequada.'
    else:
        resultado += '<br><br>Você não parece apresentar sintomas significativos. No entanto, se estiver preocupado, é aconselhável consultar um profissional de saúde.'

    return render_template('resultado.html', resultado=resultado)


if __name__ == '__main__':
    app.run()