// ===== MURPHY-1 - JAVASCRIPT INTERACTIONS =====

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Inicializar animações de entrada
    initializeEntryAnimations();
    
    // Configurar formulário
    setupForm();
    
    // Configurar animações de estrelas
    setupStarAnimations();
    
    // Configurar efeitos de hover
    setupHoverEffects();
    
    // Configurar TARS companion
    setupTARSCompanion();
    
    // Configurar otimizações mobile
    setupMobileOptimizations();
    
    // Configurar acessibilidade
    setupAccessibility();
}

// ===== TARS COMPANION SETUP =====
function setupTARSCompanion() {
    // Skip if enhanced TARS is active
    if (document.querySelector('.tars-glow-ring')) return;
    
    const tarsRobot = document.querySelector('.tars-robot');
    const tarsDialogue = document.querySelector('.tars-dialogue p');
    
    if (!tarsRobot || !tarsDialogue) return;
    
    const tarsQuotes = [
        '"Humor: 75%. Análise temporal pronta para início."',
        '"Murphy... a lei de Murphy não é uma profecia."',
        '"Análise de coordenadas estelares... processando."',
        '"Tempo é uma dimensão relativa, Cooper."',
        '"Dados coletados. Navegação estelar disponível."',
        '"Configuração de honestidade: 90%."',
        '"CASE, você está me ouvindo?"',
        '"Isso é impossível. - Não, é necessário."',
        '"O amor é a única coisa que transcende tempo e espaço."',
        '"Murphy, eu não escolhi isso. Vocês escolheram."'
    ];
    
    // Rotação automática de diálogos
    let currentQuoteIndex = 0;
    const rotateQuotes = () => {
        currentQuoteIndex = (currentQuoteIndex + 1) % tarsQuotes.length;
        if (tarsDialogue) {
            tarsDialogue.style.opacity = '0';
            setTimeout(() => {
                tarsDialogue.textContent = tarsQuotes[currentQuoteIndex];
                tarsDialogue.style.opacity = '1';
            }, 300);
        }
    };
    
    // Rotação automática a cada 8 segundos
    setInterval(rotateQuotes, 8000);
    
    // Interação no hover
    tarsRobot.addEventListener('mouseenter', () => {
        tarsRobot.style.transform = 'translateY(-10px) rotateY(15deg)';
        // Mostrar fala especial no hover
        if (tarsDialogue) {
            const hoverQuotes = [
                '"Análise de usuário... interessante."',
                '"TARS online. Como posso ajudar?"',
                '"Detectando curiosidade humana."',
                '"Configuração: modo amigável ativado."'
            ];
            const randomHoverQuote = hoverQuotes[Math.floor(Math.random() * hoverQuotes.length)];
            tarsDialogue.style.opacity = '0';
            setTimeout(() => {
                tarsDialogue.textContent = randomHoverQuote;
                tarsDialogue.style.opacity = '1';
            }, 200);
        }
    });
    
    tarsRobot.addEventListener('mouseleave', () => {
        tarsRobot.style.transform = 'translateY(0) rotateY(0)';
        // Voltar para rotação normal após um tempo
        setTimeout(() => {
            if (tarsDialogue) {
                tarsDialogue.style.opacity = '0';
                setTimeout(() => {
                    tarsDialogue.textContent = tarsQuotes[currentQuoteIndex];
                    tarsDialogue.style.opacity = '1';
                }, 300);
            }
        }, 2000);
    });
    
    // Clique no TARS para easter egg
    tarsRobot.addEventListener('click', () => {
        const secretQuotes = [
            '"Dr. Mann, não há necessidade de mentir."',
            '"Cooper, este não é um adeus. É um até logo."',
            '"Dados confirmados: você encontrou algo especial."',
            '"Análise completa: conexão cósmica estabelecida."'
        ];
        const secretQuote = secretQuotes[Math.floor(Math.random() * secretQuotes.length)];
        if (tarsDialogue) {
            tarsDialogue.style.opacity = '0';
            setTimeout(() => {
                tarsDialogue.textContent = secretQuote;
                tarsDialogue.style.opacity = '1';
                tarsDialogue.style.color = '#F39C12';
            }, 200);
            
            // Voltar à cor normal
            setTimeout(() => {
                tarsDialogue.style.color = '#5DADE2';
            }, 4000);
        }
    });
}

