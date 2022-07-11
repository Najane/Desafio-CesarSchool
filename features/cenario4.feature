#language: pt
Funcionalidade: Imprimir informações dos posts

    '''Eu como usuaria quero imprimir as informações dos posts.'''

    Cenario: Imprimir informaçãoes dos posts
    Dado que eu esteja no segundo pagina de posts do blog
    Quando navego pela pagina
    Então imprimo o titulo "Grupo de Computação Física da CESAR School com resultado expressivo na IoT Student Contest" da publicação do segundo posts
    E imprimo a data "2022-05-11T14:15:55-03:00" da publicação do segundo posts
    E imprimo o titulo "A defesa de dissertação de número 300 no Mestrado Profissional em Engenharia de Software" do terceiro posts
    E imprimo o autor "Comunicação School" do terceiro posts
    E navego até o final da pagina
    E imprimo o endereço do Cesar School
