import matplotlib.pyplot as plt
import numpy as np

# Initial data
years = np.arange(2023, 2027, 1)
inflation = [138, 10, 5, 3]  # Assuming a gradual decrease in inflation
gdp_growth = [1.5, 4, 3.5, 3]  # Assuming gradual GDP growth
unemployment = [12.7, 11, 10, 9]  # Assuming a gradual decrease in unemployment
public_debt = [300, 280, 260, 240]  # Assuming a gradual decrease in public debt
interest_rate = [60, 20, 15, 10]  # Assuming a gradual decrease in interest rate
exchange_rate = [100, 90, 85, 80]  # Assuming a gradual improvement in exchange rate

# Plots
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(years, inflation, marker='o')
plt.title('Inflation over the years')
plt.xlabel('Year')
plt.ylabel('Inflation Rate (%)')

plt.subplot(3, 2, 2)
plt.plot(years, gdp_growth, marker='o')
plt.title('GDP Growth over the years')
plt.xlabel('Year')
plt.ylabel('GDP Growth Rate (%)')

plt.subplot(3, 2, 3)
plt.plot(years, unemployment, marker='o')
plt.title('Unemployment Rate over the years')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')

plt.subplot(3, 2, 4)
plt.plot(years, public_debt, marker='o')
plt.title('Public Debt over the years')
plt.xlabel('Year')
plt.ylabel('Public Debt (in billion dollars)')

plt.subplot(3, 2, 5)
plt.plot(years, interest_rate, marker='o')
plt.title('Interest Rate over the years')
plt.xlabel('Year')
plt.ylabel('Interest Rate (%)')

plt.subplot(3, 2, 6)
plt.plot(years, exchange_rate, marker='o')
plt.title('Exchange Rate over the years')
plt.xlabel('Year')
plt.ylabel('Exchange Rate (Pesos per Dollar)')

plt.tight_layout()
plt.show()