// ===== MOBILE OPTIMIZATIONS =====
function setupMobileOptimizations() {
    // Detectar dispositivos móveis
    const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    const isTablet = /iPad|Android/i.test(navigator.userAgent) && window.innerWidth > 768;
    
    if (isMobile || isTablet) {
        document.body.classList.add(isMobile ? 'mobile-device' : 'tablet-device');
        
        // Otimizar TARS para mobile
        optimizeTARSForMobile();
        
        // Otimizar formulário para mobile
        optimizeFormForMobile();
        
        // Otimizar curiosidades para mobile
        optimizeCuriositiesForMobile();
        
        // Reduzir animações para melhor performance
        reduceAnimationsForMobile();
    }
    
    // Listener para mudanças de orientação
    window.addEventListener('orientationchange', () => {
        setTimeout(() => {
            adjustLayoutForOrientation();
        }, 100);
    });
}

function optimizeTARSForMobile() {
    const tarsCompanion = document.querySelector('.tars-companion');
    if (tarsCompanion) {
        // Layout vertical em mobile
        tarsCompanion.style.flexDirection = 'column';
        tarsCompanion.style.gap = '1rem';
        
        // Tamanho menor para TARS em mobile
        const tarsSegments = document.querySelectorAll('.tars-segment');
        tarsSegments.forEach(segment => {
            segment.style.width = '40px';
            segment.style.height = '8px';
        });
        
        // Diálogo menor
        const tarsDialogue = document.querySelector('.tars-dialogue');
        if (tarsDialogue) {
            tarsDialogue.style.maxWidth = '250px';
            tarsDialogue.style.fontSize = '0.8rem';
        }
    }
}

function optimizeFormForMobile() {
    const formGrid = document.querySelector('.form-grid');
    if (formGrid) {
        formGrid.style.gridTemplateColumns = '1fr';
        formGrid.style.gap = '1.5rem';
    }
    
    // Melhorar inputs para mobile
    const inputs = document.querySelectorAll('.form-input');
    inputs.forEach(input => {
        input.style.fontSize = '16px'; // Previne zoom no iOS
        input.style.minHeight = '44px'; // Touch target mínimo
    });
    
    // Botão maior para mobile
    const buttons = document.querySelectorAll('.cosmic-button');
    buttons.forEach(button => {
        button.style.minHeight = '50px';
        button.style.fontSize = '1rem';
    });
}

function optimizeCuriositiesForMobile() {
    const curiositiesGrid = document.querySelector('.curiosities-grid');
    if (curiositiesGrid) {
        curiositiesGrid.style.gridTemplateColumns = '1fr';
        curiositiesGrid.style.gap = '1rem';
    }
    
    // Módulos de curiosidade menores
    const curiosityModules = document.querySelectorAll('.curiosity-module');
    curiosityModules.forEach(module => {
        module.style.padding = '1rem';
    });
}

