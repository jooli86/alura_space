# 🛰️ Alura Space - Diário de Bordo Django


🚀 Sobre este projeto:

Este repositório é o meu diário de bordo no aprendizado de Django. Optei por registrar minhas anotações de forma clara e direta, mostrando os conceitos que aprendi e apliquei na prática. Meu objetivo aqui é documentar minha evolução real, passo a passo.

Por ser um registro da minha evolução real passo a passo, você encontrará anotações simples e uma linguagem sem termos muito técnicos. Meu objetivo aqui é documentar meu aprendizado de forma autêntica, mostrando o que eu já sei fazer e como estou construindo minha base como desenvolvedora.

# Anotações de estudo.

🛠️ Padronização de Desenvolvimento
Para este projeto, apliquei conceitos de Conventional Commits para manter um histórico de alterações claro e profissional:

* feat: Novas funcionalidades;

* fix: Correções de bugs;

* style: Ajustes de formatação e estilo de código;

* docs: Alterações em documentações.

Nota sobre o histórico de commits:
Os primeiros commits deste projeto não seguem a convenção mencionada acima. Este padrão foi adotado a partir do estágio intermediário do projeto, fruto de uma pesquisa adicional sobre boas práticas de mercado e colaboração em equipe, indo além do conteúdo básico do curso. Acredito que a evolução técnica e a adoção de padrões profissionais devem ser aplicadas assim que o conhecimento é adquirido.

## Segurança:

* Importância das variáveis de ambiente, e segurança ao subir arquivos para o GitHub.
* Escondendo Dados Sensíveis: Aprendi que não devemos deixar "chaves" ou senhas à mostra no código que vai para o GitHub. Por isso, usei um arquivo chamado .env (Variáveis de Ambiente) para proteger informações secretas do projeto.
* Jamais esquecer o arquivo .gitignore.

## Mapeamento de Portas:

| Porta | Serviço | Importância |
| :--- | :--- | :--- |
| 8000 | Django Dev Server | Onde o projeto "mora" durante o desenvolvimento local. |
| 5432 | PostgreSQL | Porta do banco de dados relacional padrão do mercado. |
| 3306 | MySQL | Outra opção de banco de dados muito comum em empresas. |
| 6379 | Redis | Usada para cache, deixando o site extremamente veloz. |


## App e projeto:

* Um projeto pode ter vários apps e um app pode ser usado em vários projetos.

## Views e URLs:

* Organização em camadas: técnica que isola as URLs.
* Delegar tarefas com include.

## Templates:

* Criação da página HTML e conexão com settings.py
* Emmet: Aprendi alguns atalhos para criação de páginas HTML. Ex: h1{Título} + Tab gera <h1>Título</h1>

## Arquivos estáticos:

* **Modernização de caminhos:** Substituir o uso do os.path.join, usando a / como BASE_DIR, que utiliza a biblioteca pathlib, isso deixa o código mais limpo e moderno. **Observação:** Embora o pathlib (o uso da /) seja moderno, algumas funções internas mais antigas do Django (como o collectstatic) ainda esperam receber um texto puro para conversar com o sistema de arquivos do Windows. O str() garante que essa conversa aconteça sem mal-entendidos.
* Embedado: Uso do Python dentro do HTML. EX: {% ... %}
* Alterar o settings.py.
* Baixar os arquivos.
* Comando para reunir todos os assets na pasta raiz de produção. Ex: python manage.py collectstatic
* Carregamento da Tag Library: Indicar ao HTML que temos arquivos estáticos. {% load static %}
* Vinculação Dinâmica de Static Assets: Garantir que o servidor encontre o arquivo css independente da URL.
  Ex: <link rel="stylesheet" href="{% static 'styles/style.css' %}">
* Injeção de Tags de Template em Atributos src:Envolvemos o caminho de cada tag <img> com o motor do Django para que o navegador consiga localizar as pastas de assets processadas pelo servidor. Ex: <img src="{% static 'caminho/da/imagem.png' %}">

## URL name:
Para que os links do site funcionem sempre, mesmo que eu mude o endereço da página no futuro, aprendi a usar o sistema de Nomes de Rota do Django:

* No urls.py (O Apelido):
Adiciono o argumento name= dentro de cada path. Isso cria um "apelido" para a rota que o Django consegue identificar em qualquer lugar do projeto. Ex: path('imagem/', views.imagem, name='imagem')

* Nos arquivos HTML:
  Em vez de escrever o caminho fixo (como imagem.html), uso o código embedado do Django para chamar o "apelido" que criei.

