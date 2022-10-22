class Score:
    def __init__(self) -> None:
        self.score = 0
        self.highest_score = Score.get_highest_score(self)


    def save(self):
        f=open("data/score.txt",'r')
        try:
            lines = f.readlines()
            last_line = lines[-1]
            game_number = int(last_line.split(" : ")[0].split("_")[1])
        except IndexError:
            game_number = 0
        f.close()
        with open("data/score.txt",'a') as f:
            f.write(f"game_{game_number+1} : {self.score}\n")

    def get_highest_score(self):
        with open("data/score.txt",'r') as f:
            try:
                lines = f.readlines()
                score = [int(elt.split(" : ")[1]) for elt in lines]
                highest_score = max(score)
                if highest_score == None:
                    raise
                else:
                    self.highest_score = highest_score
                    return highest_score

            except IndexError and ValueError:
                self.highest_score = 0
                return 0
    
    def sayHighestScore(self,score):
        if self.score > self.highest_score:
            print("Nouveau record !")
            Score.get_highest_score(self)
            print(f"Highest Score : {self.highest_score}")
        else:
            print("Dommage, vous battrez votre meilleur score la prochaine fois")
            print(f"Score : {self.score}")
            print(f"Highest Score : {self.highest_score}")
