import csv
import math
import operator
import matplotlib.pyplot as plt 
from datetime import datetime
from datetime import date
from decimal import Decimal

allEntries = {}
allCosts = {}
earning = {}
weekOne = {}
weekTwo = {}
weekThree = {} 
weekFour = {}
spendingDates = []
dateArray = []

with open('test.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')

	def loadDataIntoSummedDict():
		changeInBalance = 0
		thisMonthSpending = 0
		lastMonthSpending = 0
		for row in reader:
			price = row[2]
			vendor = row[1]
			date = row[0]

			if (price):
				splitDate = date.split('/')
				month = splitDate[1]
				thisMonth = getThisMonth()
				lastMonth = getPreviousMonth()
				nonStringPrice = Decimal(price)
				print(nonStringPrice)

				if (nonStringPrice < 0):

					if (month == thisMonth):
						thisMonthSpending += Decimal(price)
					if (month == lastMonth):
						lastMonthSpending += Decimal(price)

				#dateOfMonth = int(date[:2])
				changeInBalance += Decimal(price)
				spendingDates.append(date)

				if vendor not in allEntries:
					allEntries[vendor] = Decimal(price)
				else:
					allEntries[vendor] += Decimal(price)
		

			else:
				bants = 100; #its lit	

		print(thisMonthSpending)
		print(lastMonthSpending)

		weekOneTotal = sum(weekOne.values())
		weekTwoTotal = sum(weekTwo.values())
		weekThreeTotal = sum(weekThree.values())
		weekFourTotal = sum(weekFour.values())

		return(changeInBalance, weekOneTotal, weekTwoTotal, weekThreeTotal, weekFourTotal, thisMonthSpending, lastMonthSpending)

	def fillSpendingAndCostsDicts():
		totalCosts = 0
		totalEarning = 0
		for key in allEntries:
			value = allEntries[key]
			if (allEntries[key] > 0):
				earning[key] = value
				totalEarning += value
			else:
				allCosts[key] = value
				totalCosts -= value
		#averageSpendPerDay(totalEarning, totalCosts)

	def averageSpendPerDay(earn, costs):
		firstDate = spendingDates[0]
		lastDate = spendingDates[-1]
		d1 = datetime.strptime(firstDate, "%d/%m/%Y")
		d2 = datetime.strptime(lastDate, "%d/%m/%Y")
		dataRangeInDays = abs((d2 - d1).days)
		averageSpend = costs / dataRangeInDays
		averageEarn = earn / dataRangeInDays
		#print(averageEarn)
		#print(averageSpend)

	def filterSpending():
		eatingOut = 0
		eatingIn = 0
		alcohol = 0
		monthlyFixedCosts = 0
		bankTransfersTotal = 0
		moneyTakenOut = 0
		travelCosts = 0
		activityCosts = 0

		foodShopPlaces = ["TESCO", "LIDL", "ALMAMLAKA"]
		eatOutPlaces = ["BURGER KING", "ZERODEGREES", "RABAIOTTI TRADE ST", "The Grazing", "CO-OP GROUP FOOD", "CHOPSTIX", "BURITO BROTHERS", "BARONE", "KHANS FISH BAR", "BOOTS", "SUBWAY", "TORTILLA", "SPAR", "YO SUSHI", "CHILLI FLAMES", "CURADO BAR", "CHICKEN COTTAGE", "BARBURRITO", "BAGUETTY JUNCTION", "THE SMOKE HAUS", "POUNDLAND", "MCDONALDS"]
		pubs = ["SLUG CARDIFF", "BLUE HONEY" "WOODVILLE", "TINY REBEL", "MACKINTOSH HOTEL", "CENTAL BAR", "ERNEST WILLOWS", "GATEKEEPER", "GASSY JACKS", "KONGS", "BOOTLEGGER", "GREAT WESTERN", "PRYZM"]
		monthlySubscriptions = ["CT landlord", "CARDIFF COUNCIL", "SPOTIFY", "NETFLIX", "JD SPORTS GYMS", "VODAFONE"]
		bankTransfersCodes = ["BP", "CR"]
		ATMCode = ["ATM"]
		funThings = ["CINEWORLD", "AMAZON", "INSTANTGAM", "SUPERBOWL"]
		travel = ["STAGECOACH SERVICE", "TRAINLINE", "UBER", "ARRIVA TRAINS"]
		shops = ["WH SMITH", "HMV", "PRIMARK", "WILKO CARDIFF"]

		eatOutDict = {}
		shoppingDict = {}
		moneyTakenOutDict = {}
		boozeDict = {}
		monthlySubscriptionsDict = {}
		bankTransfersDict = {}
		funThingsDict = {}

		for key in allCosts:
			value = allCosts[key]

			for items in eatOutPlaces:
				if items in key:
					eatingOut -= value
					eatOutDict[key] = value

			for items in foodShopPlaces:
				if items in key:
					eatingIn -= value
					shoppingDict[key] = value

			for items in ATMCode:
				if items in key:
					moneyTakenOut -= value
					moneyTakenOutDict[key] = value

			for items in pubs:
				if items in key:
					alcohol -= value
					boozeDict[key] = value

			for items in monthlySubscriptions:
				if items in key:
					monthlyFixedCosts -= value
					monthlySubscriptionsDict[key] = value

		for key in allEntries:
			for items in bankTransfersCodes:
				if items in key:
					if key not in monthlySubscriptions:
						bankTransfersTotal -= value
						bankTransfersDict[key] = value

			for items in funThings:
				if items in key:
					activityCosts -= value
					funThingsDict[key] = value

		costs = [eatingOut, eatingIn, alcohol, monthlyFixedCosts, bankTransfersTotal, travelCosts, activityCosts]
		drawGraphs(costs)

	def writeOutput():
		with open('results.csv', 'w') as f:
			test = 1

	def drawGraphs(costs):
		plt.plot([(1,2,3,4,5,6,7)], [(costs)], 'ro')
		plt.grid()
		plt.show()

	def getThisMonth():
		today = str(date.today())
		dateArray = today.split('-')
		#year = dateArray[0]
		currentMonth = dateArray[1]
		#day = dateArray[2]

		return(currentMonth)

	def getToday():
		today = str(date.today())
		dateArray = today.split('-')
		#year = dateArray[0]
		#currentMonth = dateArray[1]
		day = dateArray[2]

		return(day)

	def getThisMonthDays():
		thisMonth = getThisMonth
		thisMonthIndex = getThisMonth - 1
		numberOfDays = [31,28,31,30,31,30,31,31,30,31,30,31]
		thisMonthDays = numberOfDays[int(thisMonthIndex)]

		return(thisMonthDays)

	def getPreviousMonth():
		months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
		thisMonth = getThisMonth()
		thisMonthIndex = months.index(thisMonth)
		lastMonthsIndex = thisMonthIndex - 1
		lastMonth = months[lastMonthsIndex]

		return(lastMonth) 

	def getPreviousMonthNumberOfDays(index):
		lastMonthsIndex = int(index) - 1
		numberOfDays = [31,28,31,30,31,30,31,31,30,31,30,31]
		lastMonthDays = numberOfDays[int(lastMonthsIndex)]

		return(lastMonthDays)

	def calculateCurrentSpendingThisMonth():
		numberOfDaysSoFar = int(getToday())
		numberOfDaysLastMonth = getPreviousMonthNumberOfDays(getPreviousMonth())
		a,b,c,d,e,thisMonthSpending,lastMonthSpending = loadDataIntoSummedDict()

		averageSpendLastMonth = lastMonthSpending / numberOfDaysLastMonth

		averageSpendThisMonth = thisMonthSpending / numberOfDaysSoFar

		print("Average Spending last month:")
		print(averageSpendLastMonth)

		print("Average spending this month so far:")
		print(averageSpendThisMonth)



	calculateCurrentSpendingThisMonth()
	


