// Export the final executive map without presentation controls.
const {chromium}=require(process.argv[2]);
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const out=path.resolve(__dirname,'../../outputs/segunda-feira');
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:900},deviceScaleFactor:2});
 await page.goto(pathToFileURL(path.join(out,'REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html')).href+'#modo=executivo&quadro=encerramento');
 await page.evaluate(()=>document.fonts.ready);
 await page.locator('#encerramento .vpp-stage').screenshot({path:path.join(out,'MAPA_EXECUTIVO_IA_VP_PESSOAS.png')});
 await page.emulateMedia({media:'print'});
 await page.evaluate(()=>document.querySelectorAll('.vpp-slide').forEach(s=>s.classList.toggle('print-skip',s.id!=='encerramento')));
 await page.addStyleTag({content:'@page{size:1280px 720px;margin:0}@media print{#encerramento{width:1280px!important;height:720px!important;break-after:auto!important;page-break-after:auto!important}#encerramento .vpp-stage{transform:none!important}}'});
 await page.pdf({path:path.join(out,'MAPA_EXECUTIVO_IA_VP_PESSOAS.pdf'),pageRanges:'1',printBackground:true,preferCSSPageSize:true,margin:{top:0,bottom:0,left:0,right:0}});
 await page.emulateMedia({media:'screen'});
 await page.setViewportSize({width:390,height:844});
 await page.screenshot({path:path.resolve(__dirname,'../../output/playwright/mobile-encerramento.png'),fullPage:true});
 await page.goto(pathToFileURL(path.join(out,'REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html')).href+'#modo=executivo&quadro=gartner');
 await page.locator('#gartner [data-source="SRC-018"]').click();
 if(!(await page.locator('#dialog-body').innerText()).includes('Gartner'))throw Error('Gartner source missing');
 console.log('Map exported as PNG and PDF; Gartner source panel verified.');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
