# Selenium-Python
author: smurciac

1. Download the ChromeDriver executable.
2. Now we need to tell Selenium where it is:
   1. Open up Terminal
   2. Run sudo nano /etc/paths
   3. Enter your password
   4. Go to the bottom of the file and enter the path you wish to add
   5. i.e: /Users/name/Documents/WebDriver
   6. Control-x to quit
   7. Y to save
   8. Press enter to confirm
3. To double check, quit Terminal and relaunch it. Run echo $PATH. You should see your newly added path in the stream of other paths already there.
4. Now, you can run the tests!

Run Command:

python src/tests/test.py

Structure:

* Selenium-Python
  
  * src
  
    * actions
      * \_\_init_\_\.py
      * home_actions.py
      * result_actions.py
    * common
      * \_\_init_\_\.py
      * helpers.py
    * pages
      * \_\_init_\_\.py
      * home_page.py
      * result_page.py
    * tests
      * \_\_init_\_\.py
      * test.py
    * \_\_init_\_\.py
    
  * conftest.py
  * confvar.py
  * README.md
  * LICENSE.md
