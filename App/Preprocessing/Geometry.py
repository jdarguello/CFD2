import matplotlib.pyplot as plt

class Geo():
	"""
		OBJETIVO:
			Desarrolla la geometría del problema.
	"""
	def __init__ (self, dic, local=False):
		#Datos
		a = dic['W']['Valor']
		h = dic['H']['Valor']
		#FIGURA
		fig = plt.figure()
		self.ax = fig.add_subplot(111)
		# Dimensiones reales - ayuda a la escala de la figura
		x0, y0, dx, dy = self.ax.get_position().bounds
		maxd = max(dx, dy)
		width = 6 * maxd / dx
		height = 6 * maxd / dy

		fig.set_size_inches((width, height))
		#Rectángulo
		c = 'black'
		self.Rectangle(a,h,c)
		#Mayor distancia
		if a >= h:
			maxim = a
		else:
			maxim = h
		minim = -maxim/10
		maxim -= minim
		self.ax.set(xlim=(minim,maxim), ylim=(minim,maxim))
		if local:
			plt.show()

		#GUARDAR
		#self.Save(a,h,r,local)

	def Save(self, a,h,r,local):
		if local:
			with open('GeoData.txt', 'w+') as file:
				pass

	def Rectangle(self, a, h,c='black'):
		self.ax.plot([0,a], [0,0], c)
		self.ax.plot([0,a], [h,h], c)
		self.ax.plot([0,0], [0,h], c)
		self.ax.plot([a,a], [0,h], c)

	def Circle(self, a,h, r,c='black'):
		self.ax.add_artist(plt.Circle((a/2,h/2), r/3, fill=False))
		

if __name__ == '__main__':
	data = {
	    'Geometría': {
	        'a': {
	            'Valor':8,
	            'Units': 'm'
	        },
	        'h': {
	            'Valor': 10,
	            'Units': 'm'
	        },
	        'r': {
	            'Valor': 2,
	            'Units': 'm'
	        }
	    },
	    'Propiedades': {
	        'E': {
	            'Valor': 200E6,
	            'Units': 'MPa'
	        },
	        'v': {
	            'Valor': 0.3,
	            'Units': ''
	        }
	    }
	}
	Geo(data['Geometría'], True)