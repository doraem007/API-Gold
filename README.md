Step 1 Add .env file. In file .env.example

  Put "TO" As Your user ID
  Put "AUTHORIZATION" As Channel access token

  Save file name looklike .env

Step 2 Run_Service_With

  Dokcer
    : cd Gold-Alert
    : docker build -t gold-alert .
    : docker run -d --restart unless-stopeed --name gold-alert gold-alert
    
  python
    : cd Gold-Alert
    : pip install -r requirements.txt
    : python main.py OR python3 main.py

Reference Price Gold at https://ทองคำราคา.com/

This is first Project for me Thank.
