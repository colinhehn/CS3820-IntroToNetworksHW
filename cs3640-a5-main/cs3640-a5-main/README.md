# CS:3640 Assignment 5: Measuring Online Tracking

## Group Members
- Randy Zhang
- [Lawrence Deng](https://research-git.uiowa.edu/lldeng/cs3640-a5)
- [Angelo Zamba](https://research-git.uiowa.edu/azamba/cs3640-a5)
- Henry Krain
- Colin Hehn

## Timeline
- **(11/27/23):** Determined research question, initial project planning. - Randy, Angelo, Lawrence, Henry
- **(11/28/23):** Implementation research, started cs3640_webcrawler.py, README formatting. - Colin
- **(11/28/23):** Conducted research into methods for analyzing the size and quantity of cookies for websites - Henry
- **(11/29/23):** Created the first draft of our crawler counting the number of trackers on a site and the load time. - Angelo
- **(11/30/23):** Went to Office Hours with Rishab and realized the manner in which we were doing completely wrong, and were advised to use Playwright instead. - Angelo, Randy, Lawrence, Henry
- **(11/30/23):** Rewrote the crawler using the Playwright package and reparsed the websites from the top 1000 list available. - Angelo
- **(11/30/23):** Modified the Playwright crawler to include the Ghostery extension to crawl websites while reducing the number of trackers present on the web page. - Lawrence
- **(12/1/23):** Ran crawler with Ghostery extension on the same list of URLs and recorded the results. - Angelo, Lawrence
- **(11/30/23):** Graphed relationship between number of trackers and load time. - Colin
- **(12/2-3/23):** Wrote the cookie parser with selenium - Randy
- **(12/4/23):** Added linear regressions, correlation, sample sizes, and p-val to graphs - Randy
- **(12/4/23):** Wrote part 3 of the paper concerning the methodology. - Angelo, Randy
- **(12/4/23):** Made scripts to graph tracker versus non-tracker load times and calculate avg load time difference. - Colin
- **(12/4/23):** Helped write part 4 and 5 - Henry
- **(12/5/23):** Wrote section 4 (results section) of paper. - Lawrence
- **(12/6/23):** Edited entire paper and cleaned up graphs and files. - Lawrence

## Sources
- [List of Known Trackers from EasyList](https://easylist.to/easylist/easyprivacy.txt)
- [Detailed Ranking of Trackers across the Web](https://whotracks.me/trackers.html)
- [Python Package containing 874 most popular trackers dataset](https://pypi.org/project/whotracksme/)
- [Python Webcrawler - Top Coder](https://www.topcoder.com/thrive/articles/web-crawler-in-python)
- [Python Webcrawler - Zenrows](https://www.zenrows.com/blog/web-crawler-python#prerequisites)
- [Finding trackers on a webpage - ChatGPT Instruction](https://chat.openai.com/share/c582a376-79df-416d-87eb-74400de0c686)
- [Linear regression with seaborn](https://www.geeksforgeeks.org/seaborn-regression-plots/)
- [P-value and correlation coefficient with scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html)
- [Selenium tutorial](https://www.youtube.com/watch?v=SPM1tm2ZdK4&t=233s&ab_channel=NeuralNine)
- [Getting the size of a JSON Object/Cookie](https://stackoverflow.com/questions/71748245/how-to-get-the-equivalent-file-size-of-a-json-object-in-python)
- [Determining Website Load Time](https://www.tutorialspoint.com/how-to-check-loading-time-of-website-using-python#:~:text=get(url)%20end_time%20%3D%20time,%7Bloading_time%7D%20seconds.")
- [Playwright Documentation](https://playwright.dev/python/docs/api/class-playwright)
- [Playwright Chrome Extensions](https://playwright.dev/python/docs/chrome-extensions)
- [Locating Chrome Extensions](https://www.bleepingcomputer.com/tutorials/how-to-view-files-installed-by-a-chrome-extension/#:~:text=When%20extensions%20are%20installed%20into,the%20ID%20of%20the%20extension.)
- [Ghostery](https://chromewebstore.google.com/detail/ghostery-%E2%80%93-privacy-ad-blo/mlomiejdfkolichcflejclcbmpeaniij)
- [Boxplots in Matplotlib](https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/)
- [Subplots with Matplotlib](https://stackoverflow.com/questions/22799308/how-can-i-save-two-plots-on-a-single-file-in-python)


