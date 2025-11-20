```bash
obd2-web/
│
├── app.py            # Script principal Flask
├── Dockerfile
├── requirements.txt  # Dependências Python
├── codes.json        # Base de códigos OBD2
└── templates/
    ├── index.html    # Formulário de busca
    └── result.html   # Página de resultado
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
- Página de resultado com descrição, causas e vídeo incorporado  
- Base de dados JSON para adicionar novos códigos facilmente  
- Dockerfile pronto para rodar o site em qualquer máquina

---

## 📂 Estrutura do projeto

