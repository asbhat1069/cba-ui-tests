
 Tests have been built using Robot Framework utilizing the keyword drive approach of test development. 
 Custom keywords have been designed in python to perform various operations.
        
      NOTE:
        *  Please set the selenium drivers folder containing chromedriver.exe, firefox driver etc. in PATH variable 
       
        * To specify the browser to run on set the BROWSER environment variable
          > set BROWSER=chrome     - ON WINDOWS
          
          $ export BROWSER=chrome  - ON MAC
          
          Supported browser values:
             - chrome
             - firefox
             - ie
             - edge
          
        * To run the tests on headless chrome (if running on chrome broser) set HEADLESS environment variable
         > set HEADLESS=true
        
        * To run the tests on responsive site 
         > set RESPONSIVE=tru
        * To specify the device to run the mobile site/responsive tests on set the env variable DEVICENAME
          it is set to 'iPhone X' by default
          allowed values:
                - Galaxy S5
                - Pixel 2
                - Pixel 2XL
                - iPhone 5/SE
                - iPhone 6/7/8
                - iPhone 6/7/8 Plus
                - iPhone X
                - iPad
                - iPad Pro
                
        * SET PYTHONPATH to .
            - Run the tests from the repository root if set to . , if not set PYTHONPATH to the project directory explicitly
       
     # Running UI Tests
     ====================
        * INSTALL python 3
            * https://www.python.org/downloads/
          
       *  Download the required webdrives to run the tests on browser and set PATH
            * https://www.seleniumhq.org/download/
        
        * Navigate to the project folder. SET PYTHONPATH to .
           > set PYTHONPATH=.
           
        * Install requirements
            $ pip install - r requirements.txt
               
        * SET the environment variable BROWSER to the browser to run the tests on like chrome or firefox
            $ set BROWSER=chrome
            *** Runs on chrome by default
            ** if you want to run on headless chrome set HEADLESS=true
            
        In the project folder run the following command to run the tests
            $ robot tests\challenge_test.robot
            
            *** The reports get generated in the project folder by name report.html and log.html
        
       
       
     RUNNING THE TESTS ON A DOCKER CONTAINER
     ==========================================
        INSTALL docker on your system
            * for windows - https://runnable.com/docker/install-docker-on-windows-10
            * for mac - https://docs.docker.com/docker-for-mac/install/
        
        Execute the following commands to run the tests in parallel using docker compose:
            $ docker-compose run cba_tests robot tests/challenge_test.robot
         
            * this creates the container, builds the qa_tests service and runs the tests.
            * The system from where the tests are run needs to have docker and docker-compose installed
            * set all the env variables as mentioned above 
            * The tests run on chrome in headless mode 

     
     
     
            
     