import csv 
import numpy

class FinancialCalculator:
    def __init__(self, lebihan):
        self.lebihan = lebihan

    def calculate(self):
        growth = 0.2 * self.lebihan
        inv_kon = 0.8 * 0.7 * self.lebihan
        inv_spek_stb = 0.8 * 0.3 * 0.4 * self.lebihan
        inv_spek_krez = 0.8 * 0.3 * 0.6 * self.lebihan
        text_to_csv = [converter(round(growth)), converter(round(inv_kon)), converter(round(inv_spek_stb)), converter(round(inv_spek_krez))]
        

        result_text = [
            f"growth: <b>{converter(round(growth))}</b>",
            f"investasi konservatif: <b>{converter(round(inv_kon))}</b>",
            f"investasi spekulatif stabil: <b>{converter(round(inv_spek_stb))}</b>",
            f"investasi spekulatif krezi: <b>{converter(round(inv_spek_krez))}</b>"
        ]

        self.text_to_csv = text_to_csv

        return(result_text)
    
    def data(self):
        a = self.text_to_csv
        with open('data1.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(a)
                print(a)
    
def converter(number):
    # Convert the number to a string
    num_str = str(number)

    # Split the string into groups of three digits from the right
    groups = []
    while num_str:
        groups.append(num_str[-3:])
        num_str = num_str[:-3]

    # Join the groups with dots and reverse the string
    formatted_str = '.'.join(groups[::-1])

    return formatted_str

# Test the function with the given integer
#result = converter(input("masukin angka... "))
#print(result)  # Output: "2.600.000"
