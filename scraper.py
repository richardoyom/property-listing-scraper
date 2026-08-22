import requests, re, json, os, cv2
from bs4 import BeautifulSoup

url = "https://nigeriapropertycentre.com/for-rent/flats-apartments/abuja/jabi/3621022-luxury-furnished-3-bedroom-apartments"
save_folder = os.path.join(os.getcwd(), "images")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36"
}

os.makedirs(save_folder, exist_ok=True)

print("=" * 70)
print("Loading property page...")
print("=" * 70)

r = requests.get(url, headers=headers, timeout=30)
r.raise_for_status()
html = r.text
soup = BeautifulSoup(html, "html.parser")

# =====================================================
# PROPERTY DETAILS
# =====================================================

property_id = re.search(r"/(\d+)-", url).group(1)

title = soup.find("h1").get_text(strip=True)

price = next(
    (s.get_text(" ", strip=True) for s in soup.find_all("span")
     if s.get_text(" ", strip=True).startswith("?")
     and re.search(r"\d", s.get_text())),
    ""
)

location = next(
    (s.get_text(" ", strip=True) for s in soup.find_all("span")
     if s.get_text(" ", strip=True).endswith(", Abuja")
     and len(s.get_text(" ", strip=True)) < 60),
    ""
)

date_posted = next(
    (s.get_text(" ", strip=True).replace("Posted", "", 1).strip()
     for s in soup.find_all("span")
     if s.get_text(" ", strip=True).startswith("Posted")),
    ""
)

phone = next(
    (s.get_text(strip=True) for s in soup.find_all("span")
     if re.fullmatch(r"\+234\d{10}", s.get_text(strip=True))),
    ""
)

desc = soup.find("div", attrs={"x-ref": "body"})
description = desc.get_text("\n", strip=True) if desc else ""

rent = service_charge = legal_agency = caution = inspection = ""

for line in description.splitlines():
    line = line.strip()
    low = line.lower()

    if low.startswith("rent:"):
        rent = line
    elif "service charge" in low:
        service_charge = line
    elif "legal" in low:
        legal_agency = line
    elif "caution" in low:
        caution = line
    elif "inspection" in low:
        inspection = line

# =====================================================
# GALLERY
# =====================================================

print("\nSearching for gallery images...")

images = []

patterns = [
    r"propertyGallery\(\s*JSON\.parse\('(.+?)'\)\s*,\s*(?:true|false)\s*\)",
    r'propertyGallery\(\s*JSON\.parse\("(.+?)"\)\s*,\s*(?:true|false)\s*\)',
    r"propertyGallery\s*\(\s*JSON\.parse\s*\(\s*['\"](.+?)['\"]\s*\)"
]

for pattern in patterns:
    m = re.search(pattern, html, re.DOTALL)
    if m:
        try:
            images = json.loads(json.loads(f'"{m.group(1)}"'))
            break
        except:
            pass

print(f"Found {len(images)} images.\n")

converted = failed = 0

for i, image in enumerate(images, 1):
    try:
        img_url = image["thumb"].replace("\\/", "/")
        data = requests.get(img_url, headers=headers, timeout=30).content

        webp = os.path.join(save_folder, f"image_{i}.webp")
        jpg = os.path.join(save_folder, f"image_{i}.jpg")

        with open(webp, "wb") as f:
            f.write(data)

        img = cv2.imread(webp)

        if img is None:
            failed += 1
            continue

        cv2.imwrite(jpg, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        os.remove(webp)

        print(f"? Saved image_{i}.jpg")
        converted += 1

    except Exception as e:
        print(f"? Failed image {i}: {e}")
        failed += 1

# =====================================================
# RESULTS
# =====================================================

print("\n" + "=" * 70)
print("PROPERTY DETAILS")
print("=" * 70)

print(f"Property ID       : {property_id}")
print(f"Title             : {title}")
print(f"Price             : {price}")
print(f"Location          : {location}")
print(f"Date Posted       : {date_posted}")
print(f"Phone             : {phone}")
print(f"URL               : {url}")

print("\nDESCRIPTION")
print("-" * 70)
print(description)

print("\nFINANCIAL DETAILS")
print("-" * 70)
print(f"Rent              : {rent}")
print(f"Service Charge    : {service_charge}")
print(f"Legal & Agency    : {legal_agency}")
print(f"Caution Deposit   : {caution}")
print(f"Inspection Fee    : {inspection}")

print("\nIMAGE DOWNLOAD SUMMARY")
print("-" * 70)
print(f"Images Found      : {len(images)}")
print(f"Converted         : {converted}")
print(f"Failed            : {failed}")
print(f"Saved To          : {save_folder}")

print("\n" + "=" * 70)
print("SCRAPING COMPLETE")
print("=" * 70)
