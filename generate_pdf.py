import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_pdf():
    pdf_path = r"C:\Users\Windows 11\.gemini\antigravity\scratch\felipe-ribeiro-mediakit\assets\curriculo.pdf"
    
    # Page setup - A4 size
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,  # 0.5 in
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Paragraph Styles
    style_name = ParagraphStyle(
        'DocName',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )
    
    style_subtitle = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=6
    )
    
    style_contact = ParagraphStyle(
        'DocContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
    )
    
    style_section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=14,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )
    
    style_item_title = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#0f172a'),
        keepWithNext=True
    )
    
    style_item_subtitle = ParagraphStyle(
        'ItemSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#475569'),
        spaceAfter=4,
        keepWithNext=True
    )
    
    style_bullet = ParagraphStyle(
        'DocBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#334155'),
        leftIndent=12,
        spaceAfter=3
    )

    story = []
    
    # 1. Header (Name, Title, Contact Info)
    story.append(Paragraph("FELIPE DA SILVA RIBEIRO", style_name))
    story.append(Paragraph("Graduando em Análise e Desenvolvimento de Sistemas | Cloud Computing & DevOps Enthusiast", style_subtitle))
    
    contacts_text = (
        "São Paulo/SP &bull; felipewolf.recife@gmail.com &bull; (11) 92190-9149 / (11) 94839-6848<br/>"
        "LinkedIn: <u>linkedin.com/in/felipe-ribeiro-634559252</u> &bull; GitHub: <u>github.com/FerisReptilium/FerisReptilium</u>"
    )
    story.append(Paragraph(contacts_text, style_contact))
    
    # Divider line
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=8))
    
    # 2. Resumo Profissional
    story.append(Paragraph("RESUMO PROFISSIONAL", style_section_heading))
    resumo_text = (
        "Cursando Análise e Desenvolvimento de Sistemas no IFPE, com conhecimentos sólidos em administração "
        "de sistemas Linux e Windows e experiência prática com serviços em nuvem AWS. Participação em projetos "
        "de inovação acadêmica aplicando automação com IoT para monitoramento de parâmetros de piscicultura familiar. "
        "Foco de atuação e especialização na área de infraestrutura em nuvem, bancos de dados, DevOps/CI-CD e automação. "
        "Busco primeira oportunidade profissional na área de tecnologia, para aplicar minhas competências "
        "técnicas e crescer estrategicamente."
    )
    story.append(Paragraph(resumo_text, style_body))
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 3. Formação Acadêmica
    story.append(Paragraph("FORMAÇÃO ACADÊMICA", style_section_heading))
    story.append(Paragraph("Tecnologia em Análise e Desenvolvimento de Sistemas", style_item_title))
    story.append(Paragraph("IFPE - Instituto Federal de Pernambuco &bull; Conclusão prevista: 2027", style_item_subtitle))
    
    story.append(Paragraph("Ensino Médio", style_item_title))
    story.append(Paragraph("Escola de Referência em Ensino Médio Maria Vieira Muliterno (EREM) &bull; Conclusão: 2009", style_item_subtitle))
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 4. Competências
    story.append(Paragraph("COMPETÊNCIAS", style_section_heading))
    skills_data = [
        [
            Paragraph("<b>Competências Técnicas:</b>", style_bullet),
            Paragraph(
                "Serviços AWS (EC2, S3, RDS, IAM, Lambda, VPC, CloudWatch), Cloud Practitioner foundations, "
                "Infraestrutura como Código (Terraform, CloudFormation), DevOps (CodePipeline, CodeDeploy, Git), "
                "Bancos de Dados (SQL, RDS, DynamoDB, Redshift), Inteligência Artificial na AWS (SageMaker, Rekognition, Polly), "
                "Linguagens de Programação (Python, SQL), Administração de Sistemas Linux & Windows Server.",
                style_body
            )
        ],
        [
            Paragraph("<b>Competências Comportamentais:</b>", style_bullet),
            Paragraph(
                "Aprendizado Contínuo, Resolução de Problemas, Trabalho em Equipe, Proatividade, "
                "Adaptação e Resiliência, Pensamento Crítico, Comunicação Eficaz, Gestão do Tempo, "
                "Orientação para Resultados.",
                style_body
            )
        ]
    ]
    t_skills = Table(skills_data, colWidths=[130, 390])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 5. Experiência Profissional
    story.append(Paragraph("EXPERIÊNCIA PROFISSIONAL", style_section_heading))
    story.append(Paragraph("Estagiário em TI", style_item_title))
    story.append(Paragraph("Prefeitura de Igarassu &bull; Março/2024 – Dezembro/2024", style_item_subtitle))
    story.append(Paragraph("&bull; Desenvolvimento, manutenção e otimização de sistemas internos governamentais.", style_bullet))
    story.append(Paragraph("&bull; Suporte técnico de hardware, software e resolução de chamados de rede para usuários.", style_bullet))
    story.append(Paragraph("&bull; Colaboração integrada com equipes no planejamento e implementação de projetos digitais.", style_bullet))
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 6. Experiências Relevantes & Projetos
    story.append(Paragraph("PROJETOS E EXPERIÊNCIAS RELEVANTES", style_section_heading))
    
    story.append(Paragraph("Projeto Acadêmico – Monitoramento de Qualidade da Água com IoT (IFPE | PIBEX)", style_item_title))
    story.append(Paragraph("Janeiro/2024 – Dezembro/2024 &bull; Automação e Sustentabilidade", style_item_subtitle))
    story.append(Paragraph("Desenvolvimento de sistema de telemetria automatizada para piscicultura familiar. Integração de sensores analógicos de pH, temperatura e turbidez a microcontroladores para transmissão de dados de qualidade da água em tempo real.", style_body))
    
    story.append(Paragraph("Modelador 3D (Projeto Pessoal)", style_item_title))
    story.append(Paragraph("Janeiro/2025 – Março/2025 &bull; Asset Creation", style_item_subtitle))
    story.append(Paragraph("Criação de personagens e ambientes virtuais no Daz Studio. Produção e mapeamento de assets digitais para simulações e renderização avançada com texturização de materiais e iluminação realista.", style_body))
    
    story.append(Paragraph("Rei do Bolo Chatbot & Lar das Delícias (Web Projects)", style_item_title))
    story.append(Paragraph("Produção Ativa & Deploys Vercel", style_item_subtitle))
    story.append(Paragraph("Desenvolvimento de plataformas interativas de e-commerce e atendimento ao cliente automatizado com bots de conversação baseados em IA e persistência em banco de dados Supabase.", style_body))
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))

    # 7. Produção Científica & Pesquisa
    story.append(Paragraph("PRODUÇÃO CIENTÍFICA & PESQUISA", style_section_heading))
    story.append(Paragraph("Programa de Iniciação Científica (IC) - UFRPE", style_item_title))
    story.append(Paragraph("PIBIC/PIC &bull; Universidade Federal Rural de Pernambuco", style_item_subtitle))
    story.append(Paragraph("Bolsista de Iniciação Científica em herpetologia, atuando com análises de dados biológicos, monitoramento microambiental de campo e mapeamento.", style_body))

    story.append(Paragraph("Artigos Completos Publicados em Periódicos:", style_item_title))
    story.append(Paragraph("&bull; OITAVEN, L. P. C.; Ribeiro., S.R ; de Moura, G.J.B ; Oliveira., J.B. Parasites of <i>Gymnodactylus darwinii</i> Gray, 1845 (Squamata, Phyllodactylidae) from an Atlantic Rainforest fragment. <b>ACTA TROPICA</b>, v. 192, p. 123-128, 2019.", style_bullet))
    story.append(Paragraph("&bull; OITAVEN, L. P. C.; Ribeiro., S.R ; RIBEIRO, L. B. ; de Moura, G.J.B. <i>Gymnodactylus darwinii</i> (Darwin's Gecko). Eggs and Hatchlings. <b>HERPETOLOGICAL REVIEW</b>, v. 50, p. 140-141, 2019.", style_bullet))

    story.append(Paragraph("Capítulos de Livros Publicados:", style_item_title))
    story.append(Paragraph("&bull; OITAVEN, L. P. C. et al. As Serpentes da Ilha de Paulo Afonso - Bahia, Nordeste do Brasil. In: <i>Vertebrados Terrestres da Ilha de Paulo Afonso...</i> 1ed. Recife: EDUFRPE, 2017, v. 1, p. 159-192.", style_bullet))

    story.append(Paragraph("Apresentações de Trabalho e Resumos em Congressos (Anais):", style_item_title))
    story.append(Paragraph("&bull; Dieta de <i>Gymnodactylus darwinii</i> em remanescente de Mata Atlântica. XI Congreso Latinoamericano de Herpetología, Quito, 2017. (Anais/Apresentação Oral).", style_bullet))
    story.append(Paragraph("&bull; Especificidade microambiental de <i>Gymnodactylus darwinii</i> em remanescente de Mata Atlântica. XI Congreso Latinoamericano de Herpetología, Quito, 2017. (Anais/Apresentação Oral).", style_bullet))

    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 8. Cursos e Certificações
    story.append(Paragraph("CURSOS E CERTIFICAÇÕES", style_section_heading))
    story.append(Paragraph("&bull; AWS Certified Cloud Practitioner &bull; Amazon Web Services (AWS) &bull; Validação: b437c158e4b644ad8b939f7823aa4e3", style_bullet))
    story.append(Paragraph("&bull; Programa AWS re/Start e Inteligência Artificial (363h) &bull; Escola da Nuvem &bull; Conclusão: 19/08/2025", style_bullet))
    story.append(Paragraph("&bull; OIAGRO - Olimpíada de Inovação do Agronegócio (48h) &bull; IFRJ / CNPq (2024)", style_bullet))
    story.append(Paragraph("&bull; XII Mostra de Extensão do IFPE &bull; Apresentação: 'Parâmetros de qualidade da água para criação de tilápias' (2024)", style_bullet))
    story.append(Paragraph("&bull; AWS Certified Developer &bull; Emissor: Escola da Nuvem", style_bullet))
    story.append(Paragraph("&bull; Fundamentos de Computação em Nuvem e AWS &bull; Emissor: Escola da Nuvem", style_bullet))
    story.append(Paragraph("&bull; IoT e Automação para Monitoramento Ambiental &bull; IFPE (PIBEX)", style_bullet))
    story.append(Paragraph("&bull; Auxiliar de Laboratório de Microbiologia (162h) &bull; SENAI Paulista &bull; Conclusão: 27/03/2023", style_bullet))
    
    # Divider
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#e2e8f0'), spaceAfter=6))
    
    # 8. Informações Adicionais
    story.append(Paragraph("INFORMAÇÕES ADICIONAIS", style_section_heading))
    story.append(Paragraph("&bull; Disponibilidade para atuação Presencial (São Paulo/SP), Remota ou Híbrida.", style_bullet))
    story.append(Paragraph("&bull; Interesse técnico focado nas áreas de Cloud Engineering, DevOps Pipelines, Dados e IoT.", style_bullet))
    story.append(Paragraph("&bull; Participação contínua em eventos acadêmicos e congressos técnicos de desenvolvimento.", style_bullet))
    story.append(Paragraph("&bull; Projetos práticos voltados a tecnologias sustentáveis e soluções de impacto ecológico.", style_bullet))
    
    doc.build(story)
    print("PDF resume generated successfully.")

if __name__ == "__main__":
    build_pdf()
