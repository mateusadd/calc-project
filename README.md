# calc-project

Projeto simples de calculadora para estudo

# Linguagem

Python

# Resumo

Testes para funções presentes em uma calculadora


# Alunos

Brian Richard Kleis, João Victor Nickler, Mateus Andrade


# Palestra - Agilidade

Conceito de Governança àgil
- Atitudes visando manter um padrão de aplicação dos métodos ágeis

Histórico da transformação na TOTVS:
- Havia divisão e times, o que gerava rixas e desencontros entre os times
- Realizada unificação em vários times contendo profissionais variados, para melhorar a comunicação

Princípios da metodologia:
1. Preocupação com o indivíduo e as interações
2. Funcionamento do software
3. Colaboração com o cliente
4. Resposta à mudança

Composição dos Squads:
- Agile master
- Product owner
- DEVs (back e front-end)
- QAs, documentação
- Líder

Scrum                            X               Kanban
- Sprints regulares              |   - Flexibilidade
- Trabalhos específicos          |   - Variação dos trabalhos
- Velocidade                     |   - Lead time: tempo total de entrega
- Escopo definido                |   - Escopo maleável e adaptável
- Entrega de item completo       |   - Tamanho do item a ser entregue não especificado
- Uso do gráfico burndown        |   - Sem uso de diagrama
- Prescrição de estimativas      |   - Sem estimativas


Cerimônias ->
Daily
- O que fazer no dia para atingir o objetivo da sprint?

Planning
- Qual o objetivo desta sprint?

Reabastecimento
- Revisão de objetivos e definição de novas tarefas

Review
- Quais foram as entregas deste ciclo?

Retrospectiva
- Conquistas e no que melhorar?

Upstream -> Refinar o item, como fazer, direcionar tarefas
Downstream -> Desenvolvimento, casos de teste, conclusão

Discovery -> Descobrir o que atende melhor o cliente 
Apresentação
Experiência do usuário -> Introdução do cliente, engajamento
Design thinking, Lean Inception

Caso prático -> 
Sinergia Fluig Plataforma e Fluig No-Code
- Feedback, chamados, requisições de mercado
- Interação -> Documentação
- Descobrir e definir -> Briefing e entrevistas
- Compartilhar ideias e decidir -> Como fazer?, prioridades
- Prototipar e validar -> Protótipo, testes (internos e com o usuário)

Cocriação -> Ferramenta Miro
- Análises, organização de tarefas, comparetilhamento de ideias sobre o projeto
- Pesquisas com o cliente através de formulários


# Tutorial GIT

Como inicializar repositórios -> 

git init . ou git inid <caminho_do_diretório> REPOSITÓRIO LOCAL.  também da pra criar diretamente no github e depois clonar o repositório.
git remote add origin git@github.com:username/new_repo para criar o repositório no github.

Como fazer o primeiro commit em um projeto -> 
Depois de você alterar/criar os arquivos que você deseja commitar o recomendado é checkar quais arquivos estão inclusos nas alterações dando um git status.
Esse comando retorna os arquivos que foram adicionados ou não a todas as mudanças que serão enviadas ao repositório. Também você verifica para qual "branch" está sendo commitado as suas alterações.
Adicionado os arquivos você deve efetuar o seguinte comando: git push -u origin <nome_da_branch>. Nesse comando será enviado para o git hub na branch que você seleciono anteriormente.

Como realizar commit de mudanças ->
Após você validar quai arquivos e serão enviados ao repositório e qual branch você deve utilizar o comando git  add <arquivo>  ou git add . para adicionar todos os arquivos do contexto que foram adicionados/modificados.
git commit arquivo
git commit -m "mensagem do commit"

Como compartilhar suas mudanças com outras pessoas da equipe ->
Caso você tenha visto algo que precise alterar na main do repositório ou alguma melhora no código do seu colega você pode abrir um merge request ou um pull request para alterar e auxiliar no projeto. Feito a aceitação esse código irá entrar para o repositório do seu colega e você irá ter colaborado. 

Como desfazer alterações ->
Quando você aceita um merge request você pode selecionar a opção "cherry-pick" ou retornar o seu commit para uma versão antiga no repositório. Porém caso seja localmente pode ser desfeito as alterações com os seguintes comandos: git checkout, git revert e git reset. 

Como resolver conflitos de merge ->
git pull - os arquivos que possam estar faltando serão atualizadas.
git reset --mixed - desfazer mudanças e assim refazer todo o trabalho. Chato mas tem gente que faz.
git checkout - pode ser usado para desfazer mudanças no diretório.

Como usar branches ->
git branch <nome da branch>.
git checkout -b '<nome_da_branch>' 
para criar uma branch e trocar para a nova branch criada.
Normalmente utiliza-se branches para enviar para main ou para a dev. As branches podem ser criadas para criar merge requests e mergear para a main ou para a dev.

Como encontrar bugs (git diff, git log, git bisect, git blame) ->
git diff - para tentar verificar o que foi feito na diferença entre os arquivos commitados.
git log - verificar o histórico de alterações.
git blame - ele é usado para examinar os pontos específicos do histórico de um arquivo e obter contexto sobre quem foi o último autor que modificou a linha. É usado para explorar o histórico de código específico e responder dúvidas sobre o que, como e por que o código foi adicionado ao repositório. Após isso verificar a alteração que pode estar causando problema.
git bisect irá tentar procurar o bug através dos últimos commits pelo hash.
git bisect start - começa a procurar.
git bisect good <hash_do_commti> - commt que você sabe que não tem problemas
git bisect bad <commit_que_voce_acha_que_tem_problema> - commit que você acha que tem problemas.

Como escolher determinados commits ->
git rebase -i HEAD~3 
O editor de texto será aberto com as linhas representando os três últimos commits.
pick f7f3f6d changed my name a bit
pick 310154e updated README formatting and added blame
pick a5f4a0d added catfile
Altere para edit os commits que deseja realizar alterações.
edit f7f3f6d changed my name a bit
pick 310154e updated README formatting and added blame
pick a5f4a0d added catfile
Feche o editor de texto. Digite o comando para alterar a mensagem do commit que foi marcado como edit: 
 git commit –amend -m “Nova mensagem”
Aplique a alteração:
 git rebase --continue
