// ===== COSMIC ECHO - JAVASCRIPT INTERACTIONS =====

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
    
    // Animação dos cards de informação
    const infoCards = document.querySelectorAll('.info-card');
    infoCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 500 + (index * 200));
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
        }, 600);
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
    
    // Auto-preenchimento de exemplo (para demonstração)
    setupExampleData();
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
    errorDiv.style.color = '#dc3545';
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
    // Adicionar botão de exemplo (para demonstração)
    const formActions = document.querySelector('.form-actions');
    if (formActions) {
        const exampleButton = document.createElement('button');
        exampleButton.type = 'button';
        exampleButton.className = 'cosmic-button secondary';
        exampleButton.innerHTML = `
            <span class="button-text">USAR DADOS DE EXEMPLO</span>
            <span class="button-accent">DEMONSTRATION MODE</span>
        `;
        exampleButton.style.marginLeft = '1rem';
        
        exampleButton.addEventListener('click', fillExampleData);
        formActions.appendChild(exampleButton);
    }
}

function fillExampleData() {
    const today = new Date();
    const exampleDate = new Date(today.getFullYear() - 25, 5, 15); // 25 anos atrás, 15 de junho
    
    document.getElementById('birth_date').value = exampleDate.toISOString().split('T')[0];
    document.getElementById('birth_time').value = '14:30';
    document.getElementById('city').value = 'São Paulo';
    document.getElementById('country').value = 'Brasil';
    
    showNotification('Dados de exemplo preenchidos!', 'success');
}

// ===== LOADING OVERLAY =====
function showLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    if (overlay) {
        overlay.classList.remove('hidden');
        
        // Adicionar efeitos sonoros simulados (visual)
        simulateLoadingEffects();
    }
}

function hideLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    if (overlay) {
        overlay.classList.add('hidden');
    }
}

function simulateLoadingEffects() {
    const loadingText = document.querySelector('.loading-text p');
    if (!loadingText) return;
    
    const messages = [
        'Analisando as coordenadas do zênite...',
        'Consultando catálogo estelar...',
        'Calculando posições astronômicas...',
        'Identificando estrela relevante...',
        'Preparando visualização cósmica...'
    ];
    
    let messageIndex = 0;
    const messageInterval = setInterval(() => {
        if (messageIndex < messages.length) {
            loadingText.textContent = messages[messageIndex];
            messageIndex++;
        } else {
            clearInterval(messageInterval);
        }
    }, 1500);
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
    showNotification('🌌 MODO CÓSMICO ATIVADO! 🌌', 'success');
    
    // Adicionar efeitos especiais
    document.body.style.animation = 'cosmic-pulse 2s ease-in-out infinite';
    
    // Criar CSS para animação cósmica
    const style = document.createElement('style');
    style.textContent = `
        @keyframes cosmic-pulse {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(180deg); }
        }
    `;
    document.head.appendChild(style);
    
    // Remover efeito após 10 segundos
    setTimeout(() => {
        document.body.style.animation = '';
        style.remove();
    }, 10000);
}

// Inicializar easter eggs
setupEasterEggs();

// ===== PERFORMANCE E OTIMIZAÇÃO =====
function optimizePerformance() {
    // Lazy loading para imagens (se houver)
    const images = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    // Debounce para eventos de scroll
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(handleScroll, 16); // ~60fps
    });
}

function handleScroll() {
    // Efeitos de parallax suaves para as estrelas de fundo
    const scrollY = window.pageYOffset;
    const stars = document.querySelector('.stars');
    const stars2 = document.querySelector('.stars2');
    const stars3 = document.querySelector('.stars3');
    
    if (stars) stars.style.transform = `translateY(${scrollY * 0.1}px)`;
    if (stars2) stars2.style.transform = `translateY(${scrollY * 0.15}px)`;
    if (stars3) stars3.style.transform = `translateY(${scrollY * 0.05}px)`;
}

// Inicializar otimizações
optimizePerformance();

// ===== ACESSIBILIDADE =====
function setupAccessibility() {
    // Navegação por teclado aprimorada
    const focusableElements = document.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    
    focusableElements.forEach(element => {
        element.addEventListener('focus', function() {
            this.style.outline = '2px solid #5DADE2';
            this.style.outlineOffset = '2px';
        });
        
        element.addEventListener('blur', function() {
            this.style.outline = '';
            this.style.outlineOffset = '';
        });
    });
    
    // Suporte a leitores de tela
    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay) {
        loadingOverlay.setAttribute('aria-live', 'polite');
        loadingOverlay.setAttribute('aria-label', 'Calculando eco cósmico');
    }
}

// Inicializar acessibilidade
setupAccessibility();

console.log('🌌 Cosmic Echo initialized successfully! 🌌'); 