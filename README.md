# GS2 – Cyber Security  
## Vulnerabilidades em Aplicações

Repositório criado para a **Global Solution de Cyber Security** da FIAP, com foco em demonstrar vulnerabilidades comuns em aplicações, suas correções e a integração dessas práticas a um pipeline de **DevSecOps**.

Trabalho desenvolvido pelos alunos:

- **Felipe Bressane – RM 97688**  
- **Nicolas Boni – RM 551965**  
- **Kaue Pastori – RM 98501** :contentReference[oaicite:0]{index=0}

---

## 1. Objetivo do Projeto

O objetivo é apresentar quatro vulnerabilidades recorrentes em aplicações, cada uma com:

- Explicação do conceito e dos riscos;
- Exemplo de **código vulnerável em Python**;
- Exemplo de **código corrigido**, aplicando boas práticas de segurança;
- Demonstração de como **SAST, SCA e DAST** podem ser utilizados em um pipeline de CI/CD para detectar essas falhas automaticamente. :contentReference[oaicite:1]{index=1}  

---

## 2. Estrutura do Repositório

```text
CyberGS2/
├── sql_injection_vuln.py
├── sql_injection_fixed.py
├── xss_vuln.py
├── xss_fixed.py
├── sensitive_data_vuln.py
├── sensitive_data_fixed.py
├── requirements_vulnerable.txt
├── requirements_fixed.txt
└── .github/
    └── workflows/
        ├── semgrep-sast.yml      # SAST (Semgrep)
        ├── sca-pip-audit.yml     # SCA (pip-audit)
        └── dast-zap.yml          # DAST (OWASP ZAP)
