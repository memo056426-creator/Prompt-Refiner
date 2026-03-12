import streamlit as st
import requests

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🚀")
st.title("🚀 محسن الأوامر الذكي")

# كود تشخيصي: لنعرف ماذا يرى السيرفر في الخزنة
all_secrets = list(st.secrets.keys())

# محاولة جلب المفتاح بأكثر من اسم (للاحتياط)
API_KEY = st.secrets.get("GROQ_API_KEY") or st.secrets.get("groq_api_key")

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if not API_KEY:
        st.error(f"🚨 لم أجد المفتاح! الأسماء الموجودة في خزنتك هي: {all_secrets}")
        st.info("تأكد أنك كتبت الاسم في Secrets هكذا: GROQ_API_KEY")
    elif user_input:
        with st.spinner("⚡ جاري التحسين..."):
            try:
                url = "https://api.groq.com/openai/v1/chat/completions"
                headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [
                        {"role": "system", "content": "أنت خبير محترف في هندسة الأوامر. حسن النصوص العربية لتكون أوامر احترافية ومفصلة."},
                        {"role": "user", "content": f"حسن هذا النص ليكون أمراً احترافياً: {user_input}"}
                    ]
                }
                response = requests.post(url, headers=headers, json=data, timeout=20)
                if response.status_code == 200:
                    st.success("✅ أخيراً! نجحنا!")
                    st.code(response.json()['choices'][0]['message']['content'])
                    st.balloons()
                else:
                    st.error(f"❌ خطأ من Groq: {response.text}")
            except Exception as e:
                st.error(f"❌ حدث خطأ: {e}")
    else:
        st.warning("⚠️ اكتب نصاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
