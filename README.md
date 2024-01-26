# Kriolstock django api


## Iniciar o servidor
Criar um Projeto Django:

```django-admin startproject nome_do_projeto```
Inicia um novo projeto Django com a estrutura de diretórios padrão.

Criar uma Aplicação Django:

```python manage.py startapp nome_da_aplicacao```
Cria uma nova aplicação dentro do projeto. As aplicações são módulos que organizam o código em Django.

Criar Migrações:

```python manage.py makemigrations```
Gera arquivos de migração com base nas alterações feitas nos modelos do Django. As migrações são usadas para aplicar alterações no banco de dados.

Aplicar Migrações:

```python manage.py migrate```
Aplica as migrações pendentes e atualiza o banco de dados com base nas alterações nos modelos.
Criar um Superusuário:

```python manage.py createsuperuser```
Cria um superusuário que pode acessar o painel de administração do Django.

Iniciar Servidor de Desenvolvimento:

```python manage.py runserver```
Inicia o servidor de desenvolvimento embutido do Django para testar a aplicação localmente.

Criar um Aplicativo Administrativo:

```python manage.py startapp nome_da_aplicacao```
Cria uma aplicação administrativa padrão, incluindo modelos, visualizações e URLs, que pode ser personalizada para atender às necessidades do projeto.

Criar Módulos de Teste:

```python manage.py test nome_da_aplicacao```
Executa os testes definidos em módulos de teste para garantir que as partes da aplicação funcionem conforme o esperado.

- Criar uma Migrção Zero:

```python manage.py makemigrations --empty nome_da_aplicacao```
Cria um arquivo de migração vazio, útil quando você precisa personalizar as migrações.

-Criar Arquivos Estáticos:

```python manage.py collectstatic```
Coleta arquivos estáticos de todas as aplicações em um único diretório para servir durante a produção.


## Intalar as dependencias
pip install -r requirements.txt
