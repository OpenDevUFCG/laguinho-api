# Laguinho API [![chat on Discord](https://img.shields.io/discord/558293573494112257.svg?logo=discord)](https://discordapp.com/invite/vFFGGEE)



![LaguinhoAPI Logo](https://i.imgur.com/lgiZyDn.png)

Assim como o Laguinho da UFCG é o ponto mais central da universidade, esta API centralizará os dados utilizados nos repositórios da OpenDevUFCG.

## Galera top que ajuda a gente :heart:

[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/0)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/0)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/1)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/1)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/2)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/2)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/3)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/3)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/4)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/4)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/5)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/5)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/6)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/6)[![](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/images/7)](https://sourcerer.io/fame/JoseRenan/OpenDevUFCG/laguinho-api/links/7)

Os dados são abertos e todos podem contribuir com mais dados e endpoints. Veja mais detalhes no [CONTRIBUTING.md](CONTRIBUTING.md) e se joga no laguinho com a gente!

## Documentação 

Veja [aqui](https://github.com/OpenDevUFCG/laguinho-api/blob/master/docs/README.md) a documentação dos dos endpoints disponíveis
 
## Desenvolvimento

Para executar o Laguinho API localmente, é necessário ter o `yarn` instalado e um Personal Access Token no github.

### Gerando o Personal Access Token

Siga os passos abaixo para gerar um token no github:

1. Acesse [este link](https://github.com/settings/tokens) (solicitará login no github caso ainda não esteja logado)
1. Clique em "Generate new token"
1. Dê um nome ao token em "Token description" e marque a opção "public_repo"
1. Clique em "Generate token"

Após isso, o github exibirá o token, copie o token e crie um arquivo `.env` na raiz do projeto baseado no arquivo `.env.example` e modifique o valor da variável `GITHUB_TOKEN` adicionando o seu token.

### Executando o servidor

Para executar o servidor, basta rodar os seguintes comandos no terminal após a configuração do token:

```
yarn install
yarn start
```

Deverá aparecer a mensagem `Listening on port 8080` e o servidor estará disponível em http://localhost:8080.

Caso queira executar em uma porta diferente, poderá modificar no arquivo `.env`, que você já criou, o valor da variável `LAGUINHO_PORT` para a porta desejada.


