import requests
import json
import time

class PTTPriceFetcher:
    def __init__(self):
        self.prices = {}
        self.cache_time = 600  # cache for 10 minutes
        self.last_fetch_time = 0

    def fetch_prices(self):
        current_time = time.time()
        if current_time - self.last_fetch_time < self.cache_time:
            return self.prices  # return cached prices if still valid
        
        # API endpoint for fetching PTT fuel prices
        url = 'https://api.example.com/ptt/fuelprices'  # mock API endpoint
        response = requests.get(url)
        if response.status_code == 200:
            self.prices = response.json()
            self.last_fetch_time = current_time
            return self.prices
        else:
            raise Exception('Failed to fetch fuel prices')

    def calculate_fuel_cost(self, fuel_grade, liters):
        if fuel_grade in self.prices:
            price_per_liter = self.prices[fuel_grade]
            return price_per_liter * liters
        else:
            raise ValueError('Invalid fuel grade')

# Example usage:
# fetcher = PTTPriceFetcher()
# fetcher.fetch_prices()
# cost = fetcher.calculate_fuel_cost('91', 10)
# print(f'Cost for 10 liters of fuel grade 91: {cost}')
