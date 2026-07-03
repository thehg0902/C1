# Loading Strategy Order (per page)
1. Inline nothing except the theme-critical scrim/bg color if needed.
2. <head>: meta, title, preload hero poster + heading font, stylesheets
   (tokens, base, components, pages - in that order).
3. defer main.js; defer hero.js; defer animations.js; CDN libs last, defer.
4. Below-fold images lazy; iframes (Calendly, maps) lazy via facade
   pattern - static placeholder + click/near-viewport load (their skills
   implement it).
5. Analytics loaded after window load or on first interaction.
Weight audit method: grep each page's referenced assets, `du -b` them,
sum per page, record table in BUILD_STATE.md notes.
