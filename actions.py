from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from zomato_fetch_results import restaurants_search_results
from find_location import find_city
from sender_email_details import Config
from flask_mail_check import send_email

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		global restaurants

		print("Fetching results")
		restaurants = restaurants_search_results(loc, cuisine, price)
		top5 = restaurants.head(5) 
		# top 5 results to display
		if len(top5)>0:
			response = 'Showing you top results:' + "\n"
			for index, row in top5.iterrows():
				response = response + str(row["restaurant_name"]) + ' in ' + row['restaurant_address'] + ' has been rated ' + str(row['restaurant_rating']) + ' and the average budget for two people ' + str(row['budget_for2people'])+"\n"
			response = response + "\nShould i mail you the details? If yes, please share the email ID to which you want the details to be shared!"

		else:
			response = 'No restaurants found'
		dispatcher.utter_message(str(response))

class SendMail(Action):
	def name(self):
		return 'email_restaurant_details'
		
	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('email')

		top10_restaurants = restaurants.head(10)
		print("Receiver: {}".format(recipient))
		send_email(recipient, top10_restaurants)

		dispatcher.utter_message("Mail Sent!! Have a great day!")


class Check_location(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		check = find_city(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]
		
