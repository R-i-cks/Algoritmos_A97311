# Manifesto TPC8 

Data de início: 2021/12/5

Data de término: 2021/12/5

Supervisor: José Carlos Ramalho http://www.di.uminho.pt/~jcr/

Autor: Ricardo Lopes Araújo 


## Resumo 

* Este tpc resulta da junção do trabalho da aula prática + aula teórica.
* O módulo emd.py foi criado a partir das funções da aula prática.
* O modelo para a interface foi modelada através do modelo da aula teórica para melhor se adaptar ao tpc em questão.
* Na interface aparecem 6 botões, 1 entrada de texto e uma listbox. 
* O botão "Carregar base de dados" necessita que o utilizador escreva previamente o nome do ficheiro na entrada de texto, e carrega então a base de dados.
* O botão "Listar base de dados" apresenta 4 aspetos da base de dados na forma de lista: id,data,nome,apto ; Estes dados apresentam-se cronologicamente ordenados.
* O botão "Modalidades" lista todas as modalidades presentes na base de dados, praticadas por cada pessoa.
* O botão "Distribuições" abre uma nova janela que permite escolher o tipo de distribuição (por modalidades,clube ou ano), criar um gráfico da distribuição escolhida (embora não esteja incorporado na aplicação,funciona no editor), e um botão para sair
* Relativamente ao painel principal há ainda um botão "Limpar" para apagar o conteúdo da listbox e outro botão para sair.