import streamlit as st
import google.generativeai as genai

# 1. AI API Configuration (Gemini Brain Setup)
# Tula tuzi Google API key ithe takavi lagel
API_KEY = "AQ.Ab8RN6KooiLAvsqp1Ap90N9apJ2esQqmVvnYW00CHd8IUpDUvQ"
genai.configure(api_key=API_KEY)

# 2. Software cha Dashboard / Title (Look and Feel)
st.set_page_config(page_title="Local Business AI Marketer", page_icon="🚀")
st.title("🚀 Local Business AI Marketer Software")
st.write("Tumchya dukanacha nav ani type taka, AI tumchyasathi Marathi-English mix marketing content banvel!")

# 3. User Inputs (Client kadun mahiti ghenyasathi boxes)
business_name = st.text_input("🏪 Dukanache / Business che Nav:")
business_type = st.selectbox(
    "📊 Business cha Type niwda:",
    ["Coaching Classes", "Real Estate / Builder", "Gym & Fitness", "Clothing Brand / Boutique", "Restaurant / Sweet Shop"]
)
special_offer = st.text_input("🎁 Kahich special offer aahe ka? (Optional - e.g., 20% Discount, Free Trial)")

# 4. Prompt Engineering Setup (Internal Brain)
if st.button("Generate Marketing Content ✨"):
    if business_name:
        with st.spinner("AI tumchyasathi vichar karat aahe... 🧠"):
            
            # Formula-based Advanced Prompt
            prompt = f"""
            Tu ek expert digital marketer aahes jala Indian local market chi khup samaj aahe.
            Mala '{business_name}' ya business sathi marketing content lihun pahije.
            Business Type: {business_type}
            Special Offer: {special_offer if special_offer else "Regular high quality service"}
            
            Format:
            1. 3 Viral Headlines (Marathi + English mix - Hinglish language jashi lok social media var boltat)
            2. Ek lamb WhatsApp Broadcast Message (Offer sobat ani Call to action/Contact details chi space sodun)
            3. 5 Trending Hashtags
            
            Uttar ekdam attractive ani professional dakhva.
            """
            
            try:
                # Gemini Model call karne
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt)
                
                # 5. Output Screen Var Dakhvane
                st.success("Tूमचा Content Tyaar Aahe! 🎉")
                st.markdown("---")
                st.write(response.text)
                st.markdown("---")
                
            except Exception as e:
                st.error("Kuthetari gadbad zali. Krupaya tumchi API Key check kara.")
    else:
        st.warning("Plz pahile dukanache nav taka!")
