import turtle

isim1 = input("Lutfen birinci oyuncunun adini giriniz: ")
isim2 = input("Lutfen ikinci oyuncunun adini giriniz: ")

pencere = turtle.Screen()
pencere.title("PingPong Game")
pencere.bgcolor("black")
pencere.setup(width=800, height=600)
pencere.tracer(0)  # Bu, ekranın sürekli güncellenmesini engeller

raket1 = turtle.Turtle()
raket1.speed(0)
raket1.shape("square")
raket1.color('white')
raket1.shapesize(stretch_wid=5, stretch_len=1)  # Raket boyutu
raket1.penup()
raket1.goto(-350, 0)

raket2 = turtle.Turtle()
raket2.speed(0)
raket2.shape("square")
raket2.color('white')
raket2.shapesize(stretch_wid=5, stretch_len=1)
raket2.penup()
raket2.goto(350, 0)

top = turtle.Turtle()
top.speed(0)
top.shape('circle')
top.color("white")
top.penup()
top.dx = 1  # Topun yatay hızı
top.dy = 1  # Topun dikey hızı

puan_1 = 0
puan_2 = 0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('green')
scoreboard.penup()
scoreboard.hideturtle()  # Puan tahtasının çerçevesini gizler
scoreboard.goto(0, 250)
scoreboard.write("{} ; {} {} : {}".format(isim1, puan_1, isim2, puan_2), align='center', font=('Courier', 20, 'bold'))

# Raket kontrol fonksiyonları
def raket1_up():
    y = raket1.ycor()
    y += 20
    raket1.sety(y)

def raket1_down():
    y = raket1.ycor()
    y -= 20
    raket1.sety(y)

def raket2_up():
    y = raket2.ycor()
    y += 20
    raket2.sety(y)

def raket2_down():
    y = raket2.ycor()
    y -= 20
    raket2.sety(y)

pencere.listen()
pencere.onkeypress(raket1_up, 'w')
pencere.onkeypress(raket1_down, 's')
pencere.onkeypress(raket2_up, 'Up')
pencere.onkeypress(raket2_down, 'Down')

# Ana oyun döngüsü
while True:
    pencere.update()
    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)

    # Üst ve alt sınır kontrolü
    if top.ycor() > 290 or top.ycor() < -290:
        top.dy *= -1  # Top çarptığında dikey hareket yönünü değiştir

    # Sağ ve sol sınır kontrolü (skor güncelleme)
    if top.xcor() > 390:
        top.goto(0, 0)
        top.dx *= -1
        puan_1 += 1
        scoreboard.clear()
        scoreboard.write("{} ; {} {} : {}".format(isim1, puan_1, isim2, puan_2), align='center', font=('Courier', 20, 'bold'))

    if top.xcor() < -390:
        top.goto(0, 0)
        top.dx *= -1
        puan_2 += 1
        scoreboard.clear()
        scoreboard.write("{} ; {} {} : {}".format(isim1, puan_1, isim2, puan_2), align='center', font=('Courier', 20, 'bold'))

    # Raket ve top çarpışma kontrolü
    if (top.xcor() > 340 and top.xcor() < 350) and (top.ycor() < raket2.ycor() + 50 and top.ycor() > raket2.ycor() - 50):
        top.setx(340)
        top.dx *= -1

    if (top.xcor() < -340 and top.xcor() > -350) and (top.ycor() < raket1.ycor() + 50 and top.ycor() > raket1.ycor() - 50):
        top.setx(-340)
        top.dx *= -1
