// Browser QA of the generated local file. No network dependencies or test runner.
const {chromium}=require(process.argv[2]);
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'../..');
const out=path.join(root,'output/playwright');fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const file=pathToFileURL(path.join(root,'outputs/segunda-feira/REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html')).href;
 const check=(v,msg)=>{if(!v)throw new Error(msg);};
 await page.goto(file);
 await page.screenshot({path:path.join(out,'01-capa.png')});
 console.log('Opened local file:',await page.title());
 // Ground truth: inspect the rendered DOM before using its controls.
 console.log('Controls:',await page.getByRole('button').evaluateAll(els=>els.filter(e=>e.getBoundingClientRect().width).map(e=>e.textContent.trim())));
 await page.locator('#btn-next').click();check(await page.locator('#percurso').isVisible(),'Agenda must be second');
 await page.locator('#btn-next').click();check(await page.locator('#trabalho').isVisible(),'Work must follow agenda');
 await page.locator('#btn-read').click();check(await page.locator('#workspace-dialog').isVisible(),'Reader must open');
 check((await page.locator('#dialog-body').innerText()).includes('conversa de desenvolvimento'),'Reader should contain full chapter');
 await page.keyboard.press('Escape');check(!(await page.locator('#workspace-dialog').isVisible()),'Escape closes reader');
 await page.locator('#btn-notes').click();
 await page.locator('#meeting-notes').fill('QA: confirmar contexto e responsável.');
 await page.locator('.dialog-close').click();
 await page.reload();await page.locator('#btn-notes').click();
 check(await page.locator('#meeting-notes').inputValue()==='QA: confirmar contexto e responsável.','Notes persist after reload');
 const dl=page.waitForEvent('download');await page.locator('[data-export-notes]').click();
 const download=await dl;await download.saveAs(path.join(out,'qa-notas.md'));
 check(fs.readFileSync(path.join(out,'qa-notas.md'),'utf8').includes('confirmar contexto'),'Notes export content');
 await page.locator('#meeting-notes').fill('');await page.keyboard.press('Escape');
 // Navigate to the benchmark overview through the advertised map.
 await page.locator('#btn-map').click();await page.locator('[data-map-slide="mercado"]').click();
 await page.locator('#mercado [data-jump="nubank"]').click();
 check(await page.locator('#nubank').isVisible(),'Case drill opens');
 check(await page.locator('#return-strip').isVisible(),'Drill return shown');
 await page.locator('#return-strip').click();check(await page.locator('#mercado').isVisible(),'Return preserves origin');
 await page.locator('[data-open-sources="all"]').click();await page.locator('#source-search').fill('Nubank');
 check(await page.locator('.source-card').count()>0,'Search should find Nubank');
 await page.keyboard.press('Escape');
 // All visual frames: bound checks, content/source overlap, screenshots for review.
 const slides=await page.locator('section.vpp-slide').evaluateAll(els=>els.map(el=>({id:el.id,title:el.getAttribute('aria-label')})));
 const report={errors,desktop:[],mobile:[],routes:{}};
 for(const mode of ['20','120','240']){
   await page.locator(`[data-mode="${mode}"]`).click();
   const route=await page.evaluate(()=>({ids:route(),seconds:Object.values(timing()).reduce((a,b)=>a+b,0)}));
   check(route.seconds===Number(mode)*60-(mode==='240'?900:0),'Route duration must add up');
   report.routes[mode]={count:route.ids.length,seconds:route.seconds};
   await page.goto(file+`#modo=${mode}&quadro=abertura`);
   const walked=[];
   for(let i=0;i<route.ids.length;i++){
     const id=await page.locator('.vpp-slide.active').getAttribute('id');walked.push(id);
     if(i<route.ids.length-1)await page.locator('#btn-next').click();
   }
   check(JSON.stringify(walked)===JSON.stringify(route.ids),`Route ${mode} sequence mismatch`);
   check(await page.locator('#btn-next').isDisabled(),'End of route disables Next');
 }
 for(const [i,s] of slides.entries()){
   await page.goto(file+`#modo=240&quadro=${s.id}`);
   const metrics=await page.locator('.vpp-slide.active').evaluate(el=>{
     const stage=el.querySelector('.vpp-stage').getBoundingClientRect();
     const body=el.querySelector('.visual-body').getBoundingClientRect();
     const sources=el.querySelector('.slide-sources').getBoundingClientRect();
     const overflow=[...el.querySelectorAll('.visual-body *')].filter(x=>{const b=x.getBoundingClientRect(),st=getComputedStyle(x);return b.width&&st.position!=='absolute'&&(b.bottom>stage.bottom-28||b.right>stage.right+2||b.left<stage.left-2);}).map(x=>x.tagName+'.'+x.className);
     return {id:el.id,overflow,bodyBottom:Math.round(body.bottom),sourcesTop:Math.round(sources.top),overlapsSources:sources.width>0&&body.bottom>sources.top-4};
   });report.desktop.push(metrics);
   await page.screenshot({path:path.join(out,`slide-${String(i+1).padStart(2,'0')}-${s.id}.png`)});
 }
 await page.setViewportSize({width:390,height:844});
 for(const s of slides){
   await page.goto(file+`#modo=240&quadro=${s.id}`);
   report.mobile.push(await page.evaluate(()=>({id:document.querySelector('.active.vpp-slide').id,overflow:document.documentElement.scrollWidth>innerWidth+1})));
 }
 for(const id of ['abertura','apostas','camadas','comparacao']){
   await page.goto(file+`#modo=240&quadro=${id}`);
   await page.screenshot({path:path.join(out,`mobile-${id}.png`),fullPage:true});
 }
 await page.goto(file+'#modo=20&quadro=mercado');
 await page.locator('#mercado [data-jump="nubank"]').click();await page.reload();
 await page.locator('#return-strip').click();check(await page.locator('#mercado').isVisible(),'Deep-link reload preserves return');
 await page.setViewportSize({width:1440,height:900});
 await page.goto(file+'#modo=240&quadro=comparacao');
 await page.locator('[data-compare="empresa"]').click();
 check((await page.locator('#comparison-content').innerText()).includes('Skill Vetter'),'Comparison toggle works');
 await page.goto(file+'#modo=240&quadro=camadas');await page.locator('[data-layer="2"]').click();
 check((await page.locator('#layer-detail').innerText()).includes('patrimônio comum'),'Architecture detail works');
 // Public sources open separately with rel protections; original local files must exist.
 const hrefs=await page.locator('a[target="_blank"]').evaluateAll(els=>els.map(el=>({href:el.getAttribute('href'),rel:el.rel})));
 check(hrefs.every(a=>a.rel.includes('noopener')),'External links should protect opener');
 await page.goto(file+'#modo=20&quadro=trabalho');await page.context().setOffline(true);
 await page.reload();await page.locator('#btn-read').click();
 check(await page.locator('.reader').isVisible(),'Offline reading works');await page.keyboard.press('Escape');
 await page.context().setOffline(false);
 await page.emulateMedia({media:'print'});
 const printVisible=await page.locator('section.vpp-slide:visible').count();check(printVisible===16,'Print follows selected route');
 await page.pdf({path:path.join(out,'qa-percurso-executivo.pdf'),printBackground:true,preferCSSPageSize:true});
 await page.emulateMedia({media:'screen'});
 check(errors.length===0,'No page errors: '+errors.join('; '));
 fs.writeFileSync(path.join(out,'qa-report.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({routes:report.routes,desktopIssues:report.desktop.filter(x=>x.overflow.length||x.overlapsSources),mobileIssues:report.mobile.filter(x=>x.overflow),pageErrors:errors,printVisible},null,2));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
