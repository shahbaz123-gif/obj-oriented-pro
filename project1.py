class Dog:
    # Class variable (shared by all instances)
    animal_type = "Canine"
    
    def __init__(self, name, breed, age):
        """
        Initialize a Dog object with instance variables
        
        Args:
            name (str): The dog's name
            breed (str): The dog's breed
            age (int): The dog's age in years
        """
        # Instance variables (unique to each instance)
        self.name = name
        self.breed = breed
        self.age = age
    
    def display_details(self):
        """
        Display the details of the dog
        """
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Animal Type: {self.animal_type}")
        print("-" * 30)
    
    def __str__(self):
        """
        String representation of the Dog object
        """
        return f"{self.name} - {self.breed} ({self.age} years old)"

# Create dogs of different breeds
if __name__ == "__main__":
    print("Dog Details:")
    print("=" * 30)
    
    # Create first dog (German Shepherd)
    dog1 = Dog("Max", "German Shepherd", 3)
    dog1.display_details()
    
    # Create second dog (Golden Retriever)
    dog2 = Dog("Bella", "Golden Retriever", 2)
    dog2.display_details()
    
    # Create third dog (different breed)
    dog3 = Dog("Charlie", "Bulldog", 4)
    dog3.display_details()
    
    # Demonstrate class variable access
    print(f"All dogs are of type: {Dog.animal_type}")