# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY kriolstock_dapi/requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie todo o restante do projeto para o diretório de trabalho
COPY . .

# Exponha a porta 8000
EXPOSE 8000

# Comando padrão para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
