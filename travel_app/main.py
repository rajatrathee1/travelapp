from journey import Journey
from luggage import suggest_luggage

def main():
    print("Welcome to the Travel Luggage Suggestion App!")
    journey_type = input("Please enter your journey type (business, vacation, adventure): ").lower()
    duration = int(input("Enter the duration of your journey in days: "))

    # Create a Journey instance
    journey = Journey(journey_type, duration)

    # Get luggage suggestions
    luggage_list = suggest_luggage(journey)

    # Display the suggested luggage items
    print("\nBased on your journey, we suggest you pack the following items:")
    for item in luggage_list:
        print(f"- {item}")

if __name__ == "__main__":
    main()