## Refatoração de Templates (Princípio DRY):

**O que é Refatoração?** É o processo de melhorar a estrutura interna do código sem alterar suas funcionalidades externas. Apliquei isso usando o princípio DRY (Don't Repeat Yourself) para eliminar repetições desnecessárias.

* O Arquivo base.html:
Criamos um arquivo central que contém toda a estrutura fixa do site (HTML, Head, Body). 
Tag de encaixe: {% block content %} ... {% endblock %}

* Nos arquivos index.html e imagem.html, removemos o código repetido e avisamos ao Django que eles devem "herdar" a moldura
  do arquivo base.
  Tag de herança: {% extends 'galeria/base.html' %} (Deve ser a primeira linha do arquivo).

* Sintaxe de Template: {% %} (lógica) e {{ }} (exibição).

O código fica muito mais curto, organizado e, se eu precisar mudar o título do site ou o CSS, mudo em apenas um arquivo (base.html).

## Organização com Partials(Componentização):

O que são Partials? São "pedaços" de código HTML que isolamos em arquivos separados para não precisarmos repetir o mesmo código em várias páginas. Se eu mudar o Menu em um lugar, ele muda no site inteiro!

* A Pasta partials:
  Criar uma pasta específica para guardar esses pedaços (ex: _header.html, _menu.html, _footer.html).
  **Impotante:** Usar o underline _ no início do nome para identificar que o arquivo é apenas um "pedaço" e não uma página completa.

* A Tag include:
  No arquivo principal (base.html), eu chamo essas peças usando o comando do Django:
  Ex: {% include 'galeria/partials/_menu.html' %}

* O Cuidado com as Tags de Estrutura:
  Aprendi que o quem abre, fecha.
  As tags que "abraçam" o site todo (como main e div) ficam no base.html.
  As partials e os blocos de conteúdo (index, imagem) não devem fechar essas tags, para não "quebrar" o desenho do site.

  # Django: Persistência de dados Admin

## Estruturando a Galeria com Banco de Dados:

Nesta etapa, deixamos de usar dados "manuais"(escrito direto no código) e passamos a utilizar o poder do Banco de Dados para
gerenciar as informações do Alura Space.

* Criar o modelo(Models): EX: Definimos que cada Fotografia no nosso site precisa ter obrigatoriamente: um nome, uma legenda, uma descrição e o caminho do arquivo da foto.

* Migrations (Migrações): Entendemos o processo de atualizar o banco de dados. Primeiro, criamos um "plano de mudança" (makemigrations) e depois aplicamos essas mudanças de fato (migrate). EX: python manage.py makemigrations: Prepara as alterações que fizemos no modelo. python manage.py migrate: Aplica as alterações e cria as tabelas no banco de dados.

* Identificação de Dados: Implementamos um método especial (__str__) para que, ao olharmos a lista de fotos no sistema, possamos ver o nome real de cada uma, facilitando a organização.


## Persistência e Manipulação de Dados:

Nesta etapa, avançamos para a comunicação direta com o Banco de Dados, aprendendo como inserir e gerenciar informações sem depender de arquivos estáticos ou dicionários manuais.

* Configuração de App: Ajustamos o registro da nossa aplicação no arquivo settings.py utilizando o caminho completo: 'galeria.apps.GaleriaConfig'. Isso garante que o Django carregue todas as configurações e funcionalidades específicas do nosso app de forma robusta.

* O Shell do Django: Aprendemos a utilizar o terminal interativo do Django. Ele funciona como uma "ponte" onde podemos falar diretamente com o Banco de Dados usando código Python.

   * Comando para entrar: python manage.py shell

   * Comando para sair: exit() ou Ctrl + Z e Enter.

* Manipulação de Objetos (CRUD inicial):

  * Importação: Primeiro avisamos ao Python qual "modelo" queremos usar. Ex: from galeria.models import Fotografia

  * Instância e Preenchimento: Criamos o objeto na memória e preenchemos seus campos (nome, legenda, foto).

  * O Método .save(): Entendi que os dados só "nascem" de verdade no banco de dados quando usamos o comando .save(). Sem ele, a informação se perde ao fechar o terminal.

  * Consultas ao Banco (Queries): Utilizamos o comando Fotografia.objects.all() para listar tudo o que já salvamos. É aqui que o Django mostra seu poder de "tradutor" (ORM), buscando os dados na tabela e nos devolvendo como objetos Python prontos para uso.