# Laguinho API
 
Assim como o Laguinho da UFCG é o ponto mais central da universidade, esta API que centralizará os dados utilizados nos repositórios da OpenDevUFCG.

Os dados serão abertos e todos podem contribuir com mais dados e endpoints. Em breve mais detalhes.

[Documentação dos endpoints disponíveis](https://github.com/OpenDevUFCG/laguinho-api/blob/master/docs/README.md) 

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
