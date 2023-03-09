#  Copyright 2022-23 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
from math import sqrt
from itertools import permutations
import pygame,sys
from pygame.locals import*
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,700))
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)  
background=(255,255,255)
purple=(187,51,255)
black="#000000"
coral="#ff7f50"



#xy={"a":[80,120],"g":[160,120],"b":[200,160],"e":[200,224],"j":[160,240],"i":[56,240],"k":[120,200],"h":[120,160],"f":[72,160],"d":[96,176],"c":[144,200]} #"l":[120,152],"m":[136,244],"n":[216,00],"0":[100,248],"p":[200,76]}

xy={"a":[80,120],"b":[170,220],"c":[180,160],"d":[150,240],"e":[60,140],"f":[56,230],"g":[130,210],"h":[120,170],"i":[72,190]}
#completed path
path="bcdefghi"
#path="bcdefghijklmnop"
ways=permutations(path)
ways=list(ways)
ways = ["a"+''.join(item)+"a" for item in ways]

#different roads
roads="abcdefghia"
#roads="abcdefghijklmnopa"
road=permutations(roads,2)
road=list(road)
road= [''.join(item) for item in road]
#print(road)


def process(a,b):
	c=(a+b)
	return c
def distance(c):
	z=sqrt(abs(c[0]**2-c[2]**2))+sqrt(abs(c[1]**2-c[3]**2))
	return z

road_d={}
for i in range(len(road)-1):
	c=road[i]
	c1=xy[c[0]]
	c2=xy[c[1]]
	p=process(c1,c2)
	k=distance(p)
	road_d[c]=k

print(road_d)
cc=[]
dd=[]
for i in range(len(ways)):
	x=ways[i]
	l=[]
	m=[]
	d=0 #total distance
	for j in range(len(x)-1):
		a=x[j]
		b=x[j+1]
		c=a+b
		d+=road_d[c]
		l.append(c)
		m.append(a)

	dd.append(d)
	pp=[xy[item] for item in m]
	cc.append(pp)


all_ways=len(cc)
ln=all_ways//2

print(all_ways)
new=0
nn=[]
def show_text(text,x=50,y=50,s=20,screen=screen,c=purple):
	distance_font=pygame.font.Font('NeoEuler.otf', s)
	distance_text=distance_font.render(text,True,c)
	screen.blit(distance_text,(x,y))
def show_most_efficient_distance(text):
	s_font=pygame.font.Font('NeoEuler.otf', 20)
	s_text=s_font.render(text,True,purple)
	screen.blit(s_text,(350,50))

lowest=0

surface=pygame.Surface((300,250))
surface2=pygame.Surface((300,250)).convert_alpha()
surface2.set_alpha(50)
surface.set_alpha(80)
points_txt=False
def draw_points(screen):
	for i in range(len(roads)-1):
		a=roads[i]
		b=xy[a]
		pygame.draw.circle(screen,(255,100,255),b,5,2)
		xt=b[0]-15
		yt=b[1]-10
		if points_txt:
			show_text(a,xt,yt,15,screen,c=coral)
		

speed_options={"60 fps":60,"100 fps":100,"200 fps":2000}
selected_option="60 fps"
show_options=False

class Option():
	def __init__(self,screen,btn_txt,c_rect,btn_color=black,corner=20,font_s=30,r=True,txt_in=True,txt='',selected=False):
		self.btn_txt=btn_txt
		self.x=c_rect[0]
		self.y=c_rect[1]
		self.x1=c_rect[2]
		self.y1=c_rect[3]
		self.btn_font=pygame.font.Font(pygame.font.get_default_font(),font_s)
		self.btn_color=btn_color
		self.color0='#CF56A6'
		self.color1="#D81B1B"
		self.btn_position=pygame.Rect(self.x,self.y,self.x1,self.y1)
		self.button_txt=self.btn_font.render(self.btn_txt,True,self.color0)
		
		if self.btn_position.collidepoint(mouse_position):
			self.btn_color='#741C1C'
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					if txt_in==True:		
						global selected_option
						selected_option=txt
	
					if selected==True:
						global show_options
						if show_options==False:
							show_options=True
		elif not self.btn_position.collidepoint(mouse_position):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button==1:	
					show_options=False
						
		else:
			self.btn_color=self.btn_color
		if r==True:
				pygame.draw.rect(screen,self.btn_color, self.btn_position, border_radius=corner)
		txt_rect=self.button_txt.get_rect()
		txt_rect.center=self.btn_position.center
		screen.blit(self.button_txt,txt_rect)

options=["Set Rendering Limit","60 fps","100 fps","200 fps"]
			
def option_view():
	if show_options==True:
		for i in range(len(options)):
			if i==0:
				Option(screen,options[i],(800,(10+40),300,50),selected=True,txt_in=False)
			else:
				Option(screen,options[i],(800,(50+i*40),200,50),txt=options[i],font_s=20)
	if show_options==False:
		Option(screen,options[0],(800,(10+40),300,50),txt="Rendering Limit",txt_in=False,selected=True)





n=0
fps=60
image=pygame.image.load("progress.png")
percentage=0


while 1:
	fps=speed_options[selected_option]
	pygame.display.set_caption("Actural Frame Rate: "+str(round(clock.get_fps(),2)))
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
			
	screen.fill('#2E0008')
	mouse_position=pygame.mouse.get_pos()
	draw_points(screen)
	pygame.draw.lines(screen,'#FFBEEA',True,cc[new],1)
	
	if new==0:
		lowest=dd[0]
	if lowest>=dd[new]:
		lowest=dd[new]
		nn=cc[new]
		
	if new<ln:
		new+=1
	show_text(str(dd[new]))
	
	surface.fill('#273500')
	pygame.draw.lines(surface,((255,100,255)),True,nn,1)
	surface2.fill((0,0,0,0))
	pygame.draw.lines(surface2,'#FFBEEA',True,cc[new],1)
	draw_points(surface)
	screen.blit(surface,(350,0))
	screen.blit(surface2,(350,300))
	show_most_efficient_distance(str(lowest))
	if not new==ln:
		screen.blit(image, (50, 300),(0, 51*n, 1000,51))
	
	if n+1<13:
		n+=1
	else:
		n=0
	
	
	option_view()
	percentage=round((new/ln)*100,1)
	show_text(str(percentage)+'%',210,250,40)

	show_text('Total check point: '+str(len(xy)),10,380,40)
	show_text('Checked: '+str(new)+' out of '+str(ln),10,440,30)
	
	show_text('All Possible Ways: '+ str(all_ways),10,510,30)
	show_text('To avoid repeated count [example: abcda or adcba the same distance]: '+str(ln),10,580,30)
	show_text('Most efficient way in '+str(new)+' ways',350,20,18)
	show_text('Copyright Mashiur Rahman Mahid  https://www.linkedin.com/in/mashiurrahman99',20,660,10)
	
	pygame.draw.rect(screen,((0,0,255,200)), (50,300,percentage*10,51), border_radius=30)


	draw_points(surface)
	points_txt=True
	pygame.display.update()
