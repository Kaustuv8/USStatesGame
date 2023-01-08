import turtle as t

import pandas
import pandas as p
Sc = t.Screen()
Sc.title("US States Game")
Sc.addshape("blank_states_img.gif")
Turt = t.Turtle()
Turt.shape("blank_states_img.gif")
Data = p.read_csv("50_states.csv")
Score = 0
missing_states = []
guessed_states = []
while Score!=50:
    State = Sc.textinput(title = f"{Score}/50 states name correct", prompt = "Whats another state name?")
    if State.title() in Data["state"].tolist():
        Turt = t.Turtle()
        Turt.hideturtle()
        Turt.penup()
        X = int(Data[Data.state == State.title()].x)
        Y = int(Data[Data.state == State.title()].y)
        Turt.setpos(X,Y)
        Turt.write(State,False,"center",font=("Ariel",8,"normal"))
        Score+=1
        guessed_states.append(State)
    if State.lower() == "exit":
        missing_states = [i for i in Data["state"].tolist() if i not in guessed_states]
        print(missing_states)
        new_data = pandas.DataFrame({"States" : missing_states})
        new_data.to_csv("states_to_learn.csv")
        break


Sc.exitonclick()
