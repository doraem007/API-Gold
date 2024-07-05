Gold-Alert with Line FlEX MESSAGE Use Messaging API

STEP 1

  Config
  
  .env file. In file .env.example

    : Put "TO" As Your user ID
  
    : Put "AUTHORIZATION" As Channel access token

    : Save file name looklike .env
  
STEP 2

  Dokcer
  
    : cd Gold-Alert
    
    : docker build -t gold-alert .
    
    : docker run -d --restart unless-stopeed --name gold-alert gold-alert

  OR
    
  python
  
    : cd Gold-Alert
    
    : pip install -r requirements.txt
    
    : python main.py OR python3 main.py

Reference Gold Price at https://ทองคำราคา.com/

This is first Project for me Thank.
