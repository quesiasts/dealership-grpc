# Concessionária gRPC

Colocando em prática o que aprendi sobre gRPC aplicando isto em um projeto Django

### O que é gRPC?
Basicamente o gRPC é uma estrutura de código aberto e alto desempenho criada pelo Google. O gRPC segue amplamente a semântica HTTP sobre HTTP/2 e, assim permite que usemos o streaming full-duplex, possibilitando a comunicação entre diferentes sistemas via conexão de rede.

### Como rodar este projeto:
1. Precisa ter o poetry instalado em sua máquina, depois rode o comando `poetry install` para instalar as dependências do projeto localmente 
2. Abra a pasta `carfactory` e rode `python manage.py grpcrunserver` no terminal
3. Abra um segundo terminal e teste diversas requisições para verificar o sistema funcionando de fato (necessita de algumas melhorias)

### Tecnologias utilizadas:
- Django
- Django Rest Framework
- gRPC
- Poetry
