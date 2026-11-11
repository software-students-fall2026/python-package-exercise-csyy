
from project.magic8ball import (
    get_question,
    select_category,
    get_response,
    custom_answer,
)


def main():
    print("\n🎱 Welcome to the Magic 8 Ball!")

    # Store custom answers throughout the game
    custom_answers = {
        "positive": [],
        "negative": [],
        "non-committal": []
    }

    while True:
        # 1. Get the player's question
        while True:
            try:
                question = get_question(
                    input("\nAsk the Magic 8 Ball a question: ")
                )
                break
            except ValueError as e:
                print("Error:", e)

        # 2. Let the player choose a number
        while True:
            try:
                number = int(input("Pick a number from 0 to 8: "))
            except ValueError:
                print("Please enter a whole number from 0 to 8.")
                continue

            if 0 <= number <= 8:
                break

            print("Please choose a number between 0 and 8.")

        category = select_category(number)

        # 3. Generate the Magic 8 Ball response
        response = get_response(category, custom_answers)

        print("\n🔮 Magic 8 Ball says:", response)

        # 4. Ask whether the player wants to add an answer
        while True:
            choice = input(
                "\nWould you like to add a custom answer? (y/n): "
            ).strip().lower()

            if choice in ("y", "n"):
                break

            print("Please enter y or n.")

        if choice == "y":
            while True:
                answer = input("Enter your custom answer: ").strip()
                if answer:
                    break
                print("Your answer cannot be empty.")

            while True:
                answer_category = input(
                    "Category (positive/negative/non-committal): "
                ).strip().lower()

                if answer_category in custom_answers:
                    break

                print("Invalid category. Please try again.")

            new_answers = custom_answer(answer, answer_category)

            # Preserve the new answer for future questions
            for key in custom_answers:
                custom_answers[key].extend(new_answers[key])

        # Ask whether to play again
        while True:
            again = input(
                "\nWould you like to ask another question? (y/n): "
            ).strip().lower()

            if again in ("y", "n"):
                break

            print("Please enter y or n.")

        if again == "n":
            print("\nThanks for playing Magic 8 Ball! 🎱")
            break


if __name__ == "__main__":
    main()
