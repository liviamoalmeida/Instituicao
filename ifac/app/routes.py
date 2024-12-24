from flask import render_template, request
from app import app

# Lista de notícias
noticias = [
    {
        'data': '20/12/2024',
        'titulo': 'Ifac publica lista final dos inscritos nos cursos técnicos para 2025',
        'link': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-publica-lista-final-dos-inscritos-nos-cursos-tecnicos-para-2025',
        'imagem': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-publica-lista-final-dos-inscritos-nos-cursos-tecnicos-para-2025/5165f302-f8e6-4df9-815a-659d79436090.png/@@images/8ecff57e-2eef-4e46-b40b-e9d4fde1e832.png'
    },
    {
        'data': '20/12/2024',
        'titulo': 'Publicado resultado final de concurso público para docente do Ifac',
        'link': 'https://www.ifac.edu.br/noticias/2024/dezembro/publicado-resultado-final-de-concurso-publico-para-docente-do-ifac',
        'imagem': 'https://www.ifac.edu.br/noticias/2024/dezembro/publicado-resultado-final-de-concurso-publico-para-docente-do-ifac/84caf175-c196-41c8-af48-daf7153d6e69.jpeg/@@images/0e017b04-ac1e-472a-8c3e-899e9652c148.jpeg'
    },
    {
        'data': '19/12/2024',
        'titulo': 'Ifac certifica primeira turma do novo campus da Transacreana',
        'link': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-certifica-primeira-turma-do-novo-campus-da-transacreana',
        'imagem': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-certifica-primeira-turma-do-novo-campus-da-transacreana/certificacao-transacreana-1.jpg/@@images/c57af4dc-cd14-4794-8afc-644f72a2deed.jpeg'
    },
    {
        'data': '19/12/2024',
        'titulo': 'Ifac convida a comunidade para conhecer o Campus Transacreana',
        'link': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-convida-a-comunidade-para-conhecer-os-projetos-do-campus-transacreana-1',
        'imagem': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-convida-a-comunidade-para-conhecer-os-projetos-do-campus-transacreana-1/campus-transacreana.jpg/@@images/9829d80f-46d2-4242-a156-8b5df6938f7f.jpeg'
    },
    {
        'data': '19/12/2024',
        'titulo': 'Ifac arrecada mais de 770 brinquedos e quase meia tonelada de alimentos em ações para o Natal',
        'link': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-arrecada-mais-de-770-brinquedos-e-quase-meia-toneladas-de-alimentos-em-acoes-para-o-natal-1',
        'imagem': 'https://www.ifac.edu.br/noticias/2024/dezembro/ifac-arrecada-mais-de-770-brinquedos-e-quase-meia-toneladas-de-alimentos-em-acoes-para-o-natal-1/imagens_materias_capa_20241219_111647_0000.png/@@images/bb646b34-5a4f-4c4d-8e39-1bad9515931e.png'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos/')
def cursos():
    return render_template('cursos.html')

@app.route('/campi/')
def campi():
    return render_template('campi.html')

@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    query = request.form['query'].lower()  # Captura a consulta da pesquisa
    resultados = []

    # Filtra as notícias com base no título ou na data
    for noticia in noticias:
        if query in noticia['titulo'].lower() or query in noticia['data'].lower():
            resultados.append(noticia)

    # Renderiza a página de resultados com os resultados filtrados
    return render_template('resultados.html', resultados=resultados, query=query)

