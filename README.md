<<<<<<< HEAD
# Sanskrit-OCR-bulk-Converter
This Python script is used to convert large PDF documents into text online, processing them page by page.
=======
Installation Guide (By Mangal)
# This programm sent by Vipul Chhabra (IIIT student & Microsoft engineer)
!Date 20/04/2024 (Mailed by Vipul)
Download or go to the "ImageUpload" folder 
Install : - 
		pip3 install selenium
#(If not found pip then install sudo apt install python3-pip Either ignore it/ see this page's botom for solving errors)
Download geckodriver -
    #(If avalible in the current folder the file, Do not download it)
		wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
	#(Do it)
		sudo tar -xvf geckodriver-v0.34.0-linux64.tar.gz
		sudo mv geckodriver /usr/local/bin/
		cd /usr/local/bin/
		sudo chmod +x geckodriver

Change your input and output path in python3 upload_image.py file (in Window use 'r' in front of the path)

Put the images in 'Input' folder 
 #From PDF to JPEG, run the command 
            pdfimages -j pdfName outputName
Run the command :- 
			python3 upload_image.py 
See the Outputs in 'Output' folder

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Notes for errors with Installations
## For pip3 install selenium - errors 
        sudo apt install python3-pip
        pip3 install selenium
        cd /usr/lib/python3.12/
        sudo rm EXTERNALLY-MANAGED
        pip3 install selenium
        
For error and Installation 
## (For firefox error) If you find the error "Your Firefox profile cannot be loaded. It may be missing or inaccessible."
Remove the Snap firefox and follow the steps carefully 
		https://omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04
	#In this web There are 6 steps @@ copy steps and paste in Terminal
1.      sudo snap remove firefox
2.      sudo install -d -m 0755 /etc/apt/keyrings
3.      wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
4.      echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null 
    
5.      echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla
6.      sudo apt update && sudo apt install firefox 
}

# Errors installing with selenium
1. sudo apt install python3-pip
2. pip3 install selenium
3. cd /usr/lib/python3.12/
4. sudo rm EXTERNALLY-MANAGED


>>>>>>> 500008e (This Python script is used to convert large PDF documents into text online, processing them page by page.)
