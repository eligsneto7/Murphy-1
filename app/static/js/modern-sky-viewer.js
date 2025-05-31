// 🌌 MURPHY-1 ULTRA MODERN SKY VIEWER
// Advanced celestial visualization with realistic rendering

class ModernSkyViewer {
    constructor(canvasId, data) {
        console.log('🎯 ModernSkyViewer constructor called');
        console.log('📊 Canvas ID:', canvasId);
        console.log('📊 Data received:', data);
        
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.error('❌ Canvas not found:', canvasId);
            return;
        }
        
        console.log('✅ Canvas found:', this.canvas);
        
        this.ctx = this.canvas.getContext('2d', { 
            alpha: false,
            desynchronized: true
        });
        
        this.data = data;
        console.log('📊 Data assigned to this.data:', this.data);
        console.log('📊 Objects in data:', this.data?.objects?.length || 0);
        
        this.animationFrame = null;
        
        // Advanced rendering config
        this.config = {
            // Deep space colors
            spaceGradient: [
                { pos: 0, color: '#000814' },      // Deep space black
                { pos: 0.3, color: '#001d3d' },    // Midnight blue
                { pos: 0.6, color: '#003566' },    // Deep blue
                { pos: 0.85, color: '#1e3a5f' },   // Horizon blue
                { pos: 1, color: '#2a4a7c' }       // Atmosphere edge
            ],
            
            // Star colors by temperature
            starColors: {
                O: '#9bb0ff',  // Blue-white (hottest)
                B: '#aabfff',  // Blue
                A: '#cad7ff',  // Blue-white
                F: '#f8f7ff',  // White
                G: '#fff4ea',  // Yellow-white (Sun)
                K: '#ffd2a1',  // Orange
                M: '#ffcc6f'   // Red (coolest)
            },
            
            // Visual effects
            milkyWayOpacity: 0.15,
            starGlowIntensity: 0.8,
            nebulaeCount: 3,
            shootingStarChance: 0.002,
            
            // UI colors
            zenithColor: '#5dade2',
            gridColor: 'rgba(93, 173, 226, 0.15)',
            textColor: '#ecf0f1',
            glowColor: '#fff',
            
            // Animation
            rotationSpeed: 0.00005,
            twinkleSpeed: 0.003,
            parallaxFactor: 0.3
        };
        
        // State management
        this.state = {
            zoom: 1,
            targetZoom: 1,
            rotation: 0,
            panX: 0,
            panY: 0,
            targetPanX: 0,
            targetPanY: 0,
            hoveredObject: null,
            selectedObject: null,
            mouseX: 0,
            mouseY: 0,
            time: 0,
            shootingStars: [],
            particles: [],
            // Drag state
            isDragging: false,
            dragStartX: 0,
            dragStartY: 0,
            dragPanStartX: 0,
            dragPanStartY: 0,
            // Touch state
            lastTouchDistance: 0,
            touchStartX: 0,
            touchStartY: 0
        };
        
        // Performance optimization
        this.layers = {
            background: null,
            milkyWay: null,
            deepSpace: null,
            stars: null
        };
        
