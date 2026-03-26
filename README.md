# Anotações de estudo.

## Segurança

* Aprendi sobre a importância das variáveis de ambiente, e sobre segurança ao subir arquivos para o GitHub.

## Mapeamento de Portas:

| Porta | Serviço | Importância |
| :--- | :--- | :--- |
| 8000 | Django Dev Server | Onde o projeto "mora" durante o desenvolvimento local. |
| 5432 | PostgreSQL | Porta do banco de dados relacional padrão do mercado. |
| 3306 | MySQL | Outra opção de banco de dados muito comum em empresas. |
| 6379 | Redis | Usada para cache, deixando o site extremamente veloz. |


## App e projeto

* Um projeto pode ter vários apps e um app pode ser usado em vários projetos.

## Views e URLs

* Organização em camadas: técnica que isola as URLs.
* Delegar tarefas com include.

## Templates

* Criação da página HTML e conexão com settings.py
* Emmet: Aprendi alguns atalhos para criação de páginas HTML. Ex: h1{Título} + Tab gera <h1>Título</h1>

## Arquivos estáticos

* Substituir o uso do os.path.join, usando a / como BASE_DIR(que utiliza a biblioteca pathlib), isso deixa o código mais limpo e moderno. Observação: Embora o pathlib (o uso da /) seja moderno, algumas funções internas mais antigas do Django (como o collectstatic) ainda esperam receber um texto puro para conversar com o sistema de arquivos do Windows. O str() garante que essa conversa aconteça sem mal-entendidos.
* Embedado: Uso do Python dentro do HTML. EX: {% ... %}
* Alterar o settings.py.
* Baixar os arquivos.
* Comando para reunir todos os assets na pasta raiz de produção. Ex: python manage.py collectstatic
* Carregamento da Tag Library: Indicar ao HTML que temos arquivos estáticos. {% load static %}
* Vinculação Dinâmica de Static Assets: Garantir que o servidor encontre o arquivo css independente da URL.
  Ex: <link rel="stylesheet" href="{% static 'styles/style.css' %}">
* Injeção de Tags de Template em Atributos src:Envolvemos o caminho de cada tag <img> com o motor do Django para que o navegador consiga localizar as pastas de assets processadas pelo servidor. Ex: <img src="{% static 'caminho/da/imagem.png' %}">