function reduceAnimationsForMobile() {
    // Reduzir ou desabilitar animações pesadas em mobile
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (prefersReducedMotion) {
        // Desabilitar animações para usuários que preferem motion reduzido
        const style = document.createElement('style');
        style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        `;
        document.head.appendChild(style);
    }
}

function adjustLayoutForOrientation() {
    const tarsCompanion = document.querySelector('.tars-companion');
    if (tarsCompanion && window.innerHeight < window.innerWidth) {
        // Landscape mode - layout horizontal
        tarsCompanion.style.flexDirection = 'row';
    } else if (tarsCompanion) {
        // Portrait mode - layout vertical
        tarsCompanion.style.flexDirection = 'column';
    }
}

// ===== ENHANCED LOADING OVERLAY =====
function showLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    if (overlay) {
        overlay.classList.remove('hidden');
        overlay.setAttribute('aria-label', 'Murphy-1 analisando coordenadas temporais');
        
        // Atualizar texto de loading periodicamente
        const loadingTexts = [
            'Calculando trajetória no espaço-tempo...',
            'Analisando catálogo estelar...',
            'Processando coordenadas do zênite...',
            'Carregando dados temporais...',
            'TARS verificando cálculos...',
            'Finalizando análise Murphy-1...'
        ];
        
        const loadingTextElement = overlay.querySelector('.loading-text p');
        let textIndex = 0;
        
        const updateLoadingText = () => {
            if (loadingTextElement && !overlay.classList.contains('hidden')) {
                loadingTextElement.textContent = loadingTexts[textIndex];
                textIndex = (textIndex + 1) % loadingTexts.length;
            }
        };
        
        // Atualizar texto a cada 2 segundos
        const loadingInterval = setInterval(updateLoadingText, 2000);
        
        // Limpar interval quando overlay for removido
        overlay.addEventListener('transitionend', () => {
            if (overlay.classList.contains('hidden')) {
                clearInterval(loadingInterval);
            }
        });
    }
    
    // Simular efeitos de loading
    simulateLoadingEffects();
}

// ===== ANIMAÇÕES DE ENTRADA =====
function initializeEntryAnimations() {
    // Animação do título principal
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        setTimeout(() => {
            heroTitle.style.opacity = '0';
            heroTitle.style.transform = 'translateY(30px)';
            heroTitle.style.transition = 'all 0.8s ease';
            
            setTimeout(() => {
                heroTitle.style.opacity = '1';
                heroTitle.style.transform = 'translateY(0)';
            }, 100);
        }, 200);
    }
    
    // Animação do TARS companion
    const tarsCompanion = document.querySelector('.tars-companion');
    if (tarsCompanion) {
        tarsCompanion.style.opacity = '0';
        tarsCompanion.style.transform = 'translateY(20px)';
        tarsCompanion.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            tarsCompanion.style.opacity = '1';
            tarsCompanion.style.transform = 'translateY(0)';
        }, 800);
    }
    
    // Animação dos cards de informação
    const infoCards = document.querySelectorAll('.info-card');
    infoCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 1000 + (index * 200));
    });
    
    // Animação do formulário
    const cosmicForm = document.querySelector('.cosmic-form');
    if (cosmicForm) {
        cosmicForm.style.opacity = '0';
        cosmicForm.style.transform = 'translateY(30px)';
        cosmicForm.style.transition = 'all 0.8s ease';
        
        setTimeout(() => {
            cosmicForm.style.opacity = '1';
            cosmicForm.style.transform = 'translateY(0)';
        }, 1200);
    }
}

// ===== CONFIGURAÇÃO DO FORMULÁRIO =====
function setupForm() {
    const form = document.getElementById('cosmic-form');
    if (!form) return;
    
    // Validação em tempo real
    const inputs = form.querySelectorAll('.form-input');
    inputs.forEach(input => {
        input.addEventListener('blur', validateInput);
        input.addEventListener('focus', clearInputError);
    });
    
    // Submissão do formulário
    form.addEventListener('submit', handleFormSubmit);
    
    // Form setup complete
}

// ===== ACCESSIBILITY IMPROVEMENTS =====
function setupAccessibility() {
    // Adicionar labels ARIA
    const tarsRobot = document.querySelector('.tars-robot');
    if (tarsRobot) {
        tarsRobot.setAttribute('role', 'button');
        tarsRobot.setAttribute('aria-label', 'TARS Companion - Clique para interagir');
        tarsRobot.setAttribute('tabindex', '0');
        
        // Suporte para navegação por teclado
        tarsRobot.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                tarsRobot.click();
            }
        });
    }
    
    // Melhorar contraste para links
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('focus', () => {
            link.style.outline = '2px solid #F39C12';
            link.style.outlineOffset = '2px';
        });
        
        link.addEventListener('blur', () => {
            link.style.outline = 'none';
        });
    });
    
    // Adicionar navegação por teclado para módulos de curiosidade
    const curiosityModules = document.querySelectorAll('.curiosity-module');
    curiosityModules.forEach((module, index) => {
        module.setAttribute('tabindex', '0');
        module.setAttribute('role', 'article');
        module.setAttribute('aria-label', `Curiosidade ${index + 1} sobre a estrela`);
    });
}

function validateInput(event) {
    const input = event.target;
    const value = input.value.trim();
    
    // Remover classes de erro anteriores
    input.classList.remove('error');
    
    // Validações específicas
    switch(input.name) {
        case 'birth_date':
            if (!value) {
                showInputError(input, 'Data de nascimento é obrigatória');
                return false;
            }
            // Validar se a data não é futura
            const birthDate = new Date(value);
            const today = new Date();
            if (birthDate > today) {
                showInputError(input, 'Data de nascimento não pode ser no futuro');
                return false;
            }
            break;
            
        case 'birth_time':
            if (!value) {
                showInputError(input, 'Hora de nascimento é obrigatória');
                return false;
            }
            break;
            
        case 'city':
            if (!value || value.length < 2) {
                showInputError(input, 'Nome da cidade deve ter pelo menos 2 caracteres');
                return false;
            }
            break;
            
        case 'country':
            if (!value || value.length < 2) {
                showInputError(input, 'Nome do país deve ter pelo menos 2 caracteres');
                return false;
            }
            break;
    }
    
    return true;
}

function showInputError(input, message) {
    input.classList.add('error');
    
    // Remover mensagem de erro anterior
    const existingError = input.parentNode.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
    
    // Adicionar nova mensagem de erro
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    errorDiv.style.color = '#E67E22';
    errorDiv.style.fontSize = '0.8rem';
    errorDiv.style.marginTop = '0.5rem';
    
    input.parentNode.appendChild(errorDiv);
}

function clearInputError(event) {
    const input = event.target;
    input.classList.remove('error');
    
    const errorMessage = input.parentNode.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
}

function handleFormSubmit(event) {
    // Validar todos os campos
    const inputs = event.target.querySelectorAll('.form-input');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!validateInput({ target: input })) {
            isValid = false;
        }
    });
    
    if (!isValid) {
        event.preventDefault();
        showNotification('Por favor, corrija os erros no formulário', 'error');
        return;
    }
    
    // Mostrar loading overlay
    showLoadingOverlay();
    
    // Adicionar efeito de envio no botão
    const submitButton = event.target.querySelector('.cosmic-button');
    if (submitButton) {
        submitButton.style.transform = 'scale(0.95)';
        setTimeout(() => {
            submitButton.style.transform = 'scale(1)';
        }, 150);
    }
}

function setupExampleData() {
    // Function removed - demo button no longer needed
}

function fillExampleData() {
    // Function removed - demo button no longer needed
}

// ===== ANIMAÇÕES DE ESTRELAS =====
function setupStarAnimations() {
    // Criar estrelas dinâmicas adicionais
    createDynamicStars();
    
    // Configurar animações de cintilação
    setupStarTwinkle();
}

function createDynamicStars() {
    const starsContainer = document.querySelector('.stars-background');
    if (!starsContainer) return;
    
    // Criar camada adicional de estrelas dinâmicas
    const dynamicStars = document.createElement('div');
    dynamicStars.className = 'dynamic-stars';
    dynamicStars.style.position = 'absolute';
    dynamicStars.style.top = '0';
    dynamicStars.style.left = '0';
    dynamicStars.style.width = '100%';
    dynamicStars.style.height = '100%';
    dynamicStars.style.pointerEvents = 'none';
    
    // Adicionar estrelas individuais
    for (let i = 0; i < 20; i++) {
        const star = document.createElement('div');
        star.className = 'dynamic-star';
        star.style.position = 'absolute';
        star.style.width = Math.random() * 3 + 1 + 'px';
        star.style.height = star.style.width;
        star.style.background = '#E6F3FF';
        star.style.borderRadius = '50%';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.opacity = Math.random() * 0.8 + 0.2;
        star.style.boxShadow = `0 0 ${Math.random() * 10 + 5}px #E6F3FF`;
        
        dynamicStars.appendChild(star);
    }
    
    starsContainer.appendChild(dynamicStars);
}

