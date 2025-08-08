# 🛒 Controle de Estoque de Produtos Django

Este projeto é um sistema completo de cadastro e controle de estoque de produtos, desenvolvido com Django e pronto para deploy no PythonAnywhere. Com uma interface moderna e responsiva, você pode cadastrar produtos com nome, foto e quantidade em estoque, além de editar, excluir e ajustar o estoque de forma prática e intuitiva.

## Funcionalidades

- Cadastro de produtos com nome, foto e quantidade em estoque
- Edição e exclusão de produtos
- Ações rápidas para adicionar ou remover unidades do estoque
- Interface web bonita, responsiva e fácil de usar (Bootstrap)
- Upload e exibição de fotos dos produtos
- Painel administrativo completo do Django
- Pronto para deploy gratuito no PythonAnywhere

## Tecnologias

- Django 5.x
- Bootstrap 5
- Python 3.12+
- SQLite (padrão, mas pode ser adaptado para outros bancos)
- Deploy simples no PythonAnywhere

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Rode as migrações e crie um superusuário:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse `http://127.0.0.1:8000/` no navegador.

## Deploy no PythonAnywhere

1. Suba seu projeto para o GitHub ou faça upload dos arquivos no PythonAnywhere.
2. Crie e ative um ambiente virtual no PythonAnywhere.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Ajuste o `ALLOWED_HOSTS` e configure os caminhos de `STATIC_ROOT` e `MEDIA_ROOT` no `settings.py`.
5. Rode as migrações, crie o superusuário e colete os arquivos estáticos:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic
   ```
6. Configure o Web App no painel do PythonAnywhere, apontando para o seu `wsgi.py`.
7. Configure os caminhos de static e media no painel Web.
8. Reinicie o servidor pelo painel.

Pronto! Seu sistema de estoque estará online 🚀

---

Sinta-se à vontade para contribuir, sugerir melhorias ou customizar para o seu negócio!
