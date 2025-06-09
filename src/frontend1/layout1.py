import streamlit as st
import pandas as pd
import io

def results_and_downloads():
    analyze_clicked = st.session_state.get('analyze', False)
    if analyze_clicked:
        st.markdown("### Results & Charts")
        st.write("Analysis results and charts will appear here after backend processing.")

        portfolio = st.session_state.get('portfolio', {})
        profile = st.session_state.get('profile', {})
        if portfolio and profile:
            risk_score = {
                "Conservative": "Low",
                "Balanced": "Medium",
                "Aggressive": "High"
            }.get(profile.get("risk_tolerance", ""), "Unknown")

            report_data = [
                ["User Age", profile.get("age", "")],
                ["Risk Tolerance", profile.get("risk_tolerance", "")],
                ["Investment Goal", profile.get("investment_goal", "")],
                ["Risk Score", risk_score],
                ["", ""],
                ["Asset", "Allocation (%)"]
            ]
            for asset, allocation in portfolio.items():
                report_data.append([asset, f"{allocation:.2f}"])
            df_report = pd.DataFrame(report_data, columns=["Field", "Value"])

            csv_buffer = io.StringIO()
            df_report.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()

            col_pdf, col_csv = st.columns(2)
            with col_pdf:
                if st.button("Download PDF"):
                    st.info("Download feature coming soon!")
            with col_csv:
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="portfolio_analysis_report.csv",
                    mime="text/csv"
                )