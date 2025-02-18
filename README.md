# Configuração do Ambiente Python

Este guia irá ajudá-lo a configurar seu ambiente Python para executar os códigos das aulas.

## 1. Instalando o Python

### Windows
1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python para Windows
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Clique em "Install Now"

Para verificar a instalação, abra o Prompt de Comando e digite:
```
python --version
```

## 2. Usando VS Code

1. Baixe e instale o VS Code: [code.visualstudio.com](https://code.visualstudio.com/)

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
   - Use o terminal integrado (`Ctrl+`):
     ```bash
     python arquivo.py
     ```

5. Depurando código:
   - Clique na linha para adicionar breakpoint (ponto vermelho)
   - Pressione F5 para iniciar depuração
   - Use os controles de depuração para:
     - Continuar (F5)
     - Step Over (F10)
     - Step Into (F11)

6. Terminal integrado:
   - Abra com Ctrl+j (acento grave)
   - Execute comandos Git, Python e Flask direto no terminal

## 3. Usando Git

1. Instale o Git pelo site oficial: [git-scm.com](https://git-scm.com/downloads)

2. Configure seu usuário Git:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

3. Comandos básicos do Git:
```bash
# Clonar um repositório
git clone [url-do-repositorio]

# Verificar status
git status

# Adicionar arquivos
git add .

# Criar commit
git commit -m "sua mensagem"

# Enviar alterações
git push

# Atualizar repositório local
git pull
```

4. Comando para a aula:
```bash
# Clonar um repositório
git clone ul
cd oop2
```


## 4. Criando um Ambiente Virtual

O ambiente virtual permite isolar as dependências do projeto. Siga os passos:

1. Abra o Prompt de Comando
2. Navegue até a pasta do projeto:
```
cd caminho/para/sua/pasta/oop2
```

3. Crie o ambiente virtual:
```
python -m uv venv
uv sync
```

4. Ative o ambiente virtual:
- Windows:
```
.venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```

## 4. Executando um Arquivo Python

1. Com o ambiente virtual ativado, você verá (venv) no início da linha de comando
2. Para executar um arquivo da aula:
```
python aula_02/app.py
```

## Dicas Importantes

- Sempre ative o ambiente virtual antes de executar os arquivos
- Para desativar o ambiente virtual, use o comando:
```
deactivate
```
- Para instalar pacotes, use:
```
uv pip install nome_do_pacote
```

## Instalando e Usando Flask

1. Verifique a instalação:
```
python -c "import flask; print(flask.__version__)"
```

2. Se não esiver instalado, execute:
Com o ambiente virtual ativado, instale o Flask:
```
pip install flask
```

3. Exemplo básico de uso (hello.py):
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

4. Execute a aplicação:
```
python hello.py
```

5. Acesse http://127.0.0.1:5000 no navegador

