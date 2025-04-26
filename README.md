Datajud Extractor 1.0

Autor: Thales Coelho
Licença: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

Descrição:

O Datajud Extractor é um aplicativo de código aberto desenvolvido em Python, com interface gráfica baseada em Tkinter, destinado à extração automatizada de metadados de processos judiciais via API pública Datajud, mantida pelo Conselho Nacional de Justiça (CNJ). O programa realiza consultas focadas em processos do Tribunal de Justiça do Estado de São Paulo (TJSP), relacionados ao assunto classificado sob o código 12484 – Fornecimento de medicamentos, e exporta os resultados obtidos para planilhas Excel (.xlsx).

Funcionalidades:

O aplicativo oferece uma interface gráfica intuitiva para a definição do intervalo de datas, integração automática com a API pública Datajud, exportação dos dados coletados para arquivos Excel e exibição do tempo de processamento de cada operação. O projeto é distribuído sob a licença Creative Commons CC BY-SA 4.0.

Requisitos:

Para a execução do programa é necessário Python 3.8 ou superior, além das seguintes bibliotecas: requests, pandas, openpyxl e tkcalendar. Também é imprescindível uma conexão estável com a internet para o acesso à API pública.

Instalação:

Para instalar o Datajud Extractor, clone este repositório e instale as dependências listadas no arquivo requirements.txt. Alternativamente, as bibliotecas podem ser instaladas individualmente utilizando o gerenciador de pacotes pip.

Utilização:

Após a instalação das dependências, execute o arquivo principal do projeto (datajud_extractor.py). O sistema abrirá uma interface gráfica que permitirá a seleção do período de busca, a realização da consulta à API e a exportação dos dados em formato Excel, além de apresentar o tempo de execução de cada etapa.

Estrutura do Projeto:

O projeto está organizado da seguinte forma: datajud_extractor.py, requirements.txt, LICENSE e README.md.

Licença:

Este projeto está licenciado sob a Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), permitindo o compartilhamento e adaptação do material, desde que atribuído o devido crédito e mantida a mesma licença em obras derivadas.

Contribuições:

Contribuições são bem-vindas para o aperfeiçoamento do projeto. Recomenda-se a criação de uma nova branch para o desenvolvimento de funcionalidades ou correções, seguida de commit, push para o repositório remoto e abertura de um Pull Request descrevendo as alterações propostas.

Contato:

Em caso de dúvidas, sugestões ou propostas de colaboração, recomenda-se utilizar a seção de Issues do GitHub ou o contato disponível no perfil do autor.

Observação:

Para a geração de versões executáveis (.exe) do aplicativo destinadas a ambientes Windows, sugere-se a utilização de ferramentas como o PyInstaller.

