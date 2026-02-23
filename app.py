# --- 6. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")

# PASTE YOUR KEY INSIDE THE QUOTES BELOW
MY_NEWS_KEY = "0SYM2E4LAG7AHT2K" 

if MY_NEWS_KEY !="0SYM2E4LAG7AHT2K":
    news_url = f"https://finnhub.io/api/v1/news?category=general&token={MY_NEWS_KEY}"
    try:
        response = requests.get(news_url)
        news_data = response.json()[:5] # This grabs the top 5 stories
        
        for item in news_data:
            # This creates a clickable dropdown for each headline
            with st.expander(item['headline']):
                st.write(item['summary'])
                st.caption(f"Source: {item['source']} | [Read Full Article]({item['url']})")
    except Exception as e:
        st.error("Could not load news at this moment.")
else:
    st.info("💡 To see live news, replace "0SYM2E4LAG7AHT2K" in the code with your real Finnhub API key.")
