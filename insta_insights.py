import requests
import json

def get_instagram_profile(username):
    """
    تحليل حساب إنستغرام عام (بدون تسجيل دخول)
    """
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            user = data.get("graphql", {}).get("user", {})

            result = {
                "👤 الاسم الكامل": user.get("full_name"),
                "🧠 اسم المستخدم": user.get("username"),
                "👥 عدد المتابعين": user.get("edge_followed_by", {}).get("count"),
                "➡️ يتابع": user.get("edge_follow", {}).get("count"),
                "📸 عدد المنشورات": user.get("edge_owner_to_timeline_media", {}).get("count"),
                "💬 الوصف": user.get("biography"),
                "🔗 رابط الصورة": user.get("profile_pic_url_hd"),
            }

            return result
        elif response.status_code == 404:
            return {"خطأ": "الحساب غير موجود."}
        else:
            return {"خطأ": f"لم يتمكن من الاتصال. الكود: {response.status_code}"}

    except Exception as e:
        return {"خطأ": f"حدث خطأ: {str(e)}"}

# تشغيل الكود للتجربة
if __name__ == "__main__":
    print("📊 أداة تحليل إنستغرام (قانونية وآمنة)")
    username = input("اكتب اسم المستخدم في إنستغرام: ").strip()
    info = get_instagram_profile(username)
    print(json.dumps(info, indent=4, ensure_ascii=False))
