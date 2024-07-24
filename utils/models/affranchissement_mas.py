class AffranchissementMas:
    '''
    La classe qui représente l'objet des données d'un affranchissement
    MAS nettoyé pour être envoyé vers l'API et stocké dans la base
    de données.
    '''
    index: int
    nom_departement: str # = client.nom
    nom_produit: str # = type_colis.types_envoi.nom
    total_montants: str # = affranchissement.montant
    unite_montants: str # = type_colis.prix
    total_objets: int # = affranchissement.quantite
    total_poids: int # = ?
    poids_unite: int # = ?
    date: str # = affranchissement.created_at
    poids_min: int # = ?
    poids_max: int # = type_colis.poids