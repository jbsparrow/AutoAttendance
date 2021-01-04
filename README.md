# AutoAttendance
(nearly) Automatic attendance filler because I got lazy and didn't wanna manually fill out attendance anymore. It's nearly automatic because I couldn't figure out how to automate dropdowns on google forms.

To get the program running you first need to run it and log in to your account so that it remembers it because in my case you need to be logged in to do the attendance, if you don't need to be logged in just comment the bit that says "option.add_argument("user-data-dir=selenium")" After running it and logging in uncomment "submitbutton.click()" and "browser.close()" 

Then fill in student number, teacher name, your name, course name, and the link to the form. 

The next step is to go to the form, right click on the submit button, click inspect, right click on it again and click inspect again, then click on the highlighted HTML and click "copy full xpath." paste that xpath into the brackets in the code that say something along the lines of "/dir/<body>/dir/" except much longer.

When you run it you have to select your grade because I couldn't figure out dropdowns but there's 7 seconds to select your grade before it's automatically submitted. To disable automatic submission delete "submitbutton.click()" or put a "#" infront of it, like this: "# submitbutton.click()"

https://chromedriver.chromium.org/downloads - here's the download for the chrome webdriver, download the version corresponding to your build of chrome. To find what version of chrome you're on click "chrome>about chrome" and you should see the version.
