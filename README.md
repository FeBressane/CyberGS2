
# Projeto de Vulnerabilidades em Aplicações

Este projeto contém exemplos **intencionais** de código vulnerável e suas respectivas versões corrigidas,
para fins de estudo em Cyber Segurança.

## Conteúdo

- `sql_injection_vuln.py` / `sql_injection_fixed.py`  
  Exemplo de **Injeção de SQL** e correção com queries parametrizadas.

- `xss_vuln.py` / `xss_fixed.py`  
  Exemplo de **Cross-Site Scripting (XSS)** em uma rota Flask e correção escapando a saída.

- `sensitive_data_vuln.py` / `sensitive_data_fixed.py`  
  Exemplo de **Exposição de Dados Sensíveis** (senha em texto puro e log inseguro) e correção usando hash.

- `requirements_vulnerable.txt` / `requirements_fixed.txt`  
  Exemplo de **Dependência Vulnerável** e versão atualizada para ser analisada por ferramentas de SCA.

## Observação

Estes arquivos são apenas para fins didáticos, para que ferramentas como Bandit, Semgrep,
ou SCA/SAST/DAST em um pipeline de CI/CD possam identificar as vulnerabilidades.
