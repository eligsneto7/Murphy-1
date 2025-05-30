# 🌌 Cosmic Echo - Demonstração

## 🚀 Como Executar o Aplicativo

### 1. Instalação Rápida
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/cosmic-echo.git
cd cosmic-echo

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 2. Acesse o Aplicativo
Abra seu navegador e vá para: **http://127.0.0.1:8000**

## 🎯 Exemplo de Uso

### Dados de Teste
Para testar o aplicativo, você pode usar estes dados de exemplo:

- **Data de Nascimento**: 15/06/1999
- **Hora de Nascimento**: 14:30
- **Cidade**: São Paulo
- **País**: Brasil

### Resultado Esperado
O aplicativo irá:

1. **Calcular o Zênite**: Determinar as coordenadas astronômicas do zênite para o momento e local especificados
2. **Encontrar a Estrela**: Buscar no catálogo Hipparcos a estrela mais relevante próxima ao zênite
3. **Exibir Visualização**: Mostrar uma representação visual do céu com a estrela destacada
4. **Apresentar Informações**: Fornecer dados detalhados sobre a estrela encontrada

## 🎨 Interface do Usuário

### Página Inicial
- **Design Inspirado em Interestelar**: Fundo escuro com estrelas animadas
- **Formulário Intuitivo**: Campos claros para entrada de dados
- **Animações Suaves**: Transições elegantes entre elementos

### Página de Resultados
- **Vista do Zênite**: Visualização circular do céu com a estrela destacada
- **Informações da Estrela**: Módulos de dados inspirados no TARS
- **Mensagem Cósmica**: Texto personalizado sobre sua conexão estelar
- **Contexto Astronômico**: Informações sobre a jornada da luz

## 🔬 Funcionalidades Técnicas

### Cálculos Astronômicos
- **Tempo Sideral Local**: Calculado a partir do tempo de Greenwich e longitude
- **Coordenadas do Zênite**: RA = Tempo Sideral Local × 15°, Dec = Latitude
- **Distância Angular**: Fórmula da distância angular entre estrelas

### Sistema de Prioridades
1. **Estrelas Nomeadas**: Prioridade para estrelas com nomes próprios (Sirius, Vega, etc.)
2. **Estrelas Brilhantes**: Magnitude < 3.0 dentro de 3° do zênite
3. **Mais Próxima**: Estrela mais próxima do zênite calculado

### Catálogo de Estrelas
- **Fonte**: Catálogo Hipparcos da ESA
- **Filtro**: ~9.000 estrelas com magnitude < 6.0 (visíveis a olho nu)
- **Dados**: Coordenadas precisas, magnitude, classe espectral estimada

## 🎮 Recursos Interativos

### Animações
- **Estrelas de Fundo**: Movimento parallax suave
- **Loading Screen**: Grid animado inspirado em interfaces espaciais
- **Revelação de Dados**: Efeitos de fade-in para informações

### Easter Eggs
- **Konami Code**: Digite ↑↑↓↓←→←→BA para ativar o "Modo Cósmico"
- **Efeitos Especiais**: Animações de cores e filtros especiais

### Responsividade
- **Mobile-First**: Interface adaptável para dispositivos móveis
- **Breakpoints**: Otimizado para tablets e desktops
- **Touch-Friendly**: Botões e elementos adequados para toque

## 🐛 Solução de Problemas Comuns

### Erro de Localização
```
Erro: "Localização não encontrada"
Solução: Use nomes de cidades conhecidas em português ou inglês
Exemplo: "São Paulo" ou "Rio de Janeiro"
```

### Primeira Execução Lenta
```
Situação: Download de dados astronômicos na primeira execução
Tempo: ~2-3 minutos para download do catálogo Hipparcos
Solução: Aguarde o download completar (acontece apenas uma vez)
```

### Porta em Uso
```
Erro: "Address already in use"
Solução: Mude a porta ou termine processos existentes
Comando: uvicorn app.main:app --port 8001
```

## 📊 Métricas de Performance

### Tempos de Resposta
- **Primeira Execução**: 30-60 segundos (carregamento do catálogo)
- **Cálculos Subsequentes**: 2-5 segundos
- **Geocodificação**: 1-3 segundos (depende da API Nominatim)

### Uso de Memória
- **Catálogo Carregado**: ~50MB RAM
- **Por Requisição**: ~5MB adicional
- **Cache**: Dados astronômicos persistem entre requisições

## 🔮 Próximas Funcionalidades

### Em Desenvolvimento
- [ ] Mapa interativo para seleção de localização
- [ ] Exportação de relatório em PDF
- [ ] Compartilhamento em redes sociais
- [ ] Múltiplas datas (aniversários, eventos)

### Planejado
- [ ] Visualização 3D do céu
- [ ] Aplicativo mobile
- [ ] Realidade aumentada
- [ ] Integração com telescópios

## 💡 Dicas de Uso

### Para Melhores Resultados
1. **Use Hora Precisa**: A hora de nascimento afeta significativamente o resultado
2. **Cidades Grandes**: Use nomes de cidades conhecidas para melhor geocodificação
3. **Formato 24h**: Use formato de 24 horas para evitar ambiguidade
4. **Conexão Estável**: Primeira execução requer internet para download de dados

### Interpretação dos Resultados
- **Distância do Zênite**: Quanto menor, mais preciso o alinhamento
- **Magnitude**: Quanto menor o número, mais brilhante a estrela
- **Classe Espectral**: Indica cor e temperatura da estrela
- **Distância em Anos-luz**: Tempo que a luz levou para chegar até você

---

**🌌 Explore o cosmos e descubra sua conexão estelar única!** 