from django.core.exceptions import ObjectDoesNotExist
import os
import unirest
import pprint
from restapi.models import UPC, Scan, FoodCat, WellScore, NutRule

class Food(object):
	'''
	This class will cover the lifecycle from when an item's UPC code is scanned to the return of a wellness designation (Yes, No, Unknown).

	An item in the Food class will be intiated with a UPC code and food category ID, returned via the scanner app. This class contains the functions needed to ping Nutrionix for nutrition info, enter nutrition info by hand, and calculate wellness.

	The process will cover three scenarios:
		-1. Wellness score calculated previously (yay!)
			-Score returned. The End.
		-2. Wellness score not calculated
			-3a. Item in Nutrionix API
				-Nutrition info on item added to UPC table
				-Wellness score calculated; stored in WellScore table and returned to user.
			-3b. Item not in Nutrionix API
				-User pinged to enter information

		3b folo if user can enter info: This triggers a POST request, this time with info entered via form:            
			-Info stored in UPC table
			-Wellness score calculated; stored in WellScore table and returned to user

		This will require a Nutrionix API key and ID, which can be found here: https://developer.nutritionix.com/
	'''


	def __init__(self, upc_code, food_cat, api_key, api_id):
		self.upc_code = upc_code
		self.api_key = api_key 
		self.api_id = api_id
		self.food_cat = food_cat
		self.api_reponse = self.run()
		
	def reset_keys(self, new_key):
		"""
		Change API keys
		"""
		setattr(self, 'api_key', new_key)
		
	def reset_id(self, new_id):
		"""
		Change API id
		"""
		setattr(self, 'api_id', new_id)
	

	def check_wellness(self):
		try:
			upc_key = UPC.objects.values_list('pk',flat=True).get(upc_code=self.upc_code)
			cat_key = FoodCat.objects.values_list('pk', flat=True).get(load_cat=self.food_cat)
			return WellScore.objects.filter(upc_id_id=upc_key).values()
		except ObjectDoesNotExist:
			return False


	def get_food_item(self):
		"""
		Get nutritional info from the UPC table, Nutrionix API, or add in new item if not found
		"""

		if UPC.objects.filter(upc_code=self.upc_code).values():
			self.food_info = UPC.objects.filter(upc_code=self.upc_code).values()[0]
		else:
			response = unirest.get("https://api.nutritionix.com/v1_1/item?upc={upc}&appId={apiID}&appKey={apiKey}".format(
					apiID=self.api_id, apiKey=self.api_key,upc=self.upc_code),
								   headers={"Accept": "application/json"})
			if response.code == 200:
				self.food_info = response.body
				new_dict_keys = map(lambda x:str(x).replace('nf_',''), self.food_info.keys())
				new_dict_keys = ['ingredients' if name=='ingredient_statement' else name for name in new_dict_keys]
				self.food_info = dict(zip(new_dict_keys,self.food_info.values()))

				obj = UPC(
						upc_code=self.upc_code,
						item_name=self.food_info['item_name'],
						brand_id=self.food_info['brand_id'],
						brand_name=self.food_info['brand_name'],
						item_description=self.food_info['item_description'],
						api_last_update=self.food_info['updated_at'],
						ingredients=self.food_info['ingredients'],
						#redo these to be NaN or other float compatible format
						calories=float(0 if not self.food_info['calories'] else self.food_info['calories']),
						calories_from_fat=float(0 if not self.food_info['calories_from_fat'] else self.food_info['calories_from_fat']),
						total_fat=float(0 if not self.food_info['total_fat'] else self.food_info['total_fat']),
						saturated_fat=float(0 if not self.food_info['saturated_fat'] else self.food_info['saturated_fat']),
						cholesterol=float(0 if not self.food_info['cholesterol'] else self.food_info['cholesterol']),
						sodium=float(0 if not self.food_info['sodium'] else self.food_info['sodium']),
						total_carb=float(0 if not self.food_info['total_carbohydrate'] else self.food_info['total_carbohydrate']),
						dietary_fiber=float(0 if not self.food_info['dietary_fiber'] else self.food_info['dietary_fiber']),
						sugars=float(0 if not self.food_info['sugars'] else self.food_info['sugars']),
						protein=float(0 if not self.food_info['protein'] else self.food_info['protein']),
						vitamin_a_dv=float(0 if not self.food_info['vitamin_a_dv'] else self.food_info['vitamin_a_dv']),
						vitamin_c_dv=float(0 if not self.food_info['vitamin_c_dv'] else self.food_info['vitamin_c_dv']),
						calcium_dv=float(0 if not self.food_info['calcium_dv'] else self.food_info['calcium_dv']),
						iron_dv=float(0 if not self.food_info['iron_dv'] else self.food_info['iron_dv']),
						serving_per_cont=float(0 if not self.food_info['servings_per_container'] else self.food_info['servings_per_container']),
						serving_size_qty=float(0 if not self.food_info['serving_size_qty'] else self.food_info['serving_size_qty']),
						serving_size_unit=self.food_info['serving_size_unit']
				)

				obj.save()

			else:
				self.food_info = {'error': 'API Error or Item Not Found. Please enter item details via app.'}
		
		self.food_info['category'] = str(self.food_cat) # this makes applying wellness logic easier
		
		return self.food_info

	def add_new_food_item(self):
		"""
		Add new food item, via info sent via post from app. Feature TK.
		"""
		pass
  
		
	def convert_dict_to_attributes(self):
		"""
		Convert the keys in the dictionary to object attributes
		"""
		for key, value in self.food_info:
			setattr(self, key, value)
	
	#ISSUE: These three fxns could probably be cleaned up by someone who is better at decorators	
	@property
	def main_ingredient(self):
		"""
		Extract main ingredient of the food
		"""
		self.food_info['ingredients'] = self.food_info['ingredients'].replace('+++', ',')
		return self.food_info['ingredients'].split(',')[0]
	
	def set_food_info(self, nutrition, value):
		"""
		Change the nutrtion value of food
		"""
		pass
		#setattr(self, nutrition, value)

	def get_nut_rule(self):
		cat_key = FoodCat.objects.values_list('pk', flat=True).get(load_cat=self.food_cat)
		return NutRule.objects.filter(food_cat_id_id=cat_key).values()[0]

	def wellness_logic(self):
		'''
		This functions fetches applicable nutrition rule, then applies it to food. The result is returned to user and stored in WellScore table.
		'''
		nut_rule = self.get_nut_rule()

		#ISSUE: Refactor this into multiple, more modular functions because this makes me sad
		if nut_rule['rule_type'] == 'contains':
			if nut_rule['value'].lower() in self.food_info[nut_rule['nutritional_field']].lower():
				self.wellness = nut_rule['wellness']
			else:
				self.wellness = abs(nut_rule['wellness'] - 1)
		elif nut_rule['rule_type'] == 'lte':
			if float(self.food_info[nut_rule['nutritional_field']]) <= float(nut_rule['value']):
				self.wellness = nut_rule['wellness']
			else:
				self.wellness = abs(nut_rule['wellness'] - 1)
		elif nut_rule['rule_type'] == 'first_item':
			main = self.main_ingredient()
			if nut_rule['value'].lower() in main:
				self.wellness = nut_rule['wellness']
			else:
				self.wellness = abs(nut_rule['wellness'] - 1)
		else:
			self.wellness = 0 #ISSUE: update data model to support 'Unknown' or 'None' choice

		upc_key = UPC.objects.values_list('pk',flat=True).get(upc_code=self.upc_code)
		obj = WellScore(upc_id_id=upc_key, nut_id_id=nut_rule['id'],wellness=self.wellness)
		obj.save()

		return self.wellness
		
	def run(self):
		if self.check_wellness():
			wellness = self.check_wellness()
			return wellness[0]['wellness']
		else:
			try:
				self.get_food_item()
				# self.convert_dict_to_attributes() 
				#I am not sure it's the best idea to convert to attributes because it makes applying the logic more verbose, but I am also not good at classes
				return self.wellness_logic()
			except KeyError:
				return self.food_info

if __name__ == '__main__':
	
	# api_key = ''
	# api_id = ''

	# upc_code = '725342381715'
	# # upc_code = '99999;;;'

	
	# # UPC.objects.filter(upc_code=upc_code).values()
	# upc_code = '12000017421'
	# food_cat = 27

	# upc_key = UPC.objects.values_list('pk',flat=True).get(upc_code=upc_code)
	# cat_key = FoodCat.objects.values_list('pk', flat=True).get(load_cat=food_cat) #this will be right when db is reloaded
	# # NutRule.objects.values_list('pk', flat=True).get(food_cat_id_id=cat_key)
	# nut_key = NutRule.objects.values_list('pk', flat=True).get(food_cat_id_id=food_cat)
	
	# obj = WellScore(upc_id_id=upc_key, nut_id_id=nut_key,wellness=0)

	# u = Food(upc_code, food_cat, api_key, api_id)
	# context = u.get_food_item()

	# # context.update({'upc_code': upc_code, 'request': 'ok'})

	# pprint.pprint(context)
	pass