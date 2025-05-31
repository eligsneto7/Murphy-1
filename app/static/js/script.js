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