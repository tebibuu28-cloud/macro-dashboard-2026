# --- 6. NEWS SECTION ---
st.divider()
st.subheader("📰 2026 Macro News Feed")

# Replace this with your actual Finnhub key inside the quotes
MY_NEWS_KEY = "0SYM2E4LAG7AHT2K" 

if MY_NEWS_KEY != "YOUR_FINNHUB_KEY_HERE":
    try:
        news_url = f"https://finnhub.io/api/v1/news?category=general&token={MY_NEWS_KEY}"
        response = requests.get(news_url)
        news_data = response.json()[:5]
        
        for item in news_data:
            with st.expander(item['headline']):
                st.write(item['summary'])
                st.caption(f"Source: {item['source']} | [Read Full]({item['url']})")
    except Exception as e:
        st.error("News Feed busy...")
else:
    st.info('💡 To see live news, replace "YOUR_FINNHUB_KEY_HERE" in the code with your real Finnhub API key.')
