# 📁 Organizador de Pastas

Aplicativo desktop para organizar automaticamente sua pasta Downloads, movendo arquivos para subpastas por tipo.

Desenvolvido por **Allan Lopes** — v1.0.0

---

## ✨ Funcionalidades

- **Simulação** — visualiza o que será organizado antes de mover qualquer arquivo
- **Organização automática** — move arquivos para subpastas por categoria
- **Proteção contra duplicatas** — renomeia automaticamente arquivos com nomes repetidos
- **Interface gráfica** — fácil de usar, sem precisar do terminal
- **Seletor de pasta** — escolha qualquer pasta para organizar

---

## 📂 Categorias

| Categoria   | Extensões                                    |
| ----------- | -------------------------------------------- |
| Imagens     | `.jpg` `.jpeg` `.png` `.gif` `.webp`         |
| Videos      | `.mp4` `.mkv` `.avi`                         |
| Audios      | `.mp3` `.wav` `.flac` `.ogg`                 |
| Documentos  | `.pdf` `.docx` `.txt` `.pptx`                |
| Compactados | `.zip` `.rar` `.7z`                          |
| Páginas Web | `.html`                                      |
| Outros      | tudo que não se encaixa nas categorias acima |

---

## 🚀 Como usar

### Opção 1 — Executável (sem precisar do Python)

1. Baixe o `interface.exe` na seção [Releases](../../releases)
2. Execute o arquivo (Veja o recado abaixo)
3. Clique em **Escolher Pasta** e selecione a pasta que deseja organizar
4. Clique em **Simular** para visualizar o que será movido
5. Clique em **Organizar** para confirmar

> ⚠️ O Windows pode exibir um aviso de segurança na primeira execução. Clique em **"Mais informações" → "Executar assim mesmo"**.

### Opção 2 — Rodar com Python

```bash
git clone https://github.com/AllanLps/organizador-de-pastas.git
cd organizador-de-pastas
python interface.py
```

---

## 🗂️ Estrutura do projeto

```
organizador-de-pastas/
├── categorias.py     # dicionário de categorias e extensões
├── organizador.py    # lógica de simulação e movimentação
├── interface.py      # interface gráfica (tkinter)
└── main.py           # ponto de entrada
```

---

## 😉 Sinta-se livre para melhorar ou recriar o projeto

## 🛠️ Tecnologias

- Python 3
- tkinter (interface gráfica)
- PyInstaller (geração do executável)
