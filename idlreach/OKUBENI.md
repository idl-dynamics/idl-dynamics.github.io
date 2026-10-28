# idlreach.com — statik açılış sitesi (WEB1, 28.10.2026)

Bu klasör `idlreach.com` izinli e-posta/anket kampanyasının **statik açılış sayfalarını** içerir
(güven + tanıtım + abone/çık/anket tasarımı). Hazırlayan: WEB1 iş emri. **Dalda hazır, YAYINLANMADI.**

## Nerede barınacak (ÖNEMLİ — GitHub Pages DEĞİL)

`idldynamics-web` deposu GitHub Pages'te tek alan adına (`idldynamics.com`, kök `CNAME`) bağlıdır; ikinci bir
alan adını aynı Pages sitesinden sunamaz. `idlreach.com` için plan (K-042, idl-eposta `docs/SERVIS.md`):

- **Sunucu:** OCI, idl-eposta Caddy, IP `138.2.129.130`.
- **Caddy sunar:** `idlreach.com` (kök + bu statik sayfalar), `cik.idlreach.com` (çıkış), `anket.idlreach.com` (anket).
- **DNS:** Cloudflare (**DNS only**, turuncu bulut KAPALI) — kayıtlar HENÜZ YOK (28.10 itibarıyla kök çözülmüyor).

Dağıtım seçenekleri (kurucu kararı):
1. **Önerilen:** bu dosyaları idl-eposta deposunun Caddy web köküne (`sunucu/`) kopyalayıp Caddy'nin `file_server`
   ile `idlreach.com` kökünden sunması. Dinamik uçlar (`/abone`, `/onay/<J>`, `/cik`, `cik.idlreach.com/u/<J>`,
   `anket.idlreach.com/a/<J>`) zaten idl-eposta servisinindir; bu statik sayfalar onların önüne/yanına yerleşir.
2. Alternatif: Cloudflare Pages (DNS zaten Cloudflare). Bu durumda dinamik uçlar yine OCI'de kalır; formların
   `action`'ları tam URL'ye (`https://idlreach.com/abone` vb.) güncellenir.

## Formların uçları (POST, GET-write YOK)

| Sayfa | `action` | Sahibi |
|---|---|---|
| `abone.html` | `POST /abone` → doğrulama e-postası → `/onay/<J>` | idl-eposta servisi |
| `cik.html` | `POST /cik` (ayrıca jetonlu `cik.idlreach.com/u/<J>`, RFC 8058 tek tık) | idl-eposta servisi |
| `anket.html` | örnek/şablon; gerçek anket `anket.idlreach.com/a/<J>` | idl-eposta servisi |

Bu statik sayfalar **veri toplamaz, sır içermez**; yalnızca sunum katmanıdır. İş mantığı idl-eposta servisindedir.

## Video

`yoklama.html` IDL5/v2 eğitim videosunu `idldynamics.com/attendance/nasil/video/egitim_tam_tr.mp4` adresinden gömer.
Bu dosyalar şu an `idldynamics-web` deposunun **`egitim-videosu` dalındadır** (IDL5'ten); `main`'e birleşmeden
oynatıcı boş görünür. Video tek kaynaktan sunulur, buraya kopyalanmaz.

## DNS kurulum adımları (kurucu "!" ile uygular — DNS yazımı ana pencere/kurucu işi)

Cloudflare panelinde, `idlreach.com` bölgesinde (hepsi **DNS only / Proxy KAPALI**):

```
A   idlreach.com     138.2.129.130
A   cik              138.2.129.130
A   anket            138.2.129.130
```

Not: `dict.idlreach.com` (WordBase sözlüğü) kaydına DOKUNULMAZ. Kök (`@`) kaydı eklemek
`idlreach.com`'u ilk kez canlıya alır; mevcut MX/SPF/e-posta kayıtları korunur.

Sonra sunucuda: `sudo bash /opt/idl-eposta/sunucu/kur.sh caddy` (idl-eposta `SERVIS.md` §kurulum).
TLS sertifikasını Caddy otomatik alır (Let's Encrypt).
