import streamlit as st
import time

st.set_page_config(
    page_title="Analytics Tool Performance UX Review",
    layout="wide"
)

st.sidebar.title("Audit Sections")

sections = [
    "Overview",
    "Perceived vs Actual Latency",
    "UX Issues Identified",
    "Performance UX Patterns",
    "Outcomes & Recommendations"
]

selected = st.sidebar.radio("", sections)

st.title("Performance Perception Review for Internal Analytics Tool")
st.caption("Analytics Platform · UX & Performance Audit (Anonymized)")
st.divider()

if selected == "Overview":
    st.header("Audit Context")
    st.write("""
    This UX audit reviews an internal analytics tool that users perceived as slow,
    despite backend query performance being within acceptable limits.
    
    The audit focused on UX-level contributors to perceived slowness rather than
    backend or infrastructure optimization.
    """)
    st.info(
        "Focus: perceived performance, feedback, and user confidence — not query tuning."
    )

elif selected == "Perceived vs Actual Latency":
    st.header("Perceived vs Actual Latency")

    st.write("""
    Backend metrics showed acceptable response times, but users reported
    the system as slow and unreliable.
    """)

    st.markdown("""
    **Contributing factors:**
    - No feedback during query execution
    - Blocking UI patterns
    - Empty or silent loading states
    """)

    st.subheader("Illustrative Example")
    with st.spinner("Running analytics query..."):
        time.sleep(2)
    st.success("Query completed (backend timing acceptable)")

elif selected == "UX Issues Identified":
    st.header("UX Issues Identified")

    st.markdown("""
    **Loading states**
    - Generic spinners without progress context
    - No indication of expected duration

    **Blocking interactions**
    - UI frozen during query execution
    - No ability to cancel or adjust queries

    **Feedback gaps**
    - Silent failures or retries
    """)
    
elif selected == "Performance UX Patterns":
    st.header("Performance UX Patterns")

    st.markdown("""
    - Progressive rendering of partial results
    - Skeleton states instead of blank screens
    - Clear messaging for long-running queries
    - Non-blocking UI during execution
    """)

    st.warning(
        "Improving perceived performance often requires no backend changes."
    )

elif selected == "Outcomes & Recommendations":
    st.header("Outcomes & Value")

    st.markdown("""
    - Improved perceived responsiveness through UX-only changes  
    - Reduced frustration during long-running analytics queries  
    - Clearer alignment between system behavior and user expectations  
    """)
    
    st.success(
        "All recommendations were UX-level and backend-safe."
    )
