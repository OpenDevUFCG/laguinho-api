# Laguinho API [![chat on Discord](https://img.shields.io/discord/558293573494112257.svg?logo=discord)](https://discord.gg/UgR5WrY)

![LaguinhoAPI Logo](https://i.imgur.com/lgiZyDn.png)

Assim como o Laguinho da UFCG é (era) o ponto mais central da universidade, esta API centralizará dados para pesquisas e aplicações.

# O que é o Laguinho

Desenvolvedores e pesquisadores podem utilizar o laguinho para compartilhar e consumir diferentes tipos de dados, para auxiliar o desenvolvimento de aplicações ou de pesquisas.

O laguinho é composto por 3 componentes:

- [A interface Web](https://github.com/OpenDevUFCG/laguinho)
- [A interface de linha de comando (CLI)](https://github.com/OpenDevUFCG/laguinho-cli)
- [A API de registro dos dados](https://github.com/OpenDevUFCG/laguinho-api)

Use a interface Web para encontrar novos conjuntos de dados (datasets) e os compartilhar com a comunidade, além disso, crie seu perfil e favorite os melhores.

A CLI é executada no terminal e é uma das formas de interagir com o Laguinho para quem tem familiariade, principalmente desenvolvedores.

A API é responsável por receber todas as requisições dos outros componentes e permitir o registro e obtenção dos conjuntos de dados.

## Galera top que ajuda a gente :heart:

[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/0)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/0)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/1)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/1)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/2)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/2)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/3)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/3)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/4)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/4)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/5)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/5)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/6)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/6)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/7)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/7)

Os dados são abertos e todos podem contribuir com mais dados e endpoints. Veja mais detalhes no [CONTRIBUTING.md](CONTRIBUTING.md) e se joga no laguinho com a gente!

# Preparando o ambiente

Este projeto é feito utilizando [Python 3](https://www.python.org/), você precisa tê-lo [instalado](https://www.python.org/downloads/) na sua máquina.

Para rodarmos as dependências de banco de dados e servidores externos, utilizamos Docker e Docker Compose, caso ainda não tenha instalado na sua máquina, [esse tutorial](https://docs.docker.com/install/) ajuda a instalar o docker e [esse tutorial](https://docs.docker.com/compose/install/) ajuda a instalar o docker-compose, mas lembre-se que qualquer dúvida no processo de instalação, sempre tem alguém no [discord](https://discord.gg/vMcuNtt) pra ajudar!

### Configurando a máquina

Antes de tudo, você precisa rodar as dependências com o `docker-compose` pra isso, rode o comando abaixo:

```bash
# Roda banco de dados e outras dependências
$ docker-compose up
```

Isso iniciará as dependencias e vai ficar mostrando uns logs no terminal...

Após iniciado, você deve, **em outro terminal**, rodar os comandos abaixo

```bash
# instalando o pipenv
$ pip install --user pipenv
```

### Configurando o projeto

```bash
# clonando o repositório
$ git clone https://github.com/OpenDevUFCG/laguinho-api.git
$ cd laguinho-api

# instalando as dependências
$ pipenv install --dev

# executando o script de inicialização da versão de desenvolvimento
$ pipenv run start
```

Deverá aparecer a mensagem `Running on port 8080` e o servidor estará disponível em http://localhost:8080.

Caso queira executar em uma porta diferente, terá que rodar o script de inicialização indicando a porta desejada, como por exemplo, para mudar pra porta `5000`:

```bash
pipenv run start --port 5000
```

## Como Contribuir

Quer implementar alguma nova funcionalidade ou corrigir algum bug? Pode ir dando uma olhada nas issues abertas pra saber no que estamos trabalhando ou se preferir pode abrir sua própria caso queira corrigir ou adicionar algo novo!

Qualquer dúvida é só procurar a gente via [discord](https://discord.gg/vMcuNtt) ou pelas issues mesmo!

OBS: Esse ainda é um projeto em desenvolvimento, para acompanhar melhor, tudo começou com [esta issue](https://github.com/OpenDevUFCG/laguinho-api/issues/31), a partir dela você consegue chegar em toda a discussão sobre a API
