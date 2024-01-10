![Capa](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/5f7f9ca6-31ab-49fc-a23f-c8b5ed113a65)
# Descrição do Projeto
---

Desenvolvi este projeto para demonstrar minhas competências em Python e capacidade na resolução de problemas, com foco destacado nas bibliotecas Pandas e Django. Desenvolvi uma aplicação web aplicando conceitos modernos de design e habilidades em HTML/CSS e fiz a utilizaçãoo do Power BI para criar visualizações a partir de dados tratados com Pandas, resultado em uma ferramenta poderosa para tomada de decisões. Estou ansioso para compartilhar e receber feedback sobre este trabalho.

## Inicialização
---

Ao iniciar o projeto entre no ambiente virtual `myworld` pelo caminho abaixo:
```bash
.\myworld\Scripts\activate
```

Após isto **instale todas as dependências** disponíveis no arquivo `requeriments.txt`
```bash
pip install -r requirements.txt
```
Feito as etapas anteriores você deve abrir a pasta chamada **pagina** e inicar o servidor:
```bash
cd pagina
```
```bash
python manage.py runserver
```
Agora você terá o caminho local para abrir a aplicação web

## Cadastrando Clientes
---

Ao entrar no site, você deve se deparar com a seguinte tela

<img src="https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/e5a3a623-d739-4bc3-9ae2-3d7e08e4c5ca" width="60%">

O site usa autenticação de usuário, então você só conseguirá acessar o cadastro e lista de pacientes através das credencias corretas, prossiga com o Nome de Usuário: **FuncionarioA** e Senha: **123@FuncA**.

Com essas credenciais você poderá utilizar a ferrante web a vontade. Deste cadastrar novos usuários, visualizar os 15 ultimos clientes ou pesquisar por um especifico.

![Cadastro](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/26dced8e-5937-45e0-b468-9b0f15ff08be)

![Lista](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/d51298f3-4bd5-48ec-ac0f-119adedde2ca)

## Tratamento dos dados
---

Para alimentar nosso relatório é muito simples, você só precisa executar o arquivo `to_bi.ipynb` disponível na pasta **scripts**.

![Analise](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/a9388713-b3b8-4af9-856c-0117abfeca65)

Ele é responsável por calcular a Idade, IMC, classificação do IMC que o cliente se encontra, separar a maxima e minima pressão arterial e por fim exportar os dados para a pasta "database".

![Classificacao](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/01db15a0-088d-415d-9109-054163ea4da1)

## Relatório
---

Com o banco de dados atualizado você só precisa abrir o relatório **DASHBOARD** em `app/dash`. 

Neste relatório é possivel observar métricas como o IMC médio de todos os clientes, qual a porcentagem de cada grupo presente, o peso máximo, médio e minimo registrado além de levantamentos usando a Idade e Pressão dos pacientes.

![Dashboard](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/9906c56f-d404-4228-982c-1e37137fe740)

Você ainda pode aplicar o filtro 'Masculino' ou 'Feminino' rapidamente nos filtros a esquerda, como você vê na imagem abaixo.

![Filtro](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/2f5b175e-fca5-4721-82ab-46ee838a30f0)

### Observação
---
Para alimentar o relatório e lista de pacientes o banco de dados usado foi gerado randomicamente, isto significa que a simulação não captura com precisão as características de dados reais, resultando em dados que podem ser distorcidos ou não apresentar tendências.

No arquivo **forcar-dados-novos** na pasta `scripts`, você pode fazer modificações a fim de obter dados mais previsíveis se assim preferir.
![GeracaoDeDados](https://github.com/Joao-VCorreia/saude-corporal/assets/155659371/6d96e104-fe14-4775-af61-831e567d5f28)