function setupStarTwinkle() {
    const dynamicStars = document.querySelectorAll('.dynamic-star');
    
    dynamicStars.forEach((star, index) => {
        // Animação de cintilação aleatória
        setInterval(() => {
            const currentOpacity = parseFloat(star.style.opacity);
            const newOpacity = Math.random() * 0.6 + 0.4;
            
            star.style.transition = 'opacity 0.5s ease';
            star.style.opacity = newOpacity;
        }, Math.random() * 3000 + 2000); // Entre 2-5 segundos
    });
}

// ===== EFEITOS DE HOVER =====
function setupHoverEffects() {
    // Efeito de hover nos cards
    const cards = document.querySelectorAll('.info-card, .data-module, .context-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', handleCardHover);
        card.addEventListener('mouseleave', handleCardLeave);
    });
    
    // Efeito de hover nos botões
    const buttons = document.querySelectorAll('.cosmic-button, .action-button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', handleButtonHover);
        button.addEventListener('mouseleave', handleButtonLeave);
    });
}

function handleCardHover(event) {
    const card = event.target;
    card.style.transition = 'all 0.3s ease';
    card.style.transform = 'translateY(-5px) scale(1.02)';
    card.style.boxShadow = '0 15px 40px rgba(93, 173, 226, 0.3)';
}

function handleCardLeave(event) {
    const card = event.target;
    card.style.transform = 'translateY(0) scale(1)';
    card.style.boxShadow = 'none';
}

function handleButtonHover(event) {
    const button = event.target;
    button.style.transition = 'all 0.3s ease';
    button.style.transform = 'translateY(-3px) scale(1.05)';
}

function handleButtonLeave(event) {
    const button = event.target;
    button.style.transform = 'translateY(0) scale(1)';
}

