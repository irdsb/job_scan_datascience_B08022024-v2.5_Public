from bs4 import BeautifulSoup as bs
from bs4 import NavigableString as ns
from selenium import webdriver
from selenium.webdriver.common.by import By
from rich.console import Console
from time import sleep as sp
from datetime import datetime as dt
from tabulate import tabulate as tbl
import os
import csv


console = Console()
datetime = dt.now()
datetime_format = datetime.strftime('%d%m%Y-%H%M%S')
lista_arquivos = []

info = [['DESENVOLVEDOR', 'IGOR RICARDO DOS SANTOS BARBOSA'], ['PROJETO', 'DATA SCIENCE ANALYTICS JOBSCAN'], ['VERSÃO DO PROJETO', 'B08022024 v2.5'], ['DATA DE CRIAÇÃO', '05/01/2024'], ['ULTIMA ATUALIZAÇÃO', '08/02/2024']]
console.print(tbl(info, tablefmt='grid'), style='bold yellow')

def pasta(armazenamento):
    if not os.path.exists(armazenamento):
        local_armazenamento = os.makedirs(armazenamento)
        console.print(f'PASTA "{armazenamento}" CRIADA COM SUCESSO!', style='bold yellow')
        return local_armazenamento
pasta(f'{datetime_format}_jobscan_armazenamento')

def verifica_arquivo(arquivo):
    if os.path.isfile(arquivo):
        with open(arquivo, 'r') as file:
            return file.readlines()
    else:
        console.print(f"ARQUIVO '{arquivo}' NÃO ENCONTRADO.", style='bold yellow')
        return None

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.linkedin.com/login')
sp(2)

credenciais_user = verifica_arquivo('user.txt')
credenciais_pw = verifica_arquivo('pw.txt')

if credenciais_user and credenciais_pw:
    for x in credenciais_user:
        user = x.strip()
        driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(user)

    for y in credenciais_pw:
        pw = y.strip()
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(pw)

    sp(1)

    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    driver.implicitly_wait(60)

    driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()
    sp(3)

    data_analitycs = 'https://www.linkedin.com/jobs/search/?currentJobId=3794039875&geoId=106057199&keywords=Cientista%20de%20dados&location=Brasil&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true'
    driver.get(data_analitycs)
    sp(1)

    links = []
    link_set = set()

    try:
        for page in range(1, 31):
            sp(4)
            jobs = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
            jobs_list = jobs.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')

            for x in jobs_list:
                job_links = x.find_elements(By.TAG_NAME, 'a')
                
                for a in job_links:
                   if str(a.get_attribute('href')).startswith('https://www.linkedin.com/jobs/view') and a.get_attribute('href') not in links:
                        links.append(a.get_attribute('href'))
                   else:
                        pass

                driver.execute_script('arguments[0].scrollIntoView();', x)
        
            console.print(f'COLETANDO DADOS DA PÁGINA: {page}', style='bold green')
            driver.find_element(By.XPATH, f'//button[@aria-label="Página {page}"]').click()
            sp(4)

    except Exception as e:
        print(f"Erro ao coletar links: {e}")

    total_links = len(links)
    console.print(f'TOTAL DE LINKS ENCONTRADOS: {total_links}', style='bold green')

    for i in range(total_links):
        try:
            driver.get(links[i])
            sp(4)
            driver.find_element(By.CLASS_NAME, 'artdeco-card__actions').click()
            sp(4)

        except Exception as e:
            console.print(f"ERRO AO ACESSAR O LINK: {e}", style='bold red')
            pass

        sp(4)    
        content = driver.page_source
        soup = bs(content, 'html.parser')

        nome_pasta = f'{datetime_format}_jobscan_armazenamento'
        nome_arquivo = f'{datetime_format}_jobscan_data_analytics_simple_{i+1}.html'
        caminho_e_arquivo = f'{nome_pasta}/{nome_arquivo}'

        with open(f'{nome_pasta}/{nome_arquivo}', 'w', encoding='utf-8') as arquivo:
            arquivo.write(soup.prettify())
            sp(4)
        console.print(f'CONTEÚDO {i+1} SALVO COM SUCESSO!', style='bold yellow')
        lista_arquivos.append(caminho_e_arquivo)

    sp(4)

