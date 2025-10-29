(function() {
  function initOverlayHeader(root) {
    if (!root || root.dataset.mhInit === '1') return;
    root.dataset.mhInit = '1';

    const qs = (sel) => root.querySelector(sel);
    const qsa = (sel) => root.querySelectorAll(sel);

    const hamburger = qs('[class*="main-overlay-header-hamburger-"]') || qs('.main-overlay-header-hamburger');
    const overlay = qs('[class*="main-overlay-header-mobile-overlay-"]') || qs('.main-overlay-header-mobile-overlay');
    const headerContainer = qs('[class*="main-overlay-header-container-"]') || qs('.main-overlay-header-container');
    const mobileNavLinks = qsa('[class*="main-overlay-header-mobile-nav-link-"][data-has-dropdown="true"], .main-overlay-header-mobile-nav-link[data-has-dropdown="true"]');

    function updateOverlayOffset() {
      if (!overlay || !headerContainer) return;
      const rect = headerContainer.getBoundingClientRect();
      const clamped = Math.min(Math.max(rect.bottom, 0), window.innerHeight);
      overlay.style.setProperty('--overlay-offset', clamped + 'px');
    }

    function toggleMobileMenu() {
      if (!hamburger || !overlay) return;
      const isActive = !overlay.classList.contains('active');
      hamburger.classList.toggle('active', isActive);
      overlay.classList.toggle('active', isActive);
      hamburger.setAttribute('aria-expanded', isActive ? 'true' : 'false');
      updateOverlayOffset();
      document.body.style.overflow = isActive ? 'hidden' : '';
    }

    function closeMobileMenu() {
      if (!hamburger || !overlay) return;
      hamburger.classList.remove('active');
      overlay.classList.remove('active');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      updateOverlayOffset();
    }

    function toggleMobileDropdown(link) {
      const dropdown = link.nextElementSibling;
      if (!dropdown) return;
      dropdown.classList.toggle('active');
      link.classList.toggle('active');
      const isOpen = dropdown.classList.contains('active');
      link.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }

    // Events
    if (hamburger && overlay) {
      hamburger.setAttribute('aria-expanded', 'false');
      hamburger.addEventListener('click', toggleMobileMenu);
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) closeMobileMenu();
      });
    }

    mobileNavLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        if (link.dataset.hasDropdown === 'true') {
          e.preventDefault();
          toggleMobileDropdown(link);
        }
      });
      if (link.dataset.hasDropdown === 'true') {
        link.setAttribute('aria-expanded', 'false');
      }
    });

    // Hook our search icon to open the predictive search modal
    const customSearchIcon = qs('[class*="main-overlay-header-search-icon-"]');
    if (customSearchIcon) {
      customSearchIcon.addEventListener('click', (e) => {
        e.preventDefault();
        const searchSummary = document.querySelector('.header__search summary');
        if (searchSummary) {
          searchSummary.click();
        } else {
          window.location.href = (window.routes && window.routes.predictive_search_url) || (customSearchIcon.getAttribute('href') || '/search');
        }
      });
    }

    // Icon gradient interactions
    const iconGradient = qs('[id^="mh-rainbow-icon-gradient-"]') || qs('#mh-rainbow-icon-gradient');
    const headerIcons = Array.from(qsa('[class*="main-overlay-header-icon-"] , .main-overlay-header-icon'));
    if (iconGradient && headerIcons.length) {
      const restartGradient = () => {
        iconGradient.classList.remove('mh-animate');
        void iconGradient.getBoundingClientRect();
        iconGradient.classList.add('mh-animate');
      };
      const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      headerIcons.forEach((icon) => {
        const activate = () => {
          icon.classList.add('mh-rainbow-active');
          if (!prefersReduced) restartGradient();
        };
        const deactivate = () => { icon.classList.remove('mh-rainbow-active'); };
        icon.addEventListener('mouseenter', activate);
        icon.addEventListener('mouseleave', deactivate);
        icon.addEventListener('focus', activate);
        icon.addEventListener('blur', deactivate);
        icon.addEventListener('touchstart', () => { activate(); setTimeout(deactivate, 400); }, { passive: true });
      });
    }

    window.addEventListener('resize', updateOverlayOffset);
    window.addEventListener('scroll', updateOverlayOffset, { passive: true });
    updateOverlayOffset();
  }

  function initAll() {
    document.querySelectorAll('[data-overlay-id]').forEach(initOverlayHeader);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  // Support Shopify theme editor re-renders
  document.addEventListener('shopify:section:load', initAll);
  document.addEventListener('shopify:section:unload', initAll);
})();
