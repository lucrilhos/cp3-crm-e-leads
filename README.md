<h1>uso de leads e uma breve aplicação de herança</h1>
<h2>Lucas M. Moraes - 563667</h2>
<h2>==============================================</h2>

<p>A aplicação desse sistema é fundamental para automatização dos html's, afinal manuseia dados de clientes, que podem ser inseridos através de uma linkagem com banco de dados/mysql. 
  O que muda a forma que você atende um cliente é a personalização, e com esse algoritmo em python você acessa diretamente o domínio de empresas, e-mails ou pessoas físicas, tornando a 
  funcionalidade do marketing de um projeto específico em uma instância muito mais tangível. Isso tudo se torna possível quando os valores de cada chave são destrinchados em um dicioná-
  rio que separa cada valor como uma "lead" (clientela, se traduzido literalmente), 
</p>
<break></break>
<h2>stages.py</h2>
<p>Bloco de código que simboliza a modelagem dos dados que iremos tratar, para isso é necessário o import de bibliotecas que
tratem da classe LEAD, para enxergamos cada elemento como uma clientela em potencial e definir a classe. Usa orientação a objetos, tais como: name, company, email, stage e created
A herança se faz presente aqui, com uma BaseLead que permite a reutilização das leads individualmente e de forma espontânea. Em resumo, tudo que representa uma lead é programado aqui, e utiliza-se
o método to_dict() que converte o objeto em dicionário, no caso as leads.</p>
<break></break>
<h2>repo.py</h2>
<p>Esse aqrquivo lida diretamente com o arquivo .json dentro da pasta "data". Esse código consiste na leitura dos dados .json e 
transforma em objetos leads. Lê, salva, carrega, e dá as seguintes possibilidades ao usuário: exportar dados para um arquivo
CSV e adicionar uma nova lead, além de poder retornar as leads já existentes. Também funciona como um banco de dados</p>
<break></break>
<h2>app.py</h2>
<p>O app.py é a interface de terminal de tudo que vem sendo armazenado e/ou manipulado, tem a função de controlar o fluxo do programa e seguir 
as decisões do usuário conforme a escolha. Fornece as ferramentas citadas e possibilitadas pelo arquivo repo.py, e executa no terminal.</p>
<break></break>
<h2>leads.json</h2>
<p>Aqui se armazena todos os dados (leads) que, como já foi pontuado, são salvos como dicionários. É a base para guardar os dados reais do CRM, contendo
a listagem, a busca e a exportação.</p>
<break></break>
<h2>==============================================</h2>




