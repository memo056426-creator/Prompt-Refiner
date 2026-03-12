import streamlit as st
import requests

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")
st.title("🤖 محسن الأوامر الذكي")

# جلب المفتاح
API_KEY = st.secrets.get("GEMINI_API_KEY", "").strip()

def try_generate(user_text):
    # قائمة بالموديلات والروابط (سنجربها واحد واحد)
    attempts = [
        {"url": "v1beta", "model": "gemini-1.5-flash"},
        {"url": "v1beta", "model": "gemini-pro"},
        {"url": "v1", "model": "gemini-pro"}
    ]
    
    for attempt in attempts:
        try:
            url = f"https://generativelanguage.googleapis.com/{attempt['url']}/models/{attempt['model']}:generateContent?key={API_KEY}"
            payload = {
                "contents": [{"parts": [{"text": f"أنت خبير في هندسة الأوامر. حسن هذا النص ليكون أمراً (Prompt) احترافياً ومفصلاً باللغة العربية: {user_text}"}]}]
            }
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result['candidates'][0]['content']['parts'][0]['text'], attempt['model']
        except:
            continue
    return None, None

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if not API_KEY:
        st.error("🚨 المفتاح مفقود!")
    elif user_input:
        with st.spinner("⏳ جاري البحث عن موديل متاح وتحسين طلبك..."):
            refined_text, model_used = try_generate(user_input)
            
            if refined_text:
                st.success(f"✅ تم بنجاح باستخدام {model_used}!")
                st.code(refined_text)
                st.balloons()
            else:
                st.error("❌ فشلت كل المحاولات. يبدو أن هناك مشكلة في منطقة السيرفر أو المفتاح.")
    else:
        st.warning("⚠️ اكتب نصاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
