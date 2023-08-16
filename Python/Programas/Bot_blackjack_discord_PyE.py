import pyppeteer
from pyppeteer_stealth import stealth
import asyncio
# from screeninfo import get_monitors


async def identificar_valores(page, valor_mio, valor_rival):
    await asyncio.sleep(1)
    valor_mio_text = await page.evaluate('(element) => element.textContent', valor_mio[-1])
    valor_rival_text = await page.evaluate('(element) => element.textContent', valor_rival[-1])

    return [valor_mio_text, valor_rival_text]


async def convertir_int(valor_mio_text, valor_rival_text):
    try:
        valor_rival_text = int(valor_rival_text)
        valor_mio_text = int(valor_mio_text)
        return [valor_mio_text, valor_rival_text]
    except ValueError:
        print("No se pudo convertir un str...")
        return [valor_mio_text, valor_rival_text]


async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(45000)
    await stealth(page)
    await page.goto('https://www.discord.com/login')

    # await asyncio.sleep(3)

    # monitor = get_monitors()[0]
    # width = monitor.width
    # height = monitor.height
    # await page.setViewport({'width': width, 'height': height})

    await asyncio.sleep(1)

    pages = await browser.pages()
    if len(pages) > 1:
        await pages[0].close()

    await asyncio.sleep(1)

    idioma = input("¿Discord está en ingles y/n ?: ")

    await asyncio.sleep(1)

    if idioma == "y":
        await page.waitForXPath('//input[@id="uid_5"]')
        await page.waitForXPath('//input[@id="uid_7"]')
        await page.waitForXPath("//button[./div[contains(text(), 'Log In')]]")
        print("idemtificado")

        await asyncio.sleep(0.5)

        username = await page.xpath('//input[@id="uid_5"]')
        password = await page.xpath('//input[@id="uid_7"]')
        button_start = await page.xpath("//button[./div[contains(text(), 'Log In')]]")
    else:
        await page.waitForXPath('//input[@id="uid_22"]')
        await page.waitForXPath('//input[@id="uid_24"]')
        await page.waitForXPath("//button[./div[contains(text(), 'Iniciar sesión')]]")
        await asyncio.sleep(0.5)

        username = await page.xpath('//input[@id="uid_22"]')
        password = await page.xpath('//input[@id="uid_24"]')
        button_start = await page.xpath("//button[./div[contains(text(), 'Iniciar sesión')]]")

    await username[0].click()
    await asyncio.sleep(0.3)
    await username[0].type("Digita tu correo")

    await password[0].click()
    await asyncio.sleep(0.3)
    await password[0].type("Digita tu contraseña")

    await button_start[0].click()
    await page.waitForXPath("//div[1]/div[4]/div[2]")
    await asyncio.sleep(2)

    await page.goto("https://discord.com/channels/768278151435386900/973425187301261393")

    partidas = 0

    while partidas < 100:
        await asyncio.sleep(4)
        await page.waitForXPath("//div/div[1]/div/div[3]/div/div[2]")
        input_canal = await page.xpath("//div/div[1]/div/div[3]/div/div[2]")
        await asyncio.sleep(0.4)
        await input_canal[0].click()
        await asyncio.sleep(0.4)
        await input_canal[0].type("!bj 250")
        await asyncio.sleep(0.4)
        await input_canal[0].press("Enter")

        await asyncio.sleep(2.5)

        
        await page.waitForXPath("//article/div/div/div[3]/div[1]/div[2]/code")
        await page.waitForXPath("//article/div/div/div[3]/div[2]/div[2]/code")

        await asyncio.sleep(3)
        valor_mio = await page.xpath("//article/div/div/div[3]/div[1]/div[2]/code")
        valor_rival = await page.xpath("//article/div/div/div[3]/div[2]/div[2]/code")

        valor_mio_text, valor_rival_text = await identificar_valores(page, valor_mio, valor_rival)
        valor_mio_text, valor_rival_text = await convertir_int(valor_mio_text, valor_rival_text)

        while True:
            print(f"Valor actual mio: {valor_mio_text}")
            print(f"Valor actual rival: {valor_rival_text}\n")

            if valor_mio_text == "Blackjack":
                break
            else:
                valor_mio_text = int(valor_mio_text)
                valor_rival_text = int(valor_rival_text)

            if valor_mio_text >= 15:
                print("Se activó condicional 2")
                await page.waitForXPath("//div/div/div/button[2]")
                quedarse = await page.xpath("//div/div/div/button[2]")
                await asyncio.sleep(0.4)
                await quedarse[-1].click()
                await asyncio.sleep(0.4)
                break

            elif valor_mio_text <= 12 or ((valor_mio_text == 13 or valor_mio_text == 14) and valor_rival_text <= 10):
                print("Se activó condicional 1")
                await asyncio.sleep(0.4)
                await page.waitForXPath("//div/div/div/button[1]")
                otro = await page.xpath("//div/div/div/button[1]")
                await asyncio.sleep(0.4)
                await otro[-6].click()
                await asyncio.sleep(0.4)
                valor_mio_text, valor_rival_text = await identificar_valores(page, valor_mio, valor_rival)
            else:
                print("no se cumple ningun condicional")
                print(type(valor_mio_text), valor_mio_text)
                print(type(valor_rival_text), valor_rival_text)

            

        partidas += 1

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
