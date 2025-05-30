# 🌌 Cosmic Echo

**Descubra a estrela que estava no zênite no momento exato do seu nascimento**

Cosmic Echo é um aplicativo web que conecta você com sua estrela do zênite - a estrela que estava perfeitamente alinhada acima de você no momento e local exatos do seu nascimento. Com uma interface inspirada no filme "Interestelar", o aplicativo oferece uma experiência visual e informativa impactante sobre sua conexão cósmica única.

![Cosmic Echo Preview](https://via.placeholder.com/800x400/0A0F14/5DADE2?text=COSMIC+ECHO)

## ✨ Características Principais

### 🎯 Funcionalidades Core
- **Cálculo Astronômico Preciso**: Utiliza o catálogo Hipparcos e a biblioteca Skyfield para determinar coordenadas do zênite
- **Identificação de Estrelas**: Encontra a estrela mais relevante próxima ao zênite com sistema de prioridades
- **Visualização Imersiva**: Interface 3D do céu com sua estrela destacada
- **Informações Detalhadas**: Dados completos sobre magnitude, classe espectral, distância e constelação
- **Geocodificação Automática**: Converte cidade/país em coordenadas precisas

### 🎨 Design Inspirado em Interestelar
- **Paleta de Cores**: Pretos profundos, azuis frios e acentos ciano
- **Tipografia**: Fontes modernas Exo 2 e Roboto Condensed
- **Animações**: Transições suaves e efeitos de "revelação" de dados
- **Interface TARS**: Módulos de informação inspirados no robô do filme
- **Campo Estelar**: Fundo animado com estrelas em movimento

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
git clone https://github.com/seu-usuario/cosmic-echo.git
cd cosmic-echo
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

### Acesso ao Aplicativo
Abra seu navegador e acesse:
- **Local**: http://localhost:8000
- **Rede**: http://seu-ip:8000

## 📖 Como Usar

### 1. Entrada de Dados
- **Data de Nascimento**: Selecione dia, mês e ano
- **Hora de Nascimento**: Insira hora e minuto (formato 24h)
- **Cidade**: Digite o nome da cidade onde nasceu
- **País**: Digite o nome do país

### 2. Processamento
O sistema irá:
1. Converter sua localização em coordenadas geográficas
2. Calcular as coordenadas do zênite para o momento exato
3. Buscar no catálogo estelar a estrela mais relevante
4. Preparar a visualização e informações

### 3. Resultados
Você receberá:
- **Vista do Zênite**: Visualização 2D do céu com sua estrela destacada
- **Informações da Estrela**: Nome, magnitude, classe espectral, distância
- **Mensagem Cósmica**: Texto personalizado sobre sua conexão estelar
- **Contexto Astronômico**: Informações sobre a jornada da luz

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

### Catálogo de Estrelas
- **Fonte**: Hipparcos Catalogue (ESA)
- **Filtro**: Magnitude aparente < 6.0 (visível a olho nu)
- **Dados**: ~9.000 estrelas com coordenadas precisas
- **Nomes**: 18 estrelas principais com nomes próprios

## 🎨 Personalização da Interface

### Cores Principais (CSS Variables)
```css
--deep-black: #0A0F14;      /* Fundo principal */
--dark-blue: #1A2C3D;       /* Elementos secundários */
--accent-cyan: #5DADE2;     /* Destaques e links */
--pure-white: #FFFFFF;      /* Texto principal */
--star-blue: #E6F3FF;       /* Cor das estrelas */
```

### Fontes
- **Primária**: Exo 2 (títulos e interface)
- **Secundária**: Roboto Condensed (dados técnicos)

## 🐛 Solução de Problemas

### Erro: "Localização não encontrada"
- Verifique a grafia da cidade e país
- Use nomes em português ou inglês
- Tente cidades maiores da região

### Erro: "Não foi possível baixar dados astronômicos"
- Verifique sua conexão com internet
- O download pode levar alguns minutos na primeira execução
- Tente executar novamente

### Erro: "Porta já em uso"
- Mude a porta: `uvicorn app.main:app --port 8001`
- Ou termine processos que usam a porta 8000

### Performance Lenta
- O primeiro cálculo pode ser mais lento (carregamento do catálogo)
- Cálculos subsequentes são mais rápidos (dados em cache)

## 🔮 Funcionalidades Futuras (Roadmap)

### Versão 1.1
- [ ] Mapa interativo para seleção de localização
- [ ] Eventos astronômicos históricos na data de nascimento
- [ ] Exportação de relatório em PDF
- [ ] Compartilhamento em redes sociais

### Versão 1.2
- [ ] Visualização 3D do céu
- [ ] Informações sobre constelações
- [ ] Múltiplas datas (aniversários, eventos importantes)
- [ ] Base de dados expandida de estrelas

### Versão 2.0
- [ ] Aplicativo mobile (React Native)
- [ ] Realidade aumentada para visualização do céu
- [ ] Integração com telescópios
- [ ] Comunidade de usuários

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Áreas que Precisam de Ajuda
- Tradução para outros idiomas
- Otimização de performance
- Testes automatizados
- Documentação adicional
- Design de novas funcionalidades

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- **ESA Hipparcos Mission**: Pelo catálogo de estrelas
- **Skyfield Library**: Por tornar a astronomia acessível em Python
- **Christopher Nolan**: Pela inspiração visual de "Interestelar"
- **Comunidade Astronômica**: Por manter dados abertos e acessíveis

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/seu-usuario/cosmic-echo/issues)
- **Documentação**: [Wiki do Projeto](https://github.com/seu-usuario/cosmic-echo/wiki)
- **Email**: cosmic.echo.support@gmail.com

---

**"Somewhere, something incredible is waiting to be known."** - Carl Sagan

🌌 Descubra sua conexão com o cosmos. Descubra seu Cosmic Echo. 