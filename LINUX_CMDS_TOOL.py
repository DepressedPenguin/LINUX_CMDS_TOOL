#!/usr/bin/python3
#CODE BY _DPGUIN
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QPlainTextEdit,QLabel
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
import sys

#MAKE_MAIN_WINDOW
def Cmds_Window():
	app = QApplication(sys.argv)
	w = QWidget()
	#MAKE_WINDOW_SIZE
	w.setGeometry(100,100,250,300)
	# w.setGeometry(100,100,600,300)
	#SE_NEW_ICON
	w.setWindowIcon(QIcon('icon'))
	#SET_WINDOW_TITLE
	w.setWindowTitle("LINUX CMDS")
	#STYLE_BACKGROUND_WINDOW
	w.setStyleSheet("""
		background-color:black;
		font-family:Courier;
		text-align:center;
		""")
	#MAKE_SEARCH_TITLE
	TITLE_SEARCH = QLabel(w)
	TITLE_SEARCH.setText("SEARCH :")
	#STLYE_TITLE
	TITLE_SEARCH.setStyleSheet("""
		color:white;
		font-family:Courier;
		font-size:19px;
		""")
	#MAKE_TEST_FUCTION
	def test_all():
		# SEARCH_INPUT.setText("WORK")
		# CMD_INPUT.setText("WORK")
		# TEXT_ARE_USE.setPlainText("WORK")

		cmd_text = SEARCH_INPUT.text()
		if cmd_text == 'ls':
		    CMD_INPUT.setText("Command: ls")
		    TEXT_ARE_USE.setPlainText("The most frequently used command in Linux to list directories")
		    CMD_EXAMPLE.setPlainText("ls [name directory]")

		elif cmd_text == 'pwd':
		    CMD_INPUT.setText("Command: pwd")
		    TEXT_ARE_USE.setPlainText("Print working directory command in Linux")
		    CMD_EXAMPLE.setPlainText("pwd")

		elif cmd_text == 'cd':
		    CMD_INPUT.setText("Command: cd")
		    TEXT_ARE_USE.setPlainText("Linux command to navigate through directories")
		    CMD_EXAMPLE.setPlainText("cd [directory_name]")

		elif cmd_text == 'mkdir':
		    CMD_INPUT.setText("Command: mkdir")
		    TEXT_ARE_USE.setPlainText("Command used to create directories in Linux")
		    CMD_EXAMPLE.setPlainText("mkdir [directory_name]")

		elif cmd_text == 'mv':
		    CMD_INPUT.setText("Command: mv")
		    TEXT_ARE_USE.setPlainText("Move or rename files in Linux")
		    CMD_EXAMPLE.setPlainText("mv [source] [destination]")

		elif cmd_text == 'cp':
		    CMD_INPUT.setText("Command: cp")
		    TEXT_ARE_USE.setPlainText("Similar usage as mv but for copying files in Linux")
		    CMD_EXAMPLE.setPlainText("cp [source] [destination]")

		elif cmd_text == 'rm':
		    CMD_INPUT.setText("Command: rm")
		    TEXT_ARE_USE.setPlainText("Delete files or directories")
		    CMD_EXAMPLE.setPlainText("rm [file_or_directory]")

		elif cmd_text == 'touch':
		    CMD_INPUT.setText("Command: touch")
		    TEXT_ARE_USE.setPlainText("Create blank/empty files")
		    CMD_EXAMPLE.setPlainText("touch [file_name]")

		elif cmd_text == 'ln':
		    CMD_INPUT.setText("Command: ln")
		    TEXT_ARE_USE.setPlainText("Create symbolic links (shortcuts) to other files")
		    CMD_EXAMPLE.setPlainText("ln -s [source] [link_name]")

		elif cmd_text == 'cat':
		    CMD_INPUT.setText("Command: cat")
		    TEXT_ARE_USE.setPlainText("Display file contents on the terminal")
		    CMD_EXAMPLE.setPlainText("cat [file_name]")

		elif cmd_text == 'clear':
		    CMD_INPUT.setText("Command: clear")
		    TEXT_ARE_USE.setPlainText("Clear the terminal display")
		    CMD_EXAMPLE.setPlainText("clear")

		elif cmd_text == 'echo':
		    CMD_INPUT.setText("Command: echo")
		    TEXT_ARE_USE.setPlainText("Print any text that follows the command")
		    CMD_EXAMPLE.setPlainText("echo [text]")

		elif cmd_text == 'less':
		    CMD_INPUT.setText("Command: less")
		    TEXT_ARE_USE.setPlainText("Linux command to display paged outputs in the terminal")
		    CMD_EXAMPLE.setPlainText("less [file_name]")

		elif cmd_text == 'man':
		    CMD_INPUT.setText("Command: man")
		    TEXT_ARE_USE.setPlainText("Access manual pages for all Linux commands")
		    CMD_EXAMPLE.setPlainText("man [command_name]")

		elif cmd_text == 'uname':
		    CMD_INPUT.setText("Command: uname")
		    TEXT_ARE_USE.setPlainText("Linux command to get basic information about the OS")
		    CMD_EXAMPLE.setPlainText("uname -a")

		elif cmd_text == 'whoami':
		    CMD_INPUT.setText("Command: whoami")
		    TEXT_ARE_USE.setPlainText("Get the active username")
		    CMD_EXAMPLE.setPlainText("whoami")

		elif cmd_text == 'tar':
		    CMD_INPUT.setText("Command: tar")
		    TEXT_ARE_USE.setPlainText("Command to extract and compress files in Linux")
		    CMD_EXAMPLE.setPlainText("tar -zxvf [file_name.tar.gz]")

		elif cmd_text == 'grep':
		    CMD_INPUT.setText("Command: grep")
		    TEXT_ARE_USE.setPlainText("Search for a string within an output")
		    CMD_EXAMPLE.setPlainText("grep [search_term] [file_name]")

		elif cmd_text == 'head':
		    CMD_INPUT.setText("Command: head")
		    TEXT_ARE_USE.setPlainText("Return the specified number of lines from the top")
		    CMD_EXAMPLE.setPlainText("head -n [number_of_lines] [file_name]")

		elif cmd_text == 'tail':
		    CMD_INPUT.setText("Command: tail")
		    TEXT_ARE_USE.setPlainText("Return the specified number of lines from the bottom")
		    CMD_EXAMPLE.setPlainText("tail -n [number_of_lines] [file_name]")

		elif cmd_text == 'diff':
		    CMD_INPUT.setText("Command: diff")
		    TEXT_ARE_USE.setPlainText("Find the difference between two files")
		    CMD_EXAMPLE.setPlainText("diff [file1] [file2]")

		elif cmd_text == 'cmp':
		    CMD_INPUT.setText("Command: cmp")
		    TEXT_ARE_USE.setPlainText("Allows you to check if two files are identical")
		    CMD_EXAMPLE.setPlainText("cmp [file1] [file2]")

		elif cmd_text == 'comm':
		    CMD_INPUT.setText("Command: comm")
		    TEXT_ARE_USE.setPlainText("Combines the functionality of diff and cmp")
		    CMD_EXAMPLE.setPlainText("comm [file1] [file2]")

		elif cmd_text == 'sort':
		    CMD_INPUT.setText("Command: sort")
		    TEXT_ARE_USE.setPlainText("Linux command to sort the content of a file while outputting")
		    CMD_EXAMPLE.setPlainText("sort [file_name]")

		elif cmd_text == 'export':
		    CMD_INPUT.setText("Command: export")
		    TEXT_ARE_USE.setPlainText("Export environment variables in Linux")
		    CMD_EXAMPLE.setPlainText("export [variable_name]=[value]")

		elif cmd_text == 'zip':
		    CMD_INPUT.setText("Command: zip")
		    TEXT_ARE_USE.setPlainText("Zip files in Linux")
		    CMD_EXAMPLE.setPlainText("zip [archive_name] [file1] [file2] ...")

		elif cmd_text == 'unzip':
		    CMD_INPUT.setText("Command: unzip")
		    TEXT_ARE_USE.setPlainText("Unzip files in Linux")
		    CMD_EXAMPLE.setPlainText("unzip [archive_name.zip]")

		elif cmd_text == 'ssh':
		    CMD_INPUT.setText("Command: ssh")
		    TEXT_ARE_USE.setPlainText("Secure Shell command in Linux")
		    CMD_EXAMPLE.setPlainText("ssh [user]@[hostname]")

		elif cmd_text == 'service':
		    CMD_INPUT.setText("Command: service")
		    TEXT_ARE_USE.setPlainText("Linux command to start and stop services")
		    CMD_EXAMPLE.setPlainText("service [service_name] start")

		elif cmd_text == 'ps':
		    CMD_INPUT.setText("Command: ps")
		    TEXT_ARE_USE.setPlainText("Display active processes")
		    CMD_EXAMPLE.setPlainText("ps aux")

		elif cmd_text == 'kill' or cmd_text == 'killall':
		    CMD_INPUT.setText(f"Command: {cmd_text}")
		    TEXT_ARE_USE.setPlainText("Kill active processes by process ID or name")
		    CMD_EXAMPLE.setPlainText(f"{cmd_text} [process_id_or_name]")

		elif cmd_text == 'df':
		    CMD_INPUT.setText("Command: df")
		    TEXT_ARE_USE.setPlainText("Display disk filesystem information")
		    CMD_EXAMPLE.setPlainText("df -h")

		elif cmd_text == 'mount':
		    CMD_INPUT.setText("Command: mount")
		    TEXT_ARE_USE.setPlainText("Mount file systems in Linux")
		    CMD_EXAMPLE.setPlainText("mount [device] [mount_point]")

		elif cmd_text == 'chmod':
		    CMD_INPUT.setText("Command: chmod")
		    TEXT_ARE_USE.setPlainText("Command to change file permissions")
		    CMD_EXAMPLE.setPlainText("chmod [permissions] [file_name]")

		elif cmd_text == 'chown':
		    CMD_INPUT.setText("Command: chown")
		    TEXT_ARE_USE.setPlainText("Command for granting ownership of files or folders")
		    CMD_EXAMPLE.setPlainText("chown [new_owner]:[new_group] [file_name]")

		elif cmd_text == 'ifconfig':
		    CMD_INPUT.setText("Command: ifconfig")
		    TEXT_ARE_USE.setPlainText("Display network interfaces and IP addresses")
		    CMD_EXAMPLE.setPlainText("ifconfig")

		elif cmd_text == 'traceroute':
		    CMD_INPUT.setText("Command: traceroute")
		    TEXT_ARE_USE.setPlainText("Trace all the network hops to reach the destination")
		    CMD_EXAMPLE.setPlainText("traceroute [hostname_or_ip]")

		elif cmd_text == 'wget':
		    CMD_INPUT.setText("Command: wget")
		    TEXT_ARE_USE.setPlainText("Directly download files from the internet")
		    CMD_EXAMPLE.setPlainText("wget [file_url]")

		elif cmd_text == 'ufw':
		    CMD_INPUT.setText("Command: ufw")
		    TEXT_ARE_USE.setPlainText("Firewall command")
		    CMD_EXAMPLE.setPlainText("ufw [options]")

		elif cmd_text == 'iptables':
		    CMD_INPUT.setText("Command: iptables")
		    TEXT_ARE_USE.setPlainText("Base firewall for all other firewall utilities to interface with")
		    CMD_EXAMPLE.setPlainText("iptables [options]")

		elif cmd_text in ('apt', 'pacman', 'yum', 'rpm'):
		    CMD_INPUT.setText(f"Command: {cmd_text}")
		    TEXT_ARE_USE.setPlainText(f"Package manager depending on the distro ({cmd_text})")
		    CMD_EXAMPLE.setPlainText(f"{cmd_text} [options] [package_name]")

		elif cmd_text == 'sudo':
		    CMD_INPUT.setText("Command: sudo")
		    TEXT_ARE_USE.setPlainText("Command to escalate privileges in Linux")
		    CMD_EXAMPLE.setPlainText("sudo [command]")

		elif cmd_text == 'cal':
		    CMD_INPUT.setText("Command: cal")
		    TEXT_ARE_USE.setPlainText("View a command-line calendar")
		    CMD_EXAMPLE.setPlainText("cal [month] [year]")

		elif cmd_text == 'alias':
		    CMD_INPUT.setText("Command: alias")
		    TEXT_ARE_USE.setPlainText("Create custom shortcuts for your regularly used commands")
		    CMD_EXAMPLE.setPlainText("alias [shortcut]='[command]'")

		elif cmd_text == 'dd':
		    CMD_INPUT.setText("Command: dd")
		    TEXT_ARE_USE.setPlainText("Majorly used for creating bootable USB sticks")
		    CMD_EXAMPLE.setPlainText("dd [options] if=[input_file] of=[output_file]")

		elif cmd_text == 'whereis':
		    CMD_INPUT.setText("Command: whereis")
		    TEXT_ARE_USE.setPlainText("Locate the binary, source, and manual pages for a command")
		    CMD_EXAMPLE.setPlainText("whereis [command_name]")

		elif cmd_text == 'whatis':
		    CMD_INPUT.setText("Command: whatis")
		    TEXT_ARE_USE.setPlainText("Find what a command is used for")
		    CMD_EXAMPLE.setPlainText("whatis [command_name]")

		elif cmd_text == 'top':
		    CMD_INPUT.setText("Command: top")
		    TEXT_ARE_USE.setPlainText("View active processes live with their system usage")
		    CMD_EXAMPLE.setPlainText("top")

		elif cmd_text in ('useradd', 'usermod'):
		    CMD_INPUT.setText(f"Command: {cmd_text}")
		    TEXT_ARE_USE.setPlainText(f"Add new user or change existing user's data ({cmd_text})")
		    CMD_EXAMPLE.setPlainText(f"{cmd_text} [options] [username]")

		elif cmd_text == 'passwd':
		    CMD_INPUT.setText("Command: passwd")
		    TEXT_ARE_USE.setPlainText("Create or update passwords for existing users")
		    CMD_EXAMPLE.setPlainText("passwd [username]")






	#MAKE_SEARCH_INPUT
	SEARCH_INPUT = QLineEdit(w)
	SEARCH_INPUT.setGeometry(5,10,90,37)
	SEARCH_INPUT.move(100,5)
	#STYLE_SEARCH_INPUUT
	SEARCH_INPUT.setStyleSheet("""
		border-radius:5px;
		border:1px solid white;
		color:white;
		font-size:17px;
		""")
	SEARCH_INPUT.show()
	#MAKE_BTN_SEARCH
	BTN_SEARCH = QPushButton(w)
	BTN_SEARCH.setText("LOOK")
	BTN_SEARCH.setGeometry(180,4,40,38)
	BTN_SEARCH.setStyleSheet("""
		color:black;
		background-color:white;
		font-family:Courier;
		font-size:14px;
		border-radius:3px;
		""")
	BTN_SEARCH.move(200,3)
	#MAKE_BORDER_TO_SPELT_WINDOW
	HALF_BORDER = QLabel(w)
	HALF_BORDER.setGeometry(0,49,600,3)
	HALF_BORDER.setStyleSheet("background-color:blue;")
	TITLE_SEARCH.move(10,15)
	#MAKE_TITLE_FOR_CMD_NAME
	CMD_NAME = QLabel(w)
	CMD_NAME.setText("CMD NAME :")
	#STYLE_CMD_NAME
	CMD_NAME.setStyleSheet("""
		color:white;
		font-family:Courier;
		font-size:16px;
		""")
	CMD_NAME.move(5,70)
	#MAKE_CMD_INPUT
	CMD_INPUT = QLineEdit(w)
	CMD_INPUT.setGeometry(110,60,130,37)
	CMD_INPUT.setStyleSheet("""
		border-radius:5px;
		border:1px solid white;
		color:white;
		""")
	#ANOTHER_BORDER_TO_SPEEL_THEM
	BORDER_FOR_CMD = QLabel(w)
	BORDER_FOR_CMD.setGeometry(0,113,250,3)
	BORDER_FOR_CMD.setStyleSheet("background-color:blue;")
	#MAKE_USEABILITY_TITLE
	USEABILITY_Title = QLabel(w)
	USEABILITY_Title.setText("USEABILITY CMD : ")
	USEABILITY_Title.setStyleSheet("""
		color:white;
		font-family:Courier;
		font-size:16px;
		""")
	USEABILITY_Title.move(5,130)
	#MAKE_TEXT_AREA_FOR_USE
	TEXT_ARE_USE = QPlainTextEdit(w)
	TEXT_ARE_USE.setGeometry(0,150,250,70)
	TEXT_ARE_USE.setPlaceholderText("USEABILITY")
	TEXT_ARE_USE.setStyleSheet("""
		color:white;
		border:1px solid blue;
		""")
	BTN_SEARCH.clicked.connect(test_all)
	#EXAMPLE_AREA
	EXAMPLE_CMD_TITLE = QLabel(w)
	EXAMPLE_CMD_TITLE.setText("EXAMPLE :")
	#STYLE_EXAMPLE_CMD
	EXAMPLE_CMD_TITLE.setStyleSheet("""
		color:white;
		font-size:17px;
		font-family:Courier;
		""")
	EXAMPLE_CMD_TITLE.move(5,224)
	EXAMPLE_CMD_TITLE.show()
	#MAKE_EX_AREA
	CMD_EXAMPLE = QPlainTextEdit(w)
	CMD_EXAMPLE.setGeometry(5,245,239,50)
	CMD_EXAMPLE.setStyleSheet("""
		border:1px solid blue;
		color:white;
		font-size:15px;
		""")
	CMD_EXAMPLE.setPlaceholderText("EX :")
	CMD_EXAMPLE.show()
	#MAKE_NEW_WINDOW_PAGE
	def Window_Page():
		w.setGeometry(100,100,600,300)
	#MAKE_BTN_FOR_ALL_OF_TOOLS
	BTN_NEW_WINDOW = QPushButton(w)
	BTN_NEW_WINDOW.setText("ALL CMDS")
	#STYLE_BTN
	BTN_NEW_WINDOW.setGeometry(170,120,80,27)
	BTN_NEW_WINDOW.setStyleSheet("""
		background-color:white;
		border-radius:5px;
		font-size:12px;
		""")
	#BTN_POSS
	BTN_NEW_WINDOW.move(165,120)
	BTN_NEW_WINDOW.show()
	#MAKE_BORDER_SPLIT
	BORDER_SPLIT = QLabel(w)
	BORDER_SPLIT.setGeometry(255,0,3,300)
	BORDER_SPLIT.setStyleSheet("background-color:blue;")
	#TITLE_SHOW_CMDS
	TITLE_DISPLAY = QLabel(w)
	TITLE_DISPLAY.setText("BASIC CMDS : CLICK TO SHOW")
	TITLE_DISPLAY.setStyleSheet("""
		color:white;
		font-size:18px;
		""")
	TITLE_DISPLAY.move(290,15)
	TITLE_DISPLAY.show()
	#WINDOW_COMMANDS
	def ls_fill():
		CMD_INPUT.setText("Command: ls")
		TEXT_ARE_USE.setPlainText("The most frequently used command in Linux to list directories")
		CMD_EXAMPLE.setPlainText("ls [name directory]")

	#CD COMMAND
	def cd_fill():
		CMD_INPUT.setText("Command: cd")
		TEXT_ARE_USE.setPlainText("Linux command to navigate through directories")
		CMD_EXAMPLE.setPlainText("cd [directory_name]")


	# MKDIR COMMAND
	def mkdir_fill():
		CMD_INPUT.setText("Command: mkdir")
		TEXT_ARE_USE.setPlainText("Command used to create directories in Linux")
		CMD_EXAMPLE.setPlainText("mkdir [directory_name]")

	#CP COMMAND
	def cp_fill():
		CMD_INPUT.setText("Command: mv")
		TEXT_ARE_USE.setPlainText("Move or rename files in Linux")
		CMD_EXAMPLE.setPlainText("mv [source] [destination]")

	def cat_fill():
		CMD_INPUT.setText("Command: cat")
		TEXT_ARE_USE.setPlainText("Display file contents on the terminal")
		CMD_EXAMPLE.setPlainText("cat [file_name]")

	def clear_fill():
		CMD_INPUT.setText("Command: clear")
		TEXT_ARE_USE.setPlainText("Clear the terminal display")
		CMD_EXAMPLE.setPlainText("clear")

	def man_fill():
		CMD_INPUT.setText("Command: man")
		TEXT_ARE_USE.setPlainText("Access manual pages for all Linux commands")
		CMD_EXAMPLE.setPlainText("man [command_name]")

	def rm_fill():
		CMD_INPUT.setText("Command: rm")
		TEXT_ARE_USE.setPlainText("Delete files or directories")
		CMD_EXAMPLE.setPlainText("rm [file_or_directory]")

	def mv_fill():
		CMD_INPUT.setText("Command: rm")
		TEXT_ARE_USE.setPlainText("Delete files or directories")
		CMD_EXAMPLE.setPlainText("rm [file_or_directory]")

	def cp_fill():
		 CMD_INPUT.setText("Command: cp")
		 TEXT_ARE_USE.setPlainText("Similar usage as mv but for copying files in Linux")
		 CMD_EXAMPLE.setPlainText("cp [source] [destination]")

	def echo_fill():
		CMD_INPUT.setText("Command: echo")
		TEXT_ARE_USE.setPlainText("Print any text that follows the command")
		CMD_EXAMPLE.setPlainText("echo [text]")

	def grep_fill():
		CMD_INPUT.setText("Command: grep")
		TEXT_ARE_USE.setPlainText("Search for a string within an output")
		CMD_EXAMPLE.setPlainText("grep [search_term] [file_name]")

	def usermod_fill():
		CMD_INPUT.setText(f"Command: cmd_text")
		TEXT_ARE_USE.setPlainText(f"Add new user or change existing user's data (cmd_text)")
		CMD_EXAMPLE.setPlainText(f"cmd_text [options] [username]")

	def sudo_fill():
		CMD_INPUT.setText("Command: sudo")
		TEXT_ARE_USE.setPlainText("Command to escalate privileges in Linux")
		CMD_EXAMPLE.setPlainText("sudo [command]")

	def ifconif_fill():
		CMD_INPUT.setText("Command: ifconfig")
		TEXT_ARE_USE.setPlainText("Display network interfaces and IP addresses")
		CMD_EXAMPLE.setPlainText("ifconfig")

	def df_fill():
		CMD_INPUT.setText("Command: df")
		TEXT_ARE_USE.setPlainText("Display disk filesystem information")
		CMD_EXAMPLE.setPlainText("df -h")

	def chmod_fill():
		CMD_INPUT.setText("Command: chmod")
		TEXT_ARE_USE.setPlainText("Command to change file permissions")
		CMD_EXAMPLE.setPlainText("chmod [permissions] [file_name]")


	def trace_fill():
		CMD_INPUT.setText("Command: traceroute")
		TEXT_ARE_USE.setPlainText("Trace all the network hops to reach the destination")
		CMD_EXAMPLE.setPlainText("traceroute [hostname_or_ip]")

	def sort_fill():
		CMD_INPUT.setText("Command: sort")
		TEXT_ARE_USE.setPlainText("Linux command to sort the content of a file while outputting")
		CMD_EXAMPLE.setPlainText("sort [file_name]")

	def service_fill():
		CMD_INPUT.setText("Command: service")
		TEXT_ARE_USE.setPlainText("Linux command to start and stop services")
		CMD_EXAMPLE.setPlainText("service [service_name] start")

	def top_fill():
		CMD_INPUT.setText("Command: head")
		TEXT_ARE_USE.setPlainText("Return the specified number of lines from the top")
		CMD_EXAMPLE.setPlainText("head -n [number_of_lines] [file_name]")

	def tar_fill():
		CMD_INPUT.setText("Command: tar")
		TEXT_ARE_USE.setPlainText("Command to extract and compress files in Linux")
		CMD_EXAMPLE.setPlainText("tar -zxvf [file_name.tar.gz]")

	def ln_fill():
		CMD_INPUT.setText("Command: ln")
		TEXT_ARE_USE.setPlainText("Create symbolic links (shortcuts) to other files")
		CMD_EXAMPLE.setPlainText("ln -s [source] [link_name]")

	def head_fill():
		CMD_INPUT.setText("Command: head")
		TEXT_ARE_USE.setPlainText("Return the specified number of lines from the top")
		CMD_EXAMPLE.setPlainText("head -n [number_of_lines] [file_name]")

	def export_fill():
		CMD_INPUT.setText("Command: export")
		TEXT_ARE_USE.setPlainText("Export environment variables in Linux")
		CMD_EXAMPLE.setPlainText("export [variable_name]=[value]")

	def tail_fill():
		CMD_INPUT.setText("Command: tail")
		TEXT_ARE_USE.setPlainText("Return the specified number of lines from the bottom")
		CMD_EXAMPLE.setPlainText("tail -n [number_of_lines] [file_name]")

	def diff_fill():
		CMD_INPUT.setText("Command: diff")
		TEXT_ARE_USE.setPlainText("Find the difference between two files")
		CMD_EXAMPLE.setPlainText("diff [file1] [file2]")



	#######################ITEMS_ZONE
	#CONTAINER TOOLS SECTIONS
	item_1 = QPushButton(w)
	item_1.setText("ls")
	#STYLE_IT
	item_1.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_1.move(265,60)
	item_1.show()
	################################
	item_2 = QPushButton(w)
	item_2.setText("cd")
	#STYLE_IT
	item_2.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_2.move(350,60)
	item_2.show()
	#################################
	item_3 = QPushButton(w)
	item_3.setText("touch")
	#STYLE_IT
	item_3.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_3.move(435,60)
	item_3.show()
	#################################
	item_4 = QPushButton(w)
	item_4.setText("mkdir")
	#STYLE_IT
	item_4.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_4.move(435,60)
	item_4.show()

	#################################
	item_5 = QPushButton(w)
	item_5.setText("cp")
	#STYLE_IT
	item_5.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_5.move(520,60)
	item_5.show()
	#################################
	item_6 = QPushButton(w)
	item_6.setText("cat")
	#STYLE_IT
	item_6.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_6.move(265,100)
	item_6.show()

	##################################
	item_7 = QPushButton(w)
	item_7.setText("clear")
	#STYLE_IT
	item_7.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_7.move(350,100)
	item_7.show()
	##################################
	item_8 = QPushButton(w)
	item_8.setText("man")
	#STYLE_IT
	item_8.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_8.move(435,100)
	item_8.show()
	##################################
	item_9 = QPushButton(w)
	item_9.setText("rm")
	#STYLE_IT
	item_9.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_9.move(520,100)
	item_9.show()
	##################################
	item_10 = QPushButton(w)
	item_10.setText("rm")
	#STYLE_IT
	item_10.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_10.move(265,138)
	item_10.show()
	##################################
	item_11 = QPushButton(w)
	item_11.setText("cp")
	#STYLE_IT
	item_11.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_11.move(350,138)
	item_11.show()
	##################################
	item_12 = QPushButton(w)
	item_12.setText("echo")
	#STYLE_IT
	item_12.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_12.move(435,138)
	item_12.show()
	##################################
	item_13 = QPushButton(w)
	item_13.setText("grep")
	#STYLE_IT
	item_13.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_13.move(520,138)
	item_13.show()
	##################################
	item_14 = QPushButton(w)
	item_14.setText("usermod")
	#STYLE_IT
	item_14.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_14.move(264,175)
	item_14.show()
	##################################
	item_15 = QPushButton(w)
	item_15.setText("sudo")
	#STYLE_IT
	item_15.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_15.move(350,175)
	item_15.show()
	##################################
	item_16 = QPushButton(w)
	item_16.setText("ifconfig")
	#STYLE_IT
	item_16.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_16.move(435,175)
	item_16.show()
	##################################
	item_17 = QPushButton(w)
	item_17.setText("df")
	#STYLE_IT
	item_17.setGeometry(525,175,70,28)
	item_17.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_17.move(526,175)
	item_17.show()
	##################################
	item_18 = QPushButton(w)
	item_18.setText("chmod")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_18.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_18.move(264,210)
	item_18.show()
	##################################
	item_19 = QPushButton(w)
	item_19.setText("sort")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_19.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_19.move(350,210)
	item_19.show()
	##################################
	item_20 = QPushButton(w)
	item_20.setText("service")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_20.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_20.move(350,210)
	item_20.show()
	##################################
	item_21 = QPushButton(w)
	item_21.setText("top")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_21.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_21.move(435,210)
	item_21.show()
	##################################
	item_22 = QPushButton(w)
	item_22.setText("diff")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_22.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_22.move(520,210)
	item_22.show()
	##################################
	item_23 = QPushButton(w)
	item_23.setText("tar")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_23.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_23.move(520,210)
	item_23.show()
	##################################
	item_23 = QPushButton(w)
	item_23.setText("tar")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_23.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_23.move(520,210)
	item_23.show()
	##################################
	item_24 = QPushButton(w)
	item_24.setText("ln")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_24.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_24.move(264,250)
	item_24.show()
	##################################
	item_25 = QPushButton(w)
	item_25.setText("head")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_25.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_25.move(264,250)
	item_25.show()
	##################################
	item_26 = QPushButton(w)
	item_26.setText("export")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_26.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_26.move(350,250)
	item_26.show()
	##################################
	item_27 = QPushButton(w)
	item_27.setText("tail")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_27.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_27.move(435,250)
	item_27.show()
	##################################
	item_28 = QPushButton(w)
	item_28.setText("diff")
	#STYLE_IT
	# item_18.setGeometry(525,175,70,28)
	item_28.setStyleSheet("""
		color:black;
		background-color:white;
		font-size:17px;
		""")
	item_28.move(517,250)
	item_28.show()
	##################################


	#CLICK_TO_MAKE_SIZE_MUCH_BIGER
	BTN_NEW_WINDOW.clicked.connect(Window_Page)
	#CONNECT_ls_TO_dISPLAY_RES
	item_1.clicked.connect(ls_fill)
	item_2.clicked.connect(cd_fill)
	item_4.clicked.connect(mkdir_fill)
	item_5.clicked.connect(cp_fill)
	item_6.clicked.connect(cat_fill)
	item_7.clicked.connect(clear_fill)
	item_8.clicked.connect(man_fill)
	item_9.clicked.connect(rm_fill)
	item_10.clicked.connect(mv_fill)
	item_11.clicked.connect(cp_fill)
	item_12.clicked.connect(echo_fill)
	item_13.clicked.connect(grep_fill)
	item_14.clicked.connect(usermod_fill)
	item_15.clicked.connect(sudo_fill)
	item_16.clicked.connect(ifconif_fill)
	item_17.clicked.connect(df_fill)
	item_18.clicked.connect(chmod_fill)
	item_19.clicked.connect(sort_fill)
	item_20.clicked.connect(service_fill)
	item_21.clicked.connect(top_fill)
	item_23.clicked.connect(tar_fill)
	item_24.clicked.connect(ln_fill)
	item_25.clicked.connect(head_fill)
	item_26.clicked.connect(export_fill)
	item_27.clicked.connect(tail_fill)
	item_28.clicked.connect(diff_fill)








	w.show()
	sys.exit(app.exec())

Cmds_Window()