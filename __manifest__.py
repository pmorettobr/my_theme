# -*- coding: utf-8 -*-
{
    'name': 'Modern Theme - Backend UI',
    'version': '16.0.1.0.0',
    'summary': 'Tema visual moderno para o backend Odoo 16 Community',
    'description': """
        Moderniza completamente o visual do backend do Odoo 16 Community.
        Inclui:
        - Nova paleta de cores profissional
        - Tipografia refinada (DM Sans)
        - Sidebar elegante com gradiente escuro
        - Cards com sombras suaves e bordas arredondadas
        - Botões e inputs modernos
        - Kanban, List e Form views estilizados
        - Navbar e menus aprimorados
        - Animações e micro-interações suaves
        - Scrollbar customizada
    """,
    'author': 'My Company',
    'category': 'Themes/Backend',
    'depends': ['web'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'views/assets.xml',
    ],
    'assets': {
        # Bundle 1: Variáveis primárias — carregadas ANTES do Bootstrap
        # Só variáveis e mixins, ZERO regras CSS aqui
        'web._assets_primary_variables': [
            ('prepend', 'my_theme/static/src/scss/01_primary_variables.scss'),
        ],
        # Bundle 2: Estilos do backend — aplicados após o framework
        'web.assets_backend': [
            'my_theme/static/src/scss/02_bootstrap_overrides.scss',
            'my_theme/static/src/scss/03_layout.scss',
            'my_theme/static/src/scss/04_components.scss',
            'my_theme/static/src/scss/05_views.scss',
            'my_theme/static/src/scss/06_animations.scss',
        ],
    },
}
