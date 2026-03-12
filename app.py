import streamlit as st
import requests

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")
st.title("🤖 محسن الأوامر الذكي")

# جلب المفتاح من الخزنة
API_KEY = st.secrets.get("GEMINI_API_KEY", "").strip()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if not API_KEY:
        st.error("🚨 المفتاح غير موجود في Secrets!")
    elif user_input:
        with st.spinner("⏳ جاري التواصل المباشر مع الذكاء الاصطناعي..."):
            try:
                # اتصال مباشر وسريع يدعم العربية 100%
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
                payload = {"contents": [{"parts": [{"text": f"أنت خبير في هندسة الأوامر. حسن هذا النص ليكون أمراً (Prompt) احترافياً ومفصلاً باللغة العربية: {user_input}"}]}]}
                
                response = requests.post(url, json=payload, timeout=30)
                result = response.json()

                if response.status_code == 200:
                    refined_text = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("✅ تم التحسين بنجاح!")
                    st.code(refined_text)
                    st.balloons()
                else:
                    error_msg = result.get('error', {}).get('message', 'خطأ غير معروف')
                    st.error(f"❌ خطأ من جوجل: {error_msg}")
            except Exception as e:
                st.error(f"❌ فشل الاتصال: {e}")
    else:
        st.warning("⚠️ اكتب نصاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
