import matplotlib.pyplot as plt
import os

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def display_bmi_categories():
    print("\nBMI Categories:")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25 - 29.9")
    print("Obesity: 30 or greater")

def save_result_to_file(name, bmi, category):
    with open("bmi_results.txt", "a") as file:
        file.write(f"{name} - BMI: {bmi}, Category: {category}\n")

def plot_bmi_chart():
    categories = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
    bmi_values = [18.5, 24.9, 29.9, 40]
    plt.bar(categories, bmi_values, color=['blue', 'green', 'yellow', 'red'])
    plt.xlabel('BMI Categories')
    plt.ylabel('BMI Range')
    plt.title('BMI Categories Visualization')

    try:
        plt.show()
    except:
        save_chart = input("GUI not available. Do you want to save the chart as a .png file? (yes/no): ")
        if save_chart.lower() == 'yes':
            plt.savefig('bmi_chart.png')
            print("BMI chart saved as 'bmi_chart.png'.")
        plt.close()

def main():
    print("Welcome to the Advanced BMI Calculator!")
    display_bmi_categories()
    
    name = input("\nEnter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    print(f"\n{name}, your BMI is {bmi}, which falls under the category: {category}")
    
    save = input("Do you want to save your results to a file? (yes/no): ")
    if save.lower() == 'yes':
        save_result_to_file(name, bmi, category)
        print("Results saved to 'bmi_results.txt'.")
    
    see_chart = input("Would you like to see the BMI categories chart? (yes/no): ")
    if see_chart.lower() == 'yes':
        plot_bmi_chart()

if __name__ == "__main__":
    main()
