# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:11:10 2019

@author: Simon Guilbert
"""

# =============================================================================
# Première partie : Accès aux données
# =============================================================================

import ply.lex as lex


tokens = ['NAME','AND','OR','GET','URL','CONTAINS','EXCLUDES','STAT','UNION','INTERSECT','DIFF']
t_ignore = r' ' # Permet d'ignorer les esapces
t_NAME = r'[a-zA-Z][a-zA-Z]*'
t_AND = r'and | AND | And'
t_OR = r'or | OR | Or'
t_GET = r'get | GET | Get'
t_URL = r'http://[a-zA-Z0-9@éèçêàâ()&-_+/\'€$£*#%]*\.html'
t_CONTAINS = r'contains | CONTAINS | Contains'
t_EXCLUDES = r'excludes | EXCLUDES | Excludes'
t_STAT = r'stat | STAT | Stat'
t_UNION = r'union | UNION | Union'
t_INTERSECT = r'intersect | INTERSECT | Intersect'
t_DIFF = r'diff | DIFF | Diff'

       
lexer = lex.lex()

# =============================================================================
# Test du bon fonctionnement du lexique
# =============================================================================

lexer.input('toto and or GET http://www.machin-truc.org/page.html contains excludes stat union intersect difftoto')
while True:
    tok = lexer.token() #lecture du prochain token ou none
    if not tok: 
        break
    print(tok)


# =============================================================================
# Grammaire
# =============================================================================

import ply.yacc as yacc

def p_assign(p):
    # On considère que le premier NAME est un GET
    '''assign : NAME URL contraintes
    | NAME URL'''

def p_contraintes(p):
    '''contraintes : CONTAINS NAME
    | EXCLUDES NAME
    | contraintes AND CONTAINS NAME
    | contraintes AND EXCLUDES NAME
    | contraintes OR CONTAINS NAME
    | contraintes OR EXCLUDES NAME'''
   
yacc.yacc()

# =============================================================================
# Test du bon fonctionnement de la lexique + grammaire
# =============================================================================

yacc.parse('get http://www.machin-truc.org/page.html contains toto and exclude titi orcontains blabla')

''' Résumé de la séance :
    J'ai eu du mal à comprendre le début de l'énoncé car on sait 
    que l'utilisateur aura besoin de recherché des informations sur 
    une page web mais les exemples de l'énoncé de mènent à aucune page
    existante. On ne peut pas se faire une idée sur la forme des mots
    ou phrases qui seront sur cette page web.
    Le lexique a l'air de fonctionner sauf pour les mots GET, AND et OR
    qui sont reconnus comme des NAME. Au niveau de la grammaire, le code ne 
    renvoie pas d'erreur pour gérer le get, l'URL et les groupes de contraintes
    mais je ne sais pas comment vérifier si il fonctionne.
    Je n'ai pas eu le temps de traiter toute la grammaire sur les stats.
    Je ne sais pas si c'est à cause de Spyder mais quand je supprime un token (par
    exemple supprimer le NAME à la ligne 15 et supprimer toute la ligne 17) le 
    logiciel renvoie l'erreur : "Rule 't_NAME' defined for an unspecified token NAME"
    alors que j'ai bien supprimé t_NAME. pour résoudre le problème il faut fermer puis 
    rouvrir Spyder.
'''    






