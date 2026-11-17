# MeuDjango

Aplicação web desenvolvida com Django durante meus estudos de desenvolvimento backend. O projeto permite cadastrar usuários e organizar tópicos de estudo com anotações pessoais.

## Funcionalidades

- Cadastro, login e logout de usuários
- Criação e edição de tópicos
- Criação e edição de anotações para cada tópico
- Conteúdo privado por usuário
- Área administrativa do Django
- Interface responsiva com tema escuro

## Tecnologias

- Python
- Django 6.1.3
- SQLite
- HTML e CSS

## Como executar

Na raiz do repositório:

```bash
python3 -m venv venv
source venv/bin/activate
pip install Django==6.1.3

cd Treinamento/Curso_Django
python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/`.

Para testar o painel administrativo, crie um usuário administrador:

```bash
python manage.py createsuperuser
```

Depois, acesse `http://127.0.0.1:8000/admin/`.
