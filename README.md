# 🤖 Murphy-1

**Sistema de análise temporal e navegação estelar**

Murphy-1 é um sistema de análise avançado que conecta você com sua estrela-guia - a estrela que estava perfeitamente alinhada acima de você no momento e local exatos do seu nascimento. Com uma interface inspirada no filme "Interestelar" e assistente TARS, o sistema oferece uma experiência visual e informativa única sobre sua trajetória através do espaço-tempo.

![Murphy-1 Preview](https://via.placeholder.com/800x400/0A0F14/5DADE2?text=MURPHY-1)

## ✨ Características Principais

### 🎯 Funcionalidades Core
- **Cálculo Astronômico Preciso**: Utiliza o catálogo Hipparcos e a biblioteca Skyfield para determinar coordenadas do zênite
- **Identificação de Estrelas**: Encontra a estrela mais relevante próxima ao zênite com sistema de prioridades
- **Análise Temporal**: Curiosidades sobre idade, história e características fascinantes das estrelas
- **Visualização Imersiva**: Interface 3D do céu com sua estrela destacada
- **Assistente TARS**: Companion robótico com diálogos interativos do filme
- **Informações Detalhadas**: Dados completos sobre magnitude, classe espectral, distância e constelação
- **Geocodificação Automática**: Converte cidade/país em coordenadas precisas

### 🎨 Design Inspirado em Interestelar
- **Paleta de Cores**: Pretos profundos, azuis frios e acentos laranja/dourado Murphy
- **Tipografia**: Fontes modernas Exo 2 e Roboto Condensed
- **Animações**: Transições suaves e efeitos de "revelação" de dados
- **Interface TARS**: Módulos de informação inspirados no robô do filme
- **Campo Estelar**: Fundo animado com estrelas em movimento
- **Companion TARS**: Renderização 3D do robô com diálogos autênticos

### 🌟 Nova Seção: Arquivo Temporal da Estrela
- **Linha Temporal Cósmica**: Idade da estrela e era de nascimento
- **História Estelar**: Contexto histórico e cultural da estrela
- **Dados Fascinantes**: Fatos científicos e curiosidades
- **Comparações Temporais**: Relação com idade da Terra e do universo
- **Jornada da Luz**: Quando a luz começou sua viagem até você

### 🔧 Tecnologias Utilizadas
- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Astronomia**: Skyfield, Astropy
- **Geocodificação**: Geopy (Nominatim)
- **Catálogo Estelar**: Hipparcos Database
- **Styling**: CSS Grid, Flexbox, CSS Variables

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com internet (para download de dados astronômicos)

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/murphy-1.git
cd murphy-1
```

### 2. Crie um Ambiente Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Primeira Execução (Download de Dados Astronômicos)
Na primeira execução, o Skyfield fará download automático dos seguintes arquivos:
- **Catálogo Hipparcos** (~100MB): Base de dados de estrelas
- **Efemérides DE421** (~17MB): Posições planetárias precisas

Estes arquivos são baixados automaticamente e armazenados localmente.

## 🎮 Como Executar

### Desenvolvimento Local
```bash
# Ativar ambiente virtual (se não estiver ativo)
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Executar o servidor
python app/main.py
```

### Produção com Uvicorn
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Deploy no Railway
O projeto inclui arquivos de configuração para deploy automático:
- `Procfile`: Comando de execução
- `railway.toml`: Configurações do Railway
- Health check endpoint: `/api/health`

### Acesso ao Sistema
Abra seu navegador e acesse:
- **Local**: http://localhost:8000
- **Rede**: http://seu-ip:8000

## 📖 Como Usar

### 1. Entrada de Dados
- **Data de Nascimento**: Selecione dia, mês e ano
- **Hora de Nascimento**: Insira hora e minuto (formato 24h)
- **Cidade**: Digite o nome da cidade onde nasceu
- **País**: Digite o nome do país

### 2. Processamento Murphy-1
O sistema irá:
1. Converter sua localização em coordenadas geográficas
2. Calcular as coordenadas do zênite para o momento exato
3. Buscar no catálogo estelar a estrela mais relevante
4. Analisar dados temporais e históricos da estrela
5. Preparar a visualização e informações completas

### 3. Resultados Completos
Você receberá:
- **Vista do Zênite**: Visualização 2D do céu com sua estrela destacada
- **Informações da Estrela**: Nome, magnitude, classe espectral, distância
- **Arquivo Temporal**: Idade, história e curiosidades da estrela
- **Mensagem Temporal**: Texto personalizado sobre sua jornada no espaço-tempo
- **Perfil Astrológico**: Análise completa com signos e influências cósmicas
- **Companion TARS**: Interação com diálogos do filme

## 🔬 Detalhes Técnicos

### Cálculo do Zênite
O zênite é calculado usando:
```python
# Tempo Sideral Local = Tempo Sideral de Greenwich + Longitude/15
# Ascensão Reta do Zênite = Tempo Sideral Local * 15°
# Declinação do Zênite = Latitude do observador
```

### Sistema de Prioridades para Estrelas
1. **Prioridade 1**: Estrelas com nome próprio dentro de 0.5° do zênite
2. **Prioridade 2**: Estrelas brilhantes (mag < 3.0) dentro de 3° do zênite  
3. **Prioridade 3**: Estrela mais próxima do zênite (qualquer magnitude)

### Base de Dados de Curiosidades
- **Estrelas Famosas**: Sirius, Vega, Betelgeuse, Rigel, Arcturus, Capella
- **Dados Históricos**: Contexto cultural e científico
- **Estimativas Inteligentes**: Para estrelas menos conhecidas baseadas em características
- **Comparações Temporais**: Idade vs Terra, universo e jornada da luz

### Catálogo de Estrelas
- **Fonte**: Hipparcos Catalogue (ESA)
- **Filtro**: Magnitude aparente < 6.0 (visível a olho nu)
- **Dados**: ~9.000 estrelas com coordenadas precisas
- **Nomes**: 18 estrelas principais com nomes próprios expandidos

## 🎨 Personalização da Interface

### Cores Principais Murphy-1 (CSS Variables)
```css
--deep-black: #0A0F14;      /* Fundo principal */
--dark-blue: #1A2C3D;       /* Elementos secundários */
--accent-cyan: #5DADE2;     /* Destaques e links */
--murphy-orange: #E67E22;   /* Destaque temporal */
--murphy-gold: #F39C12;     /* Acentos dourados */
--tars-blue: #3498DB;       /* Cor do TARS */
--pure-white: #FFFFFF;      /* Texto principal */
--star-blue: #E6F3FF;       /* Cor das estrelas */
```

### Fontes
- **Primária**: Exo 2 (títulos e interface)
- **Secundária**: Roboto Condensed (dados técnicos)
- **TARS**: Courier New (diálogos do robô)

## 🐛 Solução de Problemas

### Erro: "Localização não encontrada"
- Verifique a grafia da cidade e país
- Use nomes em português ou inglês
- Tente cidades maiores da região

### Erro: "Falha no Sistema Murphy-1"
- Verifique sua conexão com internet
- O download pode levar alguns minutos na primeira execução
- Tente executar novamente

### Erro: "Porta já em uso"
- Mude a porta: `uvicorn app.main:app --port 8001`
- Ou termine processos que usam a porta 8000

### Performance Lenta
- O primeiro cálculo pode ser mais lento (carregamento do catálogo)
- Cálculos subsequentes são mais rápidos (dados em cache)

## 📱 Otimização Mobile

O Murphy-1 é completamente responsivo e otimizado para:
- **Smartphones**: Layout adaptativo com navegação touch-friendly
- **Tablets**: Interface intermediária com controles otimizados
- **Desktop**: Experiência completa com todas as funcionalidades

### Características Mobile-Friendly:
- Formulário responsivo com inputs otimizados
- TARS companion adaptável para telas pequenas
- Visualização do céu escalável
- Módulos de curiosidades empilháveis
- Botões de ação de tamanho adequado
- Performance otimizada para conexões lentas

## 🔮 Funcionalidades Futuras (Roadmap)

### Versão 1.1
- [ ] Mapa interativo para seleção de localização
- [ ] Eventos astronômicos históricos na data de nascimento
- [ ] Exportação de relatório Murphy-1 em PDF
- [ ] Compartilhamento em redes sociais com visual do TARS

### Versão 1.2
- [ ] Visualização 3D do céu estilo Interstellar
- [ ] TARS com mais diálogos e interações
- [ ] Informações sobre constelações
- [ ] Múltiplas datas (aniversários, eventos importantes)
- [ ] Base de dados expandida de estrelas

### Versão 2.0
- [ ] Aplicativo mobile nativo (React Native)
- [ ] Realidade aumentada para visualização do céu
- [ ] Integração com telescópios
- [ ] Comunidade Murphy-1 de usuários

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Áreas que Precisam de Ajuda
- Tradução para outros idiomas
- Expansão da base de dados de estrelas
- Novos diálogos para o TARS
- Otimizações de performance
- Documentação técnica

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- **Christopher Nolan** e equipe de "Interestelar" pela inspiração
- **ESA Hipparcos Mission** pelos dados estelares precisos
- **Skyfield Library** pela excelente biblioteca astronômica
- **OpenStreetMap/Nominatim** pelos serviços de geocodificação

---

🌌 Descubra sua trajetória no espaço-tempo. Descubra seu Murphy-1. 