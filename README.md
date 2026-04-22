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
* Emmet: Aprendi alguns atalhos para criação de páginas HTML. Ex: `h1{Título} + Tab gera '<h1>Título</h1>`

## Arquivos estáticos:

* **Modernização de caminhos:** Substituir o uso do os.path.join, usando a / como BASE_DIR, que utiliza a biblioteca pathlib, isso deixa o código mais limpo e moderno. **Observação:** Embora o pathlib (o uso da /) seja moderno, algumas funções internas mais antigas do Django (como o collectstatic) ainda esperam receber um texto puro para conversar com o sistema de arquivos do Windows. O str() garante que essa conversa aconteça sem mal-entendidos.
* Embedado: Uso do Python dentro do HTML. EX: {% ... %}
* Alterar o settings.py.
* Baixar os arquivos.
* Comando para reunir todos os assets na pasta raiz de produção. Ex: python manage.py collectstatic
* Carregamento da Tag Library: Indicar ao HTML que temos arquivos estáticos. {% load static %}
* Vinculação Dinâmica de Static Assets: Garantir que o servidor encontre o arquivo css independente da URL.
  Ex: `<link rel="stylesheet" href="{% static 'styles/style.css' %}">`
* Injeção de Tags de Template em Atributos src:Envolvemos o caminho de cada tag `<img>` com o motor do Django para que o navegador consiga localizar as pastas de assets processadas pelo servidor. Ex: `<img src="{% static 'caminho/da/imagem.png' %}">`

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

* Estrutura de Arquivos e Novas Entradas:
Além da manipulação via Shell, nesta etapa ficou clara a importância da organização dos arquivos físicos:

 * Desenvolvimento vs. Produção: Entendi que novas imagens devem ser adicionadas sempre em setup/static/assets/imagens/galeria/. A pasta static na raiz é gerada automaticamente pelo Django (collectstatic) e não deve ser mexida manualmente.

 * Sincronia: Para um novo item aparecer na galeria, o nome do arquivo na pasta deve ser idêntico ao nome salvo no campo foto do banco de dados.

## Navegação Dinâmica e Detalhes da Imagem:
Nesta etapa, transformamos o site em um sistema inteligente. Agora, o Django entende qual imagem foi clicada e exibe os detalhes específicos dela em uma página dedicada, sem precisarmos criar vários arquivos HTML.

* Rotas Parametrizadas (URLs Dinâmicas): Aprendi a criar caminhos que aceitam variáveis. No urls.py, usamos o padrão <int:foto_id>, que funciona como um "espaço reservado" para o ID de cada fotografia.

  Ex: path('imagem/<int:foto_id>', ...)

* Captura de ID na View: A função imagem na views.py agora recebe esse ID e o utiliza para "pescar" no banco de dados exatamente a foto que o usuário quer ver.

* Segurança com get_object_or_404: Em vez de uma busca simples, usamos este método que garante que, se alguém tentar acessar um ID que não existe, o site exiba uma página de erro amigável (404) em vez de travar o sistema.

* Primary Key (PK): Entendi que o pk é o identificador único (a Chave Primária) de cada registro no banco de dados. É através dele que o Django faz a conexão exata entre o clique no card e a exibição da foto.

* Template Universal (imagem.html): O arquivo de imagem deixou de ter textos fixos. Agora ele funciona como um "molde" que preenche automaticamente o título, a legenda e o arquivo de imagem com base nos dados que a View envia.

  Ex: src="{% static ... %}{{ fotografia.foto }}"

* Correção de Dados via Shell: Pratiquei a edição de registros já salvos. Aprendi que, se eu errar uma extensão (como .png em vez de .jpg), posso buscar o objeto pelo Shell, alterar o atributo e usar o .save() para corrigir a informação no banco de dados.

Nota: A lógica de ID permite que meu site tenha 10 ou 10.000 fotos usando apenas duas páginas HTML (index e imagem).

## Administração e Controle de Dados (Django Admin)
Nesta etapa, deixamos o Shell de lado e passamos a gerenciar o conteúdo do projeto através de uma interface visual robusta, personalizada para facilitar o dia a dia.

* Superusuário: Criação de credenciais de administrador (createsuperuser) para acesso total ao painel de controle do Django.

* Registro e Personalização de Models: * Aprendi a registrar o model Fotografia no admin.py.

* Personalizei a exibição da lista com list_display, tornando a visualização de IDs, nomes e legendas muito mais intuitiva.

* Implementei links de navegação interna com list_display_links e campos de busca com search_fields.

* Filtros e Paginação: * Adicionei filtros laterais (list_filter) para organizar as imagens por categoria.

* Configurei a paginação (list_per_page) para garantir a performance do painel com grandes volumes de dados.

