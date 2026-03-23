# -*- coding: utf-8 -*-
{
    'name': 'Modern Theme - Backend UI',
    'version': '16.0.1.0.0',
    'summary': 'Tema visual moderno para o backend Odoo 16 Community',
    'author': 'My Company',
    'category': 'Themes/Backend',
    'depends': ['web'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        # ── BUNDLE 1 ────────────────────────────────────────────────
        # web._assets_primary_variables
        # Documentação oficial: variáveis Odoo que ficam disponíveis
        # em TODOS os bundles. Carregado com 'prepend' para entrar
        # ANTES das variáveis padrão do Odoo (que usam !default).
        # REGRA: ZERO CSS, ZERO @import url() — só $variáveis SCSS.
        'web._assets_primary_variables': [
            ('prepend', 'my_theme/static/src/scss/01_primary_variables.scss'),
        ],

        # ── BUNDLE 2 ────────────────────────────────────────────────
        # web._assets_backend_helpers
        # Documentação oficial: variáveis e mixins disponíveis APENAS
        # no bundle de backend. Lugar correto para overrides Bootstrap.
        # REGRA: ZERO CSS — só variáveis Bootstrap ($font-*, etc.).
        'web._assets_backend_helpers': [
            ('prepend', 'my_theme/static/src/scss/02_bootstrap_overrides.scss'),
        ],

        # ── BUNDLE 3 ────────────────────────────────────────────────
        # web.assets_backend
        # Aqui vai o CSS real: @import url(), regras visuais, etc.
        # É compilado DEPOIS que os dois bundles acima já rodaram.
        'web.assets_backend': [
            'my_theme/static/src/scss/03_layout.scss',
            'my_theme/static/src/scss/04_components.scss',
            'my_theme/static/src/scss/05_views.scss',
            'my_theme/static/src/scss/06_animations.scss',
        ],
    },
}
