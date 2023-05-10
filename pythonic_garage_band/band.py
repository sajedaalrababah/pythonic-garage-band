class Musician():
  def __init__(self,name):
    self.name = name
  def get_instrument(self):
    pass
  def __str__(self):
    pass
  def __repr__(self):
    pass

class Band(Musician):
    instances = []

    def __init__(self, name, members=None):
        super().__init__(name)
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    @classmethod
    def to_list(cls):
      return cls.instances
    def play_solos(self):
      solo = []
      for member in self.members:
        solo.append(member.play_solo())
      return solo

class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
      return 'guitar'
    def play_solo(self):
      return "face melting guitar solo"
   
class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
      return "bom bom buh bom"

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
      return "rattle boom crash"