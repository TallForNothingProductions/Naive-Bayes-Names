import csv

class UnivariateNaiveBayes:
	def __init__(self, data, categories):
		self.data = data
		self.categories = categories

	def prob_category(self,category):
		freq = 0.0
		for name_pair in self.data:
			if name_pair[1] == category:
				freq += 1
		return freq / len(self.data)

	def prob_predictor(self, predictor):
		freq = 0.0
		for name_pair in self.data:
			if name_pair[0] == predictor:
				freq += 1
		return freq / len(self.data)

	def prob_predictor_given_category(self, predictor, category):
		freq_class_given_category = 0.0
		freq_category = 0.0
		for name_pair in self.data:
			if name_pair[1] == category:
				freq_category += 1
				if name_pair[0] == predictor:
					freq_class_given_category += 1
		return freq_class_given_category / freq_category

	def prob_category_given_predictor(self, predictor, category):
		pc = self.prob_category(category)
		pp = self.prob_predictor(predictor)
		ppgc = self.prob_predictor_given_category(predictor, category)

		return  ppgc * pc / pp

	def return_probabilities(self, predictor):
		probabilities = {}
		for category in self.categories:
			probabilities[category] = self.prob_category_given_predictor(predictor, category)

		return probabilities

data = []

def male_or_female(text):
	if text.lower() == "female":
		return "F"
	return "M"

with open("Popular_Baby_Names.csv","r") as file_to_read:
	csv_to_read = csv.reader(file_to_read)
	for row in csv_to_read:
		sex = male_or_female(row[1])
		name = row[3].lower()
		number_babies = int(row[4])
		for x in range(number_babies):
			data.append([name,sex])

unb = UnivariateNaiveBayes(data, ['M','F'])
print str(unb.return_probabilities('nia'))
print str(unb.return_probabilities('alex'))
print str(unb.return_probabilities('jordan'))