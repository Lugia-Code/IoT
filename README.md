# Lugia IoT – Geração de QR Codes para Identificação de Motos

## 📌 Descrição

Este projeto tem como objetivo automatizar a criação de QR Codes contendo informações de identificação de motocicletas, como **placa** e **chassi**. Os QR Codes gerados podem ser utilizados para fins de rastreamento, identificação visual ou integração com sistemas IoT para controle de pátios.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **qrcode** – para geração de QR Codes
- **pyzbar** – para leitura de QR Codes (opcional)
- **OpenCV (opencv-python)** – para leitura de QR Codes (opcional)
- **Pillow** – para manipulação de imagens
- **NumPy** – suporte ao OpenCV

---

## 📁 Estrutura do Projeto

```
IoT/
├── qrcode_generator.py       # Script principal que gera o QR Code
├── qrcode.png                # QR Code gerado (exemplo)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## 🧪 Instruções de Uso

### 1. Clone o repositório
```bash
git clone https://github.com/Lugia-Code/IoT.git
cd IoT
```

### 2. (Opcional) Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3.1 (MacOS ou Linux) Instale o zbar
```bash
# MacOS
brew install zbar

# Linux
sudo apt-get install libzbar0
```

### 4. Execute o gerador de QR Code
```bash
python qrcode_generator.py
```

Você será solicitado a inserir:
- Placa
- Chassi
- Modelo
- Setor

Após a entrada dos dados, um arquivo chamado `qrcode.png` será salvo com o conteúdo em JSON desses dados.

---

## 🖼️ Exemplo de QR Code Gerado

```json
{
  "placa": "ABC1234",
  "chassi": "ch-9BWZZZ377VT004251",
  "modelo": "Mottu Sport",
  "setor": "Pendente"
}
```

---

## ✅ Resultados Parciais

- [x] Leitura de dados via `input()`
- [x] Geração de JSON com os dados da moto
- [x] Geração e exportação do QR Code como imagem
- [x] Leitura do QR Code
- [ ] Integração com sistema de leitura por câmera (futuro)
- [ ] Envio para base de dados ou API (futuro)
