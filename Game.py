text= "привет путник как тебя зовут?"
print(text)
name= input ()
xp= int((100))
i= int((100))
text= "Привет"
print (text,name)
text= "Выбери оружие A топор-и25 у15 3кг: B нож-и10 у9 0.3кг: V дубинка-и 50 у35 5кг: Ваши статы xp и инергия "
print(text,xp,i)
o=input()
if "b" in o:
	ammun=("нож")
elif "a"in o:
	ammun=("топор")
elif "v"in o:
	ammun=("дубинка")
print ("хороший выбор",ammun)
yppr=int()
if "b" in o:
	yppr=(9)
elif "a"in o:
	yppr=(15)
elif "v"in o:
	yppr=(35)
if "b" in o:
	iner=(10)
elif "a"in o:
	iner=(25)
elif "v"in o:
	iner=(50)
text= "(кухня светлая)впереди монстр xp-18 у-5 95%(видимости) :ваши действия A-ударить  B-бежать 15%(невидимость):Подсказка чтобы скрыться надо что бы невидимость была больше видимости "
xpbattl=int(18)
pr=int(95)
y=int(5)
print(text)
batl=input()
if "a" in batl:
	xod= xpbattl/yppr
	tt= (y*xod)
	xp=xp-tt
	ttt=(iner*xod)
	i=i-ttt
	win=100-tt
elif "b":
	print("ВАС ЗАМЕТИЛИ ПОТРАЧЕНО")
elif xp<1:
	print("ПОТРАЧЕНО")
if xp>1:
	print("ПОБЕДА Ваше xp:",xp,"Ваша инергия",i,"Награда 53 золота,20 инергии")	
	gold=int()
	gold+53
	i+20
text= "Теперь ты можешь покупать вещи в конце раунда попробуй:(A) меч У35 И25 53г,(B)тесак У16 И19 47г, (не хватка денег) яд У70 И50 140г "
print(text)
o=input()
if "b" in o:
	ammun=("Тесак")
	gold-47
elif "a"in o:
	ammun=("Меч")
	gold-53
print ("хороший выбор",ammun)
yppr=int()
if "b" in o:
	yppr=(16)
elif "a"in o:
	yppr=(35)
if "b" in o:
	iner=(19)
elif "a"in o:
	iner=(25)
text= "(гараж темно) Человек с дробовиком у-80 xp-350 27%:ваши действия A-ударить  B-бежать 90%(невидимость):Здесь темно можно легко уйти (Разговор:Сэм кто то убил кротокрыса! Осторожнее здесь кто то есть.) "
print(text)
xpbattl=int(350)
pr=int(27)
y=int(80)
batl=input()
if "a" in batl:
	xod= xpbattl/yppr
	tt= (y*xod)
	xp=xp-tt
	ttt=(iner*xod)
	i=i-ttt
	win=100-tt
if "b" in batl:
	ggg=int()
	ggg=27-90
elif ggg>0:
	xp-100
elif xp<1:
	print("ПОТРАЧЕНО")
if xp>1:
	print("ПОБЕДА Ваше xp:",xp,"Ваша инергия",i,"Награда 125 золота,30 инергии")	
	gold=int()
	gold+125
	i+30