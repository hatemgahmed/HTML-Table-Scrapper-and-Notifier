# HTML-Table-Scrapper-and-Notifier
Often we open a website every day to check for certain changes in the provided data of that website. Other times we open websites only to gather information. Usually websites offer bulk types of information through tables. However, if we want to automate the gathering of this information, APIs are generally used. Unfortunately, not all websites offer such APIs for ease of information extraction. This project aims to extract data out of HTML tables for websited that do not offer APIs, then saves the data in CSV format, and sends a notification to your mobile phone if new data is detected. The python script itself runs once, so it needs a scheduler to run periodically (ex: crontab in linux).

Keep in mind that scrapping data from a websites is not always leagal, it depends on the privacy policy of each website. Before you use this scrapping tool, make sure that the website you are scrapping is not against you scrapping it. Use this tool at your own risk.

# Dependencies
scrappy
beautifulSoup
pandas
PushBullet (You need to put the API key in pushbullet_parameters.json, further instructions at https://github.com/hatemgahmed/Email-query-specific-notifier)

# First time Initialization
Open the target website page in a browser, then press Ctrl+I and reload, and go to the network tab. Find the HTML tag and choose it. Then search for the HTML file that contains the table that appears on the website (you can find an preview by choosing the file and clicking on response tab). Once the desired file is known, click on the headers tab, and copy the [request_link].

Open the scraper_parameters.json, and fill in the domain, start_urls=[request_link], input the filename that you want the table to be saved in (to be saved inside Data/) and finally the names of the columns of the table (in the table header)

# How to Run
run the following command
scrapy crawl scrap
