### 1. **Frontend/UI Wizard**

* Build Streamlit input forms for:

  * User profile (age, risk tolerance, goals)
  * Portfolio input (assets + allocations)
* Implement interactive buttons and flow (Analyze, Reset, Download)
* Setup **`st.session_state`** to hold user inputs & results
* Make it look clean AF with nice layout and charts placeholders

---

### 2. **Data Cruncher & Visualizer**

* Handle portfolio data calculations:

  * Asset allocation breakdown (%)
  * Risk score logic based on user profile + portfolio
  * Diversification checks (detect overconcentration)
* Create charts (pie, bar) using **Plotly/Matplotlib** or Streamlit built-in
* Prepare data for recommendation engine input

---

### 3. **AI / OpenAI Specialist**

* Craft GPT prompts to analyze portfolio + user profile
* Call OpenAI API from Streamlit and process responses
* Parse GPT text output into clean, user-friendly advice
* Iterate prompt tuning for best quality explanations & suggestions

---

### 4. **Report & Export Guru**

* Build PDF/CSV export feature with summary of analysis + recommendations
* Use libs like `fpdf`, `reportlab`, or `pandas.to_csv`
* Integrate export buttons and feedback UI (download success/fail)
* Bonus: Add email share or copy-to-clipboard feature if time permits

---

### 5. **Project Manager / Integration & Testing**

* Glue all parts together & manage `st.session_state` across modules
* Write the main Streamlit app flow and navigation
* Test user journeys, fix bugs, optimize performance
* Prepare demo, run final polish (styling, error handling)
* Coordinate git commits, merges, and keep everyone on track
