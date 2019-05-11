# `/v1/repositorios`

### `GET /v1/repositorios` - Recuperar repositórios abertos de alunos de computação na UFCG

#### Parametros:

Parametros indicados com `*` são obrigatórios

- `quantity`: Quantidade máxima de repositórios na lista retornada, na ausencia do parametro, será retornado 10 por padrão

- `after`: Cursor indicando a partir de qual repositório deverá iniciar a lista retornada.

#### Exemplo de retorno:

Para uma requisição `GET /v1/repositorios?quantity=2` a API retornaria os dois primeiros repositórios da lista, algo como:

```json
{
  "repos": [
    {
      "nameWithOwner": "OpenDevUFCG/Tamburetei",
      "description": "Fazendo de tamburete as cadeiras de CC@UFCG.",
      "url": "https://github.com/OpenDevUFCG/Tamburetei",
      "forkCount": 18,
      "commitsCount": 166,
      "issuesCount": 14,
      "pullRequestsCount": 0,
      "stargazersCount": 56
    },
    {
      "nameWithOwner": "OpenDevUFCG/IssueAi",
      "description": "O Issue Ai cria um espaço de visibilidade para os projetos open source de Computação@UFCG.",
      "url": "https://github.com/OpenDevUFCG/IssueAi",
      "forkCount": 4,
      "commitsCount": 78,
      "issuesCount": 12,
      "pullRequestsCount": 1,
      "stargazersCount": 22
    }
  ],
  "endCursor": "Y3Vyc29yOjI="
}
```

O atributo `endCursor` é o cursor indicando o "ponto de parada da listagem", ele serve para caso queira carregar os próximos repositórios da lista, poderá adicionar o parâmetro `after` com o valor do `endCursor` à requisição (ex: `GET /v1/repositorios?quantity=2&after=Y3Vyc29yOjI=`)

#### Como contribuir adicionando mais repositórios

Caso você queira adicionar mais projetos Open Source de alunos da UFCG na listagem dos dados, poderá enviar um PR adicionando mais ocorrencias no array `projects` em [`/src/v1/repositorios/repositorios-data.js`](https://github.com/OpenDevUFCG/laguinho-api/blob/master/src/v1/repositorios/repositorios-data.js) seguindo o padrão dos dados já inseridos.
