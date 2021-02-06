Side-Challenge by GUOrbit

![](https://i.imgur.com/VX9BIr6.jpg)
In its mission to reach for the stars, GUOrbit is launching a 30x10x10cm satellite into orbit next year. On board will be a small processor and a 3K camera, which will work together to capture, process and store Earth Observation data so that they can be beamed back down to us. To judge the quality of an image though requires constructing some smart metrics, including things like luminosity (if it's night-time, it's probably not worth keeping the picture), cloud coverage and what you can help us with today: water coverage.
 
The challenge is this: write an ANALYTICAL (no AI allowed - not practical for a side challenge) program for extracting Binary Masks of where water is in a RGB satellite image (JPG format). The winner is whoever gets the closest match to the true binary mask (judged numerically). If your implementation is particularly good we may just incorporate it as a fallback algorithm if AI techniques fail - which means your code might just end up in space! There's also the promise of a prize pool of 50 pounds for the winners. Do not be discouraged if your similarity scores seem low, this is expected for such a complicated problem. 

If you liked this challenge, consider applying to join our Software team where you will get the chance to exploring remote sensing challenges like this one, including deep learning, safety-critical design, pair programming in a completely student-run project. You can contact me at: xavier.r.m.weiss@gmail.com
 
You will need to submit A. Your code and B. Your Binary Masks and C (optionally) your requirements.txt file. Manually-created masks (e.g. in Paint) will be disqualified. 

## Setup
To get started create a virtual environment in Python 3.8+:
1. `pip install virtualenv`
2. Create a new virtual environment: `virtualenv orbit`
3. Activate the virtual environment: `source orbit/venv/bin/activate`
4. Now inside the virtual environment, install required packages: `pip install -r requirements.txt`
5. Install additional packages that you might want to use to solve the challenge: `pip install PACKAGE_NAME`
6. When you're done, be sure to freeze your virtual environment in a new requirements.txt file so we can recreate your results: `pip freeze > requirements.txt`

**Source**: All images are from NASA. Ground truth masks were created manually for this challenge.