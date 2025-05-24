Template tirée de [Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)
# 01 - Architectural decision record

# Choix du mécanisme de base de données

## Status

Accepté

## Contexte

Le systême de point de vente doit persister beaucoup de données. Alors, de nombreux choix se présentent: des base de données noSQL comme MongoDB, ou des base de donnees relationnelles, comme PostgreSQL, SQLite ou Oracle. Ces bases de données doivent soit être en local ou serveur afin de rouler l'application.

## Décision

J'ai choisi d'utiliser PostgreSQL pour comme mécanisme de base de données pour persister les données.

## Justification



## Conséquences

What becomes easier or more difficult to do because of this change?