        this.setupCanvas();
        this.initializeLayers();
        this.setupEventListeners();
        this.startAnimation();
    }
    
    setupCanvas() {
        this.resizeCanvas();
        window.addEventListener('resize', () => this.resizeCanvas());
    }
    
    resizeCanvas() {
        const container = this.canvas.parentElement;
        const rect = container.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        
        // Optimal size for performance and quality
        const size = Math.min(rect.width, rect.height * 0.9, 800);
        
        this.canvas.width = size * dpr;
        this.canvas.height = size * dpr;
        this.canvas.style.width = size + 'px';
        this.canvas.style.height = size + 'px';
        
        this.ctx.scale(dpr, dpr);
        
        this.size = size;
        this.center = size / 2;
        this.radius = size * 0.45;
        
        // Invalidate cached layers
        Object.keys(this.layers).forEach(key => {
            this.layers[key] = null;
        });
    }
    
    initializeLayers() {
        // Pre-render static layers for performance
        this.renderBackgroundLayer();
        this.renderMilkyWayLayer();
        this.generateParticles();
    }
    
    renderBackgroundLayer() {
        const canvas = document.createElement('canvas');
        canvas.width = this.size;
        canvas.height = this.size;
        const ctx = canvas.getContext('2d');
        
        // Create realistic space gradient
        const gradient = ctx.createRadialGradient(
            this.center, this.center, 0,
            this.center, this.center, this.radius * 1.5
        );
        
        this.config.spaceGradient.forEach(stop => {
            gradient.addColorStop(stop.pos, stop.color);
        });
        
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, this.size, this.size);
        
        // Add subtle noise for depth
        const imageData = ctx.getImageData(0, 0, this.size, this.size);
        const data = imageData.data;
        
        for (let i = 0; i < data.length; i += 4) {
            const noise = (Math.random() - 0.5) * 10;
            data[i] += noise;     // R
            data[i + 1] += noise; // G
            data[i + 2] += noise; // B
        }
        
        ctx.putImageData(imageData, 0, 0);
        this.layers.background = canvas;
    }
    
    renderMilkyWayLayer() {
        const canvas = document.createElement('canvas');
        canvas.width = this.size;
        canvas.height = this.size;
        const ctx = canvas.getContext('2d');
        
        // Create milky way effect
        ctx.save();
        ctx.translate(this.center, this.center);
        ctx.rotate(-Math.PI / 6); // Tilt the milky way
        
        // Multiple layers for depth
        for (let layer = 0; layer < 3; layer++) {
            const gradient = ctx.createLinearGradient(
                -this.radius * 1.5, 0,
                this.radius * 1.5, 0
            );
            
            const opacity = (0.05 - layer * 0.015) * 255;
            gradient.addColorStop(0, `rgba(200, 200, 255, 0)`);
            gradient.addColorStop(0.2, `rgba(200, 200, 255, ${opacity / 255})`);
            gradient.addColorStop(0.5, `rgba(255, 220, 200, ${opacity * 1.2 / 255})`);
            gradient.addColorStop(0.8, `rgba(200, 200, 255, ${opacity / 255})`);
            gradient.addColorStop(1, `rgba(200, 200, 255, 0)`);
            
            ctx.fillStyle = gradient;
            
            // Irregular shape for natural look
            ctx.beginPath();
            ctx.ellipse(0, 0, this.radius * (1.8 - layer * 0.2), 
                       this.radius * (0.3 - layer * 0.05), 
                       0, 0, Math.PI * 2);
            ctx.fill();
        }
        
        ctx.restore();
        
        // Add star clusters
        for (let i = 0; i < 200; i++) {
            const angle = Math.random() * Math.PI * 2;
            const distance = (Math.random() * 0.4 + 0.3) * this.radius;
            const x = this.center + Math.cos(angle) * distance;
            const y = this.center + Math.sin(angle) * distance;
            
            ctx.fillStyle = `rgba(255, 255, 255, ${Math.random() * 0.3 + 0.1})`;
            ctx.beginPath();
            ctx.arc(x, y, Math.random() * 1.5, 0, Math.PI * 2);
            ctx.fill();
        }
        
        this.layers.milkyWay = canvas;
    }
    
    generateParticles() {
        // Generate background star particles for parallax effect
        this.state.particles = [];
        
        for (let i = 0; i < 300; i++) {
            this.state.particles.push({
                x: Math.random() * this.size,
                y: Math.random() * this.size,
                size: Math.random() * 1.5 + 0.5,
                brightness: Math.random() * 0.5 + 0.2,
                twinkleOffset: Math.random() * Math.PI * 2,
                depth: Math.random() * 0.8 + 0.2 // For parallax
            });
        }
    }
    
    setupEventListeners() {
        // Mouse events
        this.canvas.addEventListener('mousedown', (e) => this.handleMouseDown(e));
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('mouseup', () => this.handleMouseUp());
        this.canvas.addEventListener('mouseout', () => this.handleMouseOut());
        this.canvas.addEventListener('wheel', (e) => this.handleWheel(e), { passive: false });
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        
        // Touch events
        this.canvas.addEventListener('touchstart', (e) => this.handleTouchStart(e), { passive: false });
        this.canvas.addEventListener('touchmove', (e) => this.handleTouchMove(e), { passive: false });
        this.canvas.addEventListener('touchend', () => this.handleTouchEnd());
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => this.handleKeyDown(e));
    }
    
    handleMouseDown(e) {
        if (e.button === 0) { // Left mouse button
        const rect = this.canvas.getBoundingClientRect();
            this.state.isDragging = true;
            this.state.dragStartX = e.clientX - rect.left;
            this.state.dragStartY = e.clientY - rect.top;
            this.state.dragPanStartX = this.state.panX;
            this.state.dragPanStartY = this.state.panY;
            this.canvas.style.cursor = 'grabbing';
        }
    }
    
    handleMouseMove(e) {
        const rect = this.canvas.getBoundingClientRect();
        this.state.mouseX = e.clientX - rect.left;
        this.state.mouseY = e.clientY - rect.top;
        
        if (this.state.isDragging) {
            // Calculate drag delta
            const deltaX = this.state.mouseX - this.state.dragStartX;
            const deltaY = this.state.mouseY - this.state.dragStartY;
            
            // Update pan with limits
            const maxPan = this.radius * 0.5;
            this.state.targetPanX = Math.max(-maxPan, Math.min(maxPan, this.state.dragPanStartX + deltaX));
            this.state.targetPanY = Math.max(-maxPan, Math.min(maxPan, this.state.dragPanStartY + deltaY));
        } else {
            // Check for hovered objects
            this.state.hoveredObject = this.getObjectAtPosition(this.state.mouseX, this.state.mouseY);
            this.canvas.style.cursor = this.state.hoveredObject ? 'pointer' : 'grab';
        }
    }
    
    handleMouseUp() {
        this.state.isDragging = false;
        this.canvas.style.cursor = this.state.hoveredObject ? 'pointer' : 'grab';
    }
    
    handleMouseOut() {
        this.state.isDragging = false;
        this.state.hoveredObject = null;
        this.canvas.style.cursor = 'default';
    }
    
    handleWheel(e) {
        e.preventDefault();
        const delta = e.deltaY > 0 ? 0.9 : 1.1;
        this.state.targetZoom = Math.max(0.5, Math.min(5, this.state.targetZoom * delta));
    }
    
    handleClick(e) {
        // Only process click if we weren't dragging
        if (!this.state.isDragging) {
            const rect = this.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const clickedObject = this.getObjectAtPosition(x, y);
        if (clickedObject) {
            this.showObjectDetails(clickedObject);
                this.state.selectedObject = clickedObject;
            }
        }
    }
    
    handleTouchStart(e) {
        e.preventDefault();
        
        if (e.touches.length === 1) {
            // Single touch - start drag
            const touch = e.touches[0];
            const rect = this.canvas.getBoundingClientRect();
            const x = touch.clientX - rect.left;
            const y = touch.clientY - rect.top;
            
            this.state.isDragging = true;
            this.state.touchStartX = x;
            this.state.touchStartY = y;
            this.state.dragPanStartX = this.state.panX;
            this.state.dragPanStartY = this.state.panY;
            
            this.state.hoveredObject = this.getObjectAtPosition(x, y);
        } else if (e.touches.length === 2) {
            // Two touches - prepare for pinch zoom
            const dx = e.touches[0].clientX - e.touches[1].clientX;
            const dy = e.touches[0].clientY - e.touches[1].clientY;
            this.state.lastTouchDistance = Math.sqrt(dx * dx + dy * dy);
        }
    }
    
    handleTouchMove(e) {
        e.preventDefault();
        
        if (e.touches.length === 1 && this.state.isDragging) {
            // Single touch drag
            const touch = e.touches[0];
            const rect = this.canvas.getBoundingClientRect();
            const x = touch.clientX - rect.left;
            const y = touch.clientY - rect.top;
            
            const deltaX = x - this.state.touchStartX;
            const deltaY = y - this.state.touchStartY;
            
            // Update pan with limits
            const maxPan = this.radius * 0.5;
            this.state.targetPanX = Math.max(-maxPan, Math.min(maxPan, this.state.dragPanStartX + deltaX));
            this.state.targetPanY = Math.max(-maxPan, Math.min(maxPan, this.state.dragPanStartY + deltaY));
        } else if (e.touches.length === 2) {
            // Pinch zoom
            const dx = e.touches[0].clientX - e.touches[1].clientX;
            const dy = e.touches[0].clientY - e.touches[1].clientY;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (this.state.lastTouchDistance > 0) {
                const scale = distance / this.state.lastTouchDistance;
                this.state.targetZoom = Math.max(0.5, Math.min(5, this.state.targetZoom * scale));
            }
            
            this.state.lastTouchDistance = distance;
        }
    }
    
    handleTouchEnd() {
        if (this.state.hoveredObject) {
            this.showObjectDetails(this.state.hoveredObject);
            this.state.selectedObject = this.state.hoveredObject;
        }
        this.state.hoveredObject = null;
    }
    
    handleKeyDown(e) {
        switch(e.key) {
            case '+':
            case '=':
                this.state.targetZoom = Math.min(5, this.state.targetZoom * 1.2);
                break;
            case '-':
                this.state.targetZoom = Math.max(0.5, this.state.targetZoom * 0.8);
                break;
            case '0':
                this.state.targetZoom = 1;
                this.state.targetPanX = 0;
                this.state.targetPanY = 0;
                break;
        }
    }
    
    getObjectAtPosition(x, y) {
        if (!this.data || !this.data.objects) return null;
        
        // Check objects in reverse order (top to bottom)
        for (let i = this.data.objects.length - 1; i >= 0; i--) {
            const obj = this.data.objects[i];
            const screenPos = this.worldToScreen(obj.x, obj.y);
            
            const distance = Math.sqrt(
                Math.pow(x - screenPos.x, 2) + 
                Math.pow(y - screenPos.y, 2)
            );
            
            const hitRadius = Math.max(10, obj.size * this.state.zoom * 2);
            if (distance <= hitRadius) {
                return obj;
            }
        }
        
        return null;
    }
    
    worldToScreen(worldX, worldY) {
        // Apply rotation
        const angle = this.state.rotation;
        const cos = Math.cos(angle);
        const sin = Math.sin(angle);
        
        const rotatedX = worldX * cos - worldY * sin;
        const rotatedY = worldX * sin + worldY * cos;
        
        // Convert to screen coordinates with zoom and pan
        const x = this.center + (rotatedX * this.radius * this.state.zoom) + this.state.panX;
        const y = this.center - (rotatedY * this.radius * this.state.zoom) + this.state.panY;
        
        return { x, y };
    }
    
    startAnimation() {
        const animate = (timestamp) => {
            this.update(timestamp);
            this.render();
            this.animationFrame = requestAnimationFrame(animate);
        };
        animate(0);
    }
    
    update(timestamp) {
        this.state.time = timestamp;
        
        // Smooth zoom interpolation
        const zoomDiff = this.state.targetZoom - this.state.zoom;
        this.state.zoom += zoomDiff * 0.1;
        
        // Smooth pan interpolation
        const panXDiff = this.state.targetPanX - this.state.panX;
        const panYDiff = this.state.targetPanY - this.state.panY;
        this.state.panX += panXDiff * 0.1;
        this.state.panY += panYDiff * 0.1;
        
        // Gentle rotation for dynamic feel
        this.state.rotation += this.config.rotationSpeed;
        
        // Update shooting stars
        this.updateShootingStars();
    }
    
    updateShootingStars() {
        // Remove finished shooting stars
        this.state.shootingStars = this.state.shootingStars.filter(star => star.life > 0);
        
        // Randomly create new shooting stars
        if (Math.random() < this.config.shootingStarChance && this.state.shootingStars.length < 3) {
            const angle = Math.random() * Math.PI * 2;
            const startRadius = this.radius * (0.7 + Math.random() * 0.3);
            
            this.state.shootingStars.push({
                x: this.center + Math.cos(angle) * startRadius,
                y: this.center + Math.sin(angle) * startRadius,
                vx: (Math.random() - 0.5) * 3,
                vy: Math.random() * 2 + 1,
                life: 1,
                trail: []
            });
        }
        
        // Update existing shooting stars
        this.state.shootingStars.forEach(star => {
            star.trail.push({ x: star.x, y: star.y, life: star.life });
            star.x += star.vx;
            star.y += star.vy;
            star.life -= 0.02;
            
            // Limit trail length
            if (star.trail.length > 20) {
                star.trail.shift();
            }
        });
    }
    
    render() {
        // Clear canvas
        this.ctx.fillStyle = '#000';
        this.ctx.fillRect(0, 0, this.size, this.size);
        
        // Draw layers
        this.drawBackground();
        this.drawParticles();
        this.drawMilkyWay();
        this.drawGrid();
        this.drawHorizon();
        this.drawCelestialObjects();
        this.drawShootingStars();
        this.drawZenithIndicator();
        this.drawUI();
    }
    
    drawBackground() {
        if (this.layers.background) {
            this.ctx.drawImage(this.layers.background, 0, 0);
        }
    }
    
    drawParticles() {
        // Background stars with parallax effect
        this.state.particles.forEach(particle => {
            const parallaxOffset = particle.depth * this.config.parallaxFactor;
            const x = particle.x + this.state.panX * parallaxOffset;
            const y = particle.y + this.state.panY * parallaxOffset;
            
            // Twinkling effect
            const twinkle = Math.sin(this.state.time * this.config.twinkleSpeed + particle.twinkleOffset);
            const brightness = particle.brightness * (0.7 + twinkle * 0.3);
            
            this.ctx.fillStyle = `rgba(255, 255, 255, ${brightness})`;
            this.ctx.beginPath();
            this.ctx.arc(x, y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }
    
    drawMilkyWay() {
        if (this.layers.milkyWay) {
            this.ctx.save();
            this.ctx.globalAlpha = this.config.milkyWayOpacity;
            this.ctx.translate(this.center, this.center);
            this.ctx.rotate(this.state.rotation * 0.1); // Slow rotation
            this.ctx.translate(-this.center, -this.center);
            this.ctx.drawImage(this.layers.milkyWay, 0, 0);
            this.ctx.restore();
        }
    }
    
    drawGrid() {
        this.ctx.save();
        this.ctx.strokeStyle = this.config.gridColor;
        this.ctx.lineWidth = 1;
        this.ctx.setLineDash([2, 4]);
        
        // Concentric circles with zoom
        for (let i = 1; i <= 4; i++) {
            const radius = (this.radius * i) / 4 * this.state.zoom;
            this.ctx.beginPath();
            this.ctx.arc(
                this.center + this.state.panX, 
                this.center + this.state.panY, 
                radius, 0, Math.PI * 2
            );
            this.ctx.stroke();
        }
        
        this.ctx.restore();
    }
    
    drawHorizon() {
        // Horizon circle
        this.ctx.save();
        this.ctx.strokeStyle = this.config.zenithColor;
        this.ctx.lineWidth = 2;
        this.ctx.globalAlpha = 0.6;
        
        this.ctx.beginPath();
        this.ctx.arc(
            this.center + this.state.panX,
            this.center + this.state.panY,
            this.radius * this.state.zoom,
            0, Math.PI * 2
        );
        this.ctx.stroke();
        
        // Cardinal directions
        const directions = [
            { label: 'N', angle: -Math.PI / 2 },
            { label: 'E', angle: 0 },
            { label: 'S', angle: Math.PI / 2 },
            { label: 'W', angle: Math.PI }
        ];
        
        this.ctx.fillStyle = this.config.textColor;
        this.ctx.font = '14px "Exo 2", sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.globalAlpha = 0.8;
        
        directions.forEach(dir => {
            const angle = dir.angle + this.state.rotation;
            const x = this.center + this.state.panX + Math.cos(angle) * (this.radius * this.state.zoom + 25);
            const y = this.center + this.state.panY + Math.sin(angle) * (this.radius * this.state.zoom + 25);
            
            // Background for better readability
            this.ctx.fillStyle = 'rgba(0, 8, 20, 0.8)';
            this.ctx.fillRect(x - 12, y - 12, 24, 24);
            
            this.ctx.fillStyle = this.config.zenithColor;
            this.ctx.fillText(dir.label, x, y);
        });
        
        this.ctx.restore();
    }
    
    drawCelestialObjects() {
        console.log('🎨 drawCelestialObjects called');
        console.log('🎨 this.data:', this.data);
        console.log('🎨 this.data.objects:', this.data?.objects);
        
        if (!this.data || !this.data.objects) {
            console.warn('⚠️ No data or objects found to render');
            return;
        }
        
        console.log(`🎨 Rendering ${this.data.objects.length} objects`);
        
        // Sort objects by magnitude (dimmer first)
        const sortedObjects = [...this.data.objects].sort((a, b) => b.magnitude - a.magnitude);
        
        console.log('🎨 Sorted objects:', sortedObjects.map(obj => `${obj.name}(${obj.magnitude})`));
        
        sortedObjects.forEach((obj, index) => {
            console.log(`🎨 Drawing object ${index + 1}: ${obj.name} at (${obj.x}, ${obj.y})`);
            this.drawCelestialObject(obj);
        });
    }
    
    drawCelestialObject(obj) {
            const screenPos = this.worldToScreen(obj.x, obj.y);
        const isHovered = this.state.hoveredObject === obj;
        const isSelected = this.state.selectedObject === obj;
        const isZenithStar = obj.isZenith || obj.is_zenith || (this.data.zenith && obj.name === this.data.zenith.name);
        
        // Calculate dynamic size - INCREASED SIGNIFICANTLY for visibility
        const baseSize = Math.max(4, 12 - obj.magnitude) * 2; // Doubled base size
        const zoomSize = baseSize * this.state.zoom;
        const hoverScale = isHovered ? 1.5 : 1;
        const selectedScale = isSelected ? 2 : 1;
        let finalSize = zoomSize * hoverScale * selectedScale;
        
        // Ensure minimum size for visibility
        finalSize = Math.max(finalSize, isZenithStar ? 12 : 6);
        
        // Get star color based on spectral type
        const starColor = obj.color || this.getStarColor(obj);
        
        // Draw star glow - INCREASED glow size
        const glowSize = finalSize * 4; // Increased multiplier for more visible glow
            const gradient = this.ctx.createRadialGradient(
                screenPos.x, screenPos.y, 0,
                screenPos.x, screenPos.y, glowSize
            );
            
        if (isZenithStar) {
            // Special golden glow for zenith star - MORE PROMINENT
            gradient.addColorStop(0, 'rgba(255, 215, 0, 1.0)'); // Increased opacity
            gradient.addColorStop(0.2, 'rgba(255, 215, 0, 0.8)'); // More visible
            gradient.addColorStop(0.6, 'rgba(255, 215, 0, 0.4)');
            gradient.addColorStop(1, 'transparent');
        } else {
            // Normal star glow - ENHANCED
            const [r, g, b] = this.hexToRgb(starColor);
            gradient.addColorStop(0, `rgba(${r}, ${g}, ${b}, ${0.9 * this.config.starGlowIntensity})`); // Increased
            gradient.addColorStop(0.2, `rgba(${r}, ${g}, ${b}, ${0.7 * this.config.starGlowIntensity})`); // Increased
            gradient.addColorStop(0.6, `rgba(${r}, ${g}, ${b}, ${0.3 * this.config.starGlowIntensity})`);
            gradient.addColorStop(1, 'transparent');
        }
            
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(screenPos.x, screenPos.y, glowSize, 0, Math.PI * 2);
            this.ctx.fill();
            
        // Draw star core - ENHANCED
        this.ctx.fillStyle = isZenithStar ? '#FFD700' : starColor;
            this.ctx.beginPath();
        this.ctx.arc(screenPos.x, screenPos.y, finalSize, 0, Math.PI * 2);
            this.ctx.fill();
        
        // Add bright white center for visibility
        this.ctx.fillStyle = '#FFFFFF';
        this.ctx.beginPath();
        this.ctx.arc(screenPos.x, screenPos.y, finalSize * 0.4, 0, Math.PI * 2);
        this.ctx.fill();
            
        // Draw diffraction spikes for ALL visible stars (not just bright ones)
        if (obj.magnitude < 4 || isZenithStar) {
            this.drawDiffractionSpikes(screenPos.x, screenPos.y, finalSize * 3, starColor); // Increased spike size
        }
        
        // Draw zenith star special effects
        if (isZenithStar) {
            this.drawZenithStarEffects(screenPos.x, screenPos.y, finalSize);
        }
        
        // Draw labels for important or hovered objects
        if (isHovered || isSelected || obj.magnitude < 3 || isZenithStar) {
            this.drawObjectLabel(obj, screenPos, finalSize, isZenithStar);
        }
    }
    
    drawDiffractionSpikes(x, y, size, color) {
        this.ctx.save();
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 1;
        this.ctx.globalAlpha = 0.6;
        
        // Four main spikes
        for (let i = 0; i < 4; i++) {
            const angle = (i * Math.PI / 2) + Math.PI / 4;
            const length = size * 3;
            
            // Gradient along spike
            const gradient = this.ctx.createLinearGradient(
                x, y,
                x + Math.cos(angle) * length,
                y + Math.sin(angle) * length
            );
            gradient.addColorStop(0, color);
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.strokeStyle = gradient;
            this.ctx.beginPath();
            this.ctx.moveTo(x, y);
            this.ctx.lineTo(
                x + Math.cos(angle) * length,
                y + Math.sin(angle) * length
            );
            this.ctx.stroke();
        }
        
        this.ctx.restore();
    }
    
    drawZenithStarEffects(x, y, size) {
        // Animated golden ring
        const time = this.state.time * 0.001;
        const pulseScale = 1 + Math.sin(time * 2) * 0.2;
        
        this.ctx.save();
        this.ctx.strokeStyle = '#FFD700';
        this.ctx.lineWidth = 2;
        this.ctx.globalAlpha = 0.6;
        this.ctx.setLineDash([5, 5]);
        
        this.ctx.beginPath();
        this.ctx.arc(x, y, size * 4 * pulseScale, 0, Math.PI * 2);
        this.ctx.stroke();
        
        this.ctx.restore();
    }
    
    drawObjectLabel(obj, pos, size, isZenithStar) {
        this.ctx.save();
        
        const labelY = pos.y + size + 15;
        
        // Background
        this.ctx.fillStyle = 'rgba(0, 8, 20, 0.9)';
        const text = isZenithStar ? `★ ${obj.name} ★` : obj.name;
        this.ctx.font = isZenithStar ? 'bold 14px "Exo 2", sans-serif' : '12px "Exo 2", sans-serif';
        const metrics = this.ctx.measureText(text);
        
        this.ctx.fillRect(
            pos.x - metrics.width / 2 - 8,
            labelY - 10,
            metrics.width + 16,
            20
        );
        
        // Text
        this.ctx.fillStyle = isZenithStar ? '#FFD700' : this.config.textColor;
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText(text, pos.x, labelY);
        
        // Magnitude
        if (!isZenithStar) {
            this.ctx.font = '10px "Exo 2", sans-serif';
            this.ctx.fillStyle = this.config.zenithColor;
            this.ctx.fillText(`mag ${obj.magnitude.toFixed(1)}`, pos.x, labelY + 15);
        }
        
        this.ctx.restore();
    }
    
    drawShootingStars() {
        this.state.shootingStars.forEach(star => {
            // Draw trail
            star.trail.forEach((point, i) => {
                const alpha = (i / star.trail.length) * point.life * 0.6;
                this.ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
                this.ctx.beginPath();
                this.ctx.arc(point.x, point.y, 1, 0, Math.PI * 2);
                this.ctx.fill();
            });
            
            // Draw head
            const gradient = this.ctx.createRadialGradient(
                star.x, star.y, 0,
                star.x, star.y, 10
            );
            gradient.addColorStop(0, `rgba(255, 255, 255, ${star.life})`);
            gradient.addColorStop(1, 'transparent');
            
            this.ctx.fillStyle = gradient;
            this.ctx.beginPath();
            this.ctx.arc(star.x, star.y, 10, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }
    
    drawZenithIndicator() {
        // Draw center crosshair (true zenith)
        const zenithPos = this.worldToScreen(0, 0);
        
        this.ctx.save();
        this.ctx.strokeStyle = this.config.zenithColor;
        this.ctx.lineWidth = 1;
        this.ctx.globalAlpha = 0.4;
        
        const crossSize = 10;
        this.ctx.beginPath();
        this.ctx.moveTo(zenithPos.x - crossSize, zenithPos.y);
        this.ctx.lineTo(zenithPos.x + crossSize, zenithPos.y);
        this.ctx.moveTo(zenithPos.x, zenithPos.y - crossSize);
        this.ctx.lineTo(zenithPos.x, zenithPos.y + crossSize);
        this.ctx.stroke();
        
        // Label
        this.ctx.fillStyle = this.config.zenithColor;
        this.ctx.font = '10px "Exo 2", sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.globalAlpha = 0.6;
        this.ctx.fillText('Zênite', zenithPos.x, zenithPos.y + 20);
        
        this.ctx.restore();
    }
    
    drawUI() {
        // Zoom indicator
        const zoomPercent = Math.round(this.state.zoom * 100);
        
        this.ctx.save();
        this.ctx.fillStyle = 'rgba(0, 8, 20, 0.8)';
        this.ctx.fillRect(20, this.size - 40, 80, 25);
        
        this.ctx.fillStyle = this.config.textColor;
        this.ctx.font = '12px "Exo 2", sans-serif';
        this.ctx.textAlign = 'center';
        this.ctx.fillText(`Zoom: ${zoomPercent}%`, 60, this.size - 25);
        this.ctx.restore();
        
        // Instructions (fade out after 5 seconds)
        const fadeStart = 3000;
        const fadeDuration = 2000;
        const elapsed = this.state.time;
        
        if (elapsed < fadeStart + fadeDuration) {
            const alpha = elapsed < fadeStart ? 1 : 1 - (elapsed - fadeStart) / fadeDuration;
            
            this.ctx.save();
            this.ctx.globalAlpha = alpha * 0.8;
        this.ctx.fillStyle = this.config.textColor;
            this.ctx.font = '11px "Exo 2", sans-serif';
            this.ctx.textAlign = 'center';
            
            const instructions = this.isMobile() ? 
                'Toque para explorar • Belisque para zoom' : 
                'Clique para explorar • Scroll para zoom';
            
            this.ctx.fillText(instructions, this.center, 30);
            this.ctx.restore();
        }
    }
    
    getStarColor(obj) {
        // Determine color based on spectral type or magnitude
        if (obj.spectral_type) {
            const type = obj.spectral_type.charAt(0).toUpperCase();
            return this.config.starColors[type] || this.config.starColors.G;
        }
        
        // Estimate based on magnitude
        if (obj.magnitude < 0) return this.config.starColors.B;
        if (obj.magnitude < 1) return this.config.starColors.A;
        if (obj.magnitude < 2) return this.config.starColors.F;
        if (obj.magnitude < 3) return this.config.starColors.G;
        if (obj.magnitude < 4) return this.config.starColors.K;
        return this.config.starColors.M;
    }
    
    hexToRgb(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? [
            parseInt(result[1], 16),
            parseInt(result[2], 16),
            parseInt(result[3], 16)
        ] : [255, 255, 255];
    }
    
    showObjectDetails(obj) {
        const event = new CustomEvent('objectSelected', {
            detail: obj
        });
        document.dispatchEvent(event);
    }
    
    isMobile() {
        return window.innerWidth <= 768 || 'ontouchstart' in window;
    }
    
    destroy() {
        if (this.animationFrame) {
            cancelAnimationFrame(this.animationFrame);
        }
        
        // Remove event listeners
        window.removeEventListener('resize', () => this.resizeCanvas());
    }
}

// Initialize the viewer
function initializeModernSkyViewer(canvasId, skyData) {
    return new ModernSkyViewer(canvasId, skyData);
}

// Export for use
window.ModernSkyViewer = ModernSkyViewer;
window.initializeModernSkyViewer = initializeModernSkyViewer; 