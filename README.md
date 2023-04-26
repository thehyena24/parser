# Parser

INTRODUCTION
------------
This project iterates through a folder with subdirectories containing text files (which originally had a unique extension), opens those files, and extracts the required data line-wise. It then updates ".xlsx" file with both overall and month-wise data.


REQUIREMENTS
------------

* Python should be installed on the PC.
* Modules to be installed:
	- openpyxl



INSTALLATION
------------

* For installation of openpyxl, refer to link (a) for windows, or to link (b) for Linux:

	(a) https://www.codespeedy.com/how-to-install-openpyxl-in-python/
	(b) https://www.geeksforgeeks.org/how-to-install-python-openpyxl-package-on-linux/

* NOTE: If you haven't installed pip, refer to link (a) for windows, or to link (b) for Linux.
	
	(a) https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
	(b) https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/



USAGE
-----

* On opening the "Parser" folder, the following four python files will be visible:
	1. data_store.py
	2. main.py
	3. reader.py
	4. writer.py

* Execute "main.py". 
* Follow the on-screen instructions, and press enter/return after each instruction.



SAMPLE EXECUTION & OUTPUT
-------------------------

* On first executing "main.py", the following text appears on-screen:

	
	Enter location of directory to be read: 


  Enter the location of the directory/folder containing the ".day" files, and press enter/return.

	Example:   Enter location of directory to be read: C:\Users\EV\Desktop\Aladdin_f_trial - Copy\x  

* The following text will appear on the screen next:


	Enter location of workbook to be updated: 


  Enter the location of the ".xlsx" file to be updated and press enter/return.

	Example:   Enter location of directory to be read: C:\Users\EV\Desktop\Aladdin_f_trial - Copy\x\s1.xlsx 

* The following message will get displayed:

	
	Parsing in progress. This may take several minutes...


* After several minutes, either of thw two will happen:

	1. The Command Prompt will close.
	2. The following message will be displayed on-screen :

		Parsing complete. Worbook has been updated.

  Either case implies that the ".xlsx" file has been updated.
  
  
  Note: To see the kind of data being processed, see the text file "sample_data.txt".
