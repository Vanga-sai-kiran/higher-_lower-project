import art
import game
import random
from replit import clear
print(art.logo)

initial_score=0
game_should_continue=True
account_b=random.choice(game.data)
while game_should_continue:
    account_a=account_b
    account_b=random.choice(game.data)
    
    if account_b==account_a:
        account_b=random.choice(game.data)
            
        
    def format(account):
        name=account["name"]
        description=account["description"]
        country=account["country"]
        return f"{name},a {description},from {country}"
        
    print(f"Compare A:{format(account_a)}")
    print(art.vs)
    print(f"Compare B:{format(account_b)}")
    
    guess=input("Who has more followers? Type 'A' or 'B' ").lower()
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    
    def who_more(guess,a_follower_count,b_follower_count):
        if a_follower_count>b_follower_count:
            return guess=="a"
        else:
            return guess=="b"
            
    is_correct=who_more(guess,a_follower_count,b_follower_count)
    clear()
    print(art.logo)
    if is_correct:
        initial_score+=1
        print(f"you got it! Current score:{initial_score}")
    else:
        clear()
        print(f"sorry,wrong answer! Current score:{initial_score}")
        game_should_continue=False

    
