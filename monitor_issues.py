import requests
from requests.auth import HTTPBasicAuth


#Configuração da Requisição
email = "email"
token_api = "token_api"
jira_domain = "jira_domain"
project_key = "project_key"

url = f"https://{jira_domain}/rest/api/3/search"

query = {
    "jql": f"project={project_key}"
}

headers = {
    "Accept": "application/json"
}

response = requests.get(
    url,
    headers=headers,
    params=query,
    auth=HTTPBasicAuth(email, token_api)
)

#Tratando e requisição
if response.status_code == 200:
    data = response.json()
    total_issues = data.get("total", 0)
    issues = data.get("issues", [])

    status_count = {}
    for issue in issues:
        status = issue['fields']['status']['name']
        status_count[status] = status_count.get(status, 0) + 1

    print(f"Total de issues no projeto: {total_issues}")
    print("Contagem por Status:")
    for status, count in status_count.items():
        print(f"   - {status}: {count}")
else:
    print(f"Erro {response.status_code}: {response.text}")