* Lógica de Publicação: * Implementei um campo booleano (BooleanField) para controlar quais imagens devem aparecer no site.

* Utilizei list_editable para permitir que o administrador publique ou oculte fotos diretamente da lista principal, sem precisar abrir item por item.

* Gestão de Tempo e Ordenação:

  * Adicionei um campo de data e hora (DateTimeField) com valor automático (default=datetime.now).

  * Ajustei a view principal para exibir as fotografias por ordem de postagem (order_by("-data_fotografia")), garantindo que as novidades apareçam primeiro para o usuário.

## Gerenciamento de Mídia e Upload de Arquivos

Nesta etapa, implementei a capacidade do sistema de receber e organizar arquivos de imagem de forma dinâmica, saindo do modelo de arquivos estáticos manuais para um sistema de upload real.

* Upload Dinâmico com ImageField: Substituí o campo de texto (CharField) por um campo de imagem (ImageField) no model Fotografia, permitindo o upload direto pelo Django Admin.

* Organização Inteligente de Pastas: Configurei o parâmetro upload_to para organizar as fotos automaticamente por data (fotos/%Y/%m/%d/), evitando conflitos de nomes e facilitando a manutenção do servidor.

* Configuração de Media Files:

* Defini MEDIA_URL e MEDIA_ROOT no settings.py para gerenciar o armazenamento físico e o acesso via URL das imagens.

* Configurei as rotas no urls.py do projeto para servir os arquivos de mídia durante o desenvolvimento.

* Tratamento de Exceções (Fallback): * Implementei uma lógica condicional no index.html para verificar a existência de imagens.

  * Caso uma fotografia não possua arquivo, o sistema exibe automaticamente uma imagem padrão (not-found.png) via arquivos estáticos.

  * Integração com Pillow: Instalação e configuração da biblioteca Pillow para processamento de imagens no backend Python.

## Funcionalidade de Busca Dinâmica

Aprendi que uma barra de busca não é apenas um desenho no topo do site; ela precisa de um "cérebro" para filtrar o que o usuário quer ver.

* Transformando HTML em Formulário: Entendi que para a busca funcionar, o campo de texto precisa estar dentro de uma tag <form>. Dei o nome (name="buscar") para o campo e transformuei a lupa em um botão de envio (type="submit").

* Capturando dados com request.GET: Aprendi que quando o usuário digita algo e clica na lupa, o Django "pesca" essa palavra na URL do navegador através do objeto request.GET.

* Filtros Inteligentes (icontains): Usei o poder do ORM do Django para filtrar o banco de dados. O comando nome__icontains é incrível porque ele busca por partes da palavra e ignora se o usuário digitou em maiúsculo ou minúsculo.

* Página de "Não Encontrado": Criei uma lógica para que, se o usuário buscar por algo que não existe (ex: "Alien"), o site exiba uma mensagem amigável de "Fotografias não encontradas" em vez de apenas ficar em branco.

## Gestão de Equipe (Usuários e Permissões)

Nesta etapa final, explorei como o Django lida com a segurança e quem pode mexer no quê dentro do painel administrativo.

* Diferença de Poderes: Entendi que um "Superusuário" pode tudo, mas um "Membro da Equipe" (Staff) só pode entrar no Admin se eu permitir.

* Permissões Granulares: Aprendi que posso criar usuários com "poderes limitados". Por exemplo: criei a usuária "Ana", que tem permissão apenas para adicionar e editar fotos, mas não pode deletar nada nem mexer nos outros usuários.

* Organização por Grupos: Em vez de dar permissão um por um, aprendi a criar Grupos. Criei o grupo "FotografiaAdmin". Agora, qualquer pessoa que eu colocar nesse grupo já "ganha" automaticamente todos os poderes de edição da galeria. Isso facilita muito a gestão quando o time cresce!









🛠️ Minha Caixa de Ferramentas
Para construir este projeto, utilizei as seguintes tecnologias:

Django 4.x: O coração do projeto.

SQLite: Onde guardo todas as informações das minhas fotografias.

Pillow: A biblioteca que me ajudou a processar os uploads de imagem.

HTML/CSS: Para dar vida e cor aos templates e partials.

🔧 Quer rodar este Diário de Bordo na sua máquina?
Se você quiser testar o projeto, aqui está o passo a passo que aprendi para configurar o ambiente:

Crie um ambiente virtual: python -m venv venv

Ative o ambiente:

Windows: .\venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Instale as dependências: pip install -r requirements.txt

Prepare o Banco de Dados: python manage.py migrate

Decole o servidor: python manage.py runserver

Este projeto é um registro da minha jornada na formação Django da Alura.