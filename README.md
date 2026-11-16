# district2media.com

Website for District 2 Media. Plain HTML, CSS and JavaScript in `public/`, no build step, hosted on Cloudflare.

## Files
- `public/index.html`: the one-page site (hero, services, who we serve, work, process, about, contact)
- `public/assets/css/style.css`: all styles; colors and fonts are the variables at the top
- `public/assets/js/site.js`: menu, viewfinder animation, contact form
- `public/assets/img/`: logo (white on transparent), icons, promo video + poster, link-preview image (`og.jpg`), work screenshots

## Before going live
1. **Contact form:** connected. Inquiries go to info@district2media.com through Web3Forms (account login: info@district2media.com). To change the inbox, create a key for the new address and replace `WEB3FORMS_KEY` in `public/assets/js/site.js`.
2. **Contact email:** `info@district2media.com` appears in `index.html` and `site.js` (`CONTACT_EMAIL`). Change both if you use a different address.
3. **Pho Sapa case study:** confirm the owner is happy to be featured.

## Deploy on Cloudflare
Compute (Workers & Pages) → Create → Import a repository → `district2media-site`. Leave the build settings empty; `wrangler.jsonc` serves `public/`. Every push to `main` redeploys. Add `district2media.com` and `www.district2media.com` under Settings → Domains & Routes once the domain's DNS is on Cloudflare.

## Changing the niche
The positioning lives in a few places in `index.html`: the hero lead, the "Built for local business" section (the amber card is the specialty) and the page `<title>`/description. Change those to specialize (for example, Asian restaurants and Asian-owned businesses) without touching the design.

## Changing the accent color
The site is black and white by default to match the logo. Highlighted headline words are drawn as outlines in the accent color, and buttons are filled with it. To try a color, change two lines at the top of `public/assets/css/style.css`:

```css
--accent: #f4f2ee;      /* e.g. #ffb81c amber, #ff5b1f flame, #5b8cff blue */
--accent-ink: #0b0b0c;  /* text on accent buttons: keep dark */
```
