import streamlit as st
import requests

st.set_page_config(page_title="محسن الأوامر Pro", page_icon="🤖")
st.title("🤖 محسن الأوامر الذكي")

# جلب المفتاح
API_KEY = st.secrets.get("GEMINI_API_KEY", "").strip()

def refine_prompt(text):
    # سنحاول مع 3 خيارات مختلفة لضمان العمل
    configs = [
        {"ver": "v1beta", "mod": "gemini-1.5-flash-latest"},
        {"ver": "v1", "mod": "gemini-1.5-flash"},
        {"ver": "v1beta", "mod": "gemini-pro"}
    ]
    
    for cfg in configs:
        try:
            url = f"https://generativelanguage.googleapis.com/{cfg['ver']}/models/{cfg['mod']}:generateContent?key={API_KEY}"
            payload = {
                "contents": [{"parts": [{"text": f"أنت خبير في هندسة الأوامر. حسن هذا النص ليكون أمراً (Prompt) احترافياً ومفصلاً باللغة العربية: {text}"}]}]
            }
            response = requests.post(url, json=payload, timeout=15)
            if response.status_code == 200:
                res_json = response.json()
                return res_json['candidates'][0]['content']['parts'][0]['text'], cfg['mod']
        except:
            continue
    return None, None

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if not API_KEY:
        st.error("🚨 المفتاح مفقود في Secrets!")
    elif user_input:
        with st.spinner("⏳ جاري تجربة أفضل محرك متاح..."):
            result, model_name = refine_prompt(user_input)
            if result:
                st.success(f"✅ تم النجاح باستخدام محرك {model_name}")
                st.code(result)
                st.balloons()
            else:
                st.error("❌ عذراً، يبدو أن هناك قيوداً جغرافية على السيرفر حالياً. جرب بعد قليل.")
    else:
        st.warning("⚠️ اكتب شيئاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
