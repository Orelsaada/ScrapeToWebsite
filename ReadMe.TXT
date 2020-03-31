https://www.peopleperhour.com/freelance-jobs/software-development/script/web-scraper-development-2757204

Client requires:
-Web Scrape to CSV automatically every 2 days.
-Email the CSV file.
-Automatic upload scraped data to website.

My program:
-Using request and BS libraries to scrape the web.
-Using smtplib and email to send the mail.
-Flask based web takes csv arguments and render it.
-Heroku host the web app and automate the whole process using apscheduler.
-Cron-job.org keeps Heroku app alive when it's needed to execute the process.

