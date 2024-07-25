class AffranchissementMas:
    '''
    La classe qui représente l'objet des données d'un affranchissement
    MAS nettoyé pour être envoyé vers l'API et stocké dans la base
    de données.
    Une validation accompagne le modèle.
    '''
    index: int
    nom_departement: str  # = client.nom
    nom_produit: str  # = type_colis.types_envoi.nom
    total_montants: float  # = affranchissement.montant
    unite_montants: float  # = type_colis.prix
    total_objets: int  # = affranchissement.quantite
    total_poids: int  # = ?
    poids_unite: int  # = ?
    date: str  # = affranchissement.created_at
    poids_min: int  # = ?
    poids_max: int  # = type_colis.poids

    def __init__(self, index: int, nom_departement: str, nom_produit: str,
                 total_montants: float, unite_montants: float, total_objets: int,
                 total_poids: int, poids_unite: int, date: str, poids_min: int, poids_max: int):
        self.index = index
        self.nom_departement = nom_departement
        self.nom_produit = nom_produit
        self.total_montants = total_montants
        self.unite_montants = unite_montants
        self.total_objets = total_objets
        self.total_poids = total_poids
        self.poids_unite = poids_unite
        self.date = date
        self.poids_min = poids_min
        self.poids_max = poids_max

    @staticmethod
    def validate(affranchissement_mas) -> bool:
        annotations = AffranchissementMas.__annotations__
        for attribute, expected_type in annotations.items():
            if not isinstance(getattr(affranchissement_mas, attribute), expected_type):
                print(f"Validation failed on {attribute}. {expected_type.__name__} expected.")
                return False
        return True