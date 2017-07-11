from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config
import psutil
from kivy.clock import Clock
from re import findall

#SET THE BOARDER SIZE

Config.set('graphics','width','200')
Config.set('graphics','height','100')
Config.set('graphics','borderless','1')
Config.set('graphics','resizable','0')
Config.set('graphics','top', 10)
Config.set('graphics','left', 10)
Config.set('graphics','position', 'custom')


Builder.load_string('''
<Label>
	font_size:'15dp'  					#----------CLASS FOR LABEL

<RootWidget>						#------ROOT WIDGET
	id:widget		
	rows:5
	padding:10
	
	ProgressBar:			#----- BAR FOR CPU
		id:pb
		value:0

	Label:					#------ CPU USAGE TEXT
		id:pb_label
		text:'CPU 0%'
	
	ProgressBar:			#------- BAR FOR RAM
		id:pb_ram
		value:0
	
	Label:					#------ RAM USAGE TEXT
		id:pb_ram_label
		text:'RAM 0%'
''')


class RootWidget(GridLayout):
		
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)	
		self.pb_bar = self.ids['pb'] # 'pb' id for CPU ProgressBar
		self.pb_ram = self.ids['pb_ram']  # 'pb_ram' id for RAM ProgressBar
		self.pb_label = self.ids['pb_label']# CPU text label
		self.pb_ram_label = self.ids['pb_ram_label']# RAM text label
		Clock.schedule_interval(self.pb, 1)# callback every 1 secs

	def pb(self, dt): 
		
		#i am using psutil to grab the usage for CPU and RAM	
		x = str(psutil.virtual_memory()) 
		z = findall(r'\d{0,9}\d{0,9}\.\d{0,9}',x) 
		self.ram = float(z[0])
		self.cpu = psutil.cpu_percent()
	
		# i am passing the result to KV file
		self.pb_bar.value = int(self.cpu)
		self.pb_label.text = "CPU Usage {}%".format(self.cpu)
		self.pb_ram.value = int(self.ram)
		self.pb_ram_label.text = "RAM Usage {}%".format(self.ram)

		return 
				

class MainApp(App):
	
	def build(self):
		return RootWidget()
		
if __name__ == "__main__":
	MainApp().run()
	
