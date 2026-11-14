# district2media.com

Website for District 2 Media. Plain HTML, CSS and JavaScript in `public/`, no build step, hosted on Cloudflare.

## Files
- `public/index.html`: the one-page site (hero, services, who we serve, work, process, about, contact)
- `public/assets/css/style.css`: all styles; colors and fonts are the variables at the top
- `public/assets/js/site.js`: menu, viewfinder animation, contact form
- `public/assets/img/`: work screenshots and the favicon

## Before going live
1. **Contact form:** get a free access key at https://web3forms.com for the inbox that should receive leads, and paste it into `WEB3FORMS_KEY` at the top of `public/assets/js/site.js`. Until then the form tells visitors to email instead.
2. **Contact email:** `hello@district2media.com` appears in `index.html` and `site.js` (`CONTACT_EMAIL`). Change both if you use a different address.
3. **Pho Sapa case study:** confirm the owner is happy to be featured.

## Deploy on Cloudflare
Compute (Workers & Pages) → Create → Import a repository → `district2media-site`. Leave the build settings empty; `wrangler.jsonc` serves `public/`. Every push to `main` redeploys. Add `district2media.com` and `www.district2media.com` under Settings → Domains & Routes once the domain's DNS is on Cloudflare.

## Changing the niche
The positioning lives in a few places in `index.html`: the hero lead, the "Built for local business" section (the amber card is the specialty) and the page `<title>`/description. Change those to specialize (for example, Asian restaurants and Asian-owned businesses) without touching the design.
