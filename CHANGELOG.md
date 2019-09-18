# Changelog
Todas as mudanças desse projeto serão documentadas nesse arquivo.

O formato foi baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e esse projeto adere a [Semantic Versioning](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [Não publicado]


## [0.0.1] - 10/09/2019

### Adicionado

- API agora feita com `Python3`, utilizando `flask` e `pipenv`.
- Endpoint `/datasets` para requisições GET, que vai retornar os datasets cadastrados.
- Endpoint `/datasets` para requisições POST, para publicar um novo dataset.
- Endpoint `/datasets/<nome>` para requisições GET, que vai retornar metadados a respeito de um dataset a partir do seu nome.
- Esse arquivo de changelog para servir de exemplo para lançamentos futuros.

### Modificado

- Foi dado início à [reformulação do laguinho](https://github.com/OpenDevUFCG/laguinho-api/issues/31).

### Removido

- API feita em `node`.
