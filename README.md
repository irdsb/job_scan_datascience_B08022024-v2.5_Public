<div align="center">
  <h1>
    <strong>Job Scan Data Science</strong>
  </h1>
  <img src="https://github.com/irdsb/job_scan_datascience_opensource/blob/main/IMG.jpg" width="200px" height="200px">
</div>

___

**O que é o Job Scan ❓**

Job Scan Data Science, é uma ferramenta que realiza a extração de dados de vagas de emprego para os cargos de “Cientista de Dados” de uma das maiores vitrines deste setor e armazena vários tipos de informações diferentes destas vagas em um arquivo para análise.

___

**📋 Descrição do Programa**

Programa em Python que realiza web scraping de vagas de emprego na plataforma do LinkedIn e armazena esses dados em um dataset para análise.

___

**📋 Versão Atual do Programa**

|DESCRIÇÃO       | INFORMAÇÕES     |
|----------------|-----------------|
|Versão Atual    |`B08022024 v2.5` |
|Data de Criação |`05/01/2024`     |
|Last Update     |`08/02/2024`     |

___

**🔴 AVISO IMPORTANTE 🔴**

Tenha em mente que é altamente recomendável não fazer web scraping em qualquer outro site sem a permissão explícita do proprietário do site.
Desta forma, faça por sua conta e risco! Não me responsabelizo pelo bloqueio ou banimento da conta utilizada para logar na plataforma.

___

**📋 Como Funciona o Job Scan?**

🎯 Para utilizar o Job Scan, siga os passos abaixo:

1° - Abra o arquivo "user.txt" e adicione um e-mail que já esteja cadastrado na plataforma;

2° - Abra o arquivo "pw.txt" e informe a senha desta conta;

3° - Isso fará com que o programa faça o login automaticamente.

4° - Após o login, será criado uma pasta para o armazenamento dos arquivos HTML de cada página de vaga de emprego;
  
5° - O programa irá automaticamente na sessão de vagas e pesquisará por "Cientista de Dados";

6° - Nesta etapa, o programa irá percorrer por 30 páginas e armazenar todos os links de vagas encontrados nestas páginas;

7° - Após a captura dos links, o programa irá abrir no navegador link por link e realizar o scraping, e salvar a página inteira em um arquivo HTML;

8° - Quando a 7° etapa for finalizada, será armazenado todas as informações abaixo em um arquivo .CSV para análise:
- Nome da vaga; 
- Modalidade (Remoto, Híbrido ou Presencial); 
- Tipo de contrato de trabalho (Tempo integral, Contrato, Estágio, Temporário); 
- Nível de senioridade exigido na vaga (Júnior, Assistente, Estágio, Diretor, Pleno-sênior e Executivo); 
- Localização da vaga; 
- Tipo de candidatura (Candidatura Simplificada ou Não); 
- Empresa que esta contratando; 
- Tamanho da empresa (Baseado na quantidade de funcionários); 
- Competências presentes na vaga (Hard e Soft Skills);  

___

**Observações**

- Todo o processo é demorado e pode levar vários minutos ou até mesmo várias horas para que seja realizado o scrpaing de todas as vagas capturadas pelo programa.

- Para utilizar o programa do jeito que está (somente sendo necessário adicionar as credenciais de acesso), instale o navegador Edge da Microsoft na máquina que será executado o script.

😀 Estarei trabalhando neste projeto, então novas versões com melhorias e correções estarão sendo lançadas periodicamente!

🖖 Obrigado!
