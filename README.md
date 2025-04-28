
# 📋 Monitoramento de Issues no Jira Software

## Descrição

Este script em Python realiza a contagem automática de issues em um projeto específico no Jira Software (Cloud), utilizando a API pública do Jira e autenticação via token de API.

🔹 **Objetivo:** Facilitar a visibilidade das demandas do time de suporte, eliminando a necessidade de contagem manual.

---

## 🚀 Tecnologias Utilizadas
- Python 3
- Biblioteca `requests` (requisições HTTP)

---

## ⚙️ Como Utilizar

1. **Clone ou baixe o repositório**:

```bash
git clone https://github.com/seu-usuario/monitor-jira-issues.git
cd monitor-jira-issues
```

2. **Instale a dependência necessária**:

```bash
pip install requests
```

3. **Configure o script**:
   - Abra o arquivo `monitor_issues.py`
   - Edite as seguintes variáveis:
     - `email`: seu e-mail cadastrado no Jira
     - `token_api`: seu token gerado em [Atlassian API Tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
     - `jira_domain`: seu domínio do Jira (ex: `seu-dominio.atlassian.net`)
     - `project_key`: chave do projeto a ser monitorado

4. **Execute o script**:

```bash
python monitor_issues.py
```

---

## 📄 Exemplo de Saída

```
🔹 Total de issues no projeto SUPORTE: 37
🔹 Contagem por Status:
   - To Do: 10
   - In Progress: 15
   - Done: 12
```

---

## 📌 Observações
- O script trata erros de autenticação ou problemas na consulta.
- A contagem por status é opcional e pode ser removida ou ajustada conforme necessidade.
- A API do Jira pode limitar o número de resultados retornados. Para projetos muito grandes, pode ser necessário implementar paginação.

---

## ✨ Melhorias Futuras
- Implementar paginação automática para projetos com muitos tickets
- Exportar relatórios em CSV ou JSON

---

