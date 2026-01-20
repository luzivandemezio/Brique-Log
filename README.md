#📦 Brique Log - v0.1

#📌 Motivação

Quem vive do brique sabe: a mente não para. Estamos o tempo todo calculando margens de lucro, custos de retirada e valores de revenda. Tentar manter tudo isso de cabeça é pedir para sair no prejuízo, e usar calculadoras comuns ou papel não resolve o problema da consistência e da organização a longo prazo.

O Brique Log nasceu da necessidade de centralizar esses cálculos. É uma ferramenta feita por quem entende a "coceira" de negociar e precisa de um lugar rápido para jogar ideias, gastos de conserto e fretes, garantindo que o lucro final seja real e não apenas uma estimativa mental furada. 🧠💸

#🛠️ O que o Script faz hoje

• Atualmente, o script em Python permite:

• Cadastro Detalhado: Registro de nome, custo de compra, gastos com logística/entrega e custos de conserto/reforma.

• Gestão de Status: Diferenciação entre itens já Vendidos e itens Em Estoque.

• Cálculo Automático: O sistema gera automaticamente o lucro real (para vendidos) e o lucro estimado (para o que ainda vai ser vendido).

• Relatório de Performance: Um resumo final que mostra o gasto total investido, o montante já recebido e o que ainda está previsto para entrar no bolso.

• Alerta de Prejuízo: Identifica e lista nominalmente quais briques não deram retorno positivo. ⚠️

#🚀 Como usar

Execute o script Python.
Informe quantos itens deseja cadastrar (ou siga o fluxo contínuo).
Responda às perguntas sobre gastos extras (S/N).
Defina se o item está em estoque ou se já foi "passado adiante".
Ao finalizar, veja o resumo completo das suas finanças de brique na tela.

#📅 Roadmap (Upgrades Futuros)

O projeto está em fase inicial (v0.1) e já temos os próximos passos planejados:
Persistência de Dados (Banco de Dados): Implementação de SQLite para que os dados não sumam ao fechar o programa. 💾

Gestão Dinâmica: Funções para editar itens, atualizar o status de "Estoque" para "Vendido" e remover briques que não deram certo ou foram retirados de venda.

Histórico de Gastos Irrecuperáveis: Garantir que, mesmo que um item saia do estoque sem ser vendido (quebra ou perda), o gasto investido continue registrado no histórico financeiro, pois o prejuízo precisa ser contabilizado.

#Desenvolvido por um briqueiro, para briqueiros. 🤝
