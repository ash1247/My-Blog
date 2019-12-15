Welcome to the documentation of Synosis Blog Project. This documentation will guide you with the instructions to run the project in your system.
This steps provided here will ensure that the project will run in Windows and Linux.

Steps:
	1) Install python3. In windows download python3.xx from their respected website. In linux, open bash and type in this command:
		sudo apt install python3 (For debian distribution)
		sudo yum install python3 (For RHEL distribution)
	2) Install pip3. In windows just click on check box while installing python in the python installer. In Linux type in this command in bash terminal:
		sudo apt install pip3 (For debian distribution)
		sudo yum install pip3 (For RHEL distribution)
	3) Install virtualenv from pip. In windows type in this command in terminal (Provided you added path value for python or after completing python setup, you clicked on the "set path" text box.):
		pip install virtualenv
	  In Linux:
	  	pip3 install virtualenv
	4) Activate the virtualenv named myenv provided in the given folder.
		source /path/to/the/virtual/environment/myenv/bin/activate
	   If successfully activated, you should see the environment name in parentheses in front of every line of the terminal. To deactivate the virtual environment, simply type "deactivate" in the terminal to deactivate the environment.
	5) While the virtual environment is activated, go to the project folder named "blog_project" and type in this command in the bash.
		pip install -r requirements.txt
	6) After completing install, while in the project folder, type in:
		python manage.py runserver
	7) Open a browser and type in this address.
		localhost:8000
	8) The project will run successsfully.
