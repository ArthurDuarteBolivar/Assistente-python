# Assistente de Voz em Python

Este é um assistente de voz criado em Python que permite interagir com várias funcionalidades usando comandos de voz. O assistente utiliza várias bibliotecas Python para executar suas tarefas.

## Funcionalidades

O assistente oferece as seguintes funcionalidades:

- **Bom Dia / Como você vai**: Cumprimenta o usuário e responde ao cumprimento.
- **Abrir Navegador**: Abre um navegador web (Brave) no sistema.
- **Abrir Editor de Texto**: Abre o editor de texto padrão (Notepad) no sistema.
- **Tocar Música**: Inicia o Spotify e reproduz música (requer a presença do Spotify instalado).
- **Suspender Computador**: Coloca o computador em modo de suspensão.
- **Desligar Computador**: Desliga o computador.
- **Fechar Navegador**: Encerra o navegador em execução.
- **Ferrou**: Bloqueia a estação de trabalho (tela de login).
- **O que você pode fazer**: Fornece uma lista de comandos disponíveis.
- **Notícias**: Obtém e lê as manchetes do site Projeto Comprova.
- **Qual o significado da palavra**: Pesquisa e fornece o significado de uma palavra.
- **Pesquisar**: Realiza uma pesquisa no Google com base na consulta.
- **Adicionar uma meta**: Adiciona uma meta (não especificada) e confirma a ação.

## Instalação e Uso

1. Certifique-se de que você tenha o Python instalado em sua máquina.
2. Instale as dependências necessárias usando o seguinte comando: pip install -r requirements.txt
3. Certifique-se de ter todas as bibliotecas listadas no arquivo `requirements.txt`.
4. Baixe o driver do Chrome (ChromeDriver) e certifique-se de que o caminho para o driver esteja configurado corretamente no código.
5. Certifique-se de ter o navegador Brave instalado para utilizar a funcionalidade de abrir o navegador.
6. Certifique-se de ter o Spotify instalado para utilizar a funcionalidade de tocar música.
7. Execute o código Python.

## Observações

- O assistente utiliza o reconhecimento de voz para ativar os comandos. Ele fica ativo após detectar a palavra "PC" e, em seguida, espera por um comando de voz.
- Algumas funcionalidades, como abrir o navegador e tocar música, dependem da disponibilidade das aplicações específicas no sistema.
- O assistente realiza pesquisas na web usando o navegador Google Chrome.
- As funcionalidades que envolvem texto falado usam a biblioteca `gTTS` para converter o texto em fala.
- O assistente pode ser personalizado adicionando ou modificando comandos na função `comandos`.

## Limitações

- O assistente depende das bibliotecas e serviços externos, então problemas de compatibilidade podem ocorrer.
- Alguns comandos podem depender da configuração do sistema, como o caminho para os executáveis dos programas.
- As funcionalidades de pesquisa e obtenção de notícias dependem da estrutura do site subjacente, que pode mudar ao longo do tempo.

## Contribuição

Sinta-se à vontade para contribuir para este projeto, adicionando novas funcionalidades, otimizando o código e corrigindo problemas.
