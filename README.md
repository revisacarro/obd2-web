```bash
obd2-web/
│
├── app.py            # Script principal Flask
├── Dockerfile
├── requirements.txt  # Dependências Python
├── codes.json        # Base de códigos OBD2
└── templates/
    ├── base.html
    ├── index.html    # Formulário de busca
    └── result.html   # Página de resultado
    └── about.html
    └── notfound.html
    └── produtos.html
    └── diagnostico_guiado.html
```


# OBD2 Code Search Web

Um site simples em Flask que permite buscar códigos de erro automotivos (OBD2) e visualizar:

- Descrição do código  
- Causas mais comuns  
- Vídeo explicativo do YouTube

Tudo rodando dentro de **Docker**, pronto para qualquer computador.

---

## 🚀 Funcionalidades

- Busca interativa de códigos OBD2  
- Página de resultado com descrição 
- Base de dados JSON para adicionar novos códigos facilmente  
- Dockerfile pronto para rodar o site em qualquer máquina

---

```
bash
[
    {
        "code": "P0301",
        "description": "Falha de ignição detectada no cilindro 1.",
        "video": "r8j0XNqcUxc"
    },
    {
        "code": "P0420",
        "description": "Eficiência do catalisador abaixo do limite.",
        "video": ""
    }
]
```
formato novo json

## 📂 Estrutura do projeto

