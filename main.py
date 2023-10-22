class GameRecommendationEngine:
  def __init__(self):
      # Sample game data
      self.games_data = {
          "The Witcher 3": ["Cyberpunk 2077", "Red Dead Redemption 2", "Assassin's Creed Odyssey"],
          "Overwatch": ["Valorant", "Apex Legends", "Fortnite"],
          "Minecraft": ["Terraria", "Stardew Valley", "Roblox"],
          "Final Fantasy VII": ["Final Fantasy XV", "Kingdom Hearts III", "Dragon Quest XI"],
          "Super Mario Odyssey": ["Super Mario Maker 2", "Luigi's Mansion 3", "Super Mario 3D World"]
      }

  def get_recommendations(self, selected_games):
      recommended_games = set()
      for game in selected_games:
          if game in self.games_data:
              recommended_games.update(self.games_data[game])
      # Remove games that the user already selected
      return list(recommended_games - set(selected_games))

  def start(self):
      print("Welcome to the Game Recommendation Engine!")
      print("Please select the games you enjoy from the following list:")

      for idx, game in enumerate(self.games_data.keys(), 1):
          print(f"{idx}. {game}")

      selected_indices = input("Enter the numbers of the games you enjoy (separated by commas): ").split(',')
      selected_games = [list(self.games_data.keys())[int(idx) - 1] for idx in selected_indices]

      recommendations = self.get_recommendations(selected_games)
      print("\nBased on your selections, we recommend you try out the following games:")
      for game in recommendations:
          print(f"- {game}")


if __name__ == "__main__":
  engine = GameRecommendationEngine()
  engine.start()
