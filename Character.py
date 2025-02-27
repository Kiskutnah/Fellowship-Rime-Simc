from Spell import Spell
from functools import cached_property

class Character:
    intellect_points: int
    crit_points: int
    haste_points: int
    expertise_points: int
    spirit_points: int
    mana: int
    winter_orbs: int
    spells: list[Spell]
    talents: list[str]
    
    anima_spikes: Spell
    soulfrost: Spell
    boosted_blast: Spell
    soulfrost_buff: Spell
    glacial_assault_buff: Spell
    cometBonus: Spell

    intellectPerPoint = 1
    critPerPoint = 0.21
    expertisePerPoint = 0.21
    hastePerPoint = 0.21
    spiritPerPoint = 0.21

    def __init__(self, 
                 intellect_points: int,  
                 crit_points: int, 
                 expertise_points: int, 
                 haste_points: int, 
                 spirit_points: int
                 ):
        self.intellect_points = intellect_points
        self.crit_points = crit_points
        self.expertise_points = expertise_points
        self.haste_points = haste_points
        self.spirit_points = spirit_points
        self.mana = 0
        self.winter_orbs = 0
        self.spells: list[Spell] = []  # This will hold the character's available spells
        self.talents: list[str] = [] # All the talents.
        self.anima_spikes = Spell("Anima Spikes", cast_time=0, cooldown=0, mana_generation=0, winter_orb_cost=0, damage_percent=36, hits=3)
        #Damage is set to 1560 because of ingame bug.
        self.soulfrost = Spell("Soulfrost Torrent", cast_time=2.0, cooldown=10, mana_generation=12, winter_orb_cost=0, damage_percent=1560, channeled=True, ticks=12)
        self.boosted_blast = Spell("Glacial Blast", cast_time=0, cooldown=0, mana_generation=0, winter_orb_cost=2, damage_percent=604)

        self.soulfrost_buff = Spell("Soulfrost Torrent", isBuff=True, debuffDuration=100000)
        self.glacial_assault_buff = Spell("Glacial Assault", isBuff=True, debuffDuration=100000)
        self.cometBonus = Spell("Ice Comet", cast_time=0, cooldown=0, mana_generation=0, winter_orb_cost=0, damage_percent=300)


    def _calculate_stat_value(self, points: int, statPerPoint: float):
        return points * statPerPoint

    @cached_property
    def intellect(self):
        return self._calculate_stat_value(self.intellect_points, Character.intellectPerPoint)

    @cached_property
    def crit(self):
        return self._calculate_stat_value(self.crit_points, Character.critPerPoint) + 5
    
    @cached_property
    def expertise(self):
        return self._calculate_stat_value(self.expertise_points, Character.expertisePerPoint)
    
    @cached_property
    def haste(self):
        return self._calculate_stat_value(self.haste_points, Character.hastePerPoint)

    @cached_property
    def spirit(self):
        return self._calculate_stat_value(self.spirit_points, Character.spiritPerPoint)

    def add_spell(self, spell: Spell):
        self.spells.append(spell)
    
    def add_talent(self, talent: str):
        self.talents.append(talent)

    def update_stats(self, intellect, crit, expertise, haste, spirit):
        self.intellect = intellect * Character.intellectPerPoint
        self.crit = crit * Character.critPerPoint
        self.expertise = expertise * Character.expertisePerPoint
        self.haste = haste * Character.hastePerPoint
        self.spirit = spirit * Character.spiritPerPoint