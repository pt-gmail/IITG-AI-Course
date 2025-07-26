### 1. Data Import and Investigation

The dataset was successfully imported, and all variables listed in the data dictionary were checked for presence in the main data. Special attention was given to variables like `Dt_Customer` and `Income` to ensure correct import. Any discrepancies or missing columns were identified and addressed.

---

### 2. Missing Value Imputation for Income

Some customers had missing `Income` values. To impute these, the data was first cleaned—education and marital status categories were standardized. The average income for each (Education, Marital Status) group was calculated, and missing values were filled with the group mean. This approach assumes that customers with similar backgrounds have comparable incomes.

---

### 3. Feature Engineering: Total Children, Age, and Total Spending

- **Total Children**: Created by summing `Kidhome` and `Teenhome`.
- **Age**: Calculated as `2025 - Year_Birth`.
- **Total Spending**: Aggregated from all product spending columns.
- **Total Purchases**: Summed across web, catalog, and store channels.

These new features provide a richer understanding of customer demographics and behavior.

---

### 4. Distribution Analysis and Outlier Treatment

Box plots and histograms were generated for key variables (`Income`, `Age`, `Total_Spending`) to visualize distributions and detect outliers. Outliers were treated using the IQR method, capping extreme values to reduce their influence on further analysis.

---

### 5. Categorical Variable Encoding

- **Ordinal Encoding**: Applied to `Education` (ordered from Basic to PhD).
- **One-Hot Encoding**: Used for nominal variables like `Marital_Status_Clean` and `Country`.

This ensures that categorical data is properly formatted for analysis and modeling.

---

### 6. Correlation Heatmap

A heatmap was created to visualize correlations between numerical variables. This helped identify relationships, such as between income, age, and spending, providing insights into which factors move together.

---

## Hypothesis Testing

### a. Older people are not as tech-savvy and probably prefer shopping in-store.

Correlation analysis showed a weak positive relationship between age and both store and web purchases, suggesting that older customers do not significantly prefer in-store shopping over online channels. The hypothesis is not strongly supported.

---

### b. Customers with kids probably have less time to visit a store and would prefer to shop online.

Both web and store purchases decrease as the number of children increases, but the drop is more significant for store purchases. This suggests that customers with more children are less likely to shop in-store, supporting the hypothesis.

---

### c. Other distribution channels may cannibalize sales at the store.

Negative correlations were found between web/catalog purchases and store purchases, indicating that increased activity in alternative channels may reduce in-store sales. This supports the cannibalization hypothesis.

---

### d. Does the US fare significantly better than the rest of the world in terms of total purchases?

A t-test showed that US customers have a slightly higher average number of purchases, but the difference is not statistically significant (p-value > 0.05). Thus, the US does not perform significantly better.

---

## Visualization-Based Analysis

### 1. Which products are performing the best, and which are performing the least in terms of revenue?

Total revenue by product type was calculated and visualized. Wines generated the highest revenue, while fruits and sweets performed the least.

---

### 2. Is there any pattern between the age of customers and the last campaign acceptance rate?

There is virtually no linear relationship between age and campaign acceptance. However, the 20–30 age group had the highest acceptance rate, which then slightly decreases with age.

---

### 3. Which country has the greatest number of customers who accepted the last campaign?

By multiplying country indicators with campaign responses, the country with the most acceptances was identified and visualized. This highlights geographical differences in campaign effectiveness.

---

### 4. Do you see any pattern in the number of children at home and total spend?

Average total spending decreases as the number of children increases, suggesting families with more children may spend less per person, possibly due to budget constraints.

---

### 5. Education background of customers who complained in the last 2 years.

A bar plot showed the distribution of education levels among customers who complained. This helps identify if certain education groups are more likely to express dissatisfaction.

---
