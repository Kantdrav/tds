from playwright.sync_api import sync_playwright

def scrape_sum_for_seed(seed: int) -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}", wait_until="networkidle")
        page.wait_for_selector("table td")
        texts = page.locator("table td").all_text_contents()
        values = [int(txt.strip()) for txt in texts]
        browser.close()
        return sum(values)

if __name__ == "__main__":
    total = sum(scrape_sum_for_seed(seed) for seed in range(42, 52))
    print("Total sum:", total)


