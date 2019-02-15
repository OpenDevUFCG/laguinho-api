# Como contribuir?

Aqui vai um tutorialzinho sobre como contribuir com o Laguinho API, qualquer dúvida que tiver pode criar issue ou chamar no [gitter](https://gitter.im/OpenDevUFCG/laguinho-api) ;)

## Estrutura do projeto

A estrutura de arquivos do projeto se assemelha ao exemplo abaixo:

```
/src
  /v1
    /endpoint1
      endpoint1-controller.js
      endpoint1-data.js
      [ talvez mais alguns arquivos ]
    /endpoint2
      endpoint2-controller.js
      endpoint2-data.js
      [ talvez mais alguns arquivos ]
```

Na pasta `/src` temos todo o código do projeto, dentro dele encontraremos subpastas que seguem a estrutura da URI, por exemplo, o endpoint `GET /v1/repositories` está definido na pasta `/src/v1/repositories`

## Contribuindo com novos endpoints

Para criar um novo endpoint, seguimos a receitinha abaixo:

1. Procuramos a pasta da última versão da API, (Ex: se existir dentro do `/src` as pastas `/v1` e `/v2` escolhemos a `/v2`)
1. Criamos nela uma nova pasta com o nome do endpoint a ser criado, por exemplo `/xerox-geolocalization` e dentro dela um controller com o padrão `[nome-endpoint]-controller.js` que vai ser o módulo que implementa e exporta a(s) nova(s) rota(s)
1. Caso seja necessário um dataset para popular nosso(s) endpoint(s), criamos um `[nome-endpoint]-data.js` que vai ser responsável por conter os dados ou dados necessários para popular o(s) novo(s) endpoint(s)
1. Importamos o router no módulo da versão da API (`/src/vX/index.js`, sendo X o número da versão)
1. Adicionamos a documentação do(s) endpoint(s) no [docs](https://github.com/OpenDevUFCG/laguinho-api/blob/master/docs/README.md) baseados nos já existentes

Dica 1: Olhe a implementação e organização de endpoints existentes para entender melhor os padrões usados.

Dica 2: Sinta-se livre para criar outros arquivos ou sub-diretórios caso julgue necessário (Seja pra modularizar melhor ou o que for).

Dica 3: O endpoint pode ter sub-rotas (Ex: `/v1/repositories/contributors`) definidas no mesmo controller caso julgue desnecessário criar uma sub-pasta para isso.

## Contribuindo com endpoints existentes

Como já foi dito anteriormente, a estrutura de arquivos do projeto é baseada na URI esperada do endpoint, nesse caso, se desejar contribuir para o endpoint `GET /v1/repositories` poderá facilmente encontrar o código do endpoint na pasta `/src/v1/repositories`, o endpoint estará definido num arquivo que segue o padrão `[nome-endpoint]-controller.js`.

## Sugerindo e/ou adicionando dados

Caso você tenha um dataset interessante sobre a UFCG e queira compartilhar com a gente, sinta-se livre para criar uma issue falando sobre isso e até (caso desejar) fazer um PR [implementando um novo endpoint](#contribuindo-com-novos-endpoints) que sirva esses dados!!!

Caso queira adicionar mais dados aos datasets existentes de algum endpoint, você poderá verificar na [documentação do endpoint](https://github.com/OpenDevUFCG/laguinho-api/blob/master/docs/README.md) se existe informação de como contribuir para esses dados, e caso não exista... cria uma issue, pfvr <3
