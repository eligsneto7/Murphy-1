// ===== MODERN SKY VIEWER - INTERACTIVE CANVAS =====

class ModernSkyViewer {
    constructor(canvasId, data) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.data = data;
        
        // Estado da visualização
        this.zoom = 1.0;
        this.panX = 0;
        this.panY = 0;
        this.hoveredObject = null;
        this.animationFrame = null;
        
        // Configurações visuais
        this.config = {
            backgroundColor: '#0a0f14',
            zenithColor: '#5dade2',
            gridColor: 'rgba(93, 173, 226, 0.1)',
            textColor: '#ffffff',
            hoverColor: '#85c1e9',
            glowIntensity: 0.8,
            animationSpeed: 0.02
        };
        
        this.setupCanvas();
        this.setupEventListeners();
        this.startAnimation();
    }
    
    setupCanvas() {
        // Configurar canvas responsivo
        this.resizeCanvas();
        window.addEventListener('resize', () => this.resizeCanvas());
        
        // Configurar contexto para renderização suave
        this.ctx.imageSmoothingEnabled = true;
        this.ctx.imageSmoothingQuality = 'high';
    }
    
    resizeCanvas() {
        const container = this.canvas.parentElement;
        const rect = container.getBoundingClientRect();
        
        // Usar devicePixelRatio para telas de alta resolução
        const dpr = window.devicePixelRatio || 1;
        const size = Math.min(rect.width, 600); // Máximo 600px
        
        this.canvas.width = size * dpr;
        this.canvas.height = size * dpr;
        this.canvas.style.width = size + 'px';
        this.canvas.style.height = size + 'px';
        
        this.ctx.scale(dpr, dpr);
        this.size = size;
        this.center = size / 2;
        this.radius = size * 0.45; // 90% do raio disponível
    }
    
    setupEventListeners() {
        // Mouse events para interatividade
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('mouseout', () => this.handleMouseOut());
        this.canvas.addEventListener('wheel', (e) => this.handleWheel(e));
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        
        // Touch events para dispositivos móveis
        this.canvas.addEventListener('touchstart', (e) => this.handleTouchStart(e));
        this.canvas.addEventListener('touchmove', (e) => this.handleTouchMove(e));
        this.canvas.addEventListener('touchend', () => this.handleTouchEnd());
    }
    
    getMousePos(e) {
        const rect = this.canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }
    
    handleMouseMove(e) {
        const pos = this.getMousePos(e);
        this.hoveredObject = this.getObjectAtPosition(pos.x, pos.y);
        this.canvas.style.cursor = this.hoveredObject ? 'pointer' : 'default';
    }
    
    handleMouseOut() {
        this.hoveredObject = null;
        this.canvas.style.cursor = 'default';
    }
    
    handleWheel(e) {
        e.preventDefault();
        const zoomFactor = e.deltaY > 0 ? 0.9 : 1.1;
        this.zoom = Math.max(0.5, Math.min(3.0, this.zoom * zoomFactor));
    }
    
    handleClick(e) {
        const pos = this.getMousePos(e);
        const clickedObject = this.getObjectAtPosition(pos.x, pos.y);
        
        if (clickedObject) {
            this.showObjectDetails(clickedObject);
        }
    }
    
    handleTouchStart(e) {
        e.preventDefault();
        if (e.touches.length === 1) {
            const touch = e.touches[0];
            const pos = this.getMousePos(touch);
            this.hoveredObject = this.getObjectAtPosition(pos.x, pos.y);
        }
    }
    
    handleTouchMove(e) {
        e.preventDefault();
        // Implementar pan para touch se necessário
    }
    
    handleTouchEnd() {
        if (this.hoveredObject) {
            this.showObjectDetails(this.hoveredObject);
        }
        this.hoveredObject = null;
    }
    
    getObjectAtPosition(x, y) {
        if (!this.data || !this.data.objects) return null;
        
        for (const obj of this.data.objects) {
            const screenPos = this.worldToScreen(obj.x, obj.y);
            const distance = Math.sqrt(
                Math.pow(x - screenPos.x, 2) + Math.pow(y - screenPos.y, 2)
            );
            
            if (distance <= obj.size / 2 + 10) { // 10px de margem para clique
                return obj;
            }
        }
        
        return null;
    }
    
    worldToScreen(worldX, worldY) {
        // Converter coordenadas do mundo (-1 a 1) para coordenadas de tela
        const x = this.center + (worldX * this.radius * this.zoom) + this.panX;
        const y = this.center - (worldY * this.radius * this.zoom) + this.panY; // Y invertido
        return { x, y };
    }
    
    startAnimation() {
        const animate = (timestamp) => {
            this.render(timestamp);
            this.animationFrame = requestAnimationFrame(animate);
        };
        animate(0);
    }
    
    render(timestamp) {
        // Limpar canvas
        this.ctx.fillStyle = this.config.backgroundColor;
        this.ctx.fillRect(0, 0, this.size, this.size);
        
        // Desenhar grade de coordenadas
        this.drawGrid();
        
        // Desenhar círculo do horizonte
        this.drawHorizon();
        
        // Desenhar objetos celestes
        this.drawCelestialObjects(timestamp);
        
        // Desenhar zênite
        this.drawZenith(timestamp);
        
        // Desenhar informações de hover
        this.drawHoverInfo();
        
        // Desenhar controles de zoom
        this.drawZoomControls();
    }
    
    drawGrid() {
        this.ctx.strokeStyle = this.config.gridColor;
        this.ctx.lineWidth = 1;
        this.ctx.setLineDash([2, 4]);
        
        // Círculos concêntricos
        for (let i = 1; i <= 3; i++) {
            const radius = (this.radius * i) / 3 * this.zoom;
            this.ctx.beginPath();
            this.ctx.arc(this.center + this.panX, this.center + this.panY, radius, 0, Math.PI * 2);
            this.ctx.stroke();
        }
        
        // Linhas radiais
        for (let i = 0; i < 8; i++) {
            const angle = (i * Math.PI) / 4;
            const x1 = this.center + this.panX;
            const y1 = this.center + this.panY;
            const x2 = x1 + Math.cos(angle) * this.radius * this.zoom;
            const y2 = y1 + Math.sin(angle) * this.radius * this.zoom;
            
            this.ctx.beginPath();
            this.ctx.moveTo(x1, y1);
            this.ctx.lineTo(x2, y2);
            this.ctx.stroke();
        }
        
        this.ctx.setLineDash([]);
    }
    
    drawHorizon() {
        // Círculo externo do horizonte
        this.ctx.strokeStyle = this.config.zenithColor;
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.arc(this.center + this.panX, this.center + this.panY, this.radius * this.zoom, 0, Math.PI * 2);
        this.ctx.stroke();
        
        // Pontos cardeais
        const directions = ['N', 'E', 'S', 'W'];
        const angles = [0, Math.PI/2, Math.PI, 3*Math.PI/2];
        
        this.ctx.fillStyle = this.config.zenithColor;
        this.ctx.font = '12px "Exo 2", sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        
        directions.forEach((dir, i) => {
            const angle = angles[i] - Math.PI/2; // Ajustar para N no topo
            const x = this.center + this.panX + Math.cos(angle) * (this.radius * this.zoom + 20);
            const y = this.center + this.panY + Math.sin(angle) * (this.radius * this.zoom + 20);
            
            this.ctx.fillText(dir, x, y);
        });
    }
    
    drawCelestialObjects(timestamp) {
        if (!this.data || !this.data.objects) return;
        
        this.data.objects.forEach(obj => {
            const screenPos = this.worldToScreen(obj.x, obj.y);
            const isHovered = this.hoveredObject === obj;
            
            // Calcular tamanho com zoom e fator de brilho
            const baseSize = obj.size * this.zoom;
            const brightnessBoost = obj.brightness_factor ? obj.brightness_factor * 0.3 : 0;
            const size = baseSize * (1 + brightnessBoost);
            const glowSize = size * 1.8;
            
            // Efeito de pulsação para objetos em hover
            const pulseScale = isHovered ? 1 + 0.15 * Math.sin(timestamp * 0.005) : 1;
            const finalSize = size * pulseScale;
            
            // Desenhar glow/halo mais intenso para estrelas brilhantes
            const gradient = this.ctx.createRadialGradient(
                screenPos.x, screenPos.y, 0,
                screenPos.x, screenPos.y, glowSize
            );
            
            const glowColor = isHovered ? this.config.hoverColor : obj.color;
            const glowIntensity = obj.brightness_factor > 0.7 ? '80' : '60';
            const glowFade = obj.brightness_factor > 0.7 ? '40' : '25';
            
            gradient.addColorStop(0, glowColor + glowIntensity);
            gradient.addColorStop(0.5, glowColor + glowFade);
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(screenPos.x, screenPos.y, glowSize, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Desenhar estrela com formato de estrela
            this.ctx.fillStyle = obj.color;
            this.ctx.beginPath();
            this.drawStar(screenPos.x, screenPos.y, finalSize / 2, 5);
            this.ctx.fill();
            
            // Desenhar nome se estiver em hover ou for muito importante
            if (isHovered || obj.priority > 1000) {
                this.ctx.fillStyle = this.config.textColor;
                this.ctx.font = `${Math.max(10, 12 * this.zoom)}px "Exo 2", sans-serif`;
                this.ctx.textAlign = 'center';
                this.ctx.textBaseline = 'top';
                
                const textY = screenPos.y + finalSize / 2 + 8;
                
                // Fundo semi-transparente para o texto
                const textWidth = this.ctx.measureText(obj.name).width;
                this.ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                this.ctx.fillRect(
                    screenPos.x - textWidth/2 - 4,
                    textY - 2,
                    textWidth + 8,
                    16
                );
                
                this.ctx.fillStyle = this.config.textColor;
                this.ctx.fillText(obj.name, screenPos.x, textY);
            }
        });
    }
    
    drawStar(x, y, radius, points) {
        const angle = Math.PI / points;
        this.ctx.beginPath();
        
        for (let i = 0; i < points * 2; i++) {
            const r = i % 2 === 0 ? radius : radius * 0.5;
            const currentAngle = i * angle - Math.PI / 2;
            const px = x + Math.cos(currentAngle) * r;
            const py = y + Math.sin(currentAngle) * r;
            
            if (i === 0) {
                this.ctx.moveTo(px, py);
            } else {
                this.ctx.lineTo(px, py);
            }
        }
        
        this.ctx.closePath();
    }
    
    drawZenith(timestamp) {
        // Encontrar a estrela do usuário nos objetos
        let userStar = null;
        if (this.data && this.data.zenith) {
            // Procurar especificamente pela estrela do zênite pelo nome
            userStar = this.data.objects.find(obj => 
                obj.name === this.data.zenith.name && obj.type === 'star'
            );
            
            // Se não encontrar pelo nome exato, procurar por estrela com maior prioridade
            if (!userStar) {
                userStar = this.data.objects.find(obj => 
                    obj.type === 'star' && obj.priority > 1000
                );
            }
        }
        
        if (userStar) {
            // Desenhar indicador na posição da estrela do usuário
            const starPos = this.worldToScreen(userStar.x, userStar.y);
            
            // Círculo pulsante especial para a estrela do usuário
            const pulseScale = 1 + 0.15 * Math.sin(timestamp * 0.004);
            const starRadius = 40 * this.zoom * pulseScale;
            
            // Glow especial para a estrela do usuário
            const gradient = this.ctx.createRadialGradient(
                starPos.x, starPos.y, 0,
                starPos.x, starPos.y, starRadius * 1.5
            );
            gradient.addColorStop(0, '#FFD700' + '60'); // Dourado
            gradient.addColorStop(0.5, this.config.zenithColor + '40');
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(starPos.x, starPos.y, starRadius * 1.5, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Círculo especial para a estrela do usuário
            this.ctx.strokeStyle = '#FFD700';
            this.ctx.lineWidth = 3;
            this.ctx.setLineDash([8, 4]);
            this.ctx.beginPath();
            this.ctx.arc(starPos.x, starPos.y, starRadius, 0, Math.PI * 2);
            this.ctx.stroke();
            this.ctx.setLineDash([]);
            
            // Linha conectando ao centro (zênite astronômico)
            const centerPos = this.worldToScreen(0, 0);
            this.ctx.strokeStyle = this.config.zenithColor + '80';
            this.ctx.lineWidth = 2;
            this.ctx.setLineDash([10, 5]);
            this.ctx.beginPath();
            this.ctx.moveTo(centerPos.x, centerPos.y);
            this.ctx.lineTo(starPos.x, starPos.y);
            this.ctx.stroke();
            this.ctx.setLineDash([]);
            
            // Label especial para a estrela do usuário
            this.ctx.fillStyle = '#FFD700';
            this.ctx.font = `bold ${Math.max(14, 16 * this.zoom)}px "Exo 2", sans-serif`;
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'bottom';
            this.ctx.fillText('★ SUA ESTRELA ★', starPos.x, starPos.y - starRadius - 10);
            
            this.ctx.fillStyle = this.config.textColor;
            this.ctx.font = `${Math.max(12, 14 * this.zoom)}px "Exo 2", sans-serif`;
            this.ctx.fillText(this.data.zenith.name, starPos.x, starPos.y - starRadius - 30);
        }
        
        // Desenhar zênite astronômico (centro) de forma mais sutil
        const zenithPos = this.worldToScreen(0, 0);
        
        // Cruz pequena no centro
        this.ctx.strokeStyle = this.config.zenithColor + '60';
        this.ctx.lineWidth = 1;
        const crossSize = 8 * this.zoom;
        
        this.ctx.beginPath();
        this.ctx.moveTo(zenithPos.x - crossSize, zenithPos.y);
        this.ctx.lineTo(zenithPos.x + crossSize, zenithPos.y);
        this.ctx.moveTo(zenithPos.x, zenithPos.y - crossSize);
        this.ctx.lineTo(zenithPos.x, zenithPos.y + crossSize);
        this.ctx.stroke();
        
        // Label discreto do zênite astronômico
        this.ctx.fillStyle = this.config.zenithColor + '80';
        this.ctx.font = `${Math.max(8, 10 * this.zoom)}px "Exo 2", sans-serif`;
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'top';
        this.ctx.fillText('Zênite Astronômico', zenithPos.x, zenithPos.y + crossSize + 5);
    }
    
    drawHoverInfo() {
        if (!this.hoveredObject) return;
        
        const obj = this.hoveredObject;
        const padding = 15;
        const lineHeight = 18;
        const maxWidth = 250;
        
        // Preparar texto
        const lines = [
            `${obj.name}`,
            `Tipo: ${obj.type === 'star' ? 'Estrela' : obj.type === 'sun' ? 'Sol' : obj.type === 'planet' ? 'Planeta' : obj.type === 'moon' ? 'Lua' : 'Objeto Celeste'}`,
            `Cor: ${obj.color_name || 'Desconhecida'}`,
            `Magnitude: ${obj.magnitude.toFixed(1)}`,
            `Distância do Zênite: ${obj.distance_to_zenith.toFixed(1)}°`
        ];
        
        if (obj.temperature) {
            lines.push(`Temperatura: ${obj.temperature.toLocaleString()}K`);
        }
        
        // Calcular dimensões do tooltip
        this.ctx.font = '12px "Exo 2", sans-serif';
        const textWidth = Math.max(...lines.map(line => this.ctx.measureText(line).width));
        const tooltipWidth = Math.min(textWidth + padding * 2, maxWidth);
        const tooltipHeight = lines.length * lineHeight + padding * 2;
        
        // Posição do tooltip (canto superior direito)
        const tooltipX = this.size - tooltipWidth - 20;
        const tooltipY = 20;
        
        // Fundo do tooltip
        this.ctx.fillStyle = 'rgba(26, 44, 61, 0.95)';
        this.ctx.strokeStyle = this.config.zenithColor;
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.roundRect(tooltipX, tooltipY, tooltipWidth, tooltipHeight, 8);
        this.ctx.fill();
        this.ctx.stroke();
        
        // Texto do tooltip
        this.ctx.fillStyle = this.config.textColor;
        this.ctx.textAlign = 'left';
        this.ctx.textBaseline = 'top';
        
        lines.forEach((line, index) => {
            const y = tooltipY + padding + index * lineHeight;
            
            if (index === 0) {
                // Nome em destaque
                this.ctx.font = 'bold 14px "Exo 2", sans-serif';
                this.ctx.fillStyle = this.config.zenithColor;
            } else {
                this.ctx.font = '12px "Exo 2", sans-serif';
                this.ctx.fillStyle = this.config.textColor;
            }
            
            this.ctx.fillText(line, tooltipX + padding, y);
        });
    }
    
    drawZoomControls() {
        const controlSize = 30;
        const margin = 20;
        const x = margin;
        const y = this.size - margin - controlSize * 2 - 10;
        
        // Fundo dos controles
        this.ctx.fillStyle = 'rgba(26, 44, 61, 0.8)';
        this.ctx.strokeStyle = this.config.zenithColor;
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.roundRect(x - 5, y - 5, controlSize + 10, controlSize * 2 + 20, 5);
        this.ctx.fill();
        this.ctx.stroke();
        
        // Botão de zoom in (+)
        this.ctx.fillStyle = this.config.textColor;
        this.ctx.font = 'bold 20px "Exo 2", sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText('+', x + controlSize/2, y + controlSize/2);
        
        // Botão de zoom out (-)
        this.ctx.fillText('−', x + controlSize/2, y + controlSize + 10 + controlSize/2);
        
        // Indicador de zoom
        this.ctx.font = '10px "Exo 2", sans-serif';
        this.ctx.fillStyle = this.config.zenithColor;
        this.ctx.fillText(`${(this.zoom * 100).toFixed(0)}%`, x + controlSize/2, y + controlSize * 2 + 25);
    }
    
    showObjectDetails(obj) {
        // Criar evento customizado para mostrar detalhes
        const event = new CustomEvent('objectSelected', {
            detail: obj
        });
        document.dispatchEvent(event);
    }
    
    destroy() {
        if (this.animationFrame) {
            cancelAnimationFrame(this.animationFrame);
        }
    }
}

// Função para inicializar o visualizador
function initializeModernSkyViewer(canvasId, skyData) {
    return new ModernSkyViewer(canvasId, skyData);
}

// Adicionar método roundRect se não existir (compatibilidade)
if (!CanvasRenderingContext2D.prototype.roundRect) {
    CanvasRenderingContext2D.prototype.roundRect = function(x, y, width, height, radius) {
        this.beginPath();
        this.moveTo(x + radius, y);
        this.lineTo(x + width - radius, y);
        this.quadraticCurveTo(x + width, y, x + width, y + radius);
        this.lineTo(x + width, y + height - radius);
        this.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        this.lineTo(x + radius, y + height);
        this.quadraticCurveTo(x, y + height, x, y + height - radius);
        this.lineTo(x, y + radius);
        this.quadraticCurveTo(x, y, x + radius, y);
        this.closePath();
    };
} 