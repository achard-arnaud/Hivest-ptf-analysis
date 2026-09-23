"""Print a three-page HTML preview as PDF and one PNG per page."""
import asyncio
import sys
from pathlib import Path

from browser import launch


async def render(html, out, stem):
    from playwright.async_api import async_playwright

    async with async_playwright() as playwright:
        browser = await launch(playwright)
        page = await browser.new_page(viewport={'width': 1404, 'height': 993}, device_scale_factor=2)
        await page.set_content(html.read_text(encoding='utf-8'), wait_until='networkidle')
        await page.emulate_media(media='print')
        await page.pdf(path=str(out / f'{stem}.pdf'), print_background=True, prefer_css_page_size=True,
                       margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'})
        pages = page.locator('.page')
        if await pages.count() != 3:
            raise ValueError('Expected exactly three rendered pages')
        for index in range(3):
            await pages.nth(index).screenshot(path=str(out / f'{stem}_page{index + 1}.png'))
        await browser.close()


if __name__ == '__main__':
    asyncio.run(render(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]))
