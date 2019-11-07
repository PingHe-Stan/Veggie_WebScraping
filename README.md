# WebScraping
## This project uses python to scrape images from a web page where loging in is required.
### The further step is to download each item individually so as a clearer picture can be retrieved.
#### 1. Problems encountered
- 1.1. Request for Access to the URL was denied, and thus blank is returned. (Message 403)
     Request was denied becasue critical information was missing. Use chrome inspect "network" to see what headers is needed for access.    "User-Agent" is applied to solve the denial of access. 
- 1.2. Html retrieved using bs4 is not traditional. (where you have <img src="">) 
     Solved by importing json library and converting the result to json for easy access of information.
- 1.3. For-loop failed, because of error of certain json formatting
     Solved by applying try & exception for the continuation of execution without total interruption. 
#### 2. Functions enhanced
- 2.1. Number of images being scraped is calcuated and displayed. 
- 2.2. Name of images is automatically defined without using default setting.
- 2.3. Scraping is being made robust by introducing try & exception. 
