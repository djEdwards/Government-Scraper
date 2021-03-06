*** State Government Scrapers ***

This collection of scrapers uses Scrapy with Python to scrape all updates posted by state governments regarding COVID-19.

This scraper uses scrapy and html2text as dependencies. I am also using Python3 to create a virtual environment to create an isoalted environment to run the scraper on.

* Steps before running scraper:
Create a virtualenv and run it. (This is slightly different for Windows vs Linux/Mac)
Run pip install scrapy and pip install html2text from the virtualenv to install all the dependencies
* Running the Scraper on Windows
While inside the virtualenv cd into the root directory that contains powershell-script.ps1 and run .\powershell-script.ps1 from powershell terminal to run the script

* Running the Scraper on Mac/Linux
While inside the virtualenv cd into the root directory that contains unix-shell-script.sh and run bash unix-shell-script.sh from terminal to run the script

* Accessing the data
The CDC posts are saved on [STATE INTIALS]_RESULTS.json in the format {Title,Source,Date,Scraped,Class,Manicipality,Language,Text} for each post. The links to each update are saved on all-[STATE INTIALS]-links.txt in the same directory.

* Important Notes:
Since the addition to [STATE INTIALS]_RESULTS.json are appended on instead of overwritten, all the contents of or the whole file [STATE INTIALS]_RESULTS.json must be deleted before each run (except the first run since posts.json does not exist yet during the first run). If this step is not taken [STATE INTIALS]_RESULTS.json WILL HAVE incorrect data
DO NOT delete the file all-[STATE INTIALS]-links.txt.
Since the log settings has been set to INFO only information will be displayed during runs. If an error is encounterd and the link trying to be scraped has downloads or .pdf on it somewhere, the error message can be ignored.
While in virtualenv run deactivate to stop and exit the virtual envrionment
Source code for scraper can be found in cdc_scrape/spiders if starting from the root directory (directory containing this README)
* Individual State Scraper Notes:
(// - Indicates if scraper contains updated ISO date format)
(X - Indicates that source is blocking scraping, or mostly contains PDFS/Vidos)
Version 0 --------------------------

1. Alabama 

2. Arizona

3. California 

4. Maine 

5. Delaware

6. Georgia 

7. Hawai'i 

8. Idaho 

9. New York 

10. Washington

11. New Jersey

12. Pennsylvania

13. Texas

14. Vermont

15. Massachusetts

16. North Carolina

17. Connecticutt

Version 1 --------------------------

18. Utah

19. Wyoming

20. FDA

21. COVID Task Force Transcripts
