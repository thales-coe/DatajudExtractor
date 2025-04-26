Descrição
O Datajud Extractor é um aplicativo de código aberto desenvolvido em Python, com interface gráfica baseada em Tkinter, para extração automatizada de metadados de processos judiciais via API pública Datajud (Conselho Nacional de Justiça).

O programa realiza consultas focadas em processos do Tribunal de Justiça do Estado de São Paulo (TJSP), com o assunto classificado sob o código 12484 – Fornecimento de medicamentos, e exporta os resultados obtidos para planilhas Excel (.xlsx).

Funcionalidades
Interface gráfica para definição do intervalo de datas.

Integração com a API pública Datajud (CNJ).

Exportação automática dos dados para arquivos Excel.

Medição e exibição do tempo de processamento da busca e exportação.

Licenciamento aberto sob Creative Commons CC BY-SA 4.0.

Requisitos
Python 3.8 ou superior.

Bibliotecas adicionais:
requests
pandas
openpyxl
tkcalendar

Conexão à internet para acesso à API pública.

Instalação
Clone o repositório e instale as dependências necessárias:
git clone https://github.com/seu-usuario/DatajudExtractor.git
cd DatajudExtractor
pip install -r requirements.txt

Caso prefira instalar manualmente:
pip install requests pandas openpyxl tkcalendar

Utilização
Execute o arquivo principal:

bash
Copiar
Editar
python datajud_extractor.py
O programa abrirá uma interface gráfica para:

Seleção da Data de Início e Data Final.

Consulta automática à API Datajud conforme as datas informadas.

Geração de um arquivo Excel contendo os processos encontrados.

Exibição do tempo de execução da operação.

Estrutura do Projeto
Copiar
Editar
DatajudExtractor/
├── datajud_extractor.py
├── requirements.txt
├── LICENSE
└── README.md
Licença
Este projeto está licenciado sob a licença Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

Contribuições
Contribuições para o aprimoramento do projeto são bem-vindas.
Procedimento sugerido:

Fork este repositório.

Crie uma nova branch:

bash
Copiar
Editar
git checkout -b feature/nova-funcionalidade
Realize as alterações desejadas.

Faça commit:

bash
Copiar
Editar
git commit -m "Descrição clara da alteração"
Push para o seu repositório fork:

bash
Copiar
Editar
git push origin feature/nova-funcionalidade
Abra um Pull Request descrevendo as mudanças propostas.

Contato
Para dúvidas, sugestões ou solicitações de colaboração, utilize a seção de Issues no GitHub ou entre em contato conforme informações disponíveis no perfil.

Observação
Se desejar também gerar um executável (.exe) para facilitar o uso do aplicativo em ambientes Windows, recomenda-se utilizar o PyInstaller ou ferramentas similares.

