# Kriolstock django api

Este api sera feito com django e seu proposito é servir de api para pagina de kriolstock photo .

## Banco de dados
postgres SQL

### credenciais
As credencias de conexao com o banco de dados postgres deve seguir:

```hostname:porta:db_name:user:senha```

Schema:
```
User (Usuário): user é melhor extender da classe auth do proprio django, assim vai herdar muita coisa da autenticaçao
    user_id (Chave Primária)
    username
    email
    password (hash)
    full_name
    bio
    profile_picture
    
Documentos (Digital Assets):
    documentos_id (Chave Primária)
    title
    description
    image_url (URL da imagem)
    price
    upload_date
    visibility (público, privado, restrito)
    status (ativo, inativo)
    user_id (Chave Estrangeira referenciando a tabela de Usuários)
    
Transaction (Transação):
    transaction_id (Chave Primária)
    transaction_date
    amount
    buyer_id (Chave Estrangeira referenciando a tabela de Usuários)
    seller_id (Chave Estrangeira referenciando a tabela de Usuários)
    documentos_id (Chave Estrangeira referenciando a tabela de Artes)
    transaction_status (pago, pendente, concluído, reembolsado)
    Outros detalhes da transação

Comment (Comentário):
    comment_id (Chave Primária)
    comment
    comment_date
    user_id (Chave Estrangeira referenciando a tabela de Usuários)
    documentos_id (Chave Estrangeira referenciando a tabela de Artes)
    rating (estrelas ou outra métrica)
    status (ativo, inativo)

Category (Categoria):
    category_id (Chave Primária)
    category_name
    description
    icon (para representação visual)

Tag (Tag):
    tag_id (Chave Primária)
    tag_name
    description

DocumentoCategory (Relacionamento entre Arte e Categoria):
    documentos_id (Chave Estrangeira referenciando a tabela de Artes)
    category_id (Chave Estrangeira referenciando a tabela de Categorias)

DocumentoTag (Relacionamento entre Arte e Tag):
    documentos_id (Chave Estrangeira referenciando a tabela de Artes)
    tag_id (Chave Estrangeira referenciando a tabela de Tags)

License (Licença):
    license_id (Chave Primária)
    license_type (comercial, não comercial, etc.)
    description
    restrictions (por exemplo, limitações geográficas)

Notification (Notificação):
    notification_id (Chave Primária)
    notification_type (transação concluída, novo comentário, etc.)
    message
    notification_date
    user_id (Chave Estrangeira referenciando a tabela de Usuários)
    status (lida, não lida)

Analytics (Análises):
    analytics_id (Chave Primária)
    date
    visit_count
    purchase_count
    revenue
    documentos_id (Chave Estrangeira referenciando a tabela de Artes)

SystemConfiguration (Configurações do Sistema):
    config_id (Chave Primária)
    config_name
    config_value

SecurityLog (Registro de Segurança):
    log_id (Chave Primária)
    date_time
    event (login, logout, alteração de senha, etc.)
    user_id (Chave Estrangeira referenciando a tabela de Usuários)
    ip_address
```


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
