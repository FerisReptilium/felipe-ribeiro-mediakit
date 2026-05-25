document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  // State elements
  const body = document.body;
  const themeToggle = document.getElementById('themeToggle');
  const langToggle = document.getElementById('langToggle');
  const filterTabs = document.querySelectorAll('.filter-tab');
  const skillCards = document.querySelectorAll('.skill-card');
  const toastContainer = document.getElementById('toastContainer');
  
  // Mobile menu elements
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileMenuClose = document.querySelector('.mobile-menu-close');
  const mobileLinks = document.querySelectorAll('.mobile-link');

  /* ==========================================
     THEME TOGGLE SYSTEM
     ========================================== */
  const savedTheme = localStorage.getItem('felipe-theme') || 'dark';
  if (savedTheme === 'light') {
    body.classList.remove('dark-theme');
    body.classList.add('light-theme');
  } else {
    body.classList.add('dark-theme');
    body.classList.remove('light-theme');
  }

  themeToggle.addEventListener('click', () => {
    if (body.classList.contains('dark-theme')) {
      body.classList.remove('dark-theme');
      body.classList.add('light-theme');
      localStorage.setItem('felipe-theme', 'light');
    } else {
      body.classList.remove('light-theme');
      body.classList.add('dark-theme');
      localStorage.setItem('felipe-theme', 'dark');
    }
  });

  /* ==========================================
     LANGUAGE TOGGLE SYSTEM (PT / EN)
     ========================================== */
  const savedLang = localStorage.getItem('felipe-lang') || 'pt';
  if (savedLang === 'en') {
    body.classList.remove('lang-pt');
    body.classList.add('lang-en');
    document.documentElement.lang = 'en';
  } else {
    body.classList.add('lang-pt');
    body.classList.remove('lang-en');
    document.documentElement.lang = 'pt-BR';
  }

  langToggle.addEventListener('click', () => {
    if (body.classList.contains('lang-pt')) {
      body.classList.remove('lang-pt');
      body.classList.add('lang-en');
      document.documentElement.lang = 'en';
      localStorage.setItem('felipe-lang', 'en');
      showToast('Language changed to English!', 'Language changed to English!');
    } else {
      body.classList.remove('lang-en');
      body.classList.add('lang-pt');
      document.documentElement.lang = 'pt-BR';
      localStorage.setItem('felipe-lang', 'pt');
      showToast('Idioma alterado para Português!', 'Idioma alterado para Português!');
    }
  });

  /* ==========================================
     COPY TO CLIPBOARD & TOAST SYSTEM
     ========================================== */
  window.copyContact = function(textToCopy, successMsgPt, successMsgEn) {
    // Copy using Clipboard API
    navigator.clipboard.writeText(textToCopy).then(() => {
      showToast(successMsgPt, successMsgEn);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
      // Fallback
      const textArea = document.createElement('textarea');
      textArea.value = textToCopy;
      textArea.style.position = 'fixed';
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        showToast(successMsgPt, successMsgEn);
      } catch (err2) {
        console.error('Fallback copy failed: ', err2);
      }
      document.body.removeChild(textArea);
    });
  };

  function showToast(msgPt, msgEn) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    
    // Choose translation
    const currentLang = body.classList.contains('lang-en') ? 'en' : 'pt';
    const message = currentLang === 'en' ? msgEn : msgPt;
    
    // Populate
    toast.innerHTML = `
      <i data-lucide="check-circle" style="color: var(--accent-green);"></i>
      <span>${message}</span>
    `;
    
    toastContainer.appendChild(toast);
    
    // Instantiate Lucide inside the new toast
    if (typeof lucide !== 'undefined') {
      lucide.createIcons({
        attrs: {
          class: 'toast-icon'
        },
        nodeList: [toast.querySelector('i')]
      });
    }

    // Auto-remove toast after animation completes (3 seconds)
    setTimeout(() => {
      toast.remove();
    }, 3000);
  }

  /* ==========================================
     TECHNICAL SKILLS FILTERING
     ========================================== */
  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove active from all
      filterTabs.forEach(t => t.classList.remove('active'));
      // Add active to current
      tab.classList.add('active');
      
      const filterValue = tab.getAttribute('data-filter');
      
      skillCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        
        if (filterValue === 'all') {
          card.style.display = 'block';
          // Force reflow and animate in
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else if (cardCategory === filterValue) {
          card.style.display = 'block';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(8px)';
          // Hide after transition
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });

  /* ==========================================
     MOBILE DRAWER MENU ACTIONS
     ========================================== */
  mobileMenuToggle.addEventListener('click', () => {
    mobileMenu.classList.add('active');
  });

  mobileMenuClose.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
  });

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('active');
    });
  });
});
