from tkinter import *
import random

GAME_COMPRIMENTO= 900
GAME_ALTURA = 700
VELOCIDADE = 150
SPACE_SIZE = 50
BODY_PARTS = 50
SNAKE_COR = "#00FF00"
FOOD_COR = "#FF0000"
BG_COLOR = "#000000"




class Snake:
    def __init__(self):
        self.cordenadas = []
        self.body_size = BODY_PARTS
        self.squares = []

        for _ in range(0,BODY_PARTS):
            self.cordenadas.append([0,0])

        for x,y in self.cordenadas:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE,fill= SNAKE_COR,tags="snake")    
            self.squares.append(square)


class Food:
    
    def __init__(self):
        x = random.randint(0,(GAME_COMPRIMENTO/SPACE_SIZE) -1) * SPACE_SIZE
        y = random.randint(0,(GAME_ALTURA/SPACE_SIZE) -1) * SPACE_SIZE

        self.cordenadas = [x,y]
        canvas.create_oval(x,y, x + SPACE_SIZE, y + SPACE_SIZE,fill=FOOD_COR,tags="food")


def proximo_turno(snake,food):
    x, y = snake.cordenadas[0]


    if direcao == "up":
        y -= SPACE_SIZE
    elif direcao == "down":
        y += SPACE_SIZE
    elif direcao == "left":
        x -= SPACE_SIZE
    elif direcao == "right":   
        x += SPACE_SIZE 
    
    snake.cordenadas.insert(0,(x,y))

    square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE,fill=SNAKE_COR)

    snake.squares.insert(0,square)

    if x == food.cordenadas[0] and y == food.cordenadas[1]:

        global pontos

        pontos += 1

        label.config(text="pontos: {}".format(pontos))

        canvas.delete("food")

        food = Food()
    else:
        del snake.cordenadas[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]


    if checar_colisao(snake):
        game_over()
    else:    
        tela.after(VELOCIDADE,proximo_turno,snake,food)


    

        



def mudar_direcao(proxima_direcao):
    global direcao

    if proxima_direcao == "left":
        if direcao != "right":
            direcao = proxima_direcao
    elif proxima_direcao == "right":
        if direcao != "left":
            direcao = proxima_direcao
    elif proxima_direcao == "up":
        if direcao != "down":
            direcao = proxima_direcao
    elif proxima_direcao == "down":
        if direcao != "up":
            direcao = proxima_direcao                               

def checar_colisao(snake):
    x, y = snake.cordenadas[0]

    if x < 0 or x >= GAME_COMPRIMENTO:
        print("GAME OVER!")
        return True
    elif y < 0 or y >= GAME_ALTURA:
        print("GAME OVER!")
        return True
    for body in snake.cordenadas[1:]:
        if x == body[0] and y == body[1]:
            print("GAME OVER!")
            return True
    return False    



def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text='GAME OVER!',fill='red',tags='game_over')


tela = Tk()
tela.title("jogo da cobrinha")
tela.resizable(False,False)

pontos = 0
direcao = "right"
label = Label(tela,text="pontos:{}".format(pontos),font="arial 25")
label.pack()

canvas = Canvas(tela,bg=BG_COLOR,height= GAME_ALTURA,width=GAME_COMPRIMENTO,)
canvas.pack()

tela.update()

janela_widht = tela.winfo_width()
janela_height = tela.winfo_height()
tela_widht = tela.winfo_screenwidth()
tela_heihht = tela.winfo_screenheight()

x = int((tela_widht/2) - (janela_widht/2))
y = int((tela_heihht/2) - (janela_height/2))

tela.geometry(f"{janela_widht}x{janela_height}+{x}+{y}")

tela.bind('<Left>', lambda event: mudar_direcao('left'))
tela.bind('<Right>', lambda event: mudar_direcao('right'))
tela.bind('<Up>', lambda event: mudar_direcao('up'))
tela.bind('<Down>', lambda event: mudar_direcao('down'))

snake = Snake()
food = Food()

proximo_turno(snake,food)

mainloop()



