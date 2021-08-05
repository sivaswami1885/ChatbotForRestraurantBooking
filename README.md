# Chatbot for restaurant search

### Introduction

The bot helps the user to find good restaurants in major cities of India and chosen cuisines

All tier1 and tier2 cities are supported in this bot. 

Below is an example conversation

Your input ->  hi
Hi, How can I help you!
Your input ->  find some restaurants
In what location?
Your input ->  delhi
? What kind of cuisine would you like to have  3: North Indian (north indian)
? What's the average budget for two people  3: more than 700 (more than 700)
Showing you top results:
Bukhara - ITC Maurya in ITC Maurya, Chanakyapuri, New Delhi has been rated 4.6 and the average budget for two people 6500
Farzi Cafe in 38/39, Level 1, Block E, Inner Circle, Connaught Place, New Delhi has been rated 4.5 and the average budget for two people 2500
Gulati in 6, Pandara Road Market, New Delhi has been rated 4.4 and the average budget for two people 2500
The G.T. Road in M 39, Outer Circle, Connaught Place, New Delhi has been rated 4.4 and the average budget for two people 1200
Indian Grill Room in 315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon has been rated 4.4 and the average budget for two people 1800
Should i mail you the details? If yes, please share the email ID to which you want the details to be shared!
Your input ->  yes, please mail it to ramakanth.kusu@gmail.com
Have a great day!


### Installation

Download this attachment and cd into the folder "Rasa_Basic_Folder"

Install the dependencies
Dependencies are listed in "RequiredSwComponents.txt"

Create and activate Virtual Environment
> python -m venv --system-site-packages ./venv
> .\venv\Scripts\activate

Install RASA and the spacy en library
> pip install rasa
> python -m spacy download en

Open a command prompt in Admin mode and run the following command
> python -m spacy link en_core_web_md en


### Training the RASA 

In order to train the RASA NLU and CORE, run the following command

> rasa train


### Running the RASA on commandline

> rasa shell


## Timeout Issue occurred occasionally while trying to fetch restaurant details from Zomato
## In order to overcome this, default timeout value has been increased to 30 from 10 in the below file
venv\Lib\site-packages\rasa\core\channels\console.py - DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS changed to 30

<br><br><br>
## Privacy Statement: 
1. I have not disclosed any information regarding the business clients of my organization or the revenue 
2. I have not used any official asset for this project
3. This project is only for non moneterial purposes
