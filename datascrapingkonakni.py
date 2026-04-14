def scrape_letter(letter):
    url = f"https://www.savemylanguage.org/sml_v2/pages/dialect.php?name=GSB+Mangalore&letter={letter}"
    
    response = get_page(url)
    if response is None:
        print(f"Skipped {letter}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    data = []

    # Try table first
    rows = soup.find_all("tr")

    if rows:
        for row in rows:
            cols = row.find_all("td")
            
            if len(cols) >= 2:
                english = cols[0].text.strip()
                konkani = cols[1].text.strip()

                if english and konkani:
                    data.append([english.lower(), konkani.lower()])
    else:
        # fallback to text parsing
        text = soup.get_text(separator="\n")
        lines = text.split("\n")

        for line in lines:
            line = line.strip()

            if "=" in line:
                parts = line.split("=")

                if len(parts) >= 2:
                    konkani = parts[0].strip()
                    english = parts[1].split("(")[0].strip()

                    if konkani and english:
                        data.append([english.lower(), konkani.lower()])

    return data