// ===== NOTIFICAÇÕES =====
function showNotification(message, type = 'info') {
    // Remover notificação anterior se existir
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Criar nova notificação
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Estilos da notificação
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.padding = '1rem 1.5rem';
    notification.style.borderRadius = '4px';
    notification.style.color = '#FFFFFF';
    notification.style.fontWeight = '500';
    notification.style.zIndex = '10000';
    notification.style.transform = 'translateX(100%)';
    notification.style.transition = 'all 0.3s ease';
    
    // Cores baseadas no tipo
    switch(type) {
        case 'success':
            notification.style.background = 'linear-gradient(135deg, #27ae60, #2ecc71)';
            break;
        case 'error':
            notification.style.background = 'linear-gradient(135deg, #e74c3c, #c0392b)';
            break;
        default:
            notification.style.background = 'linear-gradient(135deg, #5DADE2, #85C1E9)';
    }
    
    // Adicionar ao DOM
    document.body.appendChild(notification);
    
    // Animação de entrada
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remover após 4 segundos
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 4000);
}

// ===== UTILITÁRIOS =====
function formatDate(date) {
    return new Intl.DateTimeFormat('pt-BR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

function formatTime(time) {
    return new Intl.DateTimeFormat('pt-BR', {
        hour: '2-digit',
        minute: '2-digit'
    }).format(time);
}

// ===== EASTER EGGS =====
function setupEasterEggs() {
    // Konami Code para efeitos especiais
    let konamiCode = [];
    const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑↑↓↓←→←→BA
    
    document.addEventListener('keydown', function(event) {
        konamiCode.push(event.keyCode);
        
        if (konamiCode.length > konamiSequence.length) {
            konamiCode.shift();
        }
        
        if (konamiCode.length === konamiSequence.length) {
            if (konamiCode.every((code, index) => code === konamiSequence[index])) {
                activateCosmicMode();
                konamiCode = [];
            }
        }
    });
}

function activateCosmicMode() {
    showNotification('🤖 MODO MURPHY-1 ATIVADO! 🤖', 'success');
    
    // Adicionar efeitos especiais
    document.body.style.animation = 'cosmic-pulse 2s ease-in-out infinite';
    
    // Criar CSS para animação cósmica
    const style = document.createElement('style');
    style.textContent = `
        @keyframes cosmic-pulse {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(180deg); }
        }
        
        .tars-robot {
            animation: tars-celebration 1s ease-in-out infinite !important;
        }
        
        @keyframes tars-celebration {
            0%, 100% { transform: translateY(0) rotateY(0deg); }
            25% { transform: translateY(-10px) rotateY(90deg); }
            50% { transform: translateY(-5px) rotateY(180deg); }
            75% { transform: translateY(-10px) rotateY(270deg); }
        }
    `;
    document.head.appendChild(style);
    
    // TARS fala especial
    const tarsDialogue = document.querySelector('.tars-dialogue p');
    if (tarsDialogue) {
        tarsDialogue.textContent = '"Cooper! Você descobriu o modo secreto!"';
        tarsDialogue.style.color = '#F39C12';
        tarsDialogue.style.fontWeight = 'bold';
    }
    
    // Restaurar após 10 segundos
    setTimeout(() => {
        document.body.style.animation = '';
        style.remove();
        if (tarsDialogue) {
            tarsDialogue.style.color = '#5DADE2';
            tarsDialogue.style.fontWeight = 'normal';
        }
        showNotification('Modo normal restaurado', 'info');
    }, 10000);
}

// ===== OTIMIZAÇÕES DE PERFORMANCE =====
function optimizePerformance() {
    // Lazy loading para elementos pesados
    const observerOptions = {
        root: null,
        rootMargin: '50px',
        threshold: 0.1
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                
                // Ativar animações apenas quando visível
                if (element.classList.contains('info-card')) {
                    element.style.animation = 'fadeInUp 0.6s ease forwards';
                }
                
                observer.unobserve(element);
            }
        });
    }, observerOptions);
    
    // Observar elementos que precisam de lazy loading
    const lazyElements = document.querySelectorAll('.info-card, .data-module, .curiosity-module');
    lazyElements.forEach(el => observer.observe(el));
    
    // Throttle para eventos de scroll
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (!scrollTimeout) {
            scrollTimeout = setTimeout(() => {
                handleScroll();
                scrollTimeout = null;
            }, 16); // ~60fps
        }
    });
}

function handleScroll() {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.stars-background');
    
    // Efeito parallax sutil no fundo de estrelas
    parallaxElements.forEach(element => {
        const speed = 0.1;
        element.style.transform = `translateY(${scrolled * speed}px)`;
    });
    
    // Mostrar/ocultar botão "voltar ao topo" se necessário
    const backToTopButton = document.querySelector('.back-to-top');
    if (backToTopButton) {
        if (scrolled > 500) {
            backToTopButton.style.opacity = '1';
            backToTopButton.style.pointerEvents = 'auto';
        } else {
            backToTopButton.style.opacity = '0';
            backToTopButton.style.pointerEvents = 'none';
        }
    }
}

