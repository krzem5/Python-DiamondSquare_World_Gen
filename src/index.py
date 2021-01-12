import random



class DiamondSquare:
	def __init__(self,s,r):
		self.s=s**2+1
		self.max=self.s-1
		self.r=r
		self._g()
		self.d()
	def _g(self):
		self.grid=[]
		for i in range(0,self.s**2):self.grid.append(-1)
		self.set(0,0,self.max)
		self.set(self.max,0,self.max/2)
		self.set(self.max,self.max,self.max)
		self.set(0,self.max,self.max/2)
	def set(self,x,y,v):
		self.grid[y*self.s+x]=v
	def get(self,x,y):
		if (x<0 or x>self.max or y<0 or y>self.max):return -1
		return self.grid[y*self.s+x]
	def d(self,s=0):
		if (s==0):s=self.max
		sc=self.r*s
		if (s/2<1):return
		h=int(s/2)
		s=int(s)
		for y in range(h,self.max,s):
			for x in range(h,self.max,s):
				self.sq(x,y,h,random.uniform(0,1)*sc*2-sc)
		for y in range(0,self.max+1,h):
			for x in range((y+h)%s,self.max+1,s):
				self.dm(x,y,h,random.uniform(0,1)*sc*2-sc)
		self.d(s/2)
	def sq(self,x,y,s,sc):
		self.set(x,y,(self.get(x-s,y-s)+self.get(x+s,y-s)+self.get(x+s,y+s)+self.get(x-s,y+s))/4+sc)
	def dm(self,x,y,s,sc):
		self.set(x,y,(self.get(x,y-s)+self.get(x+s,y)+self.get(x,y+s)+self.get(x-s,y))/4+sc)

a=DiamondSquare(3,0)
print(a.grid)