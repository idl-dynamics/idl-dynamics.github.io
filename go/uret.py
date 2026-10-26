#!/usr/bin/env python3
"""Sosyal profil bağlantıları: idldynamics.com/go/<ad>/ → cihaza göre TEK ADIMDA mağaza.
iOS → App Store · Android → Google Play (kaynak etiketi referrer'da) · masaüstü → uygulamanın tanıtım sayfası.
Play'de yayında olmayan uygulamada (ANDROID=None) Android sayfada kalır ve "yakında" notunu görür.
Değişince: python3 go/uret.py → commit."""
from pathlib import Path
import html

D = Path(__file__).resolve().parent
# ad: (başlık, dil, ios, android paketi|None, masaüstü, kaynak, "yakında" notu)
GO = {
    "sinavkocu": ("Sınav Koçu", "tr", "https://apps.apple.com/app/id6795812576", "com.idldynamics.sinavkocu", "/sinavkocu/", "ig_sk", ""),
    "lulusin": ("Lulusin", "id", "https://apps.apple.com/app/id6808125443", None, "https://apps.apple.com/app/id6808125443", "ig_lulusin", "Versi Android segera hadir."),
    "wordbase": ("WordBase", "en", "https://apps.apple.com/app/id6781988415", "com.idldynamics.wordbase", "/wordbase/?l=en&k=ig_wb_en", "ig_wb_en", ""),
    "wordbase-tr": ("WordBase", "tr", "https://apps.apple.com/app/id6781988415", "com.idldynamics.wordbase", "/wordbase/?l=tr&k=ig_wb_tr", "ig_wb_tr", ""),
    "wordbase-fi": ("WordBase", "fi", "https://apps.apple.com/app/id6781988415", "com.idldynamics.wordbase", "/wordbase/?l=fi&k=ig_wb_fi", "ig_wb_fi", ""),
    "attendance": ("IDL Attendance", "en", "https://apps.apple.com/app/id6760389433", "com.idldynamics.attendance", "/attendance/", "ig_at_en", ""),
    "yoklama": ("IDL Attendance", "tr", "https://apps.apple.com/app/id6760389433", "com.idldynamics.attendance", "/attendance/", "ig_at_tr", ""),
    "mathdoku": ("MathDoku X", "en", "https://apps.apple.com/app/id6759137802", "com.idldynamics.mathdoku", "/mathdoku/", "ig_md", ""),
}
YAZI = {"tr": ("Mağazaya yönlendiriliyorsun…", "App Store", "Google Play"),
        "en": ("Taking you to the store…", "App Store", "Google Play"),
        "fi": ("Siirrytään kauppaan…", "App Store", "Google Play"),
        "id": ("Membuka toko aplikasi…", "App Store", "Google Play")}

for ad, (baslik, dil, ios, paket, masa, kaynak, yakinda) in GO.items():
    play = (f"https://play.google.com/store/apps/details?id={paket}&referrer=utm_source%3Dinstagram%26utm_medium%3Dsocial%26utm_campaign%3D{kaynak}"
            if paket else "")
    y = YAZI[dil]
    dugme = f'<a href="{html.escape(ios)}">{y[1]}</a>' + (f'<a href="{html.escape(play)}">{y[2]}</a>' if play else "")
    not_ = f"<p>{html.escape(yakinda)}</p>" if yakinda else ""
    sayfa = f"""<!doctype html>
<html lang="{dil}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>{html.escape(baslik)}</title>
<style>body{{margin:0;min-height:100svh;display:grid;place-items:center;font:16px/1.5 system-ui,sans-serif;background:#0f1220;color:#eef}}
main{{text-align:center;padding:24px}}a{{display:block;margin:10px auto;padding:12px 20px;max-width:240px;border-radius:12px;background:#4b5cff;color:#fff;text-decoration:none;font-weight:600}}</style>
</head><body><main><h1>{html.escape(baslik)}</h1><p>{y[0]}</p>{dugme}{not_}</main>
<script>
// location.replace: geçmişe kayıt bırakmaz, mağazadan geri dönen bu sayfaya düşmez.
(function(){{var ua=navigator.userAgent||"";
var ios=/iPad|iPhone|iPod/.test(ua)||(navigator.platform==="MacIntel"&&navigator.maxTouchPoints>1);
var android=/android/i.test(ua);var play={play!r};
if(ios)location.replace({ios!r});else if(android){{if(play)location.replace(play);}}else location.replace({masa!r});}})();
</script></body></html>
"""
    (D / ad).mkdir(exist_ok=True)
    (D / ad / "index.html").write_text(sayfa, encoding="utf-8")
print("✓", ", ".join(GO))
