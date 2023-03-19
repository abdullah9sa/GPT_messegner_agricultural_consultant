<h1> AgriConsult: Messenger Bot Integration with GPT-3.5 API </h1> 
This project is a Messenger bot that integrates with OpenAI's GPT-3.5 API to provide personalized advice and recommendations to farmers related to plant and animal health, feeding, breeding, and other related topics. the project was created in 1 day for Qaf Lab AgriTech Hackathon.

The bot is built using Django and utilizes a webhook to receive messages from Messenger. Upon receiving a message, the bot filters it and generates a response based on the GPT-3.5 API and system parameters defined for AgriConsult.

<h3>Getting Started</h3>
To use this bot, you will need to have the following:

A Facebook Page
A Facebook Developer account
An OpenAI API key
Installation
Clone the repository



<code>git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
Install the required packages</code>


<code>pip install -r requirements.txt</code>
Set up environment variables for the OpenAI API key and Facebook credentials


<code>export OPENAI_API_KEY=<your-api-key>
export FACEBOOK_PAGE_ACCESS_TOKEN=<your-page-access-token>
export FACEBOOK_VERIFY_TOKEN=<your-verify-token>
Run the Django server


python manage.py runserver</code> <br>
Set up a webhook for your Facebook Page that points to the URL of your Django server, using the FACEBOOK_VERIFY_TOKEN as the verification token.

Usage <br>
To use the AgriConsult bot, simply send a message to your Facebook Page. The bot will ask for specific information related to your plants and animals in order to diagnose and analyze their health, feeding, breeding, and other related factors. This will include questions about plant type, soil type, climate conditions, pest problems, animal breed, age, and symptoms.

AgriConsult will analyze the information provided by the farmer and use machine learning algorithms to diagnose plant diseases, recommend suitable plants for the soil, analyze animal health, feeding and breeding patterns, and suggest remedies for problems related to pests, nutrition, and environment.

The bot will provide personalized recommendations to farmers based on the analysis of their plants and animals. This will include advice on how to improve plant and animal health, increase yield and productivity, optimize breeding and feeding patterns, and minimize pest and disease problems.

System Parameters<br>
AgriConsult is designed to utilize the following system parameters:

name: AgriConsult<br>
objective: To provide personalized and accurate advice on plant and animal health, feeding, breeding, and other related topics to Iraqi and Arabic farmers, using natural language processing and machine learning algorithms.
<br>features:
<br>Customized prompts: AgriConsult will ask farmers for specific information related to their plants and animals in order to diagnose and analyze their health, feeding, breeding, and other related factors. This will include questions about plant type, soil type, climate conditions, pest problems, animal breed, age, and symptoms.
<br>Diagnosis and Analysis: AgriConsult will analyze the information provided by the farmer and use machine learning algorithms to diagnose plant diseases, recommend suitable plants for the soil, analyze animal health, feeding and breeding patterns, and suggest remedies for problems related to pests, nutrition, and environment.
<br>Personalized Recommendations: AgriConsult will provide personalized recommendations to farmers based on the analysis of their plants and animals. This will include advice on how to improve plant and animal health, increase yield and productivity, optimize breeding and feeding patterns, and minimize pest and disease problems.
