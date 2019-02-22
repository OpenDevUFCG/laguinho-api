# `/v1/subjects`

### `GET /v1/subjects` - Recuperar informações de disciplinas de computação na UFCG.


#### Exemplo de retorno:

Para uma requisição `GET /v1/subjects` a API retornaria uma lista com as disciplinas, algo como:

```json
[
  {
        "codigo": "1411311",
        "nome": "Fundamentos de Matemática para Ciência da Computação I",
        "categoria": "Obrigatório",
        "creditos": "4",
        "pre_requisitos": "-",
        "periodo": "1",
        "quantidade_vagas": "120, 130",
        "areas": "",
        "dicas": "https://github.com/OpenDevUFCG/Tamburetei/tree/master/fmcc1",
        "sigla": "FMCC1"
    },
    {
        "codigo": "1411167",
        "nome": "Programação I",
        "categoria": "Obrigatório",
        "creditos": "4",
        "pre_requisitos": "-",
        "periodo": "1",
        "quantidade_vagas": "110, 120",
        "areas": "",
        "dicas": "https://github.com/OpenDevUFCG/Tamburetei/tree/master/prog1",
        "sigla": "P1"
    },
    {
        "codigo": "1411180",
        "nome": "Laboratório de Programação I",
        "categoria": "Obrigatório",
        "creditos": "4",
        "pre_requisitos": "-",
        "periodo": "1",
        "quantidade_vagas": "140, 120",
        "areas": "",
        "dicas": "https://github.com/OpenDevUFCG/Tamburetei/tree/master/prog1",
        "sigla": "LP1"
    }  
]
```


#### Como contribuir adicionando mais repositórios

Caso você queira adicionar mais disciplinas que não estejam na listagem dos dados, poderá enviar um PR adicionando mais ocorrencias no arquivo `disciplinas-ppc-2017` em [`roadmap-cc/data/disciplinas-ppc-2017.csv`](https://github.com/OpenDevUFCG/roadmap-cc/blob/master/data/disciplinas-ppc-2017.csv) seguindo o padrão dos dados já inseridos.
