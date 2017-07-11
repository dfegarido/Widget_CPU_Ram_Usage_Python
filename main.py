from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config
import psutil
from kivy.clock import Clock
from re import findall

Config.set('graphics','width','200')
Config.set('graphics','height','100')
Config.set('graphics','borderless','1')
Config.set('graphics','resizable','0')
Config.set('graphics','top', 10)
Config.set('graphics','left', 10)
Config.set('graphics','position', 'custom')


Builder.load_string('''
<Label>
	font_size:'15dp'

<RootWidget>
	id:widget
	rows:5
	padding:10
	
	ProgressBar:
		id:pb
		value:0
		
	
	Label:
		id:pb_label
		text:'CPU 0%'
	
	ProgressBar:
		id:pb_ram
		value:0
		
	
	Label:
		id:pb_ram_label
		text:'RAM 0%'
	
	# BoxLayout:
		# orientation:'horizontal'
		# spacing:10
		# Button:
			# id:start
			# text:'Start'
			# on_press:widget.start()
		
		# Button:
			# id:stop
			# text:'Stop'
			# on_press:widget.stop()

''')


class RootWidget(GridLayout):
		
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.pb_bar = self.ids['pb']
		self.pb_ram = self.ids['pb_ram']
		self.pb_label = self.ids['pb_label']
		self.pb_ram_label = self.ids['pb_ram_label']
		Clock.schedule_interval(self.pb, 1)
	
	
	
	def pb(self, dt):
		
		x = str(psutil.virtual_memory())
		z = findall(r'\d{0,9}\d{0,9}\.\d{0,9}',x)
		self.ram = float(z[0])
		self.cpu = psutil.cpu_percent()
		# print(self.ram,self.cpu)
		
		
		self.pb_bar.value = int(self.cpu)
		self.pb_label.text = "CPU Usage {}%".format(self.cpu)
		self.pb_ram.value = int(self.ram)
		self.pb_ram_label.text = "RAM Usage {}%".format(self.ram)

		
		return 
				
		
		
	

	
	def stop(self):
		pass
		
		
		


class MainApp(App):
	
	def build(self):
		return RootWidget()
		
if __name__ == "__main__":
	MainApp().run()