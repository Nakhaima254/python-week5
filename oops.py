# Base class
class Superhero:
    def __init__(self, name, power, health=100):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        return f"{self.name} uses {self.power} to attack!"

    def defend(self, damage):
        self.health -= damage
        return f"{self.name} defends but loses {damage} health. Remaining health: {self.health}"

    def display_info(self):
        return f"Superhero: {self.name}, Power: {self.power}, Health: {self.health}"


# Subclass (Inheritance + Polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power, flight_speed, health=120):
        # Call parent constructor with super()
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    # Polymorphism: override attack()
    def attack(self):
        return f"{self.name} swoops down at {self.flight_speed} km/h using {self.power}!"

    # New method unique to FlyingHero
    def fly(self):
        return f"{self.name} takes off and flies at {self.flight_speed} km/h."


# Another Subclass
class TechHero(Superhero):
    def __init__(self, name, power, gadgets, health=110):
        super().__init__(name, power, health)
        self.gadgets = gadgets

    def attack(self):
        return f"{self.name} uses {self.gadgets} and {self.power} in battle!"

    def upgrade_gadgets(self, new_gadget):
        self.gadgets += f", {new_gadget}"
        return f"{self.name} upgraded gadgets: {self.gadgets}"


# --- Testing the classes ---
if __name__ == "__main__":
    hero1 = Superhero("AquaMan", "Water Blast")
    hero2 = FlyingHero("Falcon", "Wing Strike", flight_speed=300)
    hero3 = TechHero("IronMan", "Repulsor Beam", "Nano Suit")

    print(hero1.display_info())
    print(hero1.attack())
    print(hero1.defend(20))

    print("\n" + hero2.display_info())
    print(hero2.attack())
    print(hero2.fly())

    print("\n" + hero3.display_info())
    print(hero3.attack())
    print(hero3.upgrade_gadgets("Laser Cannons"))
