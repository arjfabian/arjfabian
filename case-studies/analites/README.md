# Recuperação de dados após desastre natural

<p align="center">
  <img src="./assets/logo-analites.png" />
</p>

_Disclaimer: Para os fins deste estudo de caso simulado, a região da cidade fictícia foi escolhida com base em dados históricos de atividades sísmicas no Brasil. É importante ressaltar que a escolha não implica em maior ou menor risco em relação a outras localidades e não se trata de uma previsão de eventos futuros._



## Introdução

Analites é uma rede de laboratórios clínicos estabelecida na cidade de Avatã, no estado de Mato Grosso. Por muitos anos têm sido uma referência no setor da saúde, atendendo aos mais altos padrões internacionais de qualidade e recebendo por isso diversos reconhecimentos.

No entanto, uma série de erros cometidos nos últimos meses, combinados com um desastre natural, provocaram a paralisação das operações de toda a rede e ameaçam levar a firma à falência. Nossa equipe foi convocada de maneira urgente com o objetivo de restabelecer, ao máximo possível, o acesso aos sistemas e dados.

A esperança de recuperar os dados em nuvem rapidamente se dissipou quando a equipe de TI se deparou com uma barreira inesperada: o acesso à plataforma foi negado. Investigações posteriores revelaram que a conta da Analites havia sido comprometida por um ataque cibernético nas semanas anteriores ao terremoto. Um ransomware havia criptografado os backups, tornando os dados inacessíveis. Diante da gravidade da situação, a alta direção autorizou a contratação de uma empresa especializada em recuperação de dados para auxiliar nos esforços de restauração.

## Cronologia

### 📅 03 de maio de 2024

A alta direção da Analites está numa reunião quando o terremoto acontece. Embora pareça um evento menor, rapidamente a intensidade aumenta até atingir 5.5. A falta de manutenção no prédio provoca a queda de um pedaço do teto dentro do data center da matriz, atingindo os servidores principais. Declara-se a emergência no prédio e o encerramento temporário das atividades.

### 📅 04 de maio de 2024

A equipe de TI da Analites comparece no data center e analisa a situação da sala de servidores. O armazenamento não estava corretamente configurado e apenas contém backups velhos, não havendo, portanto, possibilidade de recuperação de dados local.
Ativa-se então o protocolo de recuperação de dados em nuvem, mas o acesso é negado.
Faz-se a consulta com o atendimento do provedor de armazenamento em nuvem, dificultada pela falta de acesso a Internet (pela própria danificação da infraestrutura).

### 📅 05 de maio de 2024

O provedor de armazenamento em nuvem menciona atividade inusual no último mês na conta. A equipe de TI da Analites aguarda o relatório completo, que chega apenas no dia seguinte. O acesso aos recursos de nuvem é bloqueado.

### 📅 06 de maio de 2024

3 dias após o incidente, chega o relatório completo do provedor de armazenamento em nuvem, que descreve como, desde finais de fevereiro, houve uma série de acessos a partir de endereços IP previamente desconhecidos e que não pertencem à infraestrutura da rede de laboratórios.

### 📅 07 de maio de 2024

A equipe revisa os relatórios e analisa o histórico de acessos. Embora os endereços IP estejam localizados no Brasil, as contas pertencem a funcionários de alto nível que estão nos laboratórios e não tinham viajado nas datas mencionadas. Começam as averiguações que incluem entrevistas aos membros da alta direção, estabelecendo-se como conclusão de que houve um ataque cibernético a finais de fevereiro. Tal ataque provocou a perda de acesso à nuvem.

Perante a falta de conhecimentos técnicos adicionais, solicita-se à alta direção autorização para chamar uma equipe especializada em recuperação de dados, concedida no final do dia. A equipe de DR é contatada para começar os trabalhos no dia seguinte.

### 📅 08 de maio de 2024

