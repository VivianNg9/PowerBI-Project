<h1 align="center">Car Sales Analysis</h1>

## Interactive Dashboard
🔗 [View the PowerBI dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzI2NjVkZGUtZWYyMi00MTdhLThhNTQtZTg0Njk2YTcwMzMxIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9)

## Overview

This project analyses a two-year car sales dataset (2022–2023) to understand how **sales volume, pricing and customer behaviour** have evolved, and to identify **clear, actionable priorities for the next 12 months**.

The analysis focuses on:

- Overall revenue, units sold and average selling price  
- Performance of key car types (SUV, Hatchback, Sedan, Passenger, Hardtop)  
- Brand, dealer and regional contribution to growth  
- Customer profile and income-based spending patterns  

> **Dataset:** +23K car sales records (2022–2023) across seven US regions, 30+ automotive brands and five car body styles  
> **Source:** [`Car Sales.xlsx`](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/Car%20Sales.xlsx) 
---
## Process

- **Data preparation:** Loaded [`Car Sales.xlsx`](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/Car%20Sales.xlsx) into Power BI, cleaned and transformed fields in Power Query, and built a simple star schema with a Date table to support time-intelligence.
- **KPI measures (DAX):** Created measures for YTD/MTD Sales, Cars Sold, Avg Price, Prior Year values and YoY growth, plus helper measures for slicers and conditional formatting.
- **Visuals:** Built line charts, bar charts, maps, scatter plots and summary tables to answer the core business questions at overall, dealer, region, brand and car-type levels.
- **Dashboard design:** Organised visuals into three pages (Overview, Dealer Insights, Car Segmentation) with consistent layout, tooltips and slicers for a clean, stakeholder-friendly experience.

---

## Core Business Questions

1. Is our **top-line growth** translating into sustainable, profitable performance – or are we buying volume through discounting and mix shifts?
2. Which **car types and brands** are truly creating value for the portfolio, and which are **diluting price and margin**?
3. How is **network performance** evolving – which regions and dealers are driving growth, and where do we see emerging risk or underperformance?
4. What does our **customer and income profile** tell us about positioning, pricing power and future demand across segments?
5. How can these insights be translated into a **clear commercial plan** for the next 12 months (inventory, pricing, campaigns and dealer strategy)?

---

## 1️⃣ Insight: Revenue & Volume Performance - What is the quality of our growth?

![Car Sales Overview](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/image/image1.png)

**Key observations**

- Total sales increased from around **$300.3M in 2022** to **$371.2M in 2023** – approximately **23.6% revenue growth**.
- Units sold increased from **10,645 cars in 2022** to **13,261 in 2023** – about **24.6% growth in volume**.
- The **average selling price** dipped slightly from **$28.2K** to **$28.0K** (around **–0.8%**), indicating that growth is **volume-led** rather than price-led.
- Weekly trends show **2023 consistently above 2022**, with visible peaks towards year-end, suggesting strong seasonal campaigns or end-of-year promotions.

 ➝ The business is in a solid **growth phase**, with strong increases in both revenue and cars sold. However, the small decline in average price indicates **emerging pressure on pricing or mix**, which could compress margins if unmanaged.

**Next 12-month focus areas**

- **Target:** Maintain double-digit revenue growth while keeping average selling price at least flat.  
  – Monitor discounting and promotional activity so that volume growth does not erode profitability.  
- **Target:** Build a clear view of **profit per unit and per segment** (when cost data is available).  
  – Extend the dashboard to include margins and gross profit, not just selling price.  
- **Target:** Use weekly trend insights to shape **campaign calendars and inventory planning**, especially around peak periods.  

---

## 2️⃣ Insight: Portfolio Mix - Which car types and brands create the most value?

![Car Types & Brand Mix](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/image/image2.png)

**Key observations**

- In 2023, revenue is concentrated in **SUVs and Hatchbacks**:  
  - **SUVs:** ≈ **$99.9M** (**26.9%** of 2023 sales, 3,728 cars, avg price ≈ **$26.8K**).  
  - **Hatchbacks:** ≈ **$82.8M** (**22.3%** of sales, 3,096 cars, avg price ≈ **$26.7K**).  
- **Sedans, Passenger cars and Hardtops** together contribute the remaining **~51%** of sales, with:  
  - **Sedans** carrying the **highest average selling price** (≈ **$29.8K**).  
  - Passenger and Hardtop cars also priced towards the higher end of the range.  
- **Chevrolet** is the top brand in 2023:  
  - ≈ **$27.1M** in sales (**7.3%** of total revenue, 1,043 cars).  
  - Followed closely by **Ford** and **Dodge**; together the top three brands contribute **~21%** of total revenue.  
- The overall price range is broad (from **$1.2K** to **$85.8K**), allowing the portfolio to cover **entry, mid and premium** positions.

 ➝ The portfolio is **well diversified**, but growth depends heavily on **mid-priced SUVs and Hatchbacks** and a **small group of strategic brands**. Higher-priced Sedans and Passenger cars are important for value and margin, even if they represent fewer units.

**Next 12-month focus areas**

- **Target:** Protect and grow the **SUV and Hatchback** franchise, as these segments anchor volume and entry-to-mid price points.  
  – Ensure adequate stock, marketing focus and financing offers tailored to these segments.  
- **Target:** Use **Sedans and Passenger cars** as **margin levers**.  
  – Develop premium packages and upsell journeys (features, warranties, service plans) for customers with higher willingness to pay.  
- **Target:** Deepen partnerships with key brands (Chevrolet, Ford, Dodge).  
  – Co-design campaigns, launches and dealer incentives that reflect each brand’s strength in specific body styles.  

---

## 3️⃣ Insight: Network Performance - Which dealers and regions are driving the portfolio?

