# TCC - UM ESTUDO DE CASO DE COLETA E PRÉ-PROCESSAMENTO DE DADOS NA APLICAÇÃO DE PROCESSAMENTO DE LINGUAGEM NATURAL

Aqui estão os códigos e arquivos gerados ao longo da elaboração do TCC para conclusão do curso de Engenharia de Telecomunicações na Universidade Federal do Rio Grande do Norte (UFRN) no semestre de 2022.01. O TCC está disponível no seguinte link do [Repositório UFRN](https://repositorio.ufrn.br/handle/123456789/49109)

Para o TCC foi feito o web crawling do jornal [iJIM](https://online-journals.org/index.php/i-jim/index) com um projeto criado utilizando o framework Scrapy. Nesse projeto foi desenvolvida a spider [papers.py](https://github.com/Gafiam/TCC/blob/main/iJIM/iJIM/spiders/papers.py) para fazer as coletas dos dados desejados que foram salvos no arquivo [articles_dataset.csv](https://github.com/Gafiam/TCC/blob/main/iJIM/articles_dataset.csv).

A seguir foi desenvolvido o código mostrado no Jupyter Notebook [dataset_modeling.ipynb](https://github.com/Gafiam/TCC/blob/main/iJIM/dataset_modeling.ipynb) onde se fez um tratamento do dataset para limpeza dos dados e análise de informações por meio de um estudo das palavras-chave dos artigos, do tf e tf-idf dos resumos deles, e a geração de uma nuvem de palavras dos textos dos resumos.

Com o tempo mais detalhes serão adicionados ao código para explicar melhor a geração de cada dataset contido na pasta iJIM desse repositório, o notebook [other.ipynb](https://github.com/Gafiam/TCC/blob/main/iJIM/other.ipynb) contém alguns códigos que foram usados ao longo do projeto para estudar melhor o dataset, mas os mesmos foram removidos do notebook principal para simplificar o código utilizado para se chegar nos resultados que foram expostos no trabalho de monografia desenvolvido.
