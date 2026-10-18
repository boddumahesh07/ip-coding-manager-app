import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="IP Medical Coding Manager Prep",
    page_icon="🏥",
    layout="wide",
)

# App Header
st.title("🏥 Inpatient Medical Coding Manager - Interview Prep App")
st.markdown(
    "Master high-level competencies for **Inpatient Coding Manager** roles in India's RCM ecosystem. "
    "Use the modules below to study operational scaling, financial metrics, and team leadership strategies."
)

# Database of Interview Questions and Expert Answers
modules = {
    "1. Operational Scaling & Productivity": [
        {
            "q": "How do you manage workflow balancing and capacity planning for a large inpatient team across multiple shifts under strict Turnaround Time (TAT) SLAs?",
            "a": "• **Forecasting & Historical Analysis:** Review historical admission volumes and seasonal US hospital surges to predict incoming chart loads.\n"
                 "• **Tiered Allocation:** Segregate charts by complexity (e.g., standard medical vs. complex surgical DRGs) and assign them based on coder credentialing (CCS, RHIT) and historical accuracy scores.\n"
                 "• **Real-time Dashboards:** Track live queue status, hourly coder output, and pending bottlenecks to dynamically shift resources between shifts.",
        },
        {
            "q": "How do you structure a continuous quality assurance (QA) framework for inpatient coding, and what is your threshold for acceptable error rates?",
            "a": "• **Target Accuracy:** Maintain a strict standard of $\ge 95\\%$ to $98\\%$ net coding accuracy.\n"
                 "• **Stratified Audits:** Implement random daily sampling alongside targeted audits focusing on high-risk MS-DRGs, surgical sequencing, and CC/MCC captures.\n"
                 "• **Feedback Loops:** Conduct mandatory 1-on-1 root-cause feedback sessions for errors, feeding data back into continuous training modules.",
        },
        {
            "q": "How do you handle severe productivity bottlenecks or backlogs caused by missing physician queries or delayed CDI responses?",
            "a": "• **Escalation Matrix:** Establish a clear protocol with the client-side Clinical Documentation Improvement (CDI) and HIM teams.\n"
                 "• **A/R Risk Mitigation:** Isolate unbilled accounts to protect the Discharged Not Final Billed (DNFB) pipeline.\n"
                 "• **Proactive Tracking:** Maintain a aging report for pending queries to prevent accounts from stalling revenue realization.",
        },
    ],
    "2. Financial Metrics & Client Management": [
        {
            "q": "How does Inpatient coding directly impact the client's Case Mix Index (CMI) and overall hospital reimbursement?",
            "a": "• **CMI Definition:** CMI reflects the average severity and resource intensity of a hospital's patient population.\n"
                 "• **Revenue Impact:** Accurate capture of secondary diagnoses, Complications and Comorbidities (CC), and Major Complications and Comorbidities (MCC) directly elevates the assigned MS-DRG weight.\n"
                 "• **Monitoring:** Track CMI trends monthly against national benchmarks to ensure proper resource utilization representation and avoid undercoding/revenue leakage.",
        },
        {
            "q": "How do you manage client expectations or SLA breaches when attrition or volume surges hit your floor?",
            "a": "• **Early Warning System:** Proactively communicate volume spikes or staffing drops to onshore stakeholders before SLAs are breached.\n"
                 "• **Mitigation Plan:** Cross-skill capable outpatient coders into basic inpatient charts, or utilize approved weekend/overtime shifts.\n"
                 "• **Root Cause Reporting:** Provide transparent post-mortem analysis detailing the incident and preventive measures taken.",
        },
        {
            "q": "What key metrics do you review daily, weekly, and monthly in your operational dashboard?",
            "a": "• **Daily:** Coder productivity (charts/hour), DNFB status, daily attendance/shrinkage.\n"
                 "• **Weekly:** Net coding accuracy/QA scores, query turnaround rates, backlog aging.\n"
                 "• **Monthly:** Case Mix Index (CMI), first-pass payment yield, client SLA compliance, and billable hours utilization.",
        },
    ],
    "3. People Leadership & Attrition": [
        {
            "q": "Inpatient coding requires high-skill talent (like CCS). How do you address high attrition rates and bridge the skill gap?",
            "a": "• **Internal Career Pathing:** Build structured internal upskilling tracks to transition outpatient coders into inpatient settings.\n"
                 "• **Retention Programs:** Provide continuous education credits, clear promotion frameworks, and competitive compensation bands matching market realities.\n"
                 "• **Floor Culture:** Foster a collaborative, low-burnout environment with flexible hybrid or remote policies where feasible.",
        },
        {
            "q": "How do you handle performance management for an experienced coder who meets quality targets but falls short on productivity?",
            "a": "• **Root-Cause Diagnosis:** Evaluate if low output is due to chart complexity mix, system/tool latency, or time-management issues.\n"
                 "• **Targeted Mentorship:** Pair them with a high-performing peer to audit workflow efficiencies and navigation shortcuts.\n"
                 "• **Corrective Action Plan (CAP):** Set realistic, incremental milestones over a 30-day period with structured check-ins.",
        },
    ],
]

# Sidebar Navigation
st.sidebar.header("Navigation Panel")
selected_module = st.sidebar.selectbox("Select Study Module:", list(modules.keys()))

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Pro Tip for Interviews:** Use the **STAR method** (Situation, Task, Action, Result) "
    "and map your past Assistant Manager experiences to these answers."
)

# Main Content Area
st.header(selected_module)
st.markdown("Click on **'Toggle Answer'** under each question to check industry benchmarks.")

# Loop through questions in the selected module
for i, item in enumerate(modules[selected_module]):
    with st.container():
        st.subheader(f"Question {i+1}: {item['q']}")
        
        answer_key = f"ans_{selected_module}_{i}"
        
        if answer_key not in st.session_state:
            st.session_state[answer_key] = False

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Toggle Answer", key=f"btn_{answer_key}"):
                st.session_state[answer_key] = not st.session_state[answer_key]

        if st.session_state[answer_key]:
            st.markdown("> **Industry-Standard Expert Strategy:**")
            st.markdown(item["a"])
            
        st.markdown("---")

# Footer
st.markdown("*Ready to test yourself? Use this app to practice your manager interview prep right from your mobile device!*")
