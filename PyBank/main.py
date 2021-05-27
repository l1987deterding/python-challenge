{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "Total Months:86\n",
      "Total Amount:38382578\n",
      "-2315.1176470588234\n",
      "Feb-2012 1926159\n",
      "Sep-2013 -2196167\n"
     ]
    }
   ],
   "source": [
    "#import file\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#declare the csv path\n",
    "csvpath = os.path.join('Resources','budget_data.csv')\n",
    "\n",
    "#declare the variables \n",
    "total_months = 0\n",
    "total_revenue =0\n",
    "changes =[]\n",
    "date_count = []\n",
    "greatest_increase = 0\n",
    "greatest_increase_month = 0\n",
    "greatest_decrease = 0\n",
    "greatest_decrease_month = 0\n",
    "\n",
    "# Open the csv\n",
    "with open(csvpath, newline = '') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter = ',')\n",
    "    next(csvreader, None)\n",
    "    row = next(csvreader)\n",
    "    \n",
    "    # calculate the total number of months and total revenue\n",
    "    previous_profit = int(row[1])\n",
    "    total_months = total_months + 1\n",
    "    total_revenue = total_revenue + int(row[1])\n",
    "    greatest_increase = int(row[1])\n",
    "    greatest_increase_month = row[0]\n",
    "\n",
    "    for row in csvreader:\n",
    " \n",
    "        total_months = total_months + 1\n",
    "        total_revenue = total_revenue + int(row[1])\n",
    "\n",
    "        # calculate change from month-to-month\n",
    "        change = int(row[1]) - previous_profit\n",
    "        changes.append(change)\n",
    "        previous_profit = int(row[1])\n",
    "        date_count.append(row[0])\n",
    "        \n",
    "        #calculate the greatest increase\n",
    "        if int(row[1]) > greatest_increase:\n",
    "            greatest_increase = int(row[1])\n",
    "            greatest_increase_month = row[0]\n",
    "            \n",
    "        #calculate the greatest decrease\n",
    "        if int(row[1]) < greatest_decrease:\n",
    "            greatest_decrease = int(row[1])\n",
    "            greatest_decrease_month = row[0]  \n",
    "            \n",
    "    # calculate the average and date\n",
    "    average_change = sum(changes)/len(changes)\n",
    "\n",
    "    high = max(changes)\n",
    "    low = min(changes)\n",
    "\n",
    "    # print values\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"Total Months:\" + str(total_months))\n",
    "    print(\"Total Amount:\" + str(total_revenue))\n",
    "    print(average_change)\n",
    "    print(greatest_increase_month, max(changes))\n",
    "    print(greatest_decrease_month, min(changes))\n",
    "\n",
    "\n",
    "    # write output files\n",
    "    PyBank = open(\"output.txt\",\"w+\")\n",
    "    PyBank.write(\"Financial Analysis\") \n",
    "    PyBank.write('\\n' +\"Total Months\" + str(total_months)) \n",
    "    PyBank.write('\\n' +\"Total Amount\" + str(total_revenue)) \n",
    "    PyBank.write('\\n' +\"Average\" + str(average_change)) \n",
    "    PyBank.write('\\n' +greatest_increase_month) \n",
    "    PyBank.write('\\n' +str(high))\n",
    "    PyBank.write('\\n' +greatest_decrease_month) \n",
    "    PyBank.write('\\n' +str(low))              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.1 64-bit ('3.9')",
   "language": "python",
   "name": "python391jvsc74a57bd07812ea015bdcee6f23a998adcdd2ef97c151c0c241b7b7070987d9313e41299d"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "metadata": {
   "interpreter": {
    "hash": "7812ea015bdcee6f23a998adcdd2ef97c151c0c241b7b7070987d9313e41299d"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
