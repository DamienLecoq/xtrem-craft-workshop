# Backlog

## What can be improved in the codebase ?

bank.py: 
- Remplacer la méthode create par un constructeur supplémentaire comportant les paramètres de la méthode create (currency1, currency2, rate)
- La méthode addEchangeRate devrait être nommée addExchangeRate
- Choisir l'implémentation entre self et "Bank" sachant que self est utilisé dans les méthodes __init__, addEchangeRate et convert.

currency.py:
- Renommer le fichier pour qu'on comprenne que c'est une Enum

missing_exchange_rate_error.py:
- Mettre plus d'information dans le message d'erreur.

money_calculator.py:
- Les paramètres currency de chaque méthode n'est jamais utilisé.
- 