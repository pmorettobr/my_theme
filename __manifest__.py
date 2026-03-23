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
        # Bundle 1: variáveis Odoo — disponível em TODOS os bundles
        # Confirmado na doc oficial 16.0 — existe no Community
        'web._assets_primary_variables': [
            ('prepend', 'my_theme/static/src/scss/01_primary_variables.scss'),
        ],
        # Bundle 2: CSS do backend — compilado depois do bundle 1
        # O mais seguro — existe em TODAS as versões do Odoo
        'web.assets_backend': [
            'my_theme/static/src/scss/02_theme.scss',
        ],
    },
}
