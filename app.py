import streamlit as st
import requests

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")
st.title("🤖 محسن الأوامر الذكي")

# تأكد أنك وضعت المفتاح في Secrets باسم GEMINI_API_KEY
API_KEY = st.secrets.get("GEMINI_API_KEY", "").strip()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if not API_KEY:
        st.error("🚨 المفتاح غير موجود في الإعدادات!")
    elif user_input:
        with st.spinner("⏳ جاري استنطاق الذكاء الاصطناعي..."):
            try:
                # سنستخدم الرابط الأكثر استقراراً عالمياً
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                
                payload = {
                    "contents": [{
                        "parts": [{"text": f"حسن هذا النص ليكون أمراً احترافياً بالعربية: {user_input}"}]
                    }]
                }
                
                response = requests.post(url, json=payload, timeout=20)
                
                # هنا السحر.. سنرى ماذا قالت جوجل بالضبط
                if response.status_code == 200:
                    result = response.json()
                    refined_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("✅ اشتغل يا وحش!")
                    st.code(refined_text)
                    st.balloons()
                else:
                    # سيعرض لك الكود رد جوجل الرسمي بالإنجليزية لتعرف المشكلة
                    st.warning(f"⚠️ رد السيرفر (كود {response.status_code}):")
                    st.json(response.json()) 
            except Exception as e:
                st.error(f"❌ فشل تقني: {e}")
    else:
        st.warning("⚠️ اكتب نصاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
