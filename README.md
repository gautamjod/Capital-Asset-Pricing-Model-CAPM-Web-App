# Capital-Asset-Pricing-Model-CAPM-Web-App

🔍 Overview
The CAPM Web App is an interactive financial analysis tool developed using Streamlit. It enables users to explore the relationship between individual stock performance and overall market risk by implementing the Capital Asset Pricing Model (CAPM). The app is tailored for educational use, personal investment analysis, and portfolio comparison.

🎯 Objectives
Provide a user-friendly interface for stock risk and return analysis.

Visualize stock price trends and relative volatility.

Calculate Beta values and expected returns using real market data.

📊 Key Features
Stock Selector: Choose up to 4 major tech stocks.

Custom Time Frame: Analyze performance over 1 to 10 years.

Dynamic Visualizations:

Historical stock prices

Volatility comparison (normalized prices)

Statistical Analysis:

Daily returns calculation

Beta and Alpha via linear regression

Expected return using CAPM

⚙️ Technologies Used
Python

Streamlit (for web app interface)

Pandas & NumPy (for data manipulation)

yFinance & FRED (for data sourcing)

Plotly Express (for interactive visualizations)

Linear Regression (NumPy Polyfit) for CAPM analysis

📈 CAPM Model Used
Expected Return
=
𝑅
𝑓
+
𝛽
(
𝑅
𝑚
−
𝑅
𝑓
)
Expected Return=R 
f
​
 +β(R 
m
​
 −R 
f
​
 )
Where:

𝑅
𝑓
R 
f
​
  = Risk-free rate (set to 0%)

𝛽
β = Volatility relative to the market

𝑅
𝑚
R 
m
​
  = Expected market return (annualized S&P 500)

✅ Outcome
The app provides clear insights into how different stocks react to market movements, helping users better understand stock risk profiles and expected returns through CAPM. It successfully bridges data visualization and quantitative finance for intuitive financial analysis.
