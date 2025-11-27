import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ipywidgets import interact, FloatSlider


def plot_trig_functions():

    try:
        x = np.linspace(0, 2 * np.pi, 500)
        y_sin, y_cos, y_tan = np.sin(x), np.cos(x), np.tan(x)

        plt.figure(figsize=(8, 5))
        plt.plot(x, y_sin, label='sin(x)', color='blue')
        plt.plot(x, y_cos, label='cos(x)', color='green')
        plt.plot(x, y_tan, label='tan(x)', color='red')
        plt.ylim(-3, 3)
        plt.title('Графіки тригонометричних функцій')
        plt.xlabel('x')
        plt.ylabel('Значення функції')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Помилка при побудові графіка тригонометричних функцій: {e}")



def plot_pie_chart():

    try:
        specialties = ['Інформатика', 'Математика', 'Фізика', 'Хімія', 'Біологія']
        students = [45, 32, 28, 15, 20]
        explode = [0.1 if x == max(students) else 0 for x in students]

        plt.figure(figsize=(6, 6))
        plt.pie(
            students,
            labels=specialties,
            autopct='%1.1f%%',
            explode=explode,
            shadow=True,
            startangle=90
        )
        plt.title('Розподіл студентів за спеціальностями')
        plt.show()
    except Exception as e:
        print(f"Помилка при створенні секторної діаграми: {e}")



def plot_combined():

    try:
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        x = np.linspace(0, 2 * np.pi, 500)
        axs[0, 0].plot(x, np.sin(x), label='sin(x)', color='blue')
        axs[0, 0].plot(x, np.cos(x), label='cos(x)', color='green')
        axs[0, 0].plot(x, np.tan(x), label='tan(x)', color='red')
        axs[0, 0].set_ylim(-3, 3)
        axs[0, 0].set_title('Тригонометричні функції')
        axs[0, 0].legend()
        axs[0, 0].grid(True)

        specialties = ['Інформатика', 'Математика', 'Фізика', 'Хімія', 'Біологія']
        students = [45, 32, 28, 15, 20]
        explode = [0.1 if x == max(students) else 0 for x in students]
        axs[0, 1].pie(students, labels=specialties, autopct='%1.1f%%', explode=explode)
        axs[0, 1].set_title('Розподіл студентів за спеціальностями')

        days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
        temps = [2, 3, 5, 7, 8, 6, 4]
        axs[1, 0].bar(days, temps, color='orange')
        axs[1, 0].set_title('Температура протягом тижня')
        axs[1, 0].set_ylabel('°C')


        years = np.arange(2015, 2025)
        population = [42.8, 42.6, 42.5, 42.4, 42.1, 41.9, 41.8, 41.7, 41.5, 41.3]
        axs[1, 1].plot(years, population, marker='o', color='green')
        axs[1, 1].set_title('Зміна населення України (2015–2024)')
        axs[1, 1].set_xlabel('Рік')
        axs[1, 1].set_ylabel('Млн осіб')
        axs[1, 1].grid(True)

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Помилка при побудові комбінованої візуалізації: {e}")



def interactive_trig(a=1.0):

    try:
        x = np.linspace(0, 2 * np.pi, 500)
        plt.figure(figsize=(7, 5))
        plt.plot(x, np.sin(a * x), label=f'sin({a}x)')
        plt.plot(x, np.cos(a * x), label=f'cos({a}x)')
        plt.legend()
        plt.title(f'Інтерактивний графік sin({a}x) та cos({a}x)')
        plt.xlabel('x')
        plt.ylabel('Значення функції')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Помилка в інтерактивному графіку: {e}")



def main():

    print("▶️ Побудова тригонометричних функцій...")
    plot_trig_functions()
    plt.savefig("functions_plot.png")

    print("▶️ Побудова секторної діаграми...")
    plot_pie_chart()
    plt.savefig("pie_chart.png")

    print("▶️ Побудова комбінованої фігури...")
    plot_combined()
    plt.savefig("combined_plots.png")

    print("✅ Усі графіки створено та збережено у PNG-файли.")



if __name__ == "__main__":
    main()
    interact(interactive_trig, a=FloatSlider(min=0.5, max=5, step=0.1, value=1.0))