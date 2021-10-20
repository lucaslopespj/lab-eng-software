## Metas de projeto (O que queremos fazer no futuro)

Os usuários **Leiloeiros** possuem duas funções especiais. Eles podem ***emitir relatórios*** que detalham transações realizadas no site e ***decide se um lote de produtos é aceito ou rejeitado*** para leilão.
Funcionalidades comuns a todos os usuários são ***ofertar lotes*** e ***realizar lances***.

Todos os usuários (**Leiloeiros** e **Compradores/Vendedores**) possuem um saldo que é atualizado após depósitos ou pagamentos.

A página inicial mostra todos os catálogos abertos e seus respectivos itens atualmente em leilão.

### Ofertar lotes de produtos

Tendo decidido ofetar um lote no site, o usuário Vendedor escolhe o catálogo onde quer realizar sua oferta e realiza login.

Após preencher os dados de cadastro do lote, o vendedor paga a taxa de comissão e aguarda confirmação do Leiloeiro.

O sistema envia um email de notificação para o Leiloeiro. Ao acessar o site, na aba **lotes pendentes** o Leiloeiro pode aprovar ou rejeitar o lote cadastrado.

Caso o lote seja aceito, o catálogo é atualizado para incluir o item.

Caso o lote seja recusado, a  taxa de comissão é ressarcida ao vendedor que recebe por uma email uma mensagem dizendo que seu lote foi recusado.

### Realizar Leilão

Após o lote ter sido adicionado ao catálogo, durante a data de validade do Leilão usuários podem realizar lances.

Ao final do período, o Comprador com maior lance é declarado vencedor.

O valor do lance final mais taxa de comissão é debitado do Comprador. Vendedor recebe valor do lance final e o Leiloeiro recebe o valor da taxa de comissão.

Todas as partes interessadas são notificadas por email.

### Gerar Relatórios

Para gerar um relatório, o Leiloeiro escolhe um período de tempo desejada. É gerada uma página HTML contendo todos as taxas de comissão pagas a ele no período.
