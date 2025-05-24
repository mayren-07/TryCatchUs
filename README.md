# 🕵️‍♂️ Lux — Combate à Desinformação

## 🚀 Proposta

**Lux** é uma solução mobile, integrada a uma extensão no Android, que permite aos usuários verificarem rapidamente se uma notícia é verdadeira ou falsa.

Ao abrir a aba lateral do Android e clicar na extensão, o usuário pode selecionar o texto da notícia e votar se acredita que ela é real ou fake. Essa interação não só educa, como também gera **insights importantes**, como:

- Quantos usuários caem em fake news
- Faixa etária mais suscetível
- Tipos de desinformação mais recorrentes

### 🔍 Processo de Verificação:

1. O texto selecionado é consultado na **API do Google Fact Check**.
2. Se houver um retorno relevante, é aplicado um **algoritmo de similaridade textual** para validar se a afirmação bate com o que consta na base.
3. Se confirmado como falso, o usuário é notificado imediatamente.
4. Caso não haja correspondência:

   - O sistema consulta o banco interno de fake news já validadas pela curadoria do Lux.
   - Se ainda não encontrar, a notícia é encaminhada para uma **curadoria humana interna**.
   - Assim que a curadoria retorna o veredito, o usuário é notificado.

### 🏅 Gamificação:

- Usuários recebem **medalhas de reconhecimento** sempre que acertam na validação das notícias.

### 📰 Feed Educativo:

- O app oferece um feed atualizado com fake news verificadas.
- Quinzenalmente, os usuários recebem um **e-mail educativo** com exemplos de fake news e orientações de **letramento midiático** para se proteger da desinformação.

---

## 📄 Documentação

- 📑 **Definição Técnica e de Negócio:**
  [🔗 Acessar no Figma](https://www.figma.com/board/KlMN8EPum5tvjZ3fAlIerz/Lux?node-id=0-1&p=f&t=FTFrZrMk8iy83F2Q-0)

- 📱 **Protótipo do Aplicativo:**
  [🔗 Acessar no Figma](https://www.figma.com/proto/wKdIiK1PIiqduo333KDq9q/Untitled?node-id=7-476&t=bvGciUBGWVTQuDZX-0&scaling=scale-down&content-scaling=fixed&page-id=2%3A1203&starting-point-node-id=4%3A3)

- 📧 **Protótipo da Newsletter:**
  [🔗 Acessar no Figma](https://www.figma.com/design/wKdIiK1PIiqduo333KDq9q/Untitled?node-id=11-778&t=bvGciUBGWVTQuDZX-0)

---

Perfeito! Aqui está a seção da **Demonstração Técnica** atualizada, incluindo a **newsletter em HTML e CSS**, com os caminhos dos arquivos funcionando como links clicáveis no GitHub.

---

## 🧠 Demonstração Técnica

### 🔍 Verificador de Fake News

Um exemplo da lógica de busca na API do Google Fact Check está disponível no seguinte caminho:

[👉 `scripts/script.py`](./scripts/script.py)

### 🔧 O que o script faz?

- Recebe uma afirmação como entrada.
- Consulta a API pública do Google Fact Check.
- Calcula a **similaridade textual** entre a afirmação digitada e as checagens disponíveis.
- Se encontrar um texto com similaridade maior ou igual a `0.45`, retorna que é **FALSO**.
- Caso contrário, informa que a afirmação será encaminhada para **curadoria humana**.

### ▶️ Como executar:

1. Crie um arquivo `.env` na raiz do projeto com sua chave da API:

```env
GOOGLE_FACT_CHECK_API_KEY=sua_api_key_aqui
```

2. Execute o script:

```bash
python scripts/script.py
```

3. Insira a afirmação a ser verificada e veja o resultado no console.

---

### 📨 Protótipo da Newsletter

O protótipo da nossa **newsletter educativa**, desenvolvido em **HTML e CSS**, está disponível no seguinte caminho:

[👉 `newsLetter`](./newsLetter/index.html)

- **Online (hospedado no Render):** [🌐 Acesse a newsletter](https://lux-newsletter.onrender.com)

### 🔧 O que contém:

- Um arquivo HTML representando o modelo da newsletter.
- Um arquivo CSS para estilização.
- Simula exatamente como será enviado o e-mail quinzenal para os usuários, com:

  - Fake news recentes.
  - Dicas de letramento midiático.
  - Informações de combate à desinformação.

---

### 🧠 Tecnologias Utilizadas

- 🐍 **Python** — Backend de verificação
- 🌐 **API Google Fact Check** — Checagem de fatos
- 📦 **Requests** — Requisições HTTP
- 🔍 **Difflib** — Similaridade textual
- 🔑 **Dotenv** — Gerenciamento de variáveis
- 📰 **HTML + CSS** — Protótipo da Newsletter

---

## 👩‍💻 Equipe **TryCatchUs**

- Ana Clara Oliveira Damasceno
- Mayla de Oliveira Renze
- Lavínia Ferreira De Brito

---