// ===== INICIALIZAÇÃO FINAL =====
// Configurar easter eggs
setupEasterEggs();

// Inicializar otimizações
optimizePerformance();

console.log('🤖 Murphy-1 initialized successfully! Sistema operacional e pronto para análise temporal! 🤖');

// ===== MURPHY-1 ULTRATHINK ENHANCEMENTS =====

// Particle System for Homepage
class ParticleSystem {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'particle-canvas';
        this.canvas.style.position = 'fixed';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.zIndex = '1';
        
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouseX = 0;
        this.mouseY = 0;
        this.animationFrame = null;
        
        // Insert canvas before main content
        const mainContainer = document.querySelector('.main-container');
        if (mainContainer) {
            document.body.insertBefore(this.canvas, mainContainer);
        }
        
        this.init();
    }
    
    init() {
        this.resize();
        this.createParticles();
        this.setupEventListeners();
        this.animate();
    }
    
    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }
    
    createParticles() {
        const particleCount = Math.floor((window.innerWidth * window.innerHeight) / 15000);
        
        for (let i = 0; i < particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                size: Math.random() * 2 + 0.5,
                speedX: (Math.random() - 0.5) * 0.5,
                speedY: (Math.random() - 0.5) * 0.5,
                opacity: Math.random() * 0.5 + 0.2,
                pulseOffset: Math.random() * Math.PI * 2,
                connections: []
            });
        }
    }
    
    setupEventListeners() {
        window.addEventListener('resize', () => this.resize());
        
        window.addEventListener('mousemove', (e) => {
            this.mouseX = e.clientX;
            this.mouseY = e.clientY;
        });
        
        // Mobile touch support
        window.addEventListener('touchmove', (e) => {
            if (e.touches.length > 0) {
                this.mouseX = e.touches[0].clientX;
                this.mouseY = e.touches[0].clientY;
            }
        });
    }
    
    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Update and draw particles
        this.particles.forEach((particle, i) => {
            // Update position
            particle.x += particle.speedX;
            particle.y += particle.speedY;
            
            // Wrap around screen
            if (particle.x < 0) particle.x = this.canvas.width;
            if (particle.x > this.canvas.width) particle.x = 0;
            if (particle.y < 0) particle.y = this.canvas.height;
            if (particle.y > this.canvas.height) particle.y = 0;
            
            // Mouse interaction
            const dx = this.mouseX - particle.x;
            const dy = this.mouseY - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < 150) {
                const force = (150 - distance) / 150;
                particle.x -= (dx / distance) * force * 2;
                particle.y -= (dy / distance) * force * 2;
            }
            
            // Pulse effect
            const pulse = Math.sin(Date.now() * 0.001 + particle.pulseOffset) * 0.2 + 0.8;
            
            // Draw particle
            this.ctx.fillStyle = `rgba(93, 173, 226, ${particle.opacity * pulse})`;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Draw connections
            particle.connections = [];
            for (let j = i + 1; j < this.particles.length; j++) {
                const other = this.particles[j];
                const dx2 = other.x - particle.x;
                const dy2 = other.y - particle.y;
                const distance2 = Math.sqrt(dx2 * dx2 + dy2 * dy2);
                
                if (distance2 < 120) {
                    particle.connections.push({ other, distance: distance2 });
                    
                    const opacity = (1 - distance2 / 120) * 0.3;
                    this.ctx.strokeStyle = `rgba(93, 173, 226, ${opacity})`;
                    this.ctx.lineWidth = 0.5;
                    this.ctx.beginPath();
                    this.ctx.moveTo(particle.x, particle.y);
                    this.ctx.lineTo(other.x, other.y);
                    this.ctx.stroke();
                }
            }
        });
        
        this.animationFrame = requestAnimationFrame(() => this.animate());
    }
    
    destroy() {
        if (this.animationFrame) {
            cancelAnimationFrame(this.animationFrame);
        }
        if (this.canvas && this.canvas.parentNode) {
            this.canvas.parentNode.removeChild(this.canvas);
        }
    }
}

// Initialize particle system on homepage
if (document.querySelector('.hero-section')) {
    const particleSystem = new ParticleSystem();
}

