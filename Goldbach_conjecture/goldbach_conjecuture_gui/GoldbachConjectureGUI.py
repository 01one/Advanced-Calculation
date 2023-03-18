#  Copyright 2021-2023 Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import time
from multiprocessing import Process,Queue

def calculate(x,q):
	if x%2==0:
		prime=[]
		for i in range(2,x+1):
			for j in range(2,i):
				if i%j==0:
					break
			else:
				prime.append(i)
		y=len(prime)

		l=[]
		for i in range(y):
			for j in range(i+1):
				a=prime[i]
				b=prime[j]
				k=a+b
				if k==x:
					l.append([a,b])
		calculation_complete=True
		q.put(l)
	else:
		q.put("Enter an even number greater than two")


if __name__ == '__main__':
	q =Queue()
	import pygame,sys
	from pygame.locals import*
	pygame.init()
	clock=pygame.time.Clock()

	w=1280
	h=720

	screen=pygame.display.set_mode((w,h),RESIZABLE)
	pygame.display.set_caption("Goldbach's Conjecture")
	surface=pygame.Surface((1020,720)).convert_alpha()
	background=pygame.image.load('background.png')
	icon=pygame.image.load('icon.png')
	pygame.display.set_icon(icon)


	then=time.time()
	txt=""
	pulse='|'
	font=pygame.font.Font(pygame.font.get_default_font(),40)
	font1=pygame.font.Font('SourceCodePro-ExtraLight.ttf',20)
	total_digit=0

	class TextView():
		def __init__(self,screen,text='',t_x=0,t_y=0,t_w=200,t_h=200,text_color="#000000"):
			self.screen=screen
			self.t_x=t_x
			self.t_y=t_y
			self.t_w=t_w
			self.t_h=t_h
			self.text_color=text_color 
			self.text=text
			self.text_font=pygame.font.Font('SourceCodePro-ExtraLight.ttf',20)
			self.text_lines=[]
			self.splitted_lines=self.text.splitlines()
			for splitted_line in self.splitted_lines:
				if self.text_font.size(splitted_line)[0] > self.t_w:
					words = splitted_line.split(' ')
					fitted_line=""
					for word in words:
						test_line = fitted_line + word + " "
						if self.text_font.size(test_line)[0] < self.t_w:
							fitted_line = test_line
						else:
							self.text_lines.append(fitted_line)
							fitted_line = word + " "
					self.text_lines.append(fitted_line)
				else:
					self.text_lines.append(splitted_line)
			
			text_row=self.t_y

			for line in self.text_lines:
				if line != "":
					text_surface = self.text_font.render(line, 1, self.text_color)
					first_line=(self.text_font.render(self.text_lines[0], 1, self.text_color)).get_rect()
					txt_rect=text_surface.get_rect()
					txt_rect=(self.t_x,self.t_y,txt_rect[2],txt_rect[3])
					pygame.draw.rect(screen,"#ff033e",txt_rect)
					self.screen.blit(text_surface, (self.t_x, self.t_y))
				self.t_y +=self.text_font.size(line)[1]
				if text_row>h:
					break

	def EntryValue(screen,text='',t_x=0,t_y=0,t_w=200,t_h=400,text_color="#666666",pulse=''):
			text=text+pulse	
			text_surface = font.render(text, 1,text_color)
			first_line=(font.render(text, 1,text_color)).get_rect()
			txt_rect=text_surface.get_rect()
			txt_rect=(t_x,t_y,txt_rect[2],txt_rect[3])
			pygame.draw.rect(screen,"#ccffcc",txt_rect)
			screen.blit(text_surface, (t_x, t_y))

				
	program_running=True
	calculation_in_process=False
	result=''

	button_position=pygame.Rect(580,225,210,60)
	clipboard=pygame.Rect(1055,360,40,50)


	while program_running:
		clock.tick(60)
		surface.fill((0,0,0,0))
		screen.blit(background,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==pygame.VIDEORESIZE:
				w,h=event.size
			if event.type==pygame.TEXTINPUT:
				t=(event.text)
				try:
					if int(t)==int(t):
						total_digit=len(txt)
						if  total_digit<25:
							txt+=t
				except:
					pass
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					pygame.key.set_repeat(200,5)
					if len(txt)==0:
						pass
					else:
						txt=txt[:-1]
							
				if event.key==pygame.K_RETURN:
					if len(txt)>0:
						try:
							multiprocessing.current_process().terminate()
						except:
							pass
						result=''
						x_input=int(txt)
						process1=Process(target=calculate,args=(x_input,q))
						process1.start()
						calculation_in_process=True
			mouse_position=pygame.mouse.get_pos()
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button==1:
					if button_position.collidepoint(mouse_position):
						if len(txt)>0:
							try:
								multiprocessing.current_process().terminate()
							except:
								pass
							result=''
							x_input=int(txt)
							process1=Process(target=calculate,args=(x_input,q))
							process1.start()
							calculation_in_process=True
					if clipboard.collidepoint(mouse_position):
						if len(result)>0:
							pygame.scrap.init()
							txt_clipboard=bytes(result, 'utf-8')
							pygame.scrap.put(pygame.SCRAP_TEXT, txt_clipboard)
							display_text=font1.render("Copied to Clipboard",True,2)
							screen.blit(display_text,(980,260))
									
					
		now=time.time()
		d=now-then
		if d>=1 and d<=2:
			then=now
			pulse=''

		else:
			pulse='|'
			if calculation_in_process:
				processing_text=font1.render("Processing",True,2)
				screen.blit(processing_text,(980,180))

		EntryValue(screen,text=txt,t_x=390,t_y=140,t_w=w-50,t_h=h,pulse=pulse)
		TextView(surface,text=result,t_x=0,t_y=0,t_w=1020,t_h=h)
		
		screen.blit(surface,(160,440))
		try:
			while not q.empty():
				result=str(q.get())
				calculation_in_process=False		
		except:
			calculation_in_process=True
			pass
		pygame.display.update()
