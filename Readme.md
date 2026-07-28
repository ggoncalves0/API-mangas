# API de Mangás 📚

Uma API REST simples feita com Flask para gerenciar uma lista de mangás (criar, listar, editar e deletar).

## Tecnologias

- Python 3
- Flask

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd NOME_DO_REPO
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python app.py
```

A API vai rodar em `http://localhost:5000`.

## Endpoints

### Listar todos os mangás
```
GET /mangas
```
**Resposta (200):**
```json
[
  { "id": 1, "titulo": "Tokyo Ghoul", "autor": "Sui Ishida" },
  { "id": 2, "titulo": "Berserk", "autor": "Kentaro Miura" }
]
```

### Buscar um mangá por ID
```
GET /mangas/<id>
```
**Resposta (200):**
```json
{ "id": 1, "titulo": "Tokyo Ghoul", "autor": "Sui Ishida" }
```
**Resposta (404):**
```json
{ "erro": "Manga não encontrado" }
```

### Criar um novo mangá
```
POST /mangas
```
**Corpo da requisição:**
```json
{ "titulo": "One Piece", "autor": "Eiichiro Oda" }
```
> O `id` é gerado automaticamente pela API.

**Resposta (201):**
```json
{ "id": 4, "titulo": "One Piece", "autor": "Eiichiro Oda" }
```

### Editar um mangá existente
```
PUT /mangas/<id>
```
**Corpo da requisição (envie apenas os campos que quer alterar):**
```json
{ "titulo": "One Piece (Edição Especial)" }
```
**Resposta (200):**
```json
{ "id": 4, "titulo": "One Piece (Edição Especial)", "autor": "Eiichiro Oda" }
```

### Deletar um mangá
```
DELETE /mangas/<id>
```
**Resposta (200):**
```json
{ "message": "Manga deletado com sucesso!" }
```
**Resposta (404):**
```json
{ "erro": "Manga não encontrado" }
```

## Observações

- Os dados são armazenados em memória (uma lista Python), ou seja, **são perdidos a cada reinicialização** do servidor. Para persistência, o próximo passo seria integrar um banco de dados como SQLite via SQLAlchemy.
- Projeto criado para fins de estudo/portfólio.

👨‍💻 Autor
Gabriel Gonçalves de Oliveira
📧 ggoncalvesy03@gmail.com