A equipe de DR chega ao local
O suporte do provedor é acionado para recuperar o acesso à conta e o CEO da Analites realiza a verificação de identidade. Recupera-se o acesso à nuvem, mas o backup foi cifrado com um ransomware relacionado aos ataques de fevereiro. Programam-se entrevistas com os funcionários da alta direção, a ser realizadas no dia seguinte.

### 📅 09 de maio de 2024

Realizam-se entrevistas com os funcionários da alta direção e, obtendo antes as autorizações pertinentes por escrito, a equipe de DR acessa cada computador e verifica se os protocolos de segurança foram respeitados. Detecta-se que um dos computadores tinha uma conta com privilégios de administrador e sem senha. Analisa-se o sistema de arquivos com software de segurança e solucionam-se todas as infecções detectadas. Especificamente, detecta-se a mensagem de correio eletrônico que gerou a infecção inicial (em ordem cronológica) e, na mesma caixa de e-mail, um e-mail exigindo um pagamento para o resgate, que o funcionário tinha deixado passar sem falar do assunto. (O funcionário alega ter esquecido do assunto, pois não percebeu nada inusual no seu computador.)

### 📅 10 de maio de 2024

Uma semana depois do desastre

### Dia???

Usando do organograma da empresa, identificam-se as funções que interagem com o sistema e solicita-se ao chefe ou responsável de cada setor a coleta de documentos (planilhas, cópias impressas, etc) para reconstruir a base de dados.
Cria-se um script 

A equipe de segurança da informação foi convocada para lidar com a situação, enfrentando um desafio duplo: recuperar os dados perdidos e eliminar o ransomware da rede. O trabalho foi árduo e entediante, envolvendo a análise de backups antigos, a conciliação de cópias locais feitas pelos usuários e o desenvolvimento de scripts para automatizar a recuperação.

Após semanas de esforço incansável, a equipe conseguiu recuperar uma parte significativa dos dados e eliminar o ransomware da rede. No entanto, a perda de duas cópias de backup deixou um gosto amargo, e a empresa aprendeu uma lição valiosa sobre a importância da redundância e da manutenção de backups atualizados.

## Metodologia



## Lições Aprendidas

### Redundância

Manter múltiplas cópias de backup em locais diferentes é essencial para garantir a recuperação de dados em caso de desastre.

### Atualização de Backups

Verificar regularmente a integridade e a atualidade dos backups é fundamental para evitar a perda de dados irreparáveis.

### Conscientização da Alta Direção

É crucial envolver a alta direção na tomada de decisões relacionadas à segurança da informação e à recuperação de desastres.

### Capacitação dos Usuários

Treinar os usuários sobre boas práticas de segurança e a importância de fazer backups locais pode ajudar a mitigar os riscos.

### Planejamento e Simulação

(Desenvolver um plano de recuperação de desastres e realizar simulações regulares são medidas preventivas essenciais.)

## Conclusão

Este cenário hipotético demonstra a importância de uma abordagem proativa e preventiva para a segurança da informação e a recuperação de desastres. Ao investir em tecnologias robustas, capacitar os funcionários e manter uma cultura de segurança, as empresas podem minimizar os riscos e proteger seus dados valiosos.


---

Metodologia:
Ferramentas utilizadas (software de análise forense, sistemas de detecção de intrusões).
Procedimentos de investigação (análise de logs, entrevistas com funcionários).
Cronograma das atividades de recuperação.
Resultados:
Detalhes sobre a extensão dos danos (perda de dados, tempo de inatividade).
Descrição das ações de contenção e recuperação (isolamento de sistemas, restauração de backups).
Análise das causas raiz do incidente (falhas de segurança, erros humanos).
Lições Aprendidas:
Pontos fortes e fracos da resposta ao incidente.
Recomendações para melhoria dos processos e procedimentos.
Plano de ação para implementar as mudanças propostas.
Conclusão:
Síntese dos principais pontos do relatório.
Reforço da importância da preparação para incidentes de segurança.






## Créditos

<div>Icons made from <a href="https://www.onlinewebfonts.com/icon">svg icons</a>is licensed by CC BY 4.0</div>