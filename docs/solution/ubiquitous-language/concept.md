# Money

> Représente une somme d'argent dans une devise donnée (ex: 10 EUR, 5 USD).

## Properties

- `amount` : le montant (nombre décimal)
- `currency` : la devise (USD, EUR ou KRW)

## Responsibilities

- Additionner, multiplier, diviser un montant
- Vérifier l'égalité entre deux montants

## Invariants

- Pas d'addition entre devises différentes
- Pas de multiplication par un nombre négatif
- Pas de division par zéro

## Collaborators

- `Currency`, `Bank`, `Portfolio`

---

# Bank

> Gère les taux de change et convertit un montant d'une devise à une autre.

## Properties

- `exchange_rate` : taux de change par paire de devises (ex: `EUR->USD`)

## Responsibilities

- Ajouter ou mettre à jour un taux de change
- Convertir un `Money` vers une devise cible

## Invariants

- Si le taux est inconnu, lève une `MissingExchangeRateError`
- Convertir vers la même devise retourne le même montant

## Collaborators

- `Money`, `Currency`, `MissingExchangeRateError`

---

# Portfolio

> Regroupe plusieurs montants en devises différentes et les évalue dans une devise cible.

## Properties

- `moneyList` : liste des montants ajoutés

## Responsibilities

- Ajouter un montant
- Évaluer tous les montants dans une devise via la banque

## Invariants

- Si un taux est manquant, lève une `MissingExchangeRateError`

## Collaborators

- `Money`, `Bank`, `Currency`