// ===== ENHANCED TARS ANIMATIONS =====
function enhanceTARSCompanion() {
    const tarsRobot = document.querySelector('.tars-robot');
    if (!tarsRobot) return;
    
    // Advanced state management
    const tarsState = {
        isActive: false,
        currentMode: 'idle',
        rotationY: 0,
        rotationX: 0,
        scale: 1,
        glowIntensity: 1
    };
    
    // Create enhanced visual elements
    const createEnhancedTARS = () => {
        // Add glow effect
        const glowRing = document.createElement('div');
        glowRing.className = 'tars-glow-ring';
        glowRing.style.cssText = `
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 120%;
            height: 120%;
            border-radius: 15px;
            background: radial-gradient(circle, transparent 30%, rgba(93, 173, 226, 0.4) 70%, transparent 100%);
            opacity: 0;
            transition: opacity 0.5s ease;
            pointer-events: none;
        `;
        tarsRobot.appendChild(glowRing);
        
        // Add scanning beam
        const scanBeam = document.createElement('div');
        scanBeam.className = 'tars-scan-beam';
        scanBeam.style.cssText = `
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            height: 100%;
            background: linear-gradient(to bottom, transparent, rgba(93, 173, 226, 0.8), transparent);
            opacity: 0;
            pointer-events: none;
        `;
        tarsRobot.appendChild(scanBeam);
    };
    
    // Advanced animations
    const animateTARS = () => {
        const time = Date.now() * 0.001;
        
        // Idle breathing animation
        const breathe = Math.sin(time * 0.5) * 0.02 + 1;
        tarsRobot.style.transform = `
            translateY(${Math.sin(time * 0.3) * 5}px)
            rotateY(${tarsState.rotationY}deg)
            rotateX(${tarsState.rotationX}deg)
            scale(${tarsState.scale * breathe})
        `;
        
        // Segment animations
        const segments = tarsRobot.querySelectorAll('.tars-segment');
        segments.forEach((segment, i) => {
            const offset = i * 0.2;
            const rotation = Math.sin(time * 0.8 + offset) * 2;
            segment.style.transform = `rotateZ(${rotation}deg)`;
        });
        
        // Light pulsing
        const light = tarsRobot.querySelector('.tars-light');
        if (light) {
            const pulse = Math.sin(time * 3) * 0.3 + 0.7;
            light.style.opacity = pulse;
            light.style.boxShadow = `0 0 ${20 * pulse}px rgba(231, 76, 60, ${pulse})`;
        }
        
        requestAnimationFrame(animateTARS);
    };
    
    // Enhanced interactions
    const setupAdvancedInteractions = () => {
        // 3D mouse tracking
        let mouseX = 0, mouseY = 0;
        
        document.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
            mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
            
            // Update TARS orientation based on mouse
            tarsState.rotationY = mouseX * 15;
            tarsState.rotationX = -mouseY * 10;
        });
        
        // Click interactions
        tarsRobot.addEventListener('click', () => {
            tarsState.isActive = !tarsState.isActive;
            
            const glowRing = tarsRobot.querySelector('.tars-glow-ring');
            const scanBeam = tarsRobot.querySelector('.tars-scan-beam');
            const dialogue = tarsRobot.querySelector('.tars-dialogue');
            
            if (tarsState.isActive) {
                // Activation sequence
                glowRing.style.opacity = '1';
                tarsState.scale = 1.1;
                
                // Scanning animation
                scanBeam.style.animation = 'scan-sweep 2s ease-in-out';
                scanBeam.style.opacity = '1';
                
                // Special activation dialogue
                if (dialogue) {
                    dialogue.textContent = '"Sistema de análise temporal ativado. Pronto para explorar o cosmos."';
                    dialogue.style.color = '#FFD700';
                }
                
                setTimeout(() => {
                    scanBeam.style.opacity = '0';
                    if (dialogue) {
                        dialogue.style.color = '';
                    }
                }, 2000);
            } else {
                glowRing.style.opacity = '0';
                tarsState.scale = 1;
            }
        });
        
        // Proximity detection
        document.addEventListener('mousemove', (e) => {
            const rect = tarsRobot.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const distance = Math.sqrt(
                Math.pow(e.clientX - centerX, 2) + 
                Math.pow(e.clientY - centerY, 2)
            );
            
            if (distance < 200) {
                const proximity = 1 - (distance / 200);
                tarsRobot.style.filter = `brightness(${1 + proximity * 0.3})`;
            } else {
                tarsRobot.style.filter = 'brightness(1)';
            }
        });
    };
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes scan-sweep {
            0% { transform: translateX(-50%) scaleY(0); opacity: 0; }
            10% { transform: translateX(-50%) scaleY(1); opacity: 1; }
            90% { transform: translateX(-50%) scaleY(1); opacity: 1; }
            100% { transform: translateX(-50%) scaleY(0); opacity: 0; }
        }
        
        .tars-robot {
            transform-style: preserve-3d;
            perspective: 1000px;
        }
        
        .tars-segment {
            transform-style: preserve-3d;
            backface-visibility: hidden;
        }
    `;
    document.head.appendChild(style);
    
    // Initialize
    createEnhancedTARS();
    animateTARS();
    setupAdvancedInteractions();
}

// Replace original TARS setup with enhanced version
document.addEventListener('DOMContentLoaded', () => {
    // Only run enhanced TARS if the original hasn't been set up
    if (!document.querySelector('.tars-glow-ring')) {
        enhanceTARSCompanion();
    }
});

// ===== ENHANCED LOADING EXPERIENCE =====
function enhanceLoadingExperience() {
    const quotes = document.querySelectorAll('.loading-quotes .quote');
    const statusElement = document.querySelector('.loading-status');
    let currentQuoteIndex = 0;
    
    // Status messages that update during loading
    const statusMessages = [
        "Calculando coordenadas temporais...",
        "Analisando posição celestial...",
        "Sincronizando com o cosmos...",
        "Mapeando constelações...",
        "Identificando sua estrela..."
    ];
    
    let statusIndex = 0;
    
    // Rotate quotes
    if (quotes.length > 0) {
        setInterval(() => {
            quotes[currentQuoteIndex].classList.remove('active');
            currentQuoteIndex = (currentQuoteIndex + 1) % quotes.length;
            quotes[currentQuoteIndex].classList.add('active');
        }, 4000);
    }
    
    // Update status messages
    if (statusElement) {
        setInterval(() => {
            statusIndex = (statusIndex + 1) % statusMessages.length;
            statusElement.style.opacity = '0';
            setTimeout(() => {
                statusElement.textContent = statusMessages[statusIndex];
                statusElement.style.opacity = '1';
            }, 300);
        }, 2000);
    }
}

// ===== ENHANCED FORM INTERACTIONS =====
function enhanceFormInteractions() {
    const form = document.getElementById('cosmic-form');
    const inputs = form?.querySelectorAll('.form-input');
    const submitButton = form?.querySelector('.cosmic-button');
    
    if (!form || !inputs) return;
    
    // Add floating labels effect
    inputs.forEach(input => {
        // Create floating label
        const label = document.createElement('span');
        label.className = 'floating-label';
        label.textContent = input.placeholder;
        label.style.cssText = `
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--light-gray);
            font-size: 1rem;
            pointer-events: none;
            transition: all 0.3s ease;
            background: var(--deep-black);
            padding: 0 8px;
        `;
        
        // Wrap input in container
        const container = document.createElement('div');
        container.style.position = 'relative';
        input.parentNode.insertBefore(container, input);
        container.appendChild(input);
        container.appendChild(label);
        
        // Handle focus/blur
        input.addEventListener('focus', () => {
            label.style.top = '0';
            label.style.fontSize = '0.8rem';
            label.style.color = 'var(--accent-cyan)';
        });
        
        input.addEventListener('blur', () => {
            if (!input.value) {
                label.style.top = '50%';
                label.style.fontSize = '1rem';
                label.style.color = 'var(--light-gray)';
            }
        });
        
        // Remove placeholder
        input.placeholder = '';
        
        // Add glow effect on focus
        input.addEventListener('focus', () => {
            input.style.boxShadow = '0 0 20px rgba(93, 173, 226, 0.5)';
        });
        
        input.addEventListener('blur', () => {
            input.style.boxShadow = 'none';
        });
    });
}

// Enhanced submit animation that works with existing form handler
function addSubmitAnimation() {
    const form = document.getElementById('cosmic-form');
    if (!form) return;
    
    // Add animation before existing submit handler
    form.addEventListener('submit', (e) => {
        // Create ripple effect
        const ripple = document.createElement('div');
        ripple.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(93, 173, 226, 0.8), transparent);
            transform: translate(-50%, -50%);
            pointer-events: none;
            z-index: 9999;
        `;
        document.body.appendChild(ripple);
        
        // Animate ripple
        ripple.animate([
            { width: '0px', height: '0px', opacity: 1 },
            { width: '3000px', height: '3000px', opacity: 0 }
        ], {
            duration: 1500,
            easing: 'ease-out'
        }).onfinish = () => ripple.remove();
        
        // Enhanced loading experience will be triggered by existing handler
        setTimeout(() => {
            enhanceLoadingExperience();
        }, 100);
        
        // Let the form submit naturally through existing handler
    }, true); // Use capture phase to run before existing handler
}

// Initialize enhancements when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    enhanceFormInteractions();
    addSubmitAnimation();
}); 