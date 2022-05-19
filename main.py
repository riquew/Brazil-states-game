import turtle
import pandas
from user import User
FONT = ('Courier', 12, 'bold')

screen = turtle.Screen()
screen.title('Brazil States Game')
map_img = 'Mapa-Brasil.gif'
screen.addshape(map_img)
screen.setup(width=1000, height=1000)

user = User()
score = 0
data = pandas.read_csv('27_states.csv')
states = data.state.tolist()
turtle.shape(map_img)

while score < 27:
    user_answer = screen.textinput(title='Brazil states.', prompt=f'Write the name of a brazilian state {score}/27: ').title()
    if user_answer in states:
        score += 1
        states.remove(user_answer)
        coord = data[data.state == user_answer]
        new_x = int(coord.x)
        new_y = int(coord.y)
        user.goto(x=new_x, y=new_y)
        user.write(user_answer, font=FONT)
        user.home()
    elif user_answer == 'Exit':
        states_to_learn = pandas.DataFrame(states)
        states_to_learn.to_csv('states_to_learn.csv')
        break

if score == 27:
    user.home()
    user.write('YOU WON!', font=('Courier', 20, 'bold'))

screen.exitonclick()