![Dealer Insights](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/image/image3.png)

**Key observations**

- **Rabun Used Car Sales** is the **top dealer**, achieving approximately **$20.7M** in 2023 sales from **730 cars**, with strong year-on-year growth.
- Several other dealers – such as **Progressive Shippers Cooperative Association**, **Saab-Belle Dodge**, **U-Haul CO** and **Tri-State Mack Inc** – also deliver **$19–20M+** each, forming a **high-performing core group**.
- All seven regions show healthy growth between **20–26%** from 2022 to 2023:  
  - **Austin** is the largest region (**$65.0M**, **17.5%** of 2023 revenue) and grows by **24.7%**.  
  - **Scottsdale** records the highest relative growth (~**25.5%**).  
  - Other regions (Aurora, Greenville, Janesville, Pasco, Middletown) all grow above **20%**, indicating **broad-based demand**.  
- Average selling prices by region are fairly consistent (around **$27.6K–$28.5K**), suggesting pricing strategy is reasonably aligned across territories.

 ➝ Growth is **distributed across regions**, but a relatively small set of **dealers and locations account for a large share of total sales**. This presents an opportunity to leverage best practices from leading dealers and to intervene early where performance or pricing deviates.

**Next 12-month focus areas**

- **Target:** Codify and replicate **top-dealer playbooks**.  
  – Analyse sales processes, product mix and campaigns at high-performing dealers and roll them out to under-performing locations.  
- **Target:** Provide tailored support to regions with growth below the network average.  
  – Use the dashboard to identify where volumes are high but average prices are falling faster than expected.  
- **Target:** Link dealer incentives more directly to **balanced performance** – revenue, units and pricing discipline – rather than volume alone.  

---

## 4️⃣ Insight: Customer Portfolio - How are income and segments shaping demand?

![Customer & Income Behaviour](https://github.com/VivianNg9/PowerBI-Project/blob/main/PowerBI-Car-Sales-Analysis/image/image4.png)

**Key observations**

- The customer base expands from **~2,020 unique buyers in 2022** to **~2,638 in 2023** – around **31% growth in customers**, outpacing the growth in cars sold.
- As a result, cars per customer edge down slightly (from **5.27 to 5.03**), indicating that growth is increasingly driven by **new customers entering the franchise**, not just repeat purchases.
- The dataset is **male-skewed**: around **78.6% of purchases are made by male customers** and **21.4% by female customers**, highlighting an opportunity to better engage female buyers.
- Average annual income across the customer base is high (median ≈ **$735K**, average ≈ **$831K**), but differs slightly by body style in 2023:  
  - **Hatchback and Sedan buyers** show the **highest average income** (~**$840K** and **$821K**, respectively).  
  - **Passenger car buyers** have slightly lower average income (~**$773K**), despite similar or higher average prices compared to SUVs.  
  - **SUV and Hardtop** sit in the middle, appealing to a broad range of income levels.  
- The **Spending Behaviour** scatterplot (car type vs income) shows that **higher-income buyers gravitate towards higher-priced Sedans and Passenger cars**, while **SUVs and Hatchbacks** attract a mix of mid- to high-income customers at lower price points.

 ➝ The brand is successfully widening its customer base, particularly among **higher-income segments**, but there is a significant **gender imbalance** and an opportunity to refine positioning by income tier and car type.

**Next 12-month focus areas**

- **Target:** Expand presence among **female buyers**.  
  – Develop marketing, showroom experiences and financing offers that speak directly to this segment, particularly in SUV and Hatchback categories.  
- **Target:** Build differentiated propositions for **income tiers**.  
  – For higher-income buyers: premium Sedans and Passenger cars with upgraded features, concierge-style service and long-term warranty packages.  
  – For mid-income buyers: value-led SUV and Hatchback offers with transparent pricing and cost-of-ownership messaging.  
- **Target:** Strengthen early-life customer journeys.  
  – Use CRM and dealer follow-up processes to convert first-time buyers into long-term relationships (service retention, trade-in programs, upgrade offers).  

---

## Executive Summary

Between 2022 and 2023, the car sales business moved into a phase of **strong, broad-based growth**:

- Revenue grew by approximately **23.6%**, units sold by **24.6%**, and the customer base by **~31%**.  
- Growth is underpinned by **mid-priced SUVs and Hatchbacks**, with **Sedans and Passenger cars** providing important opportunities for higher value per unit.  
- Performance is **well distributed across regions**, with Austin, Scottsdale and Janesville standing out as both large and fast-growing.  
- A core group of **top dealers and brands** (notably Chevrolet, Ford and Dodge) drive a significant share of overall results.  
- The customer base is **high-income but heavily male-skewed**, and spending patterns differ subtly by car type and income.

At the same time, the data highlights emerging risks and choices:

- **Average selling price is slipping**, suggesting that volume growth is partly supported by discounting or a shift towards lower-priced models.  
- Dependence on **specific segments (SUVs, Hatchbacks) and a small group of strategic brands and dealers** creates concentration risk.  
- There is sizeable untapped potential among **female buyers and certain income brackets**, especially in segments where the brand is already competitive.

To turn recent growth into **sustainable, profitable performance**, the recommended priorities for the next 12 months are to:

1. **Maintain growth while protecting price and margin** – monitor discounting closely and extend the dashboard to include cost and profitability metrics.  
2. **Optimise the product and segment mix** – double-down on SUVs and Hatchbacks for volume while using Sedans and Passenger cars as premium, higher-margin offers.  
3. **Systematically leverage dealer and regional best practice** – identify high-performing dealers and regions and scale their approaches across the network.  
4. **Refine customer strategy by income and gender** – design targeted propositions for different income tiers and actively grow engagement with female buyers.
