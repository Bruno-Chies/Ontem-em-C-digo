🤖 Ontem em Código - Resumo Diário Automatizado de Notícias Tech

Um sistema desenvolvido em Python que automatiza o processo de acessar diariamente diversos sites e blogs de tecnologia, extrai as principais notícias do dia, utiliza inteligência artificial para gerar um resumo inteligente e envia o boletim direto para o e-mail do usuário.

🎯 Sobre o Projeto

O "Ontem em Código" resolve o problema de ter que navegar manualmente por vários portais de notícias de tecnologia todos os dias. O script realiza a varredura automatizada nos sites selecionados, processa o conteúdo coletado com o auxílio de IA para criar uma curadoria objetiva e faz o disparo automático do resumo por e-mail, mantendo você atualizado de forma prática e sem esforço.

✨ Funcionalidades

🤖 Automação de coleta de dados em múltiplos sites e blogs de tecnologia
🧠 Processamento de conteúdo com Inteligência Artificial para geração de resumos automatizados
📧 Envio programado e diário do resumo diretamente para a caixa de entrada do e-mail
⚙️ Configuração flexível de fontes de notícias e destinatários
🔄 Execução periódica facilitada (compatível com agendadores de tarefas)

🛠️ Tecnologias Utilizadas

Python 3
Bibliotecas de Web Scraping e Requisições (para varredura dos sites)
APIs de Inteligência Artificial / Processamento de Linguagem Natural
Serviços de Envio de E-mail (SMTP)

📋 Pré-requisitos

Python 3.8 ou superior
Conexão com a internet (para acessar os portais e enviar os e-mails)
Credenciais configuradas (contas de e-mail remetentes/destinatárias e chaves de API necessárias, se aplicável)

📦 Instalação

Clone este repositório:
git clone https://github.com/Bruno-Chies/Ontem-em-Codigo.git
cd Ontem-em-Codigo

(Opcional, mas recomendado) Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências do projeto:
pip install -r requirements.txt

(Nota: Se houver um arquivo de configuração ou variáveis de ambiente necessárias, lembre-se de configurar o arquivo .env com suas credenciais antes de rodar).

▶️ Como Usar

Para executar o script de varredura e envio manual:
python main.py

O fluxo do sistema irá:

Conectar automaticamente aos blogs e sites de tecnologia cadastrados.

Coletar as postagens e notícias mais recentes do dia.

Enviar o conteúdo para o módulo de IA gerar um resumo consolidado.

Disparar o e-mail formatado com as novidades para o destinatário configurado.

📁 Estrutura do Projeto

Ontem-em-Codigo/
├── main.py             # Script principal de execução
├── scraper.py          # Lógica de varredura e coleta dos sites
├── ai_summary.py       # Integração com a IA para geração do resumo
├── mailer.py           # Configuração e disparo de e-mails
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto

🚧 Possíveis Melhorias Futuras

Ampliação da lista de blogs e fontes de tecnologia monitoradas
Adição de interface gráfica ou painel de controle simples
Personalização de categorias de interesse (ex: Inteligência Artificial, Hardware, Programação)
Suporte a múltiplos canais de entrega (como Telegram ou WhatsApp além do e-mail)

📄 Licença

Este projeto está disponível sob licença MIT. Sinta-se livre para usar, modificar e distribuir.

👤 Autor

Desenvolvido por Bruno Chies e Felipe Krein como parte da jornada de estudos e projetos práticos em Python.