vagas = []
horarios = []
hora = []
modalidades = []
niveis = []
storange_niveis = []
competencias = []
storange_candidaturas = []
localizacoes = []
storange_localizacoes = []
candidaturas = []
storange_competencias = []
empresas = []
setores = []
storange_setores = []
funcionarios = []
palavras_filtro = ['Júnior', 'Assistente', 'Pleno', 'Sênior', 'Estágio', 'Diretor', 'Pleno-sênior', 'Executivo']
filter_mod = ['Tempo integral', 'Contrato', 'Estágio', 'Temporário']

for archive in lista_arquivos:
    with open(archive, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    soup = bs(conteudo, 'html.parser')

    try:
        vaga = soup.find('h1').text.strip()
    except AttributeError:
        vagas.append('null')
    vagas.append(vaga)
    
    try:    
        horario = soup.find('span', class_='jobs-unified-top-card__workplace-type').text.strip()
        horarios.append(horario)
    except AttributeError:
        horarios.append('null')
 
    try:    
        modalidade = soup.find('div', class_='mt3 mb2').text.strip()
    except AttributeError:
        modalidades.append('null')
    modalidades.extend([m.text.strip() for m in niveis if any(palavra in m.text for palavra in filter_mod)])    
    
    try:
        niveis = soup.find_all('span', class_='job-details-jobs-unified-top-card__job-insight-view-model-secondary')
    except AttributeError:
        storange_niveis.append('null')
    storange_niveis.extend([n.text.strip() for n in niveis if any(palavra in n.text for palavra in palavras_filtro)])
  
    try:    
        localizacao = soup.find('span', class_='jobs-unified-top-card__bullet').text
    except AttributeError:
        storange_localizacoes.append('null')
    storange_localizacoes.append(localizacao.strip())

    try:    
        candidatura = soup.find_all('span', class_='artdeco-button__text')
        candidaturas.append(candidatura)
        filter_candidatura = candidaturas[0][4]
        for ca in filter_candidatura:
            storange_candidaturas.append(ca.strip())
    except AttributeError:
        storange_candidaturas.append('null')

    try:    
        empresa = soup.find('a', class_='ember-view link-without-visited-state inline-block t-black').text.strip()
        empresas.append(empresa)
    except AttributeError:
        empresas.append('null')
    
    try:    
        setor = soup.find_all(class_='t-14 mt5')
        setores.append(setor)
        filter_setores = setores[0][0]
        for s in filter_setores:
            linhas = s.get_text().split('\n')
            linhas = [linha for linha in linhas if linha.strip() != '']
            filter_setor = linhas
            for linha in filter_setor:
                storange_setores.append(linha.strip())
            break
    except AttributeError:
        storange_setores.append('null')
    
    try:    
        funcionario = soup.find('span', class_='jobs-company__inline-information').text
    except AttributeError:
        funcionario = 'null'
    funcionarios.append(funcionario.strip())

    try:    
        competencia = soup.find('a', class_='app-aware-link job-details-how-you-match__skills-item-subtitle t-14 overflow-hidden').text
        competencias.append(competencia)
        for c in competencias:
            storange_competencias.append(c.strip())
            storange_competencias = list(set(storange_competencias))
            for co in range(len(storange_competencias)):
                storange_competencias[co] = storange_competencias[co].replace(',', '-')
    except AttributeError:
        storange_competencias.append('null')
 
    sp(4)

ds_header = ['Vaga', 'Horario', 'Modalidade', 'Nivel', 'Localizacao','Candidatura', 'Empresa', 'Funcionario', 'Competencia']
ds_database = list(map(list, zip(vagas, horarios, modalidades, storange_niveis, storange_localizacoes, storange_candidaturas, empresas, funcionarios, storange_competencias)))
ds_database_file = f'{datetime_format}_datascience_analytics_jobscan.csv'

with open(ds_database_file, 'w', newline='', encoding='utf-8') as ds_csvfile:
    ds_csv_writer = csv.writer(ds_csvfile)
    ds_csv_writer.writerow(ds_header)
    ds_csv_writer.writerows(ds_database)

console.print(f'DADOS DAS VAGAS SALVAS COM SUCESSO: {ds_database_file}', style='bold green')
