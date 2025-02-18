# Configuração do Ambiente Python

Este guia irá ajudá-lo a configurar seu ambiente Python para executar os códigos das aulas.

## 1. Instalando o interpretador Python, Pip e Virtualenv

### Windows
1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python para Windows
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Clique em "Install Now"

### Debian GNU/Linux
Execute no terminal:
```
$ sudo apt install python3-pip python3-venv
```

### Verificar a instalação
Para verificar a instalação, abra o Prompt de Comando e digite:
```
$ python --version
```

## 2. Usando VS Code

1. Baixe e instale o VS Code: [code.visualstudio.com](https://code.visualstudio.com/)  
para usuários de Debian, siga as [instruções da distribuição](https://wiki.debian.org/VisualStudioCode) ou instale manualmente:
```
$ sudo apt install ~/Downloads/<code>.deb
```

2. Extensões recomendadas:
   - Python (Microsoft)
   - Git Lens
   - Python Indent
   - Material Icon Theme

3. Configurando o ambiente:
   - Abra a pasta do projeto: File > Open Folder
   - Selecione o interpretador Python: 
     1. Pressione `Ctrl+Shift+P`
     2. Digite "Python: Select Interpreter"
     3. Selecione o ambiente virtual (venv)

4. Executando código:
   - Abra um arquivo Python
   - Clique no botão ▶️ no canto superior direito ou
   - Use o terminal integrado (`` Ctrl+` ``):
     ```
     $ python arquivo.py
     ```

5. Depurando código:
   - Clique na linha para adicionar breakpoint (ponto vermelho)
   - Pressione F5 para iniciar depuração
   - Use os controles de depuração para:
     - Continuar (F5)
     - Step Over (F10)
     - Step Into (F11)

6. Terminal integrado:
   - Abra com `` Ctrl+` `` (acento grave)
   - Execute comandos Git, Python e Flask direto no terminal

## 3. Usando Git

1. Instale o Git pelo site oficial: [git-scm.com](https://git-scm.com/downloads)  
Em Debian por Aptitude: `$ sudo apt install git`  
Opcionalmente instale GitHub Desktop: `$ sudo apt install git-gui`

2. Configure seu usuário Git:
```
$ git config --global user.name "Seu Nome"
$ git config --global user.email "seu.email@exemplo.com"
```

3. Comandos básicos do Git:
```
# Clonar um repositório
$ git clone <https://github.com/url-do-repositorio>

# Verificar status dos arquivos
$ git status

# Adicionar arquivos
$ git add <nome_do_arquivo>

# Cometer modificações
$ git commit

# Enviar alterações para o repositório remoto
$ git push

# Atualizar repositório local
$ git pull
```

4. Comando para a aula:
```
# Clonar o repositório
$ git clone https://github.com/Anhanguera-rafael-calassara/2025-01-oop-2.git
$ cd 2025-01-oop-2
```

## 4. Criando um ambiente virtual de Python e instalando Flask

O ambiente virtual permite isolar as dependências do projeto. Siga os passos:

1. Abra o Prompt de Comando (ou emulador de terminal)
2. Navegue até a pasta do projeto:
```
$ cd <caminho/para/sua/pasta/oop2>
```

3. Crie o ambiente virtual:
```
$ python -m venv .venv
```

4. Ative o ambiente virtual:
- Windows:
```
$ .venv\Scripts\activate
```
- Linux/Mac:
```
$ source .venv/bin/activate
```

5. Instale flask
```
(.venv) $ pip install flask
```

## 4. Executando um Arquivo Python

1. Com o ambiente virtual ativado, você verá (.venv) no início da linha de comando
2. Para executar um arquivo da aula:
```
(.venv) $ python aula_02/app.py
```

## Dicas Importantes

- Sempre ative o ambiente virtual antes de executar os arquivos
- Para desativar o ambiente virtual, use o comando:
```
(.venv) $ deactivate
```
- Para instalar pacotes, use:
```
(.venv) $ pip install nome_do_pacote
```

## Usando Flask

1. Exemplo básico de uso (hello.py):
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

2. Execute a aplicação:
```
(.venv) $ python hello.py
```

3. Acesse http://127.0.0.1:5000 no navegador
