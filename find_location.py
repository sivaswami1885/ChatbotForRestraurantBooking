import zomatopy
import json

city_dict = ['Ahmedabad','Bengaluru','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Aligarh','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Dindigul','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur','Gwalior','Gurgaon','Guwahati','Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kakinada','Kannur','Kanpur','Karnal','Kochi','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai','Malappuram','Mathura','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Patna','Pondicherry','Purulia','Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Shimla','Siliguri','Solapur','Srinagar','Surat','Thanjavur','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Ujjain','Bijapur','Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Vellore','Warangal']

city_dict = [x.lower() for x in city_dict]
def find_city(loc,city_dict =city_dict):
	print("verifying location")
	config={"user_key":"28d00fb87ca00497440ad196c8bbc2fd"}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	results = len(location_json['location_suggestions'])

	if results ==0:
		return {'location_f' : 'notfound', 'location_new' : None}
	elif loc.lower() not in city_dict:
		return {'location_f' : 'tier3', 'location_new' : None}
	else:
		return {'location_f' : 'found', 'location_new' : loc}

		
		

