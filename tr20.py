#imports



#create PC
class Player():
    combat_classes = ["Arcanista",
               "Bárbaro",
               'Bardo',
               'Caçador',
               'Clérigo',
               'Druida',
               'Lutador',
               'Guerreiro',
               'Inventor',
               'Ladino',
               'Cavaleiro',
               'Paladino',
               'Bucaneiro',
               'Nobre']
    
    races = ['Humano',
             'Runinata',
             'Antroplantae',
             'Constructo',
             'Half Dragon',
             'Minotauro',
             'Troll',
             'Vastaya',
             'Yordle',
             'Vastinata']
    
    def __init__(self, name:str, age:int, race:str, combat_class:str, past:str = None):
        self._name = name
        self._age = age
        self._race = race
        self._combat_class = combat_class
        self._past = past
    # Propriedades
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def race(self):
        return self._race
    @property
    def combat_class(self):
        return self._combat_class
    @property
    def past(self):
        return self._past
    
    # Setters
    @name.setter
    def name(self, name:str):
        self._name = name
        return name
    @age.setter
    def age(self, age:int):
        self._age = age
        return age
    @race.setter
    def race(self, race):
        pass
    @past.setter
    def past(self, past:str):
        pass
    
    #metodos
    def details(self):
        print (f'Nome: {self._name}\nIdade: {self._age}\nRaça: {self._race}\nClasse: {self._combat_class}')
        
teste1 = Player('Juninho', 23, 'Humano', 'Druida')
teste1.details()