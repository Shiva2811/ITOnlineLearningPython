action = input("Do you like action movie? (Yes/No): ").lower() == "yes"
drama = input("Do you like drama movie? (Yes/No): ").lower() == "yes"
comedy = input("Do you like comedy movie? (Yes/No): ").lower() == "yes"

#combine boolean using logical operators
if action and comedy and not drama:
    genre = "Action-Comedy"
elif action and drama and not comedy:
    genre = "Action-Drama"
elif comedy and drama and not action:
    genre = "Comedy-Drama"
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif drama:
    genre = "Drama"
else:
    genre = "Unknown"
print("Your preferred genre is:", genre)

# Recommend movies based on the genre using conditional statements
if genre == "Action-Comedy":
    print("Recommended movies: 'Rush Hour', 'Bad Boys', 'The Nice Guys'")
elif genre == "Action-Drama":
    print("Recommended movies: 'The Dark Knight', 'Inception', 'John Wick'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'The Big Sick', 'Little Miss Sunshine', 'The Intouchables'")
elif genre == "Action":
    print("Recommended movies: 'Die Hard', 'The Matrix', 'Mission: Impossible'")
elif genre == "Comedy":
    print("Recommended movies: 'The Hangover', 'Superbad', 'Bridesmaids'")
elif genre == "Drama":
    print("Recommended movies: 'The Shawshank Redemption', 'Forrest Gump', 'The Green Mile'")
else:
    print("Sorry, we couldn't determine your movie preferences.")