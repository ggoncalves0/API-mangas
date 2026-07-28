from flask import Flask, jsonify, request

app = Flask(__name__)

mangas = [
    {
        'id': 1,
        'titulo': 'Tokyo Ghoul',
        'autor': 'Sui Ishida',
    },
    {
        'id': 2,
        'titulo': 'Berserk',
        'autor': 'Kentaro Miura',
    },
    {
        'id': 3,
        'titulo': 'Vagabond',
        'autor': 'Takehiko Inoue',
    },
]


@app.route('/mangas', methods=['GET'])
def obter_mangas():
    return jsonify(mangas)


@app.route('/mangas/<int:manga_id>', methods=['GET'])
def obter_manga_por_id(manga_id):
    for manga in mangas:
        if manga['id'] == manga_id:
            return jsonify(manga)
    return jsonify({'erro': 'Manga não encontrado'}), 404


@app.route('/mangas/<int:manga_id>', methods=['PUT'])
def editar_manga_por_id(manga_id):
    manga_alterado = request.get_json(silent=True)
    if not manga_alterado:
        return jsonify({'erro': 'JSON inválido ou ausente'}), 400

    for indice, livro in enumerate(mangas):
        if livro.get('id') == manga_id:
            mangas[indice].update(manga_alterado)
            return jsonify(mangas[indice])
    return jsonify({'erro': 'Manga não encontrado'}), 404


@app.route('/mangas', methods=['POST'])
def criar_manga():
    novo_manga = request.get_json(silent=True)
    if not novo_manga:
        return jsonify({'erro': 'JSON inválido ou ausente'}), 400

    novo_id = max((m['id'] for m in mangas), default=0) + 1
    novo_manga['id'] = novo_id
    mangas.append(novo_manga)
    return jsonify(novo_manga), 201


@app.route('/mangas/<int:manga_id>', methods=['DELETE'])
def deletar_manga_por_id(manga_id):
    for indice, manga in enumerate(mangas):
        if manga.get('id') == manga_id:
            del mangas[indice]
            return jsonify({'message': 'Manga deletado com sucesso!'})
    return jsonify({'erro': 'Manga